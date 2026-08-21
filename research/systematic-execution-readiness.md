# Systematic Execution Readiness

**Audit date:** 2026-08-20

**Scope:** Final readiness audit before systematic search execution. This artifact records execution controls only. It does not execute a query, collect a systematic result count, export a result set, create a corpus, assign Source IDs, deduplicate, screen, extract evidence, or synthesize findings.

## Authorities And Current State

The authority chain is coherent when current and historical material are distinguished:

- [`protocol.md`](./protocol.md) defines the research method, search sources, time and publication principles, record collection, deduplication, screening, and traceability requirements.
- [`search-log.md`](./search-log.md) is the durable calibration record. Its older pilot statuses remain historical calibration observations.
- [`systematic-search-design.md`](./systematic-search-design.md) defines branch purposes, database adaptations, execution-unit fields, collection, deduplication, and screening handoff.
- [`database-validation.md`](./database-validation.md) defines verified database capabilities and the ACM manual-capture workflow.
- [`systematic-queries.md`](./systematic-queries.md) is the frozen executable-query authority. Its v1 freeze audit records the current branch statuses and query inventory.

The repository contains historical pre-freeze wording such as `Requires further calibration` for F6B1/F6B2 and historical pre-validation statements about ACM export. The later focused calibration, frozen-query manifest, and completed ACM validation supersede those statements for execution. They are documentation history, not current execution instructions. No methodological contradiction remains in the current frozen specification.

## Readiness Summary

| Area | Classification | Finding |
|---|---|---|
| Research questions and protocol | Ready | Current questions, evidence boundaries, retrieval sequence, and traceability rules are documented. |
| Branch inventory | Ready | 28 branches: 22 Primary and 6 Supplementary. |
| Frozen queries | Ready | v1 contains 198 unique executable Query IDs, 33 per database. |
| Database access and search | Ready with documented limitation | All six databases have verified search paths and database-specific adaptations. |
| Raw capture | Ready with documented limitation | Export/capture controls are defined; ACM requires high-burden manual capture in Basic Edition. |
| Execution logging | Ready with documented limitation | `search-log.md` is the designated systematic execution log; raw artifact references must be added with each execution record. |
| Raw storage and naming | Ready with documented limitation | The convention below must be used when raw artifacts are first created. No raw artifact is created by this audit. |
| Methodological consistency | Ready | Historical wording is identified and does not override current frozen decisions. |
| Scopus API support | Validated for frozen-query retrieval | Query `S1-F1-SCOPUS-01-v1` matched the Web count and a 10-record EID+DOI sample; exact frozen-query and raw-provenance controls remain mandatory. |
| Scopus large-result pagination | Ready with documented view constraint | `COMPLETE` preserves the conservative metadata contract at 25 records/request; cursor pagination is required for result sets beyond the 5,000-record offset boundary. |
| Unresolved blocker | None | No issue makes the frozen search technically impossible, methodologically ambiguous, or untraceable. |

## Branch And Query Audit

The frozen artifact confirms all 28 branches occur exactly once. The six Supplementary branches are exactly:

- F3C;
- F4C2;
- F6B1;
- F6B2;
- F6C2;
- F7E.

All other branches are Primary. F6B1 and F6B2 are bounded Supplementary searches, not unresolved branches. Planning remains distinct from agent-side functional decomposition, delegation, and trajectory analysis. No excluded generic planning, generic task decomposition, generic allocation, or unqualified evaluation umbrella has silently returned.

The frozen Query ID audit confirms:

- 198 IDs are present and unique;
- each of the six databases has 33 IDs;
- every ID is v1;
- every ID maps to one branch and one database;
- F6B1 and F6B2 have two deliberate variants per database;
- F7C has four deliberate variants per database;
- all other branch/database pairs have one variant;
- every branch has all intended database adaptations or the documented F6 variant register;
- no query was silently edited after freeze.

The execution unit is **one frozen Query ID executed once against its assigned database**. It is not a branch, a database result record, or a deduplicated source. The expected first-pass execution scale is therefore **198 execution units**, not an estimate of result volume or corpus size.

## Database Readiness

| Database | Classification | Execution condition |
|---|---|---|
| Scopus | Ready with documented limitation | Advanced and fielded search and CSV export are verified. Institutional authenticated access and export batching must be recorded. |
| Web of Science Core Collection | Ready with documented limitation | Advanced search and structured Email Full Record export are verified. Direct Excel failure is historical; the 1,000-record batch limit and alternative export path must be recorded. |
| ScienceDirect | Ready with documented limitation | Search and citation export are verified. The combined Title/Abstract/Author-Keywords field must be used; independent field semantics must not be inferred. |
| IEEE Xplore | Ready with documented limitation | Public advanced/command search, fielded search, and export are verified. Frozen clauses account for the observed 25-term-per-clause constraint. |
| ACM Digital Library | Ready with documented limitation | Basic Edition search is verified. Native bulk export is unavailable, but the human-verified manual page-by-page workflow preserves complete result coverage, count reconciliation, positions, and stable ACM locators. Premium export is optional fallback; paid access is not required. |
| Springer Nature Link | Ready with documented limitation | Public advanced search and CSV export through the observed free-account workflow are verified. The Keywords field searches body text and export metadata is reduced; returned records must still be captured without relevance-based removal. |

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

Examples of formats are `csv`, `txt`, `ris`, `email`, or `manual.csv`; the extension describes the captured format and must not imply that a database supplied a format it did not supply. For ACM manual capture, the artifact or row set must additionally preserve page and position provenance. The frozen Query ID already encodes branch, database, sequence, and v1; the run timestamp distinguishes reruns. The `search-log.md` execution entry must reference the raw artifact name and report its status.

This is an operational naming/storage convention, not a corpus schema. Raw files remain retrieval artifacts and must not be placed in `evidence/`, literature notes, or final included-source records.

## Execution Log And Status Rules

The search design designates [`search-log.md`](./search-log.md) as the place for systematic execution records, appended after the untouched pilot material in a clearly marked section. Each execution record can and must contain:

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

The first pass will use a stable database-by-database order matching the frozen database list: Scopus, Web of Science Core Collection, IEEE Xplore, ACM Digital Library, ScienceDirect, and Springer Nature Link. This is an operational ordering choice, not a methodological ranking. Within each database, execute Query IDs in frozen manifest order. An interruption may resume only from an explicitly recorded incomplete unit; it must not overwrite the original execution record.

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

## Final Readiness Decision

All readiness areas are `Ready` or `Ready with documented limitation`. The historical status wording and freeze-time ACM blocker are not current instructions and do not create an execution ambiguity. No methodological inconsistency, frozen-query defect, provenance failure, or unresolved database blocker was found. The planned raw storage/naming and execution-state conventions above close the remaining correctable operational documentation gaps without changing the protocol or frozen queries.

No systematic query was executed. No systematic result count was collected. No corpus, Source ID, deduplication, screening, evidence extraction, synthesis, Work Item characteristic, or research conclusion was produced.

Scopus Search API retrieval is validated for the frozen Scopus query representation based on Query ID `S1-F1-SCOPUS-01-v1`, identical frozen query representation, matching Web/API counts of `2596`, and exact EID+DOI agreement for `10/10` sampled records. Identical ordering is not required; the observed difference was attributable to publication-date ties. This validation is Scopus-specific and does not generalize to other databases. The API may now be used for frozen Scopus systematic queries with exact-query and immutable raw-provenance controls. No full retrieval or corpus creation occurred during validation.

For future Scopus retrievals, `COMPLETE` view with 25 records/request is the default metadata-preserving policy. `pagination=auto` uses cursor pagination to avoid the 5,000-record offset boundary; offset pagination remains supported only for bounded sets. Cursor tokens, page provenance, raw responses, and reconciliation status must be retained, and repeated or incomplete cursor progression is a blocking failure.

**Systematic execution ready; begin controlled search execution**
