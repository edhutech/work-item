"""Local-first preparation tools for review normalization and screening.

This module never reads a database export. Callers must provide records
explicitly, so future execution can enforce the private raw-data boundary.
"""

from __future__ import annotations

import hashlib
import json
import re
import unicodedata
from dataclasses import dataclass, field
from difflib import SequenceMatcher
from enum import Enum
from typing import Any, Iterable, Mapping
from urllib.parse import urlsplit, urlunsplit


class ScreeningState(str, Enum):
    UNSCREENED = "UNSCREENED"
    INCLUDE = "INCLUDE"
    EXCLUDE = "EXCLUDE"
    UNCERTAIN = "UNCERTAIN"
    NEEDS_FULL_TEXT = "NEEDS_FULL_TEXT"


class MatchClass(str, Enum):
    NON_MATCH = "NON_MATCH"
    EXACT_DUPLICATE = "EXACT_DUPLICATE"
    PROBABLE_DUPLICATE = "PROBABLE_DUPLICATE"
    HUMAN_REVIEW = "HUMAN_REVIEW"


EXCLUSION_REASONS = frozenset(
    {
        "out of scope",
        "duplicate",
        "insufficient method",
        "insufficient source information",
        "not evidence for the claimed use",
        "other documented reason",
    }
)

UNCERTAINTY_REASONS = frozenset(
    {
        "ambiguous relevance",
        "missing abstract",
        "uncertain publication relationship",
        "uncertain duplicate match",
        "coding-agent versus indirect traditional-SE relevance",
        "consequential exclusion",
    }
)

VERSION_RELATIONSHIPS = frozenset(
    {
        "PREPRINT_OF",
        "EXTENDED_VERSION_OF",
        "UPDATED_VERSION_OF",
        "RELATED_VERSION",
    }
)


def _text(value: Any) -> str:
    return "" if value is None else str(value)


def normalize_doi(value: Any) -> str:
    """Normalize a DOI for exact matching without changing its source value."""
    doi = _text(value).strip()
    doi = re.sub(r"^doi:\s*", "", doi, flags=re.I)
    doi = re.sub(r"^https?://(?:dx\.)?doi\.org/", "", doi, flags=re.I)
    return doi.rstrip(" .;,").casefold()


def normalize_title(value: Any) -> str:
    """Normalize title syntax only; technical words are never removed."""
    title = unicodedata.normalize("NFKC", _text(value)).casefold()
    title = re.sub(r"\s+", " ", title).strip()
    title = re.sub(r"[^\w\s]", " ", title, flags=re.UNICODE)
    return re.sub(r"\s+", " ", title).strip()


def normalize_url(value: Any) -> str:
    url = _text(value).strip()
    if not url:
        return ""
    parts = urlsplit(url)
    return urlunsplit((parts.scheme.casefold(), parts.netloc.casefold(), parts.path, parts.query, ""))


def _first_author(authors: Any) -> str:
    if isinstance(authors, str):
        return normalize_title(authors.split(";")[0])
    if isinstance(authors, (list, tuple)) and authors:
        first = authors[0]
        return normalize_title(first.get("name", first) if isinstance(first, Mapping) else first)
    return ""


def _stable_json(value: Any) -> str:
    return json.dumps(value, sort_keys=True, ensure_ascii=True, separators=(",", ":"), default=str)


def _short_hash(value: Any) -> str:
    return hashlib.sha256(_stable_json(value).encode("utf-8")).hexdigest()[:16]


def _source_record_key(raw: Mapping[str, Any]) -> tuple[str, Any]:
    source_id = _text(raw.get("source_record_id")).strip()
    if source_id:
        return "source-record", source_id
    return "metadata-fallback", {
        "title": normalize_title(raw.get("title")),
        "year": raw.get("publication_year"),
        "first_author": _first_author(raw.get("authors")),
        "locator": normalize_url(raw.get("url")),
    }


@dataclass(frozen=True)
class RetrievedRecord:
    """Immutable-in-practice source record plus matching-only normalized values."""

    record_id: str
    source_database: str
    query_id: str
    run_identifier: str
    source_record_id: str
    original_metadata: Mapping[str, Any]
    normalized_doi: str
    normalized_title: str
    normalized_first_author: str
    publication_year: int | None
    normalized_url: str
    publication_venue: str
    publication_type: str
    publication_status: str
    peer_review_status: str
    provenance_references: tuple[str, ...]


@dataclass(frozen=True)
class SourceGroup:
    source_id: str
    record_ids: tuple[str, ...]


@dataclass(frozen=True)
class MatchDecision:
    left_record_id: str
    right_record_id: str
    classification: MatchClass
    rule: str
    requires_human_confirmation: bool
    rationale: str


@dataclass(frozen=True)
class VersionRelationship:
    source_id: str
    related_source_id: str
    relationship: str
    human_confirmed: bool
    rationale: str


@dataclass(frozen=True)
class VersionFamily:
    version_family_id: str
    source_ids: tuple[str, ...]
    relationships: tuple[VersionRelationship, ...]


@dataclass(frozen=True)
class ScreeningDecision:
    source_id: str
    stage: str
    state: ScreeningState
    actor: str
    exclusion_reason: str | None = None
    uncertainty_reason: str | None = None
    rationale: str = ""
    supersedes_decision_id: str | None = None
    decision_id: str = ""


@dataclass
class PipelineResult:
    records: list[RetrievedRecord]
    groups: list[SourceGroup]
    matches: list[MatchDecision]
    audit_events: list[dict[str, Any]] = field(default_factory=list)


def build_retrieved_record(raw: Mapping[str, Any]) -> RetrievedRecord:
    """Assign a deterministic retrieved-record ID before deduplication."""
    required = ("source_database", "query_id", "run_identifier")
    missing = [key for key in required if not _text(raw.get(key)).strip()]
    if missing:
        raise ValueError(f"missing retrieval provenance: {', '.join(missing)}")
    key_type, key_value = _source_record_key(raw)
    identity = {
        "database": _text(raw["source_database"]).strip().casefold(),
        "query_id": _text(raw["query_id"]).strip(),
        "run": _text(raw["run_identifier"]).strip(),
        "key_type": key_type,
        "key": key_value,
    }
    original = dict(raw)
    year = raw.get("publication_year")
    if year is not None:
        try:
            year = int(year)
        except (TypeError, ValueError) as exc:
            raise ValueError("publication_year must be an integer or null") from exc
    return RetrievedRecord(
        record_id=f"REC-{_short_hash(identity)}",
        source_database=_text(raw["source_database"]).strip(),
        query_id=_text(raw["query_id"]).strip(),
        run_identifier=_text(raw["run_identifier"]).strip(),
        source_record_id=_text(raw.get("source_record_id")).strip(),
        original_metadata=original,
        normalized_doi=normalize_doi(raw.get("doi")),
        normalized_title=normalize_title(raw.get("title")),
        normalized_first_author=_first_author(raw.get("authors")),
        publication_year=year,
        normalized_url=normalize_url(raw.get("url")),
        publication_venue=_text(raw.get("publication_venue")).strip(),
        publication_type=_text(raw.get("publication_type")).strip(),
        publication_status=_text(raw.get("publication_status")).strip(),
        peer_review_status=_text(raw.get("peer_review_status")).strip(),
        provenance_references=tuple(str(item) for item in raw.get("provenance_references", ()) if str(item).strip()),
    )


def normalization_audit_event(record: RetrievedRecord) -> dict[str, Any]:
    """Return provenance for the normalization transformation."""
    return {
        "event": "RECORD_NORMALIZED",
        "record_id": record.record_id,
        "source_database": record.source_database,
        "query_id": record.query_id,
        "run_identifier": record.run_identifier,
        "source_record_id": record.source_record_id,
        "provenance_references": list(record.provenance_references),
    }


def classify_match(left: RetrievedRecord, right: RetrievedRecord) -> MatchDecision:
    """Classify a pair conservatively; only exact identifiers auto-merge."""
    pair = (left.record_id, right.record_id)
    if left.normalized_doi and left.normalized_doi == right.normalized_doi:
        return MatchDecision(*pair, MatchClass.EXACT_DUPLICATE, "exact normalized DOI", False, "DOI equality")

    left_ids = left.original_metadata.get("stable_identifiers", {})
    right_ids = right.original_metadata.get("stable_identifiers", {})
    if isinstance(left_ids, Mapping) and isinstance(right_ids, Mapping):
        shared = {
            str(key): _text(value).strip().casefold()
            for key, value in left_ids.items()
            if _text(value).strip() and _text(right_ids.get(key)).strip().casefold() == _text(value).strip().casefold()
        }
        if shared:
            return MatchDecision(*pair, MatchClass.EXACT_DUPLICATE, "exact database-independent stable identifier", False, _stable_json(shared))

    if left.normalized_title and left.normalized_title == right.normalized_title:
        same_author = bool(left.normalized_first_author and left.normalized_first_author == right.normalized_first_author)
        same_year = left.publication_year is not None and left.publication_year == right.publication_year
        if same_author and same_year:
            return MatchDecision(*pair, MatchClass.EXACT_DUPLICATE, "exact normalized title + year + first author", False, "conservative bibliographic equality")
        return MatchDecision(*pair, MatchClass.HUMAN_REVIEW, "exact normalized title with conflicting or missing context", True, "same title is insufficient without compatible year and author")

    if left.normalized_title and right.normalized_title:
        similarity = SequenceMatcher(None, left.normalized_title, right.normalized_title).ratio()
        if similarity >= 0.92 and (left.normalized_first_author == right.normalized_first_author or not left.normalized_first_author or not right.normalized_first_author):
            return MatchDecision(*pair, MatchClass.PROBABLE_DUPLICATE, "high title similarity", True, f"title similarity={similarity:.3f}")
    return MatchDecision(*pair, MatchClass.NON_MATCH, "no deterministic match", False, "identifiers and conservative title checks did not agree")


def _union_find(items: Iterable[str]) -> tuple[dict[str, str], Any]:
    parent = {item: item for item in items}

    def find(item: str) -> str:
        while parent[item] != item:
            parent[item] = parent[parent[item]]
            item = parent[item]
        return item

    def union(left: str, right: str) -> None:
        root_left, root_right = find(left), find(right)
        if root_left != root_right:
            parent[max(root_left, root_right)] = min(root_left, root_right)

    return parent, (find, union)


def deduplicate(records: Iterable[RetrievedRecord], confirmed_pairs: Iterable[frozenset[str]] = ()) -> PipelineResult:
    """Create groups from automatic matches and explicitly confirmed pairs."""
    ordered = sorted(records, key=lambda record: record.record_id)
    parent, (find, union) = _union_find(record.record_id for record in ordered)
    matches: list[MatchDecision] = []
    confirmed = set(confirmed_pairs)
    for index, left in enumerate(ordered):
        for right in ordered[index + 1 :]:
            decision = classify_match(left, right)
            if decision.classification == MatchClass.EXACT_DUPLICATE or frozenset((left.record_id, right.record_id)) in confirmed:
                union(left.record_id, right.record_id)
            matches.append(decision)

    grouped: dict[str, list[str]] = {}
    for record in ordered:
        grouped.setdefault(find(record.record_id), []).append(record.record_id)
    groups = []
    for record_ids in sorted(grouped.values()):
        identity_records = [record for record in ordered if record.record_id in record_ids]
        strongest = next((record.normalized_doi for record in identity_records if record.normalized_doi), None)
        if strongest:
            identity = ("doi", strongest)
        else:
            first = identity_records[0]
            identity = ("bibliographic", first.normalized_title, first.publication_year, first.normalized_first_author)
        groups.append(SourceGroup(f"SRC-{_short_hash(identity)}", tuple(sorted(record_ids))))
    events = [
        {
            "event": "MATCH_CLASSIFIED",
            "record_ids": [match.left_record_id, match.right_record_id],
            "rule": match.rule,
            "classification": match.classification.value,
            "requires_human_confirmation": match.requires_human_confirmation,
            "provenance": {
                record.record_id: {
                    "source_database": record.source_database,
                    "query_id": record.query_id,
                    "run_identifier": record.run_identifier,
                    "source_record_id": record.source_record_id,
                }
                for record in ordered
                if record.record_id in {match.left_record_id, match.right_record_id}
            },
        }
        for match in matches
    ]
    events.extend(
        {
            "event": "SOURCE_GROUP_ASSIGNED",
            "source_id": group.source_id,
            "record_ids": list(group.record_ids),
            "provenance": [normalization_audit_event(record) for record in ordered if record.record_id in group.record_ids],
        }
        for group in groups
    )
    return PipelineResult(ordered, groups, matches, events)


def link_version(source_id: str, related_source_id: str, relationship: str, rationale: str, *, human_confirmed: bool = False) -> VersionRelationship:
    if relationship not in VERSION_RELATIONSHIPS:
        raise ValueError(f"unsupported publication relationship: {relationship}")
    if source_id == related_source_id:
        raise ValueError("a source cannot be related to itself")
    if not human_confirmed:
        raise ValueError("publication-version relationships require human confirmation")
    if not rationale.strip():
        raise ValueError("publication-version relationships require a rationale")
    return VersionRelationship(source_id, related_source_id, relationship, human_confirmed, rationale)


def build_version_family(relationships: Iterable[VersionRelationship]) -> VersionFamily:
    """Assign a family ID only from explicitly confirmed version links."""
    ordered = tuple(relationships)
    if not ordered:
        raise ValueError("a version family requires at least one relationship")
    if not all(item.human_confirmed for item in ordered):
        raise ValueError("version families require human-confirmed relationships")
    source_ids = tuple(sorted({source_id for item in ordered for source_id in (item.source_id, item.related_source_id)}))
    return VersionFamily(f"VER-{_short_hash(source_ids)}", source_ids, ordered)


def validate_screening_decision(decision: ScreeningDecision) -> None:
    if decision.stage not in {"TITLE_ABSTRACT", "FULL_TEXT"}:
        raise ValueError("unsupported screening stage")
    if decision.actor not in {"agent_recommendation", "human", "second_pass_human"}:
        raise ValueError("unsupported decision actor")
    if decision.state == ScreeningState.EXCLUDE:
        if decision.exclusion_reason not in EXCLUSION_REASONS:
            raise ValueError("EXCLUDE requires a protocol exclusion reason")
        if decision.exclusion_reason == "duplicate" and not decision.rationale.strip():
            raise ValueError("duplicate exclusion requires a relationship or group rationale")
    elif decision.exclusion_reason is not None:
        raise ValueError("exclusion reason is only valid for EXCLUDE")
    if decision.uncertainty_reason is not None and decision.uncertainty_reason not in UNCERTAINTY_REASONS:
        raise ValueError("unsupported uncertainty reason")
    if decision.state in {ScreeningState.UNCERTAIN, ScreeningState.NEEDS_FULL_TEXT} and not decision.uncertainty_reason:
        raise ValueError("uncertain or full-text states require an uncertainty reason")
    if decision.actor == "agent_recommendation" and decision.state in {ScreeningState.INCLUDE, ScreeningState.EXCLUDE}:
        raise ValueError("agent recommendations cannot be final consequential decisions")
    if not decision.decision_id:
        raise ValueError("every screening decision requires a decision_id")


def second_pass_queue(decisions: Iterable[ScreeningDecision]) -> list[ScreeningDecision]:
    """Return decisions needing human confirmation without claiming dual screening."""
    queue = []
    for decision in decisions:
        validate_screening_decision(decision)
        if decision.state in {ScreeningState.EXCLUDE, ScreeningState.UNCERTAIN, ScreeningState.NEEDS_FULL_TEXT} or decision.uncertainty_reason == "consequential exclusion":
            queue.append(decision)
    return queue


def validate_decision_log(decisions: Iterable[ScreeningDecision]) -> None:
    seen: set[str] = set()
    for decision in decisions:
        validate_screening_decision(decision)
        if decision.decision_id in seen:
            raise ValueError(f"duplicate decision_id: {decision.decision_id}")
        seen.add(decision.decision_id)
        if decision.supersedes_decision_id and decision.supersedes_decision_id not in seen:
            raise ValueError("superseded decision must precede its replacement")
