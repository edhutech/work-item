#!/usr/bin/env python3
"""Scopus Search API retrieval support; it does not alter frozen queries."""

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
DEFAULT_VIEW = "STANDARD"
DEFAULT_PAGINATION = "offset"
CURSOR_PAGINATION_AVAILABLE = False
MAX_OFFSET_RESULTS = 5000
VIEW_LIMITS = {"STANDARD": 200, "COMPLETE": 25}
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


def cursor_artifact_path(raw_dir: Path, query_id: str, run_timestamp: str, page: int) -> Path:
    if not QUERY_ID_PATTERN.fullmatch(query_id):
        raise ValueError("Query ID contains unsupported filename characters")
    if page < 1:
        raise ValueError("page must be at least 1")
    return raw_dir / f"{query_id}__run-{run_timestamp}__api-page-{page:06d}.json"


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


def _cursor_next(payload: Mapping[str, Any]) -> str | None:
    search_results = payload.get("search-results")
    cursor = search_results.get("cursor") if isinstance(search_results, Mapping) else None
    if not isinstance(cursor, Mapping):
        return None
    value = cursor.get("@next", cursor.get("next"))
    return str(value) if value not in (None, "") else None


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
    expected_total_results: int | None = None,
    view: str | None = None, pagination: str = DEFAULT_PAGINATION,
    cursor_available: bool = CURSOR_PAGINATION_AVAILABLE,
    run_timestamp: str | None = None, opener: Callable[..., Any] = urlopen,
    sleeper: Callable[[float], None] = time.sleep,
) -> RetrievalSummary:
    """Retrieve untouched Scopus pages without deduplication or screening.

    Cursor pagination remains implemented for a future entitlement, but is
    disabled by the current service-level policy. Offset pagination is the
    operational default and is limited to complete sets at or below 5,000.
    """
    if not query_id or not QUERY_ID_PATTERN.fullmatch(query_id):
        raise RetrievalError("invalid Query ID")
    if not query:
        raise RetrievalError("the exact frozen Scopus query is required")
    if not api_key:
        raise RetrievalError(f"{API_KEY_ENV} is not set")
    requested_view = view.upper() if view else None
    effective_view = requested_view or DEFAULT_VIEW
    if requested_view not in {None, *VIEW_LIMITS} or count < 1 or count > VIEW_LIMITS[effective_view]:
        raise RetrievalError(f"count must be between 1 and {VIEW_LIMITS.get(effective_view, 0)} for {effective_view} view")
    if pagination not in {"auto", "offset", "cursor"} or call_limit < 1 or retries < 0 or pace_seconds < 0:
        raise RetrievalError("invalid pagination, pacing, retry, or call-limit configuration")
    if pagination in {"auto", "cursor"} and not cursor_available:
        raise RetrievalError("cursor pagination is unavailable under the current Scopus service-level policy")
    if expected_total_results is not None and expected_total_results < 0:
        raise RetrievalError("expected totalResults cannot be negative")

    raw_dir.mkdir(parents=True, exist_ok=True)
    timestamp = run_timestamp or datetime.now(timezone.utc).strftime("%Y%m%dT%H%M%SZ")
    mode = "cursor" if pagination == "auto" else pagination
    start = 0
    cursor = "*" if mode == "cursor" else None
    seen_cursors: set[str] = set()
    total: int | None = None
    captured = 0
    calls = 0
    artifacts: list[Path] = []
    last_call_at: float | None = None

    while total is None or captured < total:
        if calls >= call_limit:
            raise RetrievalError("daily API call limit would be exceeded")
        if cursor is not None:
            if cursor in seen_cursors:
                raise RetrievalError(f"repeated Scopus cursor detected: {cursor}")
            seen_cursors.add(cursor)
        if last_call_at is not None:
            delay = pace_seconds - (time.monotonic() - last_call_at)
            if delay > 0:
                sleeper(delay)
        params = {"query": query, "count": count}
        if requested_view is not None:
            params["view"] = requested_view
        if cursor is not None:
            params["cursor"] = cursor
        else:
            params["start"] = start
        request = Request(
            f"{ENDPOINT}?{urlencode(params)}",
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
        page = len(artifacts) + 1
        response_path = (
            cursor_artifact_path(raw_dir, query_id, timestamp, page)
            if cursor is not None
            else artifact_path(raw_dir, query_id, timestamp, start)
        )
        metadata = {
            "query_id": query_id, "database": "Scopus",
            "source": "Scopus Search API", "endpoint": ENDPOINT, "start": start,
            "page": page, "count": count, "view": effective_view,
            "pagination": mode, "cursor": cursor,
            "cursor_next": _cursor_next(payload),
            "returned": returned, "totalResults": total,
            "run_timestamp": timestamp, "exact_query": query,
            "raw_response": response_path.name,
        }
        _write_immutable(response_path, payload_bytes)
        _write_immutable(_metadata_path(response_path), (json.dumps(metadata, sort_keys=True) + "\n").encode())
        artifacts.append(response_path)
        if expected_total_results is not None and page_total != expected_total_results:
            raise RetrievalError(
                f"API totalResults drift: expected {expected_total_results}, received {page_total}"
            )
        if mode == "offset" and total > MAX_OFFSET_RESULTS:
            raise RetrievalError(
                f"Scopus totalResults {total} exceeds the {MAX_OFFSET_RESULTS}-record offset boundary; use Scopus Web"
            )
        captured += returned
        if captured < total and (returned == 0 or returned < count):
            raise RetrievalError("incomplete retrieval: Scopus returned an unexpected short page or empty page")
        next_cursor = _cursor_next(payload) if cursor is not None else None
        if cursor is not None:
            if captured < total and not next_cursor:
                raise RetrievalError("incomplete retrieval: Scopus returned no next cursor before totalResults")
            cursor = next_cursor
        else:
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


def dry_run(*, query_id: str, query_reference: str, count: int, raw_dir: Path,
            view: str | None = None, pagination: str = DEFAULT_PAGINATION) -> str:
    requested_view = view.upper() if view else None
    effective_view = requested_view or DEFAULT_VIEW
    if (not QUERY_ID_PATTERN.fullmatch(query_id) or requested_view not in {None, *VIEW_LIMITS}
            or count < 1 or count > VIEW_LIMITS[effective_view]
            or pagination not in {"auto", "offset", "cursor"}):
        raise ValueError("invalid Query ID or count")
    view_line = "View: STANDARD default route" if requested_view is None else f"View: {effective_view}"
    return "\n".join([
        "Scopus Search API dry-run",
        f"Query ID: {query_id}", f"Endpoint: {ENDPOINT}",
        f"Exact frozen query/reference: {query_reference}",
        f"{view_line}; pagination: {pagination}; count={count}",
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
    parser.add_argument("--view", choices=tuple(VIEW_LIMITS))
    parser.add_argument("--pagination", choices=("auto", "offset", "cursor"), default=DEFAULT_PAGINATION)
    parser.add_argument("--expected-total-results", type=int)
    parser.add_argument("--raw-dir", type=Path, default=Path("research/raw/systematic-search"))
    parser.add_argument("--dry-run", action="store_true")
    return parser


def main(argv: Sequence[str] | None = None) -> int:
    args = build_parser().parse_args(argv)
    try:
        if args.dry_run:
            print(dry_run(query_id=args.query_id, query_reference=args.query_reference or args.query or "not supplied", count=args.count, raw_dir=args.raw_dir, view=args.view, pagination=args.pagination))
            return 0
        if not args.query:
            raise ValueError("--query is required unless --dry-run is used")
        summary = retrieve(query_id=args.query_id, query=args.query, api_key=os.environ.get(API_KEY_ENV, ""), raw_dir=args.raw_dir, count=args.count, expected_total_results=args.expected_total_results, view=args.view, pagination=args.pagination)
        print(json.dumps({"totalResults": summary.total_results, "raw_captured_records": summary.raw_captured_records, "api_calls": summary.api_calls, "reconciliation": "Complete", "raw_artifacts": [str(path) for path in summary.artifacts]}, indent=2))
        return 0
    except (ValueError, RetrievalError) as error:
        print(f"error: {redact_secret(error, os.environ.get(API_KEY_ENV))}", file=sys.stderr)
        return 2


if __name__ == "__main__":
    raise SystemExit(main())
