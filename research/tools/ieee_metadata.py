#!/usr/bin/env python3
"""Local IEEE Metadata API support; it does not translate web queries."""

from __future__ import annotations

import argparse
import json
import math
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

ENDPOINT = "https://ieeexploreapi.ieee.org/api/v1/search/articles"
API_KEY_ENV = "IEEE_API_KEY"
DEFAULT_MAX_RECORDS = 200
DEFAULT_DAILY_CALL_LIMIT = 200
DEFAULT_PACE_SECONDS = 0.2
TRANSIENT_STATUS_CODES = frozenset({408, 425, 429, 500, 502, 503, 504})
QUERY_ID_PATTERN = re.compile(r"^[A-Za-z0-9][A-Za-z0-9._-]*$")


class RetrievalError(RuntimeError):
    """Raised when retrieval cannot produce a complete raw result set."""


def redact_secret(text: object, secret: str | None) -> str:
    """Return text with the local API key removed from all user-facing errors."""
    value = str(text)
    return value.replace(secret, "[REDACTED]") if secret else value


def validate_max_records(value: int) -> int:
    if value < 1 or value > DEFAULT_MAX_RECORDS:
        raise ValueError(f"max_records must be between 1 and {DEFAULT_MAX_RECORDS}")
    return value


def planned_call_count(totalfound: int, max_records: int) -> int:
    if totalfound < 0:
        raise ValueError("totalfound cannot be negative")
    validate_max_records(max_records)
    return math.ceil(totalfound / max_records) if totalfound else 0


def api_artifact_path(raw_dir: Path, query_id: str, run_timestamp: str, start_record: int) -> Path:
    if not QUERY_ID_PATTERN.fullmatch(query_id):
        raise ValueError("Query ID contains unsupported filename characters")
    if start_record < 1:
        raise ValueError("start_record must be at least 1")
    return raw_dir / f"{query_id}__run-{run_timestamp}__api-start-{start_record:06d}.json"


def _articles(payload: Mapping[str, Any]) -> list[Any]:
    articles = payload.get("articles")
    if not isinstance(articles, list):
        raise RetrievalError("API response does not contain an articles list")
    return articles


def validate_response(payload: Any) -> tuple[int, list[Any]]:
    if not isinstance(payload, dict):
        raise RetrievalError("API response is not a JSON object")
    totalfound = payload.get("totalfound")
    if isinstance(totalfound, bool) or not isinstance(totalfound, int) or totalfound < 0:
        raise RetrievalError("API response has no valid totalfound value")
    return totalfound, _articles(payload)


def _read_retry_after(headers: Mapping[str, str]) -> float | None:
    value = headers.get("Retry-After")
    if not value:
        return None
    try:
        return max(0.0, float(value))
    except ValueError:
        return None


@dataclass(frozen=True)
class RetrievalSummary:
    totalfound: int
    raw_captured_records: int
    api_calls: int
    artifacts: tuple[Path, ...]

    @property
    def reconciled(self) -> bool:
        return self.totalfound == self.raw_captured_records


def retrieve(
    *,
    query_id: str,
    query: str,
    api_key: str,
    raw_dir: Path,
    max_records: int = DEFAULT_MAX_RECORDS,
    daily_call_limit: int = DEFAULT_DAILY_CALL_LIMIT,
    expected_totalfound: int | None = None,
    pace_seconds: float = DEFAULT_PACE_SECONDS,
    retries: int = 3,
    run_timestamp: str | None = None,
    opener: Callable[..., Any] = urlopen,
    sleeper: Callable[[float], None] = time.sleep,
) -> RetrievalSummary:
    """Fetch and preserve pages exactly as returned, without deduplication."""
    if not query_id or not QUERY_ID_PATTERN.fullmatch(query_id):
        raise RetrievalError("invalid Query ID")
    if not query:
        raise RetrievalError("an API query representation is required")
    if not api_key:
        raise RetrievalError(f"{API_KEY_ENV} is not set")
    validate_max_records(max_records)
    if daily_call_limit < 1 or retries < 0 or pace_seconds < 0:
        raise RetrievalError("invalid rate or retry configuration")
    if expected_totalfound is not None:
        required_calls = planned_call_count(expected_totalfound, max_records)
        if required_calls > daily_call_limit:
            raise RetrievalError(
                f"retrieval requires {required_calls} API calls, above daily limit {daily_call_limit}"
            )
    raw_dir.mkdir(parents=True, exist_ok=True)
    timestamp = run_timestamp or datetime.now(timezone.utc).strftime("%Y%m%dT%H%M%SZ")
    start_record = 1
    totalfound: int | None = None
    captured = 0
    calls = 0
    artifacts: list[Path] = []
    last_call_at: float | None = None

    while totalfound is None or captured < totalfound:
        if calls >= daily_call_limit:
            raise RetrievalError("daily API call limit would be exceeded")
        if last_call_at is not None:
            delay = pace_seconds - (time.monotonic() - last_call_at)
            if delay > 0:
                sleeper(delay)

        params = {"apikey": api_key, "querytext": query, "max_records": max_records, "start_record": start_record}
        request = Request(f"{ENDPOINT}?{urlencode(params)}", headers={"Accept": "application/json"})
        payload_bytes: bytes | None = None
        for attempt in range(retries + 1):
            if calls >= daily_call_limit:
                raise RetrievalError("daily API call limit would be exceeded")
            calls += 1
            last_call_at = time.monotonic()
            try:
                with opener(request, timeout=60) as response:
                    payload_bytes = response.read()
                break
            except HTTPError as error:
                if error.code not in TRANSIENT_STATUS_CODES or attempt == retries:
                    raise RetrievalError(redact_secret(f"IEEE API HTTP failure: {error}", api_key)) from None
                wait = _read_retry_after(error.headers) or min(30.0, 2**attempt)
                sleeper(wait)
            except (URLError, TimeoutError, OSError) as error:
                if attempt == retries:
                    raise RetrievalError(redact_secret(f"IEEE API transport failure: {error}", api_key)) from None
                sleeper(min(30.0, 2**attempt))
        if payload_bytes is None:
            raise RetrievalError("IEEE API returned no response")
        if api_key.encode() in payload_bytes:
            raise RetrievalError("API key appeared in the response; raw artifact was not written")
        try:
            payload = json.loads(payload_bytes)
        except json.JSONDecodeError as error:
            raise RetrievalError(f"IEEE API returned invalid JSON: {error.msg}") from None
        page_total, page_articles = validate_response(payload)
        if totalfound is None:
            totalfound = page_total
            required_calls = planned_call_count(totalfound, max_records)
            if required_calls > daily_call_limit:
                raise RetrievalError(
                    f"retrieval requires {required_calls} API calls, above daily limit {daily_call_limit}"
                )
        elif page_total != totalfound:
            raise RetrievalError("API totalfound changed during retrieval")

        artifact = api_artifact_path(raw_dir, query_id, timestamp, start_record)
        artifact.write_bytes(payload_bytes)
        artifacts.append(artifact)
        returned = len(page_articles)
        captured += returned
        if captured > totalfound:
            raise RetrievalError("raw captured record count exceeds totalfound")
        if captured < totalfound and (returned == 0 or returned < max_records):
            raise RetrievalError("incomplete retrieval: API returned an unexpected short page")
        start_record += returned
        if returned == 0 and captured < totalfound:
            raise RetrievalError("incomplete retrieval: pagination made no progress")

    summary = RetrievalSummary(totalfound, captured, calls, tuple(artifacts))
    if not summary.reconciled:
        raise RetrievalError("raw captured record count does not reconcile with totalfound")
    return summary


def evaluate_equivalence(
    *,
    web_query_id: str,
    web_field_strategy: str,
    api_representation: str,
    api_totalfound: int,
    known_web_count: int,
    web_identifiers: Iterable[str],
    api_identifiers: Iterable[str],
    api_author_keywords_supported: bool,
) -> dict[str, Any]:
    web_ids = set(web_identifiers)
    api_ids = set(api_identifiers)
    count_match = api_totalfound == known_web_count
    field_match = web_field_strategy == "Document Title; Abstract; Author Keywords"
    representation_present = bool(api_representation.strip())
    sample_match = web_ids == api_ids and bool(web_ids)
    equivalent = (
        count_match
        and field_match
        and representation_present
        and sample_match
        and api_author_keywords_supported
    )
    return {
        "web_query_id": web_query_id,
        "web_field_strategy": web_field_strategy,
        "api_representation": api_representation,
        "known_web_count": known_web_count,
        "api_totalfound": api_totalfound,
        "count_match": count_match,
        "api_representation_present": representation_present,
        "stable_identifier_sample_match": sample_match,
        "api_author_keywords_supported": api_author_keywords_supported,
        "equivalence": equivalent,
        "status": "equivalent" if equivalent else "pending validation",
    }


def dry_run(
    *,
    query_id: str,
    query_reference: str,
    max_records: int,
    raw_dir: Path,
    daily_call_limit: int,
    expected_totalfound: int | None = None,
) -> str:
    validate_max_records(max_records)
    calls = (
        str(planned_call_count(expected_totalfound, max_records))
        if expected_totalfound is not None
        else "unknown until totalfound is returned"
    )
    lines = [
        "IEEE Metadata API dry-run",
        f"Query ID: {query_id}",
        f"Endpoint: {ENDPOINT}",
        f"Query representation placeholder/reference: {query_reference}",
        f"Max records/request: {max_records}",
        f"Expected pagination: start_record=1, then advance by returned record count; planned calls: {calls}",
        f"Daily call preflight limit: {daily_call_limit}",
        f"Intended raw-output directory: {raw_dir}",
        "Intended raw filename: <QUERY-ID>__run-<UTC-timestamp>__api-start-<start-record>.json",
        "API execution: no (dry-run)",
    ]
    return "\n".join(lines)


def _json_strings(path: Path) -> list[str]:
    value = json.loads(path.read_text(encoding="utf-8"))
    if not isinstance(value, list) or not all(isinstance(item, str) for item in value):
        raise ValueError(f"identifier sample must be a JSON string array: {path}")
    return value


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--query-id", required=True)
    parser.add_argument("--max-records", type=int, default=DEFAULT_MAX_RECORDS)
    parser.add_argument("--raw-dir", type=Path, default=Path("research/raw/systematic-search"))
    parser.add_argument("--daily-call-limit", type=int, default=DEFAULT_DAILY_CALL_LIMIT)
    parser.add_argument("--expected-totalfound", type=int)
    parser.add_argument("--dry-run", action="store_true")
    parser.add_argument("--query")
    parser.add_argument("--query-reference")
    parser.add_argument("--validate-equivalence", action="store_true")
    parser.add_argument("--web-field-strategy", default="Document Title; Abstract; Author Keywords")
    parser.add_argument("--known-web-count", type=int, default=4798)
    parser.add_argument("--api-totalfound", type=int)
    parser.add_argument("--web-identifiers", type=Path)
    parser.add_argument("--api-identifiers", type=Path)
    parser.add_argument("--api-author-keywords-supported", action="store_true")
    return parser


def main(argv: Sequence[str] | None = None) -> int:
    args = build_parser().parse_args(argv)
    try:
        if args.validate_equivalence:
            if args.api_totalfound is None or not args.web_identifiers or not args.api_identifiers:
                raise ValueError("equivalence validation requires API totalfound and both identifier samples")
            result = evaluate_equivalence(
                web_query_id=args.query_id,
                web_field_strategy=args.web_field_strategy,
                api_representation=args.query_reference or "not supplied",
                api_totalfound=args.api_totalfound,
                known_web_count=args.known_web_count,
                web_identifiers=_json_strings(args.web_identifiers),
                api_identifiers=_json_strings(args.api_identifiers),
                api_author_keywords_supported=args.api_author_keywords_supported,
            )
            print(json.dumps(result, indent=2, sort_keys=True))
            return 0 if result["equivalence"] else 2
        if args.dry_run:
            print(dry_run(
                query_id=args.query_id,
                query_reference=args.query_reference or "not supplied",
                max_records=args.max_records,
                raw_dir=args.raw_dir,
                daily_call_limit=args.daily_call_limit,
                expected_totalfound=args.expected_totalfound,
            ))
            return 0
        query = args.query
        if not query:
            raise ValueError("--query is required unless --dry-run or --validate-equivalence is used")
        api_key = os.environ.get(API_KEY_ENV, "")
        summary = retrieve(
            query_id=args.query_id,
            query=query,
            api_key=api_key,
            raw_dir=args.raw_dir,
            max_records=args.max_records,
            daily_call_limit=args.daily_call_limit,
            expected_totalfound=args.expected_totalfound,
        )
        print(json.dumps({
            "totalfound": summary.totalfound,
            "raw_captured_records": summary.raw_captured_records,
            "api_calls": summary.api_calls,
            "raw_artifacts": [str(path) for path in summary.artifacts],
            "reconciliation": "Complete" if summary.reconciled else "Incomplete",
        }, indent=2))
        return 0
    except (ValueError, RetrievalError) as error:
        print(f"error: {redact_secret(error, os.environ.get(API_KEY_ENV))}", file=sys.stderr)
        return 2


if __name__ == "__main__":
    raise SystemExit(main())
