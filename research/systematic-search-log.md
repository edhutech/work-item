# Systematic Search Execution Log

This log records real systematic-search execution provenance. It is separate from the historical pilot and database-validation record in [`search-log.md`](./search-log.md).

## Protocol v1.1 Amendment Boundary

- **Protocol version:** `Research Protocol v1.1`
- **Amendment approval status:** Approved for implementation
- **Effective boundary:** The Git commit that formally records the Protocol v1.1 amendment
- **Historical provenance rule:** All entries before that commit remain Protocol v1 execution or validation provenance. They are not relabeled as v1.1 executions and are not deleted or rewritten.
- **Post-boundary rule:** Feasibility validation events and systematic retrievals after that commit follow the v1.1 tiered policy. Feasibility validation remains operational validation and is not a systematic corpus retrieval.
- **Historical execution source of truth:** This log is authoritative for completed, failed, superseded, and reused historical executions. Other documents define reuse rules and must not duplicate the complete execution inventory.
- **Current amendment status:** No new database/API request, screening, deduplication, evidence extraction, or synthesis was performed while recording this boundary.

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
- **Public provenance manifest:** `research/manifests/scopus/S1-F1-SCOPUS-01-v1__run-20260821T231713Z.manifest.json`
- **Raw data policy:** Record-level Scopus data and sidecar files are retained locally/private; the public manifest contains provenance and hashes only.
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

### S1-F2A-SCOPUS-01-v1 retry

- **Query ID:** `S1-F2A-SCOPUS-01-v1`
- **Branch ID:** `F2A`
- **Branch:** Requirements and specifications
- **Branch status:** `Primary`
- **Database:** Scopus
- **Execution mechanism:** Scopus Search API
- **Query version:** `v1`
- **Execution date:** `2026-08-21`
- **Exact frozen query:** `TITLE-ABS-KEY((software OR "software engineering") AND ("software requirements" OR "requirements engineering" OR "requirements specification" OR "software requirements specification" OR "functional requirements" OR "non-functional requirements"))`
- **Fields:** Scopus default `STANDARD` search-result route; Title, abstract, and author-keyword query semantics remain in the frozen `TITLE-ABS-KEY(...)` expression
- **Filters:** None; no date, publication-type, language, subject, or additional result filter
- **Request route:** STANDARD/default; no explicit `view` parameter
- **Pagination:** Cursor; `count=200`
- **Execution status:** `Failed`
- **API result status:** HTTP `400 Bad Request`
- **Previously observed bounded API count:** `23439`
- **Execution-time API-reported result count:** `Not available`
- **Count drift:** `Not assessable`
- **Raw captured records:** `0`
- **Raw artifacts:** `None`; failure occurred before the first cursor page was captured
- **Reconciliation:** `Not attempted`
- **Pagination integrity:** `Not assessable; no page was returned`
- **Execution-time deduplication:** `None`
- **Screening:** `Not started`
- **Evidence extraction:** `None`
- **Operational notes:** The exact frozen query was submitted unchanged. Retrieval stopped on the first cursor request; no alternate query, view, page size, or pagination mode was attempted. The earlier HTTP 401 attempt remains preserved as a separate historical record. No corpus artifact was created.

### S1-F2A-SCOPUS-01-v1 Web retrieval

- **Query ID:** `S1-F2A-SCOPUS-01-v1`
- **Branch ID:** `F2A`
- **Branch:** Requirements and specifications
- **Branch status:** `Primary`
- **Database:** Scopus
- **Retrieval mechanism:** Scopus Web
- **Query version:** `v1`
- **Execution date:** `2026-08-22`
- **Exact frozen query:** `TITLE-ABS-KEY((software OR "software engineering") AND ("software requirements" OR "requirements engineering" OR "requirements specification" OR "software requirements specification" OR "functional requirements" OR "non-functional requirements"))`
- **Fields:** Title, abstract, and author keywords through Scopus `TITLE-ABS-KEY(...)`
- **Filters:** None; no date, publication-type, language, subject, or additional result filter
- **Execution status:** `Completed`
- **Previous bounded API count:** `23439`
- **Initial Scopus Web count:** `23443`
- **Final Scopus Web verification count:** `23444`
- **Database/result-set drift observed:** `Yes`; the observed counts changed during the retrieval window from the previous bounded API count to the initial Web count and then to the final Web verification count. The earlier inferred `17215` value was not an observed database count and is not used as the final partition count.
- **Export limit encountered:** `20,000` records per Scopus Web CSV export
- **Partition strategy:** Publication year, used only to satisfy the Scopus Web CSV export limit
- **Partition 1:** `1964-2019`; `17216` raw records
- **Partition 2:** `2020-2027`; `6228` raw records
- **Combined raw records:** `23444`
- **Combined distinct EIDs:** `23444`
- **Cross-partition overlap:** None by Scopus EID or non-empty DOI
- **Raw artifacts:**
  - `research/raw/systematic-search/S1-F2A-SCOPUS-01-v1__run-20260822T012337__scopus-web__years-1964-2019.csv`
  - `research/raw/systematic-search/S1-F2A-SCOPUS-01-v1__run-20260822T012337__scopus-web__years-2020-2027.csv`
- **Public provenance manifest:** `research/manifests/scopus/S1-F2A-SCOPUS-01-v1__run-20260822T012337__scopus-web.manifest.json`
- **Raw data policy:** Record-level Scopus Web exports are retained locally/private; the public manifest contains partition provenance and hashes only.
- **Reconciliation:** `Complete`; `17216 + 6228 = 23444`, matching the final observed Scopus Web full-query count
- **Execution-time deduplication:** `None`; the raw artifacts remain unchanged and no record was removed
- **Screening:** `Not started`
- **Evidence extraction:** `None`
- **Synthesis:** `None`
- **Operational notes:** The frozen search expression was not modified. Year partitioning changed only the export batching mechanism. The final retrieval snapshot is the `23444`-record captured set. CSV diagnostics found no malformed rows, unexpected publication years, duplicate EIDs, or cross-partition EID/DOI overlap. A later `2019-2027` diagnostic view returned `7201` records, but it overlaps the `1964-2019` partition and is not part of this retrieval. The raw artifacts remain unchanged. The earlier failed API attempts remain preserved as historical provenance.

### S1-F2B-SCOPUS-01-v1

- **Query ID:** `S1-F2B-SCOPUS-01-v1`
- **Branch ID:** `F2B`
- **Branch:** User stories and acceptance criteria
- **Branch status:** `Primary`
- **Database:** Scopus
- **Execution mechanism:** Scopus Search API
- **Query version:** `v1`
- **Execution date:** `2026-08-22`
- **Exact frozen query:** `TITLE-ABS-KEY(("software engineering" OR "agile software development") AND ("user story" OR "acceptance criteria" OR Gherkin OR "Behavior-Driven Development"))`
- **Fields:** Title, abstract, and author keywords through Scopus `TITLE-ABS-KEY(...)`
- **Filters:** None; no date, publication-type, language, subject, or additional result filter
- **Request route:** STANDARD/default; no explicit `view` parameter
- **Bounded API request:** HTTP `200`; `count=1`, offset pagination, `totalResults=743`; raw response preserved as `research/raw/systematic-search/S1-F2B-SCOPUS-01-v1__run-bounded-20260822T231845Z__api-start-000000.json` with metadata sidecar
- **Initial complete request:** HTTP `400` for `count=200`; no raw page was captured
- **Complete retrieval request:** HTTP `200`; offset pagination, `count=25`; cursor pagination was not attempted
- **Execution status:** `Completed`
- **Database-reported API result count:** `743`
- **Raw captured records:** `743`
- **Pagination:** `30` API calls/pages, starts `0` through `725` in increments of `25`; final page contained `18` records
- **Raw artifacts:** `research/raw/systematic-search/S1-F2B-SCOPUS-01-v1__run-20260822T231916Z__api-start-000000.json` through `research/raw/systematic-search/S1-F2B-SCOPUS-01-v1__run-20260822T231916Z__api-start-000725.json`, with one immutable metadata sidecar per response
- **Public provenance manifests:** Complete run `research/manifests/scopus/S1-F2B-SCOPUS-01-v1__run-20260822T231916Z.manifest.json`; bounded probe `research/manifests/scopus/S1-F2B-SCOPUS-01-v1__run-bounded-20260822T231845Z.manifest.json`
- **Raw data policy:** Record-level Scopus data and sidecar files are retained locally/private; public manifests contain provenance and hashes only.
- **Reconciliation:** `743` API-reported results / `743` raw captured records
- **Reconciliation status:** `Complete`
- **Missing pagination ranges:** `No`; starts were contiguous and complete
- **Duplicate pagination ranges:** `No`
- **Execution-time deduplication:** `None`
- **Screening:** `Not started`
- **Evidence extraction:** `None`
- **Synthesis:** `None`
- **Unique corpus count:** Not derived beyond this single-query raw retrieval
- **Operational notes:** The exact frozen query was submitted unchanged. The bounded count established that the complete set fit the available non-cursor offset boundary. Raw API JSON responses were preserved before transformation with Query ID, Scopus source, page, start position, count, totalResults, run timestamp, and exact query in non-secret metadata sidecars. The API key was not written to responses, sidecars, filenames, or logs. No deduplication, screening, or evidence extraction occurred.

### S1-F3C-SCOPUS-01-v1 (repeat execution)

- **Query ID:** `S1-F3C-SCOPUS-01-v1`
- **Branch ID:** `F3C`
- **Branch:** Supplementary allocation, interdependence, and crowdsourced software work
- **Database:** Scopus
- **Execution mechanism:** Scopus Search API
- **Query version:** `v1`
- **Execution date:** `2026-08-22`
- **Execution role:** Latest complete execution associated with this systematic-search log
- **Exact frozen query:** `TITLE-ABS-KEY(("software development" OR "crowdsourcing software development") AND ("task allocation" OR "work allocation" OR "task interdependence" OR "parallel tasks"))`
- **Request route:** STANDARD/default; no explicit `view` parameter
- **Bounded API request:** HTTP `200`; `count=1`, offset pagination, `totalResults=180`; raw response preserved as `research/raw/systematic-search/S1-F3C-SCOPUS-01-v1__run-bounded-20260822T235137Z__api-start-000000.json` with metadata sidecar
- **Complete retrieval request:** HTTP `200`; offset pagination, `count=25`; cursor pagination was not attempted
- **Execution status:** `Completed`
- **Database-reported API result count:** `180`
- **Raw captured records:** `180`
- **Pagination:** `8` API calls/pages, starts `0` through `175` in increments of `25`; final page contained `5` records
- **Raw artifacts:** `research/raw/systematic-search/S1-F3C-SCOPUS-01-v1__run-20260822T235149Z__api-start-000000.json` through `research/raw/systematic-search/S1-F3C-SCOPUS-01-v1__run-20260822T235149Z__api-start-000175.json`, with one immutable metadata sidecar per response
- **Public provenance manifests:** Complete run `research/manifests/scopus/S1-F3C-SCOPUS-01-v1__run-20260822T235149Z.manifest.json`; bounded probe `research/manifests/scopus/S1-F3C-SCOPUS-01-v1__run-bounded-20260822T235137Z.manifest.json`
- **Raw data policy:** Record-level Scopus data and sidecar files are retained locally/private; public manifests contain provenance and hashes only.
- **Reconciliation:** `180` API-reported results / `180` raw captured records
- **Reconciliation status:** `Complete`
- **Missing pagination ranges:** `No`; starts were contiguous and complete
- **Duplicate pagination ranges:** `No`
- **Execution-time deduplication:** `None`
- **Screening:** `Not started`
- **Evidence extraction:** `None`
- **Operational notes:** This repeat execution used the exact frozen query unchanged. Raw API JSON responses were preserved before transformation with Query ID, Scopus source, page, start position, count, totalResults, run timestamp, and exact query in non-secret metadata sidecars. The API key was not written to responses, sidecars, filenames, or logs. No deduplication, screening, or evidence extraction occurred.

### S1-F3C-SCOPUS-01-v1

- **Query ID:** `S1-F3C-SCOPUS-01-v1`
- **Branch ID:** `F3C`
- **Branch:** Supplementary allocation, interdependence, and crowdsourced software work
- **Branch status:** `Primary`
- **Database:** Scopus
- **Execution mechanism:** Scopus Search API
- **Query version:** `v1`
- **Execution date:** `2026-08-22`
- **Execution role:** Historical complete execution; retained as separate execution provenance, not a duplicate-corpus operation
- **Exact frozen query:** `TITLE-ABS-KEY(("software development" OR "crowdsourcing software development") AND ("task allocation" OR "work allocation" OR "task interdependence" OR "parallel tasks"))`
- **Fields:** Title, abstract, and author keywords through Scopus `TITLE-ABS-KEY(...)`
- **Filters:** None; no date, publication-type, language, subject, or additional result filter
- **Request route:** STANDARD/default; no explicit `view` parameter
- **Bounded API request:** HTTP `200`; `count=1`, offset pagination, `totalResults=180`; raw response preserved as `research/raw/systematic-search/S1-F3C-SCOPUS-01-v1__run-bounded-20260822T234902Z__api-start-000000.json` with metadata sidecar
- **Complete retrieval request:** HTTP `200`; offset pagination, `count=25`; cursor pagination was not attempted
- **Execution status:** `Completed`
- **Database-reported API result count:** `180`
- **Raw captured records:** `180`
- **Pagination:** `8` API calls/pages, starts `0` through `175` in increments of `25`; final page contained `5` records
- **Raw artifacts:** `research/raw/systematic-search/S1-F3C-SCOPUS-01-v1__run-20260822T234914Z__api-start-000000.json` through `research/raw/systematic-search/S1-F3C-SCOPUS-01-v1__run-20260822T234914Z__api-start-000175.json`, with one immutable metadata sidecar per response
- **Public provenance manifests:** Complete run `research/manifests/scopus/S1-F3C-SCOPUS-01-v1__run-20260822T234914Z.manifest.json`; bounded probe `research/manifests/scopus/S1-F3C-SCOPUS-01-v1__run-bounded-20260822T234902Z.manifest.json`
- **Raw data policy:** Record-level Scopus data and sidecar files are retained locally/private; public manifests contain provenance and hashes only.
- **Reconciliation:** `180` API-reported results / `180` raw captured records
- **Reconciliation status:** `Complete`
- **Missing pagination ranges:** `No`; starts were contiguous and complete
- **Duplicate pagination ranges:** `No`
- **Execution-time deduplication:** `None`
- **Screening:** `Not started`
- **Evidence extraction:** `None`
- **Synthesis:** `None`
- **Unique corpus count:** Not derived beyond this single-query raw retrieval
- **Operational notes:** The exact frozen query was submitted unchanged. The bounded count established that the complete set fit the available non-cursor offset boundary. Raw API JSON responses were preserved before transformation with Query ID, Scopus source, page, start position, count, totalResults, run timestamp, and exact query in non-secret metadata sidecars. The API key was not written to responses, sidecars, filenames, or logs. No deduplication, screening, or evidence extraction occurred.

### S1-F3B-SCOPUS-01-v1

- **Query ID:** `S1-F3B-SCOPUS-01-v1`
- **Branch ID:** `F3B`
- **Branch:** Task descriptions and issue representations
- **Branch status:** `Primary`
- **Database:** Scopus
- **Execution mechanism:** Scopus Search API
- **Query version:** `v1`
- **Execution date:** `2026-08-22`
- **Exact frozen query:** `TITLE-ABS-KEY(("software project" OR "issue-tracking system" OR "software development") AND ("issue description" OR "issue comments" OR "textual descriptions of issues" OR "software task description"))`
- **Fields:** Title, abstract, and author keywords through Scopus `TITLE-ABS-KEY(...)`
- **Filters:** None; no date, publication-type, language, subject, or additional result filter
- **Request route:** STANDARD/default; no explicit `view` parameter
- **Bounded API request:** HTTP `200`; `count=1`, offset pagination, `totalResults=50`; raw response preserved as `research/raw/systematic-search/S1-F3B-SCOPUS-01-v1__run-bounded-20260822T233910Z__api-start-000000.json` with metadata sidecar
- **Complete retrieval request:** HTTP `200`; offset pagination, `count=25`; cursor pagination was not attempted
- **Execution status:** `Completed`
- **Database-reported API result count:** `50`
- **Raw captured records:** `50`
- **Pagination:** `2` API calls/pages, starts `0` and `25` in increments of `25`; final page contained `25` records
- **Raw artifacts:** `research/raw/systematic-search/S1-F3B-SCOPUS-01-v1__run-20260822T234430Z__api-start-000000.json` and `research/raw/systematic-search/S1-F3B-SCOPUS-01-v1__run-20260822T234430Z__api-start-000025.json`, with one immutable metadata sidecar per response
- **Public provenance manifests:** Complete run `research/manifests/scopus/S1-F3B-SCOPUS-01-v1__run-20260822T234430Z.manifest.json`; bounded probe `research/manifests/scopus/S1-F3B-SCOPUS-01-v1__run-bounded-20260822T233910Z.manifest.json`
- **Raw data policy:** Record-level Scopus data and sidecar files are retained locally/private; public manifests contain provenance and hashes only.
- **Reconciliation:** `50` API-reported results / `50` raw captured records
- **Reconciliation status:** `Complete`
- **Missing pagination ranges:** `No`; starts were contiguous and complete
- **Duplicate pagination ranges:** `No`
- **Execution-time deduplication:** `None`
- **Screening:** `Not started`
- **Evidence extraction:** `None`
- **Synthesis:** `None`
- **Unique corpus count:** Not derived beyond this single-query raw retrieval
- **Operational notes:** The exact frozen query was submitted unchanged. The bounded count established that the complete set fit the available non-cursor offset boundary. Raw API JSON responses were preserved before transformation with Query ID, Scopus source, page, start position, count, totalResults, run timestamp, and exact query in non-secret metadata sidecars. The API key was not written to responses, sidecars, filenames, or logs. No deduplication, screening, or evidence extraction occurred.

### S1-F3A-SCOPUS-01-v1

- **Query ID:** `S1-F3A-SCOPUS-01-v1`
- **Branch ID:** `F3A`
- **Branch:** Software-project decomposition and planning
- **Branch status:** `Primary`
- **Database:** Scopus
- **Execution mechanism:** Scopus Search API
- **Query version:** `v1`
- **Execution date:** `2026-08-22`
- **Exact frozen query:** `TITLE-ABS-KEY(("software development" OR "software project") AND ("task decomposition" OR "work decomposition" OR "task breakdown" OR "software project decomposition" OR "requirement-driven task decomposition"))`
- **Fields:** Title, abstract, and author keywords through Scopus `TITLE-ABS-KEY(...)`
- **Filters:** None; no date, publication-type, language, subject, or additional result filter
- **Request route:** STANDARD/default; no explicit `view` parameter
- **Bounded API request:** HTTP `200`; `count=1`, offset pagination, `totalResults=29`; raw response preserved as `research/raw/systematic-search/S1-F3A-SCOPUS-01-v1__run-bounded-20260822T233658Z__api-start-000000.json` with metadata sidecar
- **Complete retrieval request:** HTTP `200`; offset pagination, `count=25`; cursor pagination was not attempted
- **Execution status:** `Completed`
- **Database-reported API result count:** `29`
- **Raw captured records:** `29`
- **Pagination:** `2` API calls/pages, starts `0` and `25` in increments of `25`; final page contained `4` records
- **Raw artifacts:** `research/raw/systematic-search/S1-F3A-SCOPUS-01-v1__run-20260822T233712Z__api-start-000000.json` and `research/raw/systematic-search/S1-F3A-SCOPUS-01-v1__run-20260822T233712Z__api-start-000025.json`, with one immutable metadata sidecar per response
- **Public provenance manifests:** Complete run `research/manifests/scopus/S1-F3A-SCOPUS-01-v1__run-20260822T233712Z.manifest.json`; bounded probe `research/manifests/scopus/S1-F3A-SCOPUS-01-v1__run-bounded-20260822T233658Z.manifest.json`
- **Raw data policy:** Record-level Scopus data and sidecar files are retained locally/private; public manifests contain provenance and hashes only.
- **Reconciliation:** `29` API-reported results / `29` raw captured records
- **Reconciliation status:** `Complete`
- **Missing pagination ranges:** `No`; starts were contiguous and complete
- **Duplicate pagination ranges:** `No`
- **Execution-time deduplication:** `None`
- **Screening:** `Not started`
- **Evidence extraction:** `None`
- **Synthesis:** `None`
- **Unique corpus count:** Not derived beyond this single-query raw retrieval
- **Operational notes:** The exact frozen query was submitted unchanged. The bounded count established that the complete set fit the available non-cursor offset boundary. Raw API JSON responses were preserved before transformation with Query ID, Scopus source, page, start position, count, totalResults, run timestamp, and exact query in non-secret metadata sidecars. The API key was not written to responses, sidecars, filenames, or logs. No deduplication, screening, or evidence extraction occurred.

### S1-F2C-SCOPUS-01-v1

- **Query ID:** `S1-F2C-SCOPUS-01-v1`
- **Branch ID:** `F2C`
- **Branch:** Requirements quality and validation
- **Branch status:** `Primary`
- **Database:** Scopus
- **Execution mechanism:** Scopus Search API
- **Query version:** `v1`
- **Execution date:** `2026-08-22`
- **Exact frozen query:** `TITLE-ABS-KEY(("requirements engineering" OR "software requirements") AND ("requirements quality" OR "requirements quality assurance" OR "requirements quality assessment" OR "requirements validation" OR "requirements quality control"))`
- **Fields:** Title, abstract, and author keywords through Scopus `TITLE-ABS-KEY(...)`
- **Filters:** None; no date, publication-type, language, subject, or additional result filter
- **Request route:** STANDARD/default; no explicit `view` parameter
- **Bounded API request:** HTTP `200`; `count=1`, offset pagination, `totalResults=540`; raw response preserved as `research/raw/systematic-search/S1-F2C-SCOPUS-01-v1__run-bounded-20260822T233156Z__api-start-000000.json` with metadata sidecar
- **Complete retrieval request:** HTTP `200`; offset pagination, `count=25`; cursor pagination was not attempted
- **Execution status:** `Completed`
- **Database-reported API result count:** `540`
- **Raw captured records:** `540`
- **Pagination:** `22` API calls/pages, starts `0` through `525` in increments of `25`; final page contained `15` records
- **Raw artifacts:** `research/raw/systematic-search/S1-F2C-SCOPUS-01-v1__run-20260822T233210Z__api-start-000000.json` through `research/raw/systematic-search/S1-F2C-SCOPUS-01-v1__run-20260822T233210Z__api-start-000525.json`, with one immutable metadata sidecar per response
- **Public provenance manifests:** Complete run `research/manifests/scopus/S1-F2C-SCOPUS-01-v1__run-20260822T233210Z.manifest.json`; bounded probe `research/manifests/scopus/S1-F2C-SCOPUS-01-v1__run-bounded-20260822T233156Z.manifest.json`
- **Raw data policy:** Record-level Scopus data and sidecar files are retained locally/private; public manifests contain provenance and hashes only.
- **Reconciliation:** `540` API-reported results / `540` raw captured records
- **Reconciliation status:** `Complete`
- **Missing pagination ranges:** `No`; starts were contiguous and complete
- **Duplicate pagination ranges:** `No`
- **Execution-time deduplication:** `None`
- **Screening:** `Not started`
- **Evidence extraction:** `None`
- **Synthesis:** `None`
- **Unique corpus count:** Not derived beyond this single-query raw retrieval
- **Operational notes:** The exact frozen query was submitted unchanged. The bounded count established that the complete set fit the available non-cursor offset boundary. Raw API JSON responses were preserved before transformation with Query ID, Scopus source, page, start position, count, totalResults, run timestamp, and exact query in non-secret metadata sidecars. The API key was not written to responses, sidecars, filenames, or logs. No deduplication, screening, or evidence extraction occurred.
