# Systematic Review Pipeline Preparation

## Scope and activation gate

This document prepares normalization, deduplication, publication-version
linking, and title/abstract screening under Research Protocol v1.1. No real
Scopus, IEEE, or other database record is processed by the tooling or tests in
this change. The fixtures are synthetic.

The pipeline may be activated only after the relevant Protocol v1.1 retrieval
set is closed for the stage being calibrated. For calibration this means that
the eligible cross-database retrieval set is known. The pipeline does not
freeze a stopping/expansion rule, estimate marginal contribution, decide on
Supplementary branches, or reinterpret completed retrievals.

## Stage boundary

`Retrieval -> normalization -> deduplication -> title/abstract screening ->
full-text screening -> quality assessment -> evidence extraction -> synthesis`

This change prepares only normalization, deduplication, version relationships,
and title/abstract-screening contracts. Full-text screening, quality
assessment, extraction, and synthesis remain later protocol stages.

## Identity model

Each retrieved database row receives a deterministic `REC-<hash>` retrieved-
record ID before deduplication. The hash uses source database, Query ID, run,
and the source record identifier, with a documented metadata fallback when the
database has no record identifier. It is not a row number and contains no
personal information.

Deduplication then assigns a `SRC-<hash>` Source ID to each deduplicated source
group. A Source ID is independent of database naming and is stable after the
input snapshot and grouping decision are frozen. Retrieved-record IDs remain
attached to the group so every database provenance remains recoverable.
The Source ID is also the duplicate-group identifier. Confirmed publication
relationships can later assign a separate `VER-<hash>` version-family ID;
version families never replace duplicate groups.

Original source metadata is retained in `original_metadata`. The canonical
record also carries optional venue, publication type/status, peer-review status,
and provenance references when supplied. Normalized DOI, title, first-author,
year, and URL values are matching-only fields; they never overwrite source
values. Human decisions are separate records.

## Matching hierarchy

The implementation evaluates pairs in this conservative order:

1. Exact normalized DOI: automatic `EXACT_DUPLICATE`.
2. Exact shared database-independent stable identifier namespace/value:
   automatic `EXACT_DUPLICATE`.
3. Exact normalized title plus compatible publication year and first author:
   automatic `EXACT_DUPLICATE`.
4. Exact title with missing or conflicting context: `HUMAN_REVIEW`.
5. High title similarity with compatible or missing author context:
   `PROBABLE_DUPLICATE`, requiring human confirmation.
6. Otherwise: `NON_MATCH`.

Vague title similarity, overlapping authors, nearby years, or missing fields do
not automatically merge records. Every pair classification records its rule,
rationale, and whether confirmation is required. Confirmed probable matches
must be supplied explicitly; no semantic or LLM matching is performed.

Normalization uses Unicode NFKC, case folding, whitespace and punctuation
normalization, DOI prefix removal, and URL host/scheme normalization. It does
not remove technical tokens or semantically rewrite titles.

## Publication versions

Exact duplicate indexing is distinct from publication relationships. Supported
relationships are `PREPRINT_OF`, `EXTENDED_VERSION_OF`, `UPDATED_VERSION_OF`,
and `RELATED_VERSION`. Version relationships do not merge source groups and
require a human-confirmed rationale. The preferred later peer-reviewed version,
when established under later review, remains linked to its predecessor rather
than erasing predecessor provenance.

## Screening contract

The title/abstract state vocabulary is `UNSCREENED`, `INCLUDE`, `EXCLUDE`,
`UNCERTAIN`, and `NEEDS_FULL_TEXT`. A decision records Source ID, stage, state,
actor, rationale, decision ID, optional uncertainty/exclusion reason, and any
superseded decision ID.

Actors are `agent_recommendation`, `human`, and `second_pass_human`. Agent
recommendations cannot be final consequential INCLUDE or EXCLUDE decisions.
The human researcher remains responsible for final decisions. This pipeline
does not claim independent dual screening or inter-rater reliability.

Protocol exclusion reasons are:

- `out of scope`
- `duplicate`
- `insufficient method`
- `insufficient source information`
- `not evidence for the claimed use`
- `other documented reason`

Operational uncertainty reasons include ambiguous relevance, missing abstract,
uncertain publication relationship, uncertain duplicate match, indirect
traditional-software-engineering relevance, and consequential exclusion.
Contradictory evidence is not an exclusion reason.

The second-pass queue includes exclusions, uncertain decisions, and
`NEEDS_FULL_TEXT` decisions. A second pass supersedes rather than overwrites
the first decision. The audit log must retain the first recommendation, human
decision, uncertainty reason, second-pass review, and final human decision.

## Audit and data boundary

Future derived artifacts must retain database, Query ID, run identifier,
retrieved-record ID, source locator, matching rule, group ID, relationship,
screening decision, exclusion reason, actor, and review linkage. The tooling's
normalization, match, and group audit events carry this retrieval provenance;
screening decisions carry decision and supersession provenance. Raw licensed
files remain immutable and private. This public repository contains only the
tooling, schemas/contracts, documentation, and synthetic fixtures from this
preparation task.
