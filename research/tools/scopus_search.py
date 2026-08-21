#!/usr/bin/env python3
"""Setup-only Scopus Search API support; it does not alter frozen queries."""

from __future__ import annotations

import argparse
import json
import os
import re
import sys
import time
from dataclasses import dataclass
from datetime import datetime, timezone
from pathlib import Path
from typing import Any, Callable, Iterable, Mapping, Sequence
from urllib.error import HTTPError, URLError
from urllib.parse import urlencode
from urllib.request import Request, urlopen

ENDPOINT = "https://api.elsevier.com/content/search/scopus"
API_KEY_ENV = "ELSEVIER_API_KEY"
DEFAULT_COUNT = 25
DEFAULT_CALL_LIMIT = 200
DEFAULT_PACE_SECONDS = 1.0
TRANSIENT_STATUS_CODES = frozenset({408, 425, 429, 500, 502, 503, 504})
QUERY_ID_PATTERN = re.compile(r"^[A-Za-z0-9][A-Za-z0-9._-]*$")


class RetrievalError(RuntimeError):
    """Raised when a complete, secret-free raw retrieval cannot be produced."""


def redact_secret(value: object, secret: str | None) -> str:
    text = str(value)
    return text.replace(secret, "[REDACTED]") if secret else text


def artifact_path(raw_dir: Path, query_id: str, run_timestamp: str, start: int) -> Path:
    if not QUERY_ID_PATTERN.fullmatch(query_id):
        raise ValueError("Query ID contains unsupported filename characters")
    if start < 0:
        raise ValueError("start must not be negative")
    return raw_dir / f"{query_id}__run-{run_timestamp}__api-start-{start:06d}.json"


def _metadata_path(response_path: Path) -> Path:
    return response_path.with_suffix(".metadata.json")


def _total_results(payload: Mapping[str, Any]) -> int:
    search_results = payload.get("search-results")
    if not isinstance(search_results, Mapping):
        raise RetrievalError("Scopus response has no search-results object")
    value = search_results.get("opensearch:totalResults")
    try:
        total = int(value)
    except (TypeError, ValueError):
        raise RetrievalError("Scopus response has no valid totalResults value") from None
    if total < 0:
        raise RetrievalError("Scopus totalResults cannot be negative")
    return total


def _entries(payload: Mapping[str, Any]) -> list[Any]:
    entries = payload["search-results"].get("entry")
    if entries is None:
        return []
    if not isinstance(entries, list):
        raise RetrievalError("Scopus response entry is not a list")
    return entries


def _write_immutable(path: Path, data: bytes) -> None:
    flags = os.O_WRONLY | os.O_CREAT | os.O_EXCL
    try:
        fd = os.open(path, flags, 0o600)
    except FileExistsError:
        raise RetrievalError(f"refusing to overwrite existing raw artifact: {path}") from None
    try:
        with os.fdopen(fd, "wb") as handle:
            handle.write(data)
    except Exception:
        path.unlink(missing_ok=True)
        raise


def _retry_after(headers: Mapping[str, str]) -> float | None:
    try:
        return max(0.0, float(headers.get("Retry-After", "")))
    except ValueError:
        return None


@dataclass(frozen=True)
class RetrievalSummary:
    total_results: int
    raw_captured_records: int
    api_calls: int
    artifacts: tuple[Path, ...]

    @property
    def reconciled(self) -> bool:
        return self.total_results == self.raw_captured_records


def retrieve(
    *, query_id: str, query: str, api_key: str, raw_dir: Path,
    count: int = DEFAULT_COUNT, call_limit: int = DEFAULT_CALL_LIMIT,
    pace_seconds: float = DEFAULT_PACE_SECONDS, retries: int = 3,
    run_timestamp: str | None = None, opener: Callable[..., Any] = urlopen,
    sleeper: Callable[[float], None] = time.sleep,
) -> RetrievalSummary:
    """Retrieve untouched Scopus pages. No deduplication or screening occurs."""
    if not query_id or not QUERY_ID_PATTERN.fullmatch(query_id):
        raise RetrievalError("invalid Query ID")
    if not query:
        raise RetrievalError("the exact frozen Scopus query is required")
    if not api_key:
        raise RetrievalError(f"{API_KEY_ENV} is not set")
    if count < 1 or count > 200 or call_limit < 1 or retries < 0 or pace_seconds < 0:
        raise RetrievalError("invalid pagination, pacing, retry, or call-limit configuration")

    raw_dir.mkdir(parents=True, exist_ok=True)
    timestamp = run_timestamp or datetime.now(timezone.utc).strftime("%Y%m%dT%H%M%SZ")
    start = 0
    total: int | None = None
    captured = 0
    calls = 0
    artifacts: list[Path] = []
    last_call_at: float | None = None

    while total is None or captured < total:
        if calls >= call_limit:
            raise RetrievalError("daily API call limit would be exceeded")
        if last_call_at is not None:
            delay = pace_seconds - (time.monotonic() - last_call_at)
            if delay > 0:
                sleeper(delay)
        request = Request(
            f"{ENDPOINT}?{urlencode({'query': query, 'start': start, 'count': count})}",
            headers={"Accept": "application/json", "X-ELS-APIKey": api_key},
        )
        payload_bytes: bytes | None = None
        for attempt in range(retries + 1):
            if calls >= call_limit:
                raise RetrievalError("daily API call limit would be exceeded")
            calls += 1
            last_call_at = time.monotonic()
            try:
                with opener(request, timeout=60) as response:
                    payload_bytes = response.read()
                break
            except HTTPError as error:
                if error.code not in TRANSIENT_STATUS_CODES or attempt == retries:
                    raise RetrievalError(redact_secret(f"Scopus API HTTP failure: {error}", api_key)) from None
                sleeper(_retry_after(error.headers) or min(30.0, 2**attempt))
            except (URLError, TimeoutError, OSError) as error:
                if attempt == retries:
                    raise RetrievalError(redact_secret(f"Scopus API transport failure: {error}", api_key)) from None
                sleeper(min(30.0, 2**attempt))
        if payload_bytes is None:
            raise RetrievalError("Scopus API returned no response")
        if api_key.encode() in payload_bytes:
            raise RetrievalError("API key appeared in response; raw artifact was not written")
        try:
            payload = json.loads(payload_bytes)
        except json.JSONDecodeError as error:
            raise RetrievalError(f"Scopus API returned invalid JSON: {error.msg}") from None
        if not isinstance(payload, dict):
            raise RetrievalError("Scopus response is not a JSON object")
        page_total = _total_results(payload)
        page_entries = _entries(payload)
        if total is None:
            total = page_total
        elif total != page_total:
            raise RetrievalError("Scopus totalResults changed during retrieval")
        returned = len(page_entries)
        if captured + returned > total:
            raise RetrievalError("raw captured record count exceeds totalResults")
        response_path = artifact_path(raw_dir, query_id, timestamp, start)
        metadata = {
            "query_id": query_id, "endpoint": ENDPOINT, "start": start,
            "count": count, "returned": returned, "totalResults": total,
            "run_timestamp": timestamp, "exact_query": query,
            "raw_response": response_path.name,
        }
        _write_immutable(response_path, payload_bytes)
        _write_immutable(_metadata_path(response_path), (json.dumps(metadata, sort_keys=True) + "\n").encode())
        artifacts.append(response_path)
        captured += returned
        if captured < total and (returned == 0 or returned < count):
            raise RetrievalError("incomplete retrieval: Scopus returned an unexpected short page")
        start += returned
        if returned == 0 and captured < total:
            raise RetrievalError("incomplete retrieval: pagination made no progress")

    summary = RetrievalSummary(total or 0, captured, calls, tuple(artifacts))
    if not summary.reconciled:
        raise RetrievalError("raw captured record count does not reconcile with totalResults")
    return summary


def equivalence_report(*, query_id: str, web_query_id: str, web_query: str,
                       api_query: str, web_count: int, api_total_results: int,
                       web_identifiers: Iterable[str], api_identifiers: Iterable[str]) -> dict[str, Any]:
    """Prepare, but never approve, the mandatory web-vs-API equivalence gate."""
    web_sample = set(web_identifiers)
    api_sample = set(api_identifiers)
    checks = {
        "same_query_id": query_id == web_query_id,
        "exact_query_match": web_query == api_query,
        "count_match": web_count == api_total_results,
        "stable_identifier_sample_match": web_sample == api_sample and bool(web_sample),
    }
    return {"query_id": query_id, **checks, "api_retrieval_approved": False,
            "status": "pending validation"}


def dry_run(*, query_id: str, query_reference: str, count: int, raw_dir: Path) -> str:
    if not QUERY_ID_PATTERN.fullmatch(query_id) or count < 1 or count > 200:
        raise ValueError("invalid Query ID or count")
    return "\n".join([
        "Scopus Search API dry-run",
        f"Query ID: {query_id}", f"Endpoint: {ENDPOINT}",
        f"Exact frozen query/reference: {query_reference}",
        f"Pagination: start=0, then advance by returned entry count; count={count}",
        f"Raw-output directory: {raw_dir}",
        "Authentication: X-ELS-APIKey header (network not accessed)",
        "API execution: no (dry-run)",
    ])


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--query-id", required=True)
    parser.add_argument("--query")
    parser.add_argument("--query-reference")
    parser.add_argument("--count", type=int, default=DEFAULT_COUNT)
    parser.add_argument("--raw-dir", type=Path, default=Path("research/raw/systematic-search"))
    parser.add_argument("--dry-run", action="store_true")
    return parser


def main(argv: Sequence[str] | None = None) -> int:
    args = build_parser().parse_args(argv)
    try:
        if args.dry_run:
            print(dry_run(query_id=args.query_id, query_reference=args.query_reference or args.query or "not supplied", count=args.count, raw_dir=args.raw_dir))
            return 0
        if not args.query:
            raise ValueError("--query is required unless --dry-run is used")
        summary = retrieve(query_id=args.query_id, query=args.query, api_key=os.environ.get(API_KEY_ENV, ""), raw_dir=args.raw_dir, count=args.count)
        print(json.dumps({"totalResults": summary.total_results, "raw_captured_records": summary.raw_captured_records, "api_calls": summary.api_calls, "reconciliation": "Complete", "raw_artifacts": [str(path) for path in summary.artifacts]}, indent=2))
        return 0
    except (ValueError, RetrievalError) as error:
        print(f"error: {redact_secret(error, os.environ.get(API_KEY_ENV))}", file=sys.stderr)
        return 2


if __name__ == "__main__":
    raise SystemExit(main())
