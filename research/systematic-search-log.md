# Systematic Search Execution Log

This log records real systematic-search execution provenance. It is separate from the historical pilot and database-validation record in [`search-log.md`](./search-log.md).

## Batch S1-BATCH-001

- **Batch ID:** `S1-BATCH-001`
- **Database:** IEEE Xplore
- **Batch state:** `Stopped`
- **Execution scope:** First selected execution unit only; `S1-F2A-IEEE-01-v1` and `S1-F2B-IEEE-01-v1` remain unexecuted.

### S1-F1-IEEE-01-v1

- **Query ID:** `S1-F1-IEEE-01-v1`
- **Branch ID:** `F1`
- **Branch:** Software work units and work definition
- **Branch status:** `Primary`
- **Database:** IEEE Xplore
- **Query version:** `v1`
- **Execution date:** `2026-08-21`
- **Interface:** IEEE Xplore Advanced Search
- **Field strategy:** Document Title, Abstract, Author Keywords
- **Filters:** None; no date, publication-type, or language filter
- **Exact frozen query:** `("software development" OR "software engineering" OR programming) AND ("software task" OR "software development task" OR "work unit" OR "work item" OR "issue description" OR ticket OR "user story" OR "change request")`
- **Execution status:** `Failed`
- **Database-reported valid systematic result count:** `Not established`
- **Raw captured records:** `None`
- **Raw artifact:** `None`
- **Reconciliation:** `Unable to verify`
- **Failure class:** `Database interface / executable syntax representation`
- **Failure reason:** IEEE Xplore accepted the Advanced Search submission but transformed the structured field input into an internally field-expanded Boolean expression. The resulting page displayed `No results found`, revealing a compatibility problem between the frozen Advanced Search representation and current IEEE field/Boolean behavior.
- **Query modification during execution:** `None`
- **Rerun required:** `Yes`
- **Successor version:** `Pending` (separate syntax-correction process; possible `v1.1`)
- **Operational notes:** The displayed zero was not recorded as a systematic result count. The conceptual frozen query was not recalibrated. No terminology problem or retrieval conclusion was established. The original failed v1 execution remains preserved and must not be overwritten by a later correction.
- **Screening or interpretation:** `None`

## Boundary Confirmations

- No export occurred.
- No raw corpus record was collected.
- No diagnostic record was reused.
- No deduplication occurred.
- No screening occurred.
- No evidence extraction or synthesis occurred.
- No Work Item characteristic or research conclusion was derived.

## Approved Batch 1 Resumption Handoff

- **Preparation state:** Controlled resumption underway; both approved F1 v1.1 pieces have completed raw retrieval.
- **Correction status:** The approved IEEE Xplore v1.1 correction supersedes the pending successor note in the historical v1 record without altering that record.
- **F1 rerun scope:** Both approved v1.1 pieces represent the complete corrected F1 raw retrieval.
- **Execution-unit rule:** `S1-F1-IEEE-01-v1.1` and `S1-F1-IEEE-02-v1.1` are independent execution units. Each must retain its own IEEE-reported result count, raw export, execution status, and provenance.
- **Combination rule:** After both raw outputs are preserved, their records are combined as a raw union for F1. No deduplication occurs during execution or export.
- **Count rule:** The two Query ID counts must not be summed or interpreted as a unique F1 count. A unique branch-level count is a later post-capture and post-deduplication value.
- **F1 retrieval status:** Complete planned IEEE raw retrieval for conceptual branch F1 has been captured. The two query-piece raw outputs form the F1 union; no unique F1 count is reported at this stage because the sets may overlap.
- **F2A/F2B status:** `S1-F2A-IEEE-01-v1` and `S1-F2B-IEEE-01-v1` remain unexecuted; neither is marked Failed.

### Human Execution Handoff: F1

#### S1-F1-IEEE-01-v1.1

- **Query ID:** `S1-F1-IEEE-01-v1.1`
- **Branch:** Software work units and work definition (`F1`)
- **Status:** `Completed`
- **Database:** IEEE Xplore
- **Interface:** IEEE Xplore Command Search
- **Exact executable expression:** `(("Document Title":"software development" OR "Abstract":"software development" OR "Author Keywords":"software development") OR ("Document Title":"software engineering" OR "Abstract":"software engineering" OR "Author Keywords":"software engineering") OR ("Document Title":programming OR "Abstract":programming OR "Author Keywords":programming)) AND (("Document Title":"software task" OR "Abstract":"software task" OR "Author Keywords":"software task") OR ("Document Title":"software development task" OR "Abstract":"software development task" OR "Author Keywords":"software development task") OR ("Document Title":ticket OR "Abstract":ticket OR "Author Keywords":ticket) OR ("Document Title":"work unit" OR "Abstract":"work unit" OR "Author Keywords":"work unit"))`
- **Query version:** `v1.1`
- **Execution date:** `2026-08-21`
- **Filters:** None; no date, publication-type, or language filter
- **Database-reported result count:** `228`
- **Export format:** IEEE Xplore Citation export; Plain Text; Citation and Abstract
- **Raw artifacts:**
  - `research/raw/systematic-search/S1-F1-IEEE-01-v1.1__run-20260821T134155__page-001.txt` — 100 raw records
  - `research/raw/systematic-search/S1-F1-IEEE-01-v1.1__run-20260821T134155__page-002.txt` — 100 raw records
  - `research/raw/systematic-search/S1-F1-IEEE-01-v1.1__run-20260821T134155__page-003.txt` — 28 raw records
- **Total raw captured records:** `228`
- **Reconciliation:** `228` database-reported results / `228` raw captured records
- **Reconciliation status:** `Complete`
- **Execution-time deduplication:** `None`
- **Screening:** `Not started`
- **Evidence extraction:** `None`
- **Synthesis:** `None`
- **Research conclusions:** `None`

#### S1-F1-IEEE-02-v1.1

- **Query ID:** `S1-F1-IEEE-02-v1.1`
- **Branch:** Software work units and work definition (`F1`)
- **Status:** `Completed`
- **Database:** IEEE Xplore
- **Interface:** IEEE Xplore Command Search
- **Exact executable expression:** `(("Document Title":"software development" OR "Abstract":"software development" OR "Author Keywords":"software development") OR ("Document Title":"software engineering" OR "Abstract":"software engineering" OR "Author Keywords":"software engineering") OR ("Document Title":programming OR "Abstract":programming OR "Author Keywords":programming)) AND (("Document Title":"work item" OR "Abstract":"work item" OR "Author Keywords":"work item") OR ("Document Title":"issue description" OR "Abstract":"issue description" OR "Author Keywords":"issue description") OR ("Document Title":"user story" OR "Abstract":"user story" OR "Author Keywords":"user story") OR ("Document Title":"change request" OR "Abstract":"change request" OR "Author Keywords":"change request"))`
- **Query version:** `v1.1`
- **Execution date:** `2026-08-21`
- **Filters:** None; no date, publication-type, or language filter
- **Database-reported result count:** `171`
- **Export format:** IEEE Xplore Citation export; Plain Text; Citation and Abstract
- **Raw artifacts:**
  - `research/raw/systematic-search/S1-F1-IEEE-02-v1.1__run-20260821T155348__page-001.txt` — 100 raw records
  - `research/raw/systematic-search/S1-F1-IEEE-02-v1.1__run-20260821T155348__page-002.txt` — 71 raw records
- **Total raw captured records:** `171`
- **Reconciliation:** `171` database-reported results / `171` raw captured records
- **Reconciliation status:** `Complete`
- **Execution-time deduplication:** `None`
- **Screening:** `Not started`
- **Evidence extraction:** `None`
- **Synthesis:** `None`
- **Research conclusions:** `None`

The two F1 query-piece raw outputs are retained as independent provenance and form the F1 raw union. They were not combined or deduplicated during execution. Any unique F1 record count belongs to the later deduplication phase. F2A and F2B remain unexecuted, and `S1-BATCH-001` remains incomplete.

## Scopus Systematic Retrieval

### S1-F1-SCOPUS-01-v1

- **Query ID:** `S1-F1-SCOPUS-01-v1`
- **Branch ID:** `F1`
- **Branch:** Software work units and work definition
- **Branch status:** `Primary`
- **Database:** Scopus
- **Execution mechanism:** Scopus Search API
- **Query version:** `v1`
- **Execution date:** `2026-08-21`
- **Exact frozen query:** `TITLE-ABS-KEY(("software development" OR "software engineering" OR programming) AND ("software task" OR "software development task" OR "work unit" OR "work item" OR "issue description" OR ticket OR "user story" OR "change request"))`
- **Fields:** Title, abstract, and author keywords through Scopus `TITLE-ABS-KEY(...)`
- **Filters:** None; no date, publication-type, language, subject, or additional result filter
- **Time coverage:** No restriction
- **Database-reported API result count:** `2596`
- **API result status:** `Completed`; all `104` requested pages returned parseable responses without an HTTP failure
- **Raw captured records:** `2596`
- **Pagination:** `104` API calls/pages, `count=25`, starts `0` through `2575` in increments of `25`; final page contained `21` records
- **Raw artifacts:** `research/raw/systematic-search/S1-F1-SCOPUS-01-v1__run-20260821T231713Z__api-start-000000.json` through `research/raw/systematic-search/S1-F1-SCOPUS-01-v1__run-20260821T231713Z__api-start-002575.json`, with one immutable metadata sidecar per response
- **Reconciliation:** `2596` API-reported results / `2596` raw captured records
- **Reconciliation status:** `Complete`
- **Missing pagination ranges:** `No`; starts were contiguous and complete
- **Duplicate pagination ranges:** `No`
- **Execution-time deduplication:** `None`
- **Screening:** `Not started`
- **Evidence extraction:** `None`
- **Synthesis:** `None`
- **Unique corpus count:** Not derived beyond this single-query raw retrieval
- **Operational notes:** Exact frozen query was submitted unchanged. Raw API JSON responses were preserved before transformation with Query ID, Scopus source, page, start position, count, totalResults, run timestamp, and exact query in non-secret metadata sidecars. The API key was not written to responses, sidecars, filenames, or logs.

### S1-F2A-SCOPUS-01-v1

- **Query ID:** `S1-F2A-SCOPUS-01-v1`
- **Branch ID:** `F2A`
- **Branch:** Requirements and specifications
- **Branch status:** `Primary`
- **Database:** Scopus
- **Execution mechanism:** Scopus Search API
- **Query version:** `v1`
- **Execution date:** `2026-08-21`
- **Exact frozen query:** `TITLE-ABS-KEY((software OR "software engineering") AND ("software requirements" OR "requirements engineering" OR "requirements specification" OR "software requirements specification" OR "functional requirements" OR "non-functional requirements"))`
- **Fields:** Title, abstract, and author keywords through Scopus `TITLE-ABS-KEY(...)`
- **Filters:** None; no date, publication-type, language, subject, or additional result filter
- **View and pagination:** `COMPLETE`; automatic cursor pagination policy
- **Execution status:** `Failed`
- **API result status:** HTTP `401 Unauthorized`
- **API-reported result count:** `Not available`
- **Raw captured records:** `0`
- **Raw artifacts:** `None`; the request failed before the first page was captured
- **Reconciliation:** `Not attempted`
- **Pagination integrity:** `Not applicable; no page was returned`
- **Execution-time deduplication:** `None`
- **Screening:** `Not started`
- **Evidence extraction:** `None`
- **Operational notes:** The exact frozen query was submitted unchanged. Retrieval stopped on the authentication response; no alternate view, pagination mode, or query representation was attempted. No corpus artifact was created.
