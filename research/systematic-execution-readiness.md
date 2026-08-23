# Systematic Execution Readiness v1.1

**Audit date:** 2026-08-20

**Scope:** Final readiness audit before systematic search execution. This artifact records execution controls only. It does not execute a query, collect a systematic result count, export a result set, create a corpus, assign Source IDs, deduplicate, screen, extract evidence, or synthesize findings.

## Authorities And Current State

The authority chain is coherent when current and historical material are distinguished:

- [`protocol.md`](./protocol.md) defines the v1.1 research method, search sources, tiered execution, time and publication principles, record collection, deduplication, screening, and traceability requirements.
- [`systematic-search-log.md`](./systematic-search-log.md) is the authoritative execution record. The older [`search-log.md`](./search-log.md) remains the historical pilot/calibration record.
- [`systematic-search-design.md`](./systematic-search-design.md) defines branch purposes, database adaptations, execution-unit fields, collection, deduplication, and screening handoff.
- [`database-validation.md`](./database-validation.md) defines verified database capabilities and the ACM manual-capture workflow.
- [`systematic-queries.md`](./systematic-queries.md) is the frozen executable-query authority. Its v1 freeze audit records the current branch statuses and query inventory.

The repository contains historical pre-freeze wording such as `Requires further calibration` for F6B1/F6B2 and historical pre-validation statements about ACM export. The later focused calibration, frozen-query manifest, and completed ACM validation supersede those statements for execution. They are documentation history, not current execution instructions. No methodological contradiction remains in the current frozen specification.

## Readiness Summary

| Area | Classification | Finding |
|---|---|---|
| Research questions and protocol | Ready | Current questions, evidence boundaries, retrieval sequence, and traceability rules are documented. |
| Branch inventory | Ready | 28 branches: 22 Primary and 6 Supplementary. |
| Frozen queries | Ready | The inventory distinguishes 213 active executable Query IDs, 33 historical/superseded IEEE v1 IDs, and 246 total defined IDs. |
| Database access and search | Ready with documented limitation | Scopus is the systematic core. Additional databases require the v1.1 feasibility gate before seven-branch calibration. |
| Raw capture | Ready with documented limitation | Export/capture controls are defined; ACM requires high-burden manual capture in Basic Edition. |
| Execution logging | Ready with documented limitation | `systematic-search-log.md` is the designated execution source of truth; raw artifact references must be added with each execution record. |
| Raw storage and naming | Ready with documented limitation | The convention below must be used when raw artifacts are first created. No raw artifact is created by this audit. |
| Methodological consistency | Ready | Historical wording is identified and does not override current frozen decisions. |
| Scopus API support | Validated with service-level limitation | Standard non-cursor retrieval is operational when the complete result set fits the available service-level limits. Query `S1-F1-SCOPUS-01-v1` matched the Web count and a 10-record EID+DOI sample; exact-query and raw-provenance controls remain mandatory. |
| Scopus large-result pagination | Web fallback required when API completion is unavailable | Cursor support exists in the utility but is restricted by the currently available entitlement. Do not claim API retrieval of result sets above 5,000; use the validated Scopus Web CSV workflow instead. |
| Unresolved blocker | None for planned Web execution | The API limitation does not block systematic execution because Scopus Web provides the validated complete-retrieval path; F2A is handed off to Scopus Web. |

## Branch And Query Audit

The frozen artifact confirms all 28 branches occur exactly once. The six Supplementary branches are exactly:

- F3C;
- F4C2;
- F6B1;
- F6B2;
- F6C2;
- F7E.

All other branches are Primary. F6B1 and F6B2 are bounded Supplementary searches, not unresolved branches. Planning remains distinct from agent-side functional decomposition, delegation, and trajectory analysis. No excluded generic planning, generic task decomposition, generic allocation, or unqualified evaluation umbrella has silently returned.

The frozen branch inventory confirms 28 branches: 22 Primary and 6 Supplementary. Protocol v1.1 plans all 22 Primary branches for Scopus. It does not automatically execute the six Supplementary branches or assign all Primary branches to any additional database.

The current query accounting is:

- 168 conceptual branch/database combinations;
- 213 active executable Query IDs;
- 33 historical/superseded IEEE v1 Query IDs;
- 246 total defined Query IDs.

The historical generated register and versioned IEEE correction records remain intact. The frozen Query ID audit confirms:

- 213 active IDs are accounted for across the six databases and versioned IEEE corrections;
- 33 original IEEE v1 IDs remain historical/superseded;
- active IDs retain their recorded query versions, including corrected IEEE `v1.1` successors; historical IEEE `v1` IDs remain separately identified;
- every ID maps to one branch and one database;
- F6B1 and F6B2 have two deliberate variants per database;
- F7C has four deliberate variants per database;
- all other branch/database pairs have one variant;
- every branch has all intended database adaptations or the documented F6 variant register;
- no query was silently edited after freeze.

The execution unit is **one selected frozen Query ID executed once against its assigned database**. It is not a branch, a database result record, or a deduplicated source. Query IDs not selected by the tiered policy remain available for conditional expansion; no first-pass full-factorial execution scale is prescribed.

The conceptual core/calibration envelope before conditional expansion is up to 57 branch/database executions: 22 Primary Scopus executions plus up to seven calibration branches in each of five additional databases. This is not an unconditional minimum. Feasibility validation events are not systematic corpus executions.

## Database Readiness

| Database | Classification | Execution condition |
|---|---|---|
| Scopus | Ready with documented limitation | Advanced and fielded search and CSV export are verified. Institutional authenticated access and export batching must be recorded; large result sets that cannot be completed through the API use Scopus Web. |
| Web of Science Core Collection | Feasibility gate required before calibration | Advanced search and structured Email Full Record export are historically verified. The v1.1 gate must establish route completeness and record the 1,000-record batch and entitlement limitations. |
| ScienceDirect | Feasibility gate required before calibration | Search and citation export are historically verified. The combined Title/Abstract/Author-Keywords field must be used and API equivalence must not be assumed. |
| IEEE Xplore | Feasibility gate required before calibration | Public advanced/command search and export are historically verified. The v1.1 gate must validate any official API route separately; corrected web representations remain versioned. |
| ACM Digital Library | Separate capture-feasibility gate required before calibration | Basic Edition search is verified, but complete systematic capture must first be demonstrated through the approved manual workflow or authorized Premium export. |
| Springer Nature Link | Feasibility gate required before calibration | Public search and CSV export are historically verified. The v1.1 gate must record body-inclusive Keywords semantics, reduced metadata, pagination, and entitlement. |

No paid access is newly required for systematic identification. Paid full-text access remains a later screening/retrieval concern, not an execution blocker.

## Raw Result And Provenance Controls

Before deduplication or screening, every execution must preserve, at minimum:

- database;
- frozen Query ID;
- branch and query version;
- exact executed query or UI expression and selected fields;
- execution date and time;
- access edition or generic access type where relevant;
- database-reported result count;
- active sort/order state and filters;
- raw exported or manually captured result artifact reference;
- execution status;
- operational notes, errors, and rerun relationship where applicable.

The raw artifact must preserve the database output or ACM manual capture as received/captured. Normalization and metadata enrichment are separate stages. A raw record must not be dropped because it looks irrelevant, lacks an optional DOI, or duplicates another result. A later record may retain multiple query and database origins.

For ACM specifically, the raw capture must include the frozen Query ID, execution timestamp, reported total, active sort/order state, consistent page size, exhaustive page traversal, result position, raw title, and stable ACM record URL. DOI, ISBN, ACM identifier, author/editor, venue, date, content type, abstract, and other metadata are retained when available or applicable. A stable ACM URL is the mandatory fallback locator when DOI is absent or inapplicable. Captured raw count must equal the ACM-reported total before deduplication; incomplete or failed capture is not marked completed.

Crossref and OpenAlex may enrich a record only after ACM or another protocol database has identified and preserved it. They must not discover replacement records, replace the originating database, overwrite raw fields, change query provenance, or remove a record after enrichment failure.

## Raw Storage And Naming

The repository does not yet contain systematic raw-result files or a competing raw-data convention. To keep future retrieval separate from evidence and literature artifacts, raw systematic outputs should be staged under the planned directory `research/raw/systematic-search/` when execution begins. This audit does not create that directory or populate it.

Use one execution-instance artifact name of the form:

`<frozen-query-id>__run-<UTC-timestamp>.<format>`

Examples of formats are `csv`, `txt`, `ris`, `email`, or `manual.csv`; the extension describes the captured format and must not imply that a database supplied a format it did not supply. For ACM manual capture, the artifact or row set must additionally preserve page and position provenance. The frozen Query ID already encodes branch, database, sequence, and query version; the run timestamp distinguishes reruns. The `systematic-search-log.md` execution entry must reference the raw artifact name and report its status.

This is an operational naming/storage convention, not a corpus schema. Raw files remain retrieval artifacts and must not be placed in `evidence/`, literature notes, or final included-source records. The `systematic-search-log.md` execution entry must reference the raw artifact name and report its status.

## Execution Log And Status Rules

The search design designates [`systematic-search-log.md`](./systematic-search-log.md) as the place for systematic execution records. Historical and v1.1 execution records remain in that log, and each execution record can and must contain:

- frozen Query ID / Search ID;
- database and branch;
- execution date and time;
- exact query, fields, filters, time coverage, and publication filters;
- query version;
- database-reported result count;
- raw artifact reference;
- execution status;
- operational notes and errors;
- rerun relationship when applicable.

The permitted execution states are `Completed`, `Partial`, `Failed`, and `Requires rerun`. A partial export or incomplete ACM page traversal is never `Completed`. Batch completion requires reconciliation to the database-reported count where the database supplies one; if reconciliation is unavailable, the limitation must be recorded rather than concealed.

The v1.1 order is staged: Scopus Primary core; feasibility validation for each additional database; seven-branch calibration for databases that pass; then branch-sensitive conditional expansion. This is a methodological sequence, not a database ranking. An interruption may resume only from an explicitly recorded incomplete unit; it must not overwrite the original execution record.

Reruns retain the original Query ID, a new execution timestamp and raw artifact, the reason for rerun, the result count, and whether the query version changed. A rerun does not erase the original. If a query fails because the interface has drifted, stop that query, record the syntax/interface issue, distinguish syntax drift from conceptual failure, and do not silently adapt the frozen query. Any correction follows the frozen revision rules: syntax-only correction is explicitly versioned as `v1.1`; a retrieval-method or conceptual change is versioned as `v2`, with affected units, expected recall/precision effect, rerun decision, and comparability impact recorded.

## Boundaries

Systematic execution is identification only. It must not perform deduplication, relevance screening, inclusion/exclusion, evidence extraction, or synthesis. Returned records are candidates, including records that appear irrelevant. Deduplication begins only after all raw database results have been preserved. Screening begins only after the protocol's collection and deduplication handoff.

Supplementary branches remain labeled Supplementary in execution logs, raw artifact names through their Query IDs, and later analysis. They must not be merged with Primary retrieval without retaining branch status and provenance.

The frozen v1 policy applies: no convenience date, publication-type, or language restriction may be introduced unless the frozen specification explicitly contains it. The current frozen queries contain no query-level date, publication-type, or language restriction. Conference, journal, review, report, and permitted preprint records remain retrieval candidates for later classification and screening.

Full-text retrieval is later. Systematic execution does not require obtaining every full text and does not treat full-text access limitations as identification blockers.

All pilot retrievals, focused calibration retrievals, database-validation searches, and ACM manual-validation records remain diagnostic and separate. They are not systematic executions, result counts, corpus records, evidence, or findings. If a diagnostic record is independently returned by a later frozen query, it enters the raw systematic corpus only through that new execution unit.

## Human And Agent Responsibilities

Human action is required for authenticated database access, live query submission, database UI state selection, exports, ACM page-by-page capture, result-count reconciliation, and handling access or interface errors. The coding agent may prepare frozen-query checklists, validate IDs and artifact names, inspect structural completeness of logs, and assist with later file normalization only after raw capture. It must not be assumed to operate authenticated database interfaces without an actually supported access path.

Future logs and raw filenames must use only database names, frozen Query IDs, generic access descriptions, timestamps, statuses, and technical error descriptions. They must not contain institution names, proxy routes, personal emails, usernames, account identifiers, authentication details, or researcher-identifying access information.

## Protocol v1.1 Readiness Decision

All readiness areas are `Ready` or `Ready with documented limitation`. The historical status wording and freeze-time ACM blocker are not current instructions and do not create an execution ambiguity. No methodological inconsistency, frozen-query defect, provenance failure, or unresolved database blocker was found. The planned raw storage/naming and execution-state conventions above close the remaining correctable operational documentation gaps without changing the protocol or frozen queries.

This amendment performed no database/API request, retrieval, deduplication, screening, evidence extraction, synthesis, Work Item-characteristic derivation, or research conclusion. Historical executions remain governed by their original provenance in `systematic-search-log.md`. Future feasibility events and systematic retrievals after the Protocol v1.1 approval commit are governed by the tiered policy.

Scopus Search API retrieval is validated for the frozen Scopus query representation when the complete result set fits the available service-level limits. The validation basis is Query ID `S1-F1-SCOPUS-01-v1`, identical frozen query representation, matching Web/API counts of `2596`, and exact EID+DOI agreement for `10/10` sampled records. Identical ordering is not required; the observed difference was attributable to publication-date ties. This validation is Scopus-specific and does not generalize to other databases. Cursor pagination exists in the utility but is not usable with the currently available entitlement. No full retrieval or corpus creation occurred during validation.

For future Scopus API retrievals, the nominal `STANDARD` capability permits up to 200 records/request, but the current service level has empirically accepted `count=25` and rejected `count=200` with HTTP 400. The utility therefore omits `view` and defaults to `count=25`; `count=200` is not attempted by default. `COMPLETE` is explicit opt-in only, is limited to 25 records/request, and may be entitlement-restricted. STANDARD and COMPLETE response fields are not treated as equivalent; later metadata enrichment, including abstract acquisition if required, remains separate from search retrieval. Cursor pagination remains implemented but is disabled under the current entitlement policy; current systematic retrieval uses offset pagination only for complete sets at or below 5,000 results. Do not claim that result sets above 5,000 are currently retrievable through the API service level. Large result sets that cannot be completely retrieved through the available API service level must use the validated Scopus Web interface with the exact same frozen query. Cursor tokens, page provenance, raw responses, and reconciliation status must be retained for any future explicitly permitted cursor execution, and repeated or incomplete cursor progression is a blocking failure.

The immediate F2A handoff is `S1-F2A-SCOPUS-01-v1` through Scopus Web. Its known result count is `23439`; export CSV in two non-overlapping ranges, `1-20,000` and `20,001-23,439`, using the validated maximum of 20,000 documents per batch. Reconcile the untouched exports to `23,439` before later deduplication or screening. The fallback changes only the retrieval mechanism, not the frozen search strategy.

**Protocol v1.1 tiered execution ready; begin with controlled feasibility and core execution**
