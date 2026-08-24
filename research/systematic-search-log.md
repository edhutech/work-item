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

## Protocol v1.1 Operational Feasibility Event: ACM Digital Library

- **Event date:** `2026-08-23`
- **Event type:** Operational feasibility validation only; not systematic-search execution.
- **Database:** ACM Digital Library
- **Human-access observation:** Search was accessible in Basic Edition; results displayed up to `50` records per page; `Export Citations` was explicitly labeled as a Premium feature; the current account lacked Premium export capability.
- **Official systematic-search API:** No official documented public ACM Digital Library systematic-search API equivalent to the other evaluated database APIs was established.
- **Complete systematic capture:** Not currently demonstrated; the available access does not support complete bulk citation capture.
- **Seven-branch calibration:** ACM does not participate automatically under current access.
- **Gate classification:** `Conditional targeted / gap-filling source`
- **Activation triggers:** Research-question coverage gap; contradictory or boundary evidence requiring follow-up; ACM-specific literature cluster identified by snowballing; relevant paper or venue requiring targeted follow-up; or evidence of unique ACM studies not adequately covered elsewhere.
- **Study handling:** Any ACM study identified through targeted retrieval remains subject to the same screening, eligibility, quality-assessment, and evidence rules as other academic sources.
- **Gate reopening conditions:** Authorized ACM Premium access; an official documented systematic-search API; or another authorized complete-capture mechanism demonstrating reproducible reconciliation between reported and captured results.
- **Systematic execution status:** No corpus retrieval, screening, deduplication, evidence extraction, or manifest creation occurred.
- **Frozen queries:** Unchanged.
- **Detailed record:** [`database-validation.md`](./database-validation.md#protocol-v11-operational-feasibility-event-acm-digital-library)

## Protocol v1.1 Operational Feasibility Event: ScienceDirect

- **Event date:** `2026-08-23`
- **Event type:** Operational feasibility validation only; not systematic-search execution.
- **Database:** ScienceDirect
- **Representative branch:** `F2A`
- **Frozen field intent:** Combined `Title, abstract or author-specified keywords`
- **Historical Web baseline:** Not available in repository records
- **Official routes tested:** ScienceDirect Search API V2 and Article Metadata API
- **Bounded request:** Exact frozen F2A Boolean adaptation; first page only; maximum 10 metadata results requested; no full text requested
- **Search API V2 status:** HTTP `401`, Elsevier `AUTHORIZATION_ERROR`; no total or identifier sample
- **Article Metadata API status:** HTTP `401`, Elsevier `AUTHORIZATION_ERROR`; no total or identifier sample
- **Field finding:** Search API V2 is documented as searching the ScienceDirect full-text cluster. Article Metadata API is documented as field-restricted but its required Title + Abstract + Author Keywords representation was not established.
- **Completeness finding:** Official documentation states a 6,000-item total-result limit for both routes; complete retrieval is not established under the current entitlement.
- **Stable-identifier comparison:** Not possible; no records were returned.
- **Gate classification:** `C — Unsuitable as a systematic API route`
- **Systematic execution status:** No corpus retrieval, screening, deduplication, evidence extraction, or manifest creation occurred.
- **Detailed record:** [`database-validation.md`](./database-validation.md#protocol-v11-operational-feasibility-event-sciencedirect)

## Protocol v1.1 Operational Feasibility Event: Springer Nature Link

- **Event date:** `2026-08-23`
- **Event type:** Operational feasibility validation only; not systematic-search execution.
- **Database:** Springer Nature Link
- **Representative branch:** `F2A`
- **Query ID:** `S1-F2A-SPRINGER-01-v1`
- **Frozen Web field intent:** `Keywords`, documented as title + abstract + body text
- **Historical Web baseline:** Not available in repository records
- **Official route tested:** Springer Nature Meta API v2 JSON, `/meta/v2/json`
- **Bounded request:** Exact frozen F2A expression as `q`; `p=10`, `s=1`; no full-text request
- **API status:** HTTP `200`; API active under Basic access
- **API total:** `71453`
- **Pagination:** `p` page size and `s` start offset; `s=71451&p=25` returned 3 records
- **Basic page-size limit:** `p=25` accepted; `p=50` returned HTTP `403` premium-only
- **Quota:** 100 requests/minute and 500 requests/day under Basic account documentation
- **Field finding:** Generic Meta API query scope was not shown to reproduce the body-inclusive Web `Keywords` field; response metadata fields were not treated as search fields
- **Stable-identifier comparison:** API DOI/URL sample available; Web/API comparison not performed and deferred for possible future Web/manual activation
- **Complete retrieval:** Not established as complete/auditable under the six-day minimum quota window and undocumented stable ordering
- **Gate classification:** `C — Unsuitable as a systematic API route`
- **API feasibility gate:** Complete; human Web validation is not required to close this API gate
- **Human Web validation:** Deferred; required only if Springer is later activated through a Web/manual route for calibration, targeted retrieval, or gap filling
- **Licensed-data policy:** Separate Springer review required before any calibration retrieval
- **Systematic execution status:** No corpus retrieval, screening, deduplication, evidence extraction, synthesis, or manifest creation occurred
- **Detailed record:** [`database-validation.md`](./database-validation.md#protocol-v11-operational-feasibility-event-springer-nature-link)

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

### S1-F7B-SCOPUS-01-v1

- **Query ID:** `S1-F7B-SCOPUS-01-v1`
- **Branch ID:** `F7B`
- **Branch:** Review and acceptance
- **Branch status:** `Primary`
- **Database:** Scopus
- **Execution mechanism:** Scopus Search API
- **Query version:** `v1`
- **Execution date:** `2026-08-24`
- **Exact frozen query:** `TITLE-ABS-KEY(("software repository" OR GitHub) AND ("pull request acceptance" OR "merge decision" OR "maintainer decision" OR "code review acceptance"))`
- **Fields:** Title, abstract, and author keywords through Scopus `TITLE-ABS-KEY(...)`
- **Filters:** None; no date, publication-type, language, subject, or additional result filter
- **Request route:** STANDARD/default; no explicit `view` parameter
- **Bounded API request:** HTTP `200`; `count=1`, no cursor, `totalResults=14`; no bounded raw artifact was retained
- **Complete retrieval request:** HTTP `200`; offset pagination, `count=25`; cursor pagination was not attempted
- **Execution status:** `Completed`
- **Database-reported API result count:** `14`
- **Raw captured records:** `14`
- **Pagination:** `1` API call/page, start `0`; final page contained `14` records
- **Raw artifacts:** `research/raw-local/scopus/S1-F7B-SCOPUS-01-v1__run-20260824T230423Z__api-start-000000.json`, with one immutable metadata sidecar
- **Public provenance manifest:** `research/manifests/scopus/S1-F7B-SCOPUS-01-v1__run-20260824T230423Z.manifest.json`
- **SHA-256 provenance:** Recorded for the local raw response and provenance sidecar in the public manifest; byte sizes are recorded there as well
- **Raw data policy:** Record-level Scopus data and sidecar files are retained locally/private; the public manifest contains provenance and hashes only
- **Reconciliation:** `14` API-reported results / `14` raw captured records
- **Reconciliation status:** `Complete`
- **Missing pagination ranges:** `No`; the only required offset was `0`
- **Duplicate pagination ranges:** `No`
- **Execution-time deduplication:** `None`
- **Screening:** `Not started`
- **Evidence extraction:** `None`
- **Synthesis:** `None`
- **Unique corpus count:** Not derived beyond this single-query raw retrieval
- **Operational notes:** The exact frozen query was submitted unchanged. `ELSEVIER_API_KEY` was loaded only into the execution process from the ignored local `.env.local` file and was not printed, persisted, or written to responses, sidecars, filenames, manifests, or logs. No deduplication, screening, evidence extraction, interpretation, or downstream branch execution occurred. F7C was not executed.

### S1-F7A-SCOPUS-01-v1

- **Query ID:** `S1-F7A-SCOPUS-01-v1`
- **Branch ID:** `F7A`
- **Branch:** Change correctness and validation
- **Branch status:** `Primary`
- **Database:** Scopus
- **Execution mechanism:** Scopus Search API
- **Query version:** `v1`
- **Execution date:** `2026-08-24`
- **Exact frozen query:** `TITLE-ABS-KEY((patch OR "software change") AND ("patch correctness" OR "patch validation" OR "plausible patch" OR "patch overfitting"))`
- **Fields:** Title, abstract, and author keywords through Scopus `TITLE-ABS-KEY(...)`
- **Filters:** None; no date, publication-type, language, subject, or additional result filter
- **Request route:** STANDARD/default; no explicit `view` parameter
- **Bounded API request:** HTTP `200`; `count=1`, no cursor, `totalResults=192`; no bounded raw artifact was retained
- **Complete retrieval request:** HTTP `200`; offset pagination, `count=25`; cursor pagination was not attempted
- **Execution status:** `Completed`
- **Database-reported API result count:** `192`
- **Raw captured records:** `192`
- **Pagination:** `8` API calls/pages, starts `0` through `175` in increments of `25`; final page contained `17` records
- **Raw artifacts:** `research/raw-local/scopus/S1-F7A-SCOPUS-01-v1__run-20260824T230046Z__api-start-000000.json` through `research/raw-local/scopus/S1-F7A-SCOPUS-01-v1__run-20260824T230046Z__api-start-000175.json`, with one immutable metadata sidecar per response
- **Public provenance manifest:** `research/manifests/scopus/S1-F7A-SCOPUS-01-v1__run-20260824T230046Z.manifest.json`
- **SHA-256 provenance:** Recorded for every local raw response and provenance sidecar in the public manifest; byte sizes are recorded there as well
- **Raw data policy:** Record-level Scopus data and sidecar files are retained locally/private; the public manifest contains provenance and hashes only
- **Reconciliation:** `192` API-reported results / `192` raw captured records
- **Reconciliation status:** `Complete`
- **Missing pagination ranges:** `No`; starts were contiguous and complete
- **Duplicate pagination ranges:** `No`
- **Execution-time deduplication:** `None`
- **Screening:** `Not started`
- **Evidence extraction:** `None`
- **Synthesis:** `None`
- **Unique corpus count:** Not derived beyond this single-query raw retrieval
- **Operational notes:** The exact frozen query was submitted unchanged. `ELSEVIER_API_KEY` was loaded only into the execution process from the ignored local `.env.local` file and was not printed, persisted, or written to responses, sidecars, filenames, manifests, or logs. No deduplication, screening, evidence extraction, interpretation, or downstream branch execution occurred. F7B was not executed.

### S1-F6D2-SCOPUS-01-v1

- **Query ID:** `S1-F6D2-SCOPUS-01-v1`
- **Branch ID:** `F6D2`
- **Branch:** Agent trajectories and process-level execution analysis
- **Branch status:** `Primary`
- **Database:** Scopus
- **Execution mechanism:** Scopus Search API
- **Query version:** `v1`
- **Execution date:** `2026-08-24`
- **Exact frozen query:** `TITLE-ABS-KEY(("coding agent" OR "software engineering agent" OR "SWE agent") AND ("thought-action-result trajectory" OR "process-level trajectory evaluation" OR "trajectory assessment" OR "execution record"))`
- **Fields:** Title, abstract, and author keywords through Scopus `TITLE-ABS-KEY(...)`
- **Filters:** None; no date, publication-type, language, subject, or additional result filter
- **Request route:** STANDARD/default; no explicit `view` parameter
- **Bounded API request:** HTTP `200`; `count=1`, no cursor, `totalResults=1`; no bounded raw artifact was retained
- **Complete retrieval request:** HTTP `200`; offset pagination, `count=25`; cursor pagination was not attempted
- **Execution status:** `Completed`
- **Database-reported API result count:** `1`
- **Raw captured records:** `1`
- **Pagination:** `1` API call/page, start `0`; final page contained `1` record
- **Raw artifacts:** `research/raw-local/scopus/S1-F6D2-SCOPUS-01-v1__run-20260824T221553Z__api-start-000000.json`, with one immutable metadata sidecar
- **Public provenance manifest:** `research/manifests/scopus/S1-F6D2-SCOPUS-01-v1__run-20260824T221553Z.manifest.json`
- **SHA-256 provenance:** Recorded for the local raw response and provenance sidecar in the public manifest; byte sizes are recorded there as well
- **Raw data policy:** Record-level Scopus data and sidecar files are retained locally/private; the public manifest contains provenance and hashes only
- **Reconciliation:** `1` API-reported result / `1` raw captured record
- **Reconciliation status:** `Complete`
- **Missing pagination ranges:** `No`; the only required offset was `0`
- **Duplicate pagination ranges:** `No`
- **Execution-time deduplication:** `None`
- **Screening:** `Not started`
- **Evidence extraction:** `None`
- **Synthesis:** `None`
- **Unique corpus count:** Not derived beyond this single-query raw retrieval
- **Operational notes:** The exact frozen query was submitted unchanged. `ELSEVIER_API_KEY` was loaded only into the execution process from the ignored local `.env.local` file and was not printed, persisted, or written to responses, sidecars, filenames, manifests, or logs. No deduplication, screening, evidence extraction, interpretation, or downstream branch execution occurred. F7A was not executed.

### S1-F6D1-SCOPUS-01-v1

- **Query ID:** `S1-F6D1-SCOPUS-01-v1`
- **Branch ID:** `F6D1`
- **Branch:** Tool use, interfaces, and agent-environment interaction
- **Branch status:** `Primary`
- **Database:** Scopus
- **Execution mechanism:** Scopus Search API
- **Query version:** `v1`
- **Execution date:** `2026-08-24`
- **Exact frozen query:** `TITLE-ABS-KEY(("coding agent" OR "software engineering agent" OR "SWE agent") AND ("agent-computer interface" OR "agent-environment interaction" OR "tool-mediated" OR "bounded tool interface"))`
- **Fields:** Title, abstract, and author keywords through Scopus `TITLE-ABS-KEY(...)`
- **Filters:** None; no date, publication-type, language, subject, or additional result filter
- **Request route:** STANDARD/default; no explicit `view` parameter
- **Bounded API request:** HTTP `200`; `count=1`, no cursor, `totalResults=1`; no bounded raw artifact was retained
- **Complete retrieval request:** HTTP `200`; offset pagination, `count=25`; cursor pagination was not attempted
- **Execution status:** `Completed`
- **Database-reported API result count:** `1`
- **Raw captured records:** `1`
- **Pagination:** `1` API call/page, start `0`; final page contained `1` record
- **Raw artifacts:** `research/raw-local/scopus/S1-F6D1-SCOPUS-01-v1__run-20260824T194222Z__api-start-000000.json`, with one immutable metadata sidecar
- **Public provenance manifest:** `research/manifests/scopus/S1-F6D1-SCOPUS-01-v1__run-20260824T194222Z.manifest.json`
- **SHA-256 provenance:** Recorded for the local raw response and provenance sidecar in the public manifest; byte sizes are recorded there as well
- **Raw data policy:** Record-level Scopus data and sidecar files are retained locally/private; the public manifest contains provenance and hashes only
- **Reconciliation:** `1` API-reported result / `1` raw captured record
- **Reconciliation status:** `Complete`
- **Missing pagination ranges:** `No`; the only required offset was `0`
- **Duplicate pagination ranges:** `No`
- **Execution-time deduplication:** `None`
- **Screening:** `Not started`
- **Evidence extraction:** `None`
- **Synthesis:** `None`
- **Unique corpus count:** Not derived beyond this single-query raw retrieval
- **Operational notes:** The exact frozen query was submitted unchanged. `ELSEVIER_API_KEY` was loaded only into the execution process from the ignored local `.env.local` file and was not printed, persisted, or written to responses, sidecars, filenames, manifests, or logs. No deduplication, screening, evidence extraction, interpretation, or downstream branch execution occurred. F6C2 and F6D2 were not executed.

### S1-F6C1-SCOPUS-01-v1

- **Query ID:** `S1-F6C1-SCOPUS-01-v1`
- **Branch ID:** `F6C1`
- **Branch:** Clarification-seeking and requirement elicitation
- **Branch status:** `Primary`
- **Database:** Scopus
- **Execution mechanism:** Scopus Search API
- **Query version:** `v1`
- **Execution date:** `2026-08-24`
- **Exact frozen query:** `TITLE-ABS-KEY(("coding agent" OR "software engineering agent") AND ("clarification-seeking" OR "requirement elicitation" OR "underspecified instructions" OR "dialogue-driven coding agent"))`
- **Fields:** Title, abstract, and author keywords through Scopus `TITLE-ABS-KEY(...)`
- **Filters:** None; no date, publication-type, language, subject, or additional result filter
- **Request route:** STANDARD/default; no explicit `view` parameter
- **Bounded API request:** HTTP `200`; `count=1`, no cursor, `totalResults=0`; no bounded raw artifact was retained
- **Complete retrieval request:** HTTP `200`; offset pagination, `count=25`; cursor pagination was not attempted
- **Execution status:** `Completed`
- **Database-reported API result count:** `0`
- **Raw captured records:** `0`
- **Pagination:** `1` API call/page, start `0`; empty-result response preserved
- **Raw artifacts:** `research/raw-local/scopus/S1-F6C1-SCOPUS-01-v1__run-20260824T022658Z__api-start-000000.json`, with one immutable provenance sidecar
- **Public provenance manifest:** `research/manifests/scopus/S1-F6C1-SCOPUS-01-v1__run-20260824T022658Z.manifest.json`
- **SHA-256 provenance:** Recorded for the local raw response and provenance sidecar in the public manifest; byte sizes are recorded there as well
- **Raw data policy:** Record-level Scopus data and sidecar files are retained locally/private; the public manifest contains provenance and hashes only
- **Reconciliation:** `0` API-reported results / `0` raw captured records
- **Reconciliation status:** `Complete`
- **Missing pagination ranges:** `No`; the only required offset was `0`
- **Duplicate pagination ranges:** `No`
- **Execution-time deduplication:** `None`
- **Screening:** `Not started`
- **Evidence extraction:** `None`
- **Synthesis:** `None`
- **Unique corpus count:** Not derived beyond this single-query raw retrieval
- **Operational notes:** The exact frozen query was submitted unchanged. `ELSEVIER_API_KEY` was loaded only into the execution process from the ignored local `.env.local` file and was not printed, persisted, or written to responses, sidecars, filenames, manifests, or logs. No deduplication, screening, evidence extraction, interpretation, or downstream branch execution occurred. F6B1 and F6B2 were not executed.

### S1-F6A2-SCOPUS-01-v1

- **Query ID:** `S1-F6A2-SCOPUS-01-v1`
- **Branch ID:** `F6A2`
- **Branch:** Repository retrieval, selection, exploration, and navigation
- **Branch status:** `Primary`
- **Database:** Scopus
- **Execution mechanism:** Scopus Search API
- **Query version:** `v1`
- **Execution date:** `2026-08-24`
- **Exact frozen query:** `TITLE-ABS-KEY(("coding agent" OR "software engineering agent" OR "SWE agent") AND ("repository exploration" OR "structural code retrieval" OR "repository navigation" OR "repository-level understanding"))`
- **Fields:** Title, abstract, and author keywords through Scopus `TITLE-ABS-KEY(...)`
- **Filters:** None; no date, publication-type, language, subject, or additional result filter
- **Request route:** STANDARD/default; no explicit `view` parameter
- **Bounded API request:** HTTP `200`; `count=1`, no cursor, `totalResults=3`; no bounded raw artifact was retained
- **Complete retrieval request:** HTTP `200`; offset pagination, `count=25`; cursor pagination was not attempted
- **Execution status:** `Completed`
- **Database-reported API result count:** `3`
- **Raw captured records:** `3`
- **Pagination:** `1` API call/page, start `0`; final page contained `3` records
- **Raw artifacts:** `research/raw-local/scopus/S1-F6A2-SCOPUS-01-v1__run-20260824T022302Z__api-start-000000.json`, with one immutable provenance sidecar
- **Public provenance manifest:** `research/manifests/scopus/S1-F6A2-SCOPUS-01-v1__run-20260824T022302Z.manifest.json`
- **SHA-256 provenance:** Recorded for the local raw response and provenance sidecar in the public manifest; byte sizes are recorded there as well
- **Raw data policy:** Record-level Scopus data and sidecar files are retained locally/private; the public manifest contains provenance and hashes only
- **Reconciliation:** `3` API-reported results / `3` raw captured records
- **Reconciliation status:** `Complete`
- **Missing pagination ranges:** `No`; the only required offset was `0`
- **Duplicate pagination ranges:** `No`
- **Execution-time deduplication:** `None`
- **Screening:** `Not started`
- **Evidence extraction:** `None`
- **Synthesis:** `None`
- **Unique corpus count:** Not derived beyond this single-query raw retrieval
- **Operational notes:** The exact frozen query was submitted unchanged. `ELSEVIER_API_KEY` was loaded only into the execution process from the ignored local `.env.local` file and was not printed, persisted, or written to responses, sidecars, filenames, manifests, or logs. No deduplication, screening, evidence extraction, interpretation, or downstream branch execution occurred.

### S1-F6A1-SCOPUS-01-v1

- **Query ID:** `S1-F6A1-SCOPUS-01-v1`
- **Branch ID:** `F6A1`
- **Branch:** Context quantity, long-context behavior, and memory
- **Branch status:** `Primary`
- **Database:** Scopus
- **Execution mechanism:** Scopus Search API
- **Query version:** `v1`
- **Execution date:** `2026-08-24`
- **Exact frozen query:** `TITLE-ABS-KEY(("coding agent" OR "software engineering agent" OR "SWE agent") AND ("long-context" OR "context compression" OR "context budget" OR "memory management"))`
- **Fields:** Title, abstract, and author keywords through Scopus `TITLE-ABS-KEY(...)`
- **Filters:** None; no date, publication-type, language, subject, or additional result filter
- **Request route:** STANDARD/default; no explicit `view` parameter
- **Bounded API request:** HTTP `200`; `count=1`, no cursor, `totalResults=0`; no bounded raw artifact was retained
- **Initial complete attempt:** HTTP `200`; the API returned the Scopus empty-result error sentinel with `totalResults=0`; no artifact was written. Retrieval was rerun after the utility was corrected to treat this sentinel as zero records.
- **Complete retrieval request:** HTTP `200`; offset pagination, `count=25`; cursor pagination was not attempted
- **Execution status:** `Completed`
- **Database-reported API result count:** `0`
- **Raw captured records:** `0`
- **Pagination:** `1` API call/page, start `0`; empty-result response preserved
- **Raw artifacts:** `research/raw-local/scopus/S1-F6A1-SCOPUS-01-v1__run-20260824T021151Z__api-start-000000.json`, with one immutable provenance sidecar
- **Public provenance manifest:** `research/manifests/scopus/S1-F6A1-SCOPUS-01-v1__run-20260824T021151Z.manifest.json`
- **SHA-256 provenance:** Recorded for the local raw response and provenance sidecar in the public manifest; byte sizes are recorded there as well
- **Raw data policy:** Record-level Scopus data and sidecar files are retained locally/private; the public manifest contains provenance and hashes only
- **Reconciliation:** `0` API-reported results / `0` raw captured records
- **Reconciliation status:** `Complete`
- **Missing pagination ranges:** `No`; the only required offset was `0`
- **Duplicate pagination ranges:** `No`
- **Execution-time deduplication:** `None`
- **Screening:** `Not started`
- **Evidence extraction:** `None`
- **Synthesis:** `None`
- **Unique corpus count:** Not derived beyond this single-query raw retrieval
- **Operational notes:** The exact frozen query was submitted unchanged. `ELSEVIER_API_KEY` was loaded only into the execution process from the ignored local `.env.local` file and was not printed, persisted, or written to responses, sidecars, filenames, manifests, or logs. No deduplication, screening, evidence extraction, interpretation, or downstream branch execution occurred. The empty-result response contained no Scopus record.

### S1-F5C-SCOPUS-01-v1

- **Query ID:** `S1-F5C-SCOPUS-01-v1`
- **Branch ID:** `F5C`
- **Branch:** SWE-agent lineage and population boundaries
- **Branch status:** `Primary`
- **Database:** Scopus
- **Execution mechanism:** Scopus Search API
- **Query version:** `v1`
- **Execution date:** `2026-08-24`
- **Exact frozen query:** `TITLE-ABS-KEY(("SWE-agent" OR "SWE agents" OR "mini-SWE-agent") OR ("SWE-bench" AND ("coding agent" OR "software engineering agent")))`
- **Fields:** Title, abstract, and author keywords through Scopus `TITLE-ABS-KEY(...)`
- **Filters:** None; no date, publication-type, language, subject, or additional result filter
- **Request route:** STANDARD/default; no explicit `view` parameter
- **Bounded API request:** HTTP `200`; `count=1`, no cursor, `totalResults=42`; no bounded raw artifact was retained
- **Complete retrieval request:** HTTP `200`; offset pagination, `count=25`; cursor pagination was not attempted
- **Execution status:** `Completed`
- **Database-reported API result count:** `42`
- **Raw captured records:** `42`
- **Pagination:** `2` API calls/pages, starts `0` and `25` in increments of `25`; final page contained `17` records
- **Raw artifacts:** `research/raw-local/scopus/S1-F5C-SCOPUS-01-v1__run-20260824T020505Z__api-start-000000.json` and `research/raw-local/scopus/S1-F5C-SCOPUS-01-v1__run-20260824T020505Z__api-start-000025.json`, with one immutable provenance sidecar per response
- **Public provenance manifest:** `research/manifests/scopus/S1-F5C-SCOPUS-01-v1__run-20260824T020505Z.manifest.json`
- **SHA-256 provenance:** Recorded for every local raw response and provenance sidecar in the public manifest; byte sizes are recorded there as well
- **Raw data policy:** Record-level Scopus data and sidecar files are retained locally/private; the public manifest contains provenance and hashes only
- **Reconciliation:** `42` API-reported results / `42` raw captured records
- **Reconciliation status:** `Complete`
- **Missing pagination ranges:** `No`; starts were contiguous and complete
- **Duplicate pagination ranges:** `No`
- **Execution-time deduplication:** `None`
- **Screening:** `Not started`
- **Evidence extraction:** `None`
- **Synthesis:** `None`
- **Unique corpus count:** Not derived beyond this single-query raw retrieval
- **Operational notes:** The exact frozen query was submitted unchanged. `ELSEVIER_API_KEY` was loaded only into the execution process from the ignored local `.env.local` file and was not printed, persisted, or written to responses, sidecars, filenames, manifests, or logs. No deduplication, screening, or evidence extraction occurred. No subsequent branch was executed.

### S1-F5B-SCOPUS-01-v1

- **Query ID:** `S1-F5B-SCOPUS-01-v1`
- **Branch ID:** `F5B`
- **Branch:** Software-engineering-agent population
- **Branch status:** `Primary`
- **Database:** Scopus
- **Execution mechanism:** Scopus Search API
- **Query version:** `v1`
- **Execution date:** `2026-08-24`
- **Exact frozen query:** `TITLE-ABS-KEY(("software engineering agent" OR "AI software engineer" OR "SWE agent") AND ("software engineering" OR "repository-level task"))`
- **Fields:** Title, abstract, and author keywords through Scopus `TITLE-ABS-KEY(...)`
- **Filters:** None; no date, publication-type, language, subject, or additional result filter
- **Request route:** STANDARD/default; no explicit `view` parameter
- **Bounded API request:** HTTP `200`; `count=1`, no cursor, `totalResults=59`; no bounded raw artifact was retained
- **Complete retrieval request:** HTTP `200`; offset pagination, `count=25`; cursor pagination was not attempted
- **Execution status:** `Completed`
- **Database-reported API result count:** `59`
- **Raw captured records:** `59`
- **Pagination:** `3` API calls/pages, starts `0`, `25`, and `50` in increments of `25`; final page contained `9` records
- **Raw artifacts:** `research/raw-local/scopus/S1-F5B-SCOPUS-01-v1__run-20260824T015145Z__api-start-000000.json` through `research/raw-local/scopus/S1-F5B-SCOPUS-01-v1__run-20260824T015145Z__api-start-000050.json`, with one immutable provenance sidecar per response
- **Public provenance manifest:** `research/manifests/scopus/S1-F5B-SCOPUS-01-v1__run-20260824T015145Z.manifest.json`
- **SHA-256 provenance:** Recorded for every local raw response and provenance sidecar in the public manifest; byte sizes are recorded there as well
- **Raw data policy:** Record-level Scopus data and sidecar files are retained locally/private; the public manifest contains provenance and hashes only
- **Reconciliation:** `59` API-reported results / `59` raw captured records
- **Reconciliation status:** `Complete`
- **Missing pagination ranges:** `No`; starts were contiguous and complete
- **Duplicate pagination ranges:** `No`
- **Execution-time deduplication:** `None`
- **Screening:** `Not started`
- **Evidence extraction:** `None`
- **Synthesis:** `None`
- **Unique corpus count:** Not derived beyond this single-query raw retrieval
- **Operational notes:** The exact frozen query was submitted unchanged. `ELSEVIER_API_KEY` was loaded only into the execution process from the ignored local `.env.local` file and was not printed, persisted, or written to responses, sidecars, filenames, manifests, or logs. No deduplication, screening, or evidence extraction occurred. F5C and all Supplementary branches were not executed.

### S1-F5A-SCOPUS-01-v1

- **Query ID:** `S1-F5A-SCOPUS-01-v1`
- **Branch ID:** `F5A`
- **Branch:** Coding-agent population
- **Branch status:** `Primary`
- **Database:** Scopus
- **Execution mechanism:** Scopus Search API
- **Execution date:** `2026-08-24`
- **Exact frozen query:** `TITLE-ABS-KEY(("coding agent" OR "AI coding agent" OR "agentic coding") AND ("software development" OR "software engineering" OR "repository-level task"))`
- **Fields:** Title, abstract, and author keywords through Scopus `TITLE-ABS-KEY(...)`
- **Filters:** None; no date, publication-type, language, subject, or additional result filter
- **Request route:** STANDARD/default; no explicit `view` parameter
- **Bounded API request:** HTTP `200`; `count=1`; `totalResults=79`; no raw bounded artifact was retained
- **Complete retrieval request:** HTTP `200`; offset pagination; `count=25`; cursor pagination was not attempted
- **Execution status:** `Completed`
- **Database-reported API result count:** `79`
- **Raw captured records:** `79`
- **Pagination:** `4` API calls/pages, starts `0` through `75` in increments of `25`; final page contained `4` records
- **Raw artifacts:** `research/raw-local/scopus/S1-F5A-SCOPUS-01-v1__run-20260824T010748Z__api-start-000000.json` through `research/raw-local/scopus/S1-F5A-SCOPUS-01-v1__run-20260824T010748Z__api-start-000075.json`, with one immutable provenance sidecar per response
- **Public provenance manifest:** `research/manifests/scopus/S1-F5A-SCOPUS-01-v1__run-20260824T010748Z.manifest.json`
- **SHA-256 provenance:** Recorded for every local raw response and provenance sidecar in the public manifest; byte sizes are recorded there as well
- **Raw data policy:** Record-level Scopus data and sidecar files are retained locally/private; the public manifest contains provenance and hashes only
- **Reconciliation:** `79` API-reported results / `79` raw captured records
- **Reconciliation status:** `Complete`
- **Missing pagination ranges:** `No`; starts were contiguous and complete
- **Duplicate pagination ranges:** `No`
- **Execution-time deduplication:** `None`
- **Screening:** `Not started`
- **Evidence extraction:** `None`
- **Synthesis:** `None`
- **Unique corpus count:** Not derived beyond this single-query raw retrieval
- **Known-item results:** `Not verified`; no separate known-item retrieval was performed during this execution
- **Operational notes:** The exact frozen query was submitted unchanged. `ELSEVIER_API_KEY` was loaded only into the execution process from the ignored local `.env.local` file and was not printed, persisted, or written to responses, sidecars, filenames, manifests, or logs. No deduplication, screening, or evidence extraction occurred. F5B and all Supplementary branches were not executed.

### S1-F4D-SCOPUS-01-v1

- **Query ID:** `S1-F4D-SCOPUS-01-v1`
- **Branch ID:** `F4D`
- **Branch:** Documentation information and burden
- **Branch status:** `Primary`
- **Database:** Scopus
- **Execution mechanism:** Scopus Search API
- **Execution date:** `2026-08-24`
- **Exact frozen query:** `TITLE-ABS-KEY(("software development" OR "software maintenance") AND ("software documentation" OR "documentation relevance" OR "documentation quality" OR "documentation usefulness"))`
- **Fields:** Title, abstract, and author keywords through Scopus `TITLE-ABS-KEY(...)`
- **Filters:** None; no date, publication-type, language, subject, or additional result filter
- **Request route:** STANDARD/default; no explicit `view` parameter
- **Bounded API request:** HTTP `200`; `count=1`; `totalResults=302`; no raw bounded artifact was retained
- **Complete retrieval request:** HTTP `200`; offset pagination; `count=25`; cursor pagination was not attempted
- **Execution status:** `Completed`
- **Database-reported API result count:** `302`
- **Raw captured records:** `302`
- **Pagination:** `13` API calls/pages, starts `0` through `300` in increments of `25`; final page contained `2` records
- **Raw artifacts:** `research/raw-local/scopus/S1-F4D-SCOPUS-01-v1__run-20260824T005501Z__api-start-000000.json` through `research/raw-local/scopus/S1-F4D-SCOPUS-01-v1__run-20260824T005501Z__api-start-000300.json`, with one immutable provenance sidecar per response
- **Public provenance manifest:** `research/manifests/scopus/S1-F4D-SCOPUS-01-v1__run-20260824T005501Z.manifest.json`
- **SHA-256 provenance:** Recorded for every local raw response and provenance sidecar in the public manifest; byte sizes are recorded there as well
- **Raw data policy:** Record-level Scopus data and sidecar files are retained locally/private; the public manifest contains provenance and hashes only
- **Reconciliation:** `302` API-reported results / `302` raw captured records
- **Reconciliation status:** `Complete`
- **Missing pagination ranges:** `No`; starts were contiguous and complete
- **Duplicate pagination ranges:** `No`
- **Execution-time deduplication:** `None`
- **Screening:** `Not started`
- **Evidence extraction:** `None`
- **Synthesis:** `None`
- **Unique corpus count:** Not derived beyond this single-query raw retrieval
- **Known-item results:** `Not verified`; no separate known-item retrieval was performed during this execution
- **Operational notes:** The exact frozen query was submitted unchanged. `ELSEVIER_API_KEY` was loaded only into the execution process from the ignored local `.env.local` file and was not printed, persisted, or written to responses, sidecars, filenames, manifests, or logs. No deduplication, screening, or evidence extraction occurred. F4C2 was not executed.

### S1-F4C1-SCOPUS-01-v1

- **Query ID:** `S1-F4C1-SCOPUS-01-v1`
- **Branch ID:** `F4C1`
- **Branch:** Mental workload and cognitive burden
- **Branch status:** `Primary`
- **Database:** Scopus
- **Execution mechanism:** Scopus Search API
- **Execution date:** `2026-08-24`
- **Exact frozen query:** `TITLE-ABS-KEY((programmer OR "software developer" OR "software engineer") AND ("mental workload" OR "cognitive workload" OR "programmers' cognitive load" OR "program comprehension"))`
- **Fields:** Title, abstract, and author keywords through Scopus `TITLE-ABS-KEY(...)`
- **Filters:** None; no date, publication-type, language, subject, or additional result filter
- **Request route:** STANDARD/default; no explicit `view` parameter
- **Bounded API request:** HTTP `200`; `count=1`; `totalResults=637`; no raw bounded artifact was retained
- **Complete retrieval request:** HTTP `200`; offset pagination; `count=25`; cursor pagination was not attempted
- **Execution status:** `Completed`
- **Database-reported API result count:** `637`
- **Raw captured records:** `637`
- **Pagination:** `26` API calls/pages, starts `0` through `625` in increments of `25`; final page contained `12` records
- **Raw artifacts:** `research/raw-local/scopus/S1-F4C1-SCOPUS-01-v1__run-20260824T004934Z__api-start-000000.json` through `research/raw-local/scopus/S1-F4C1-SCOPUS-01-v1__run-20260824T004934Z__api-start-000625.json`, with one immutable provenance sidecar per response
- **Public provenance manifest:** `research/manifests/scopus/S1-F4C1-SCOPUS-01-v1__run-20260824T004934Z.manifest.json`
- **SHA-256 provenance:** Recorded for every local raw response and provenance sidecar in the public manifest; byte sizes are recorded there as well
- **Raw data policy:** Record-level Scopus data and sidecar files are retained locally/private; the public manifest contains provenance and hashes only
- **Reconciliation:** `637` API-reported results / `637` raw captured records
- **Reconciliation status:** `Complete`
- **Missing pagination ranges:** `No`; starts were contiguous and complete
- **Duplicate pagination ranges:** `No`
- **Execution-time deduplication:** `None`
- **Screening:** `Not started`
- **Evidence extraction:** `None`
- **Synthesis:** `None`
- **Unique corpus count:** Not derived beyond this single-query raw retrieval
- **Known-item results:** `Not verified`; no separate known-item retrieval was performed during this execution
- **Operational notes:** The exact frozen query was submitted unchanged. `ELSEVIER_API_KEY` was loaded only into the execution process from the ignored local `.env.local` file and was not printed, persisted, or written to responses, sidecars, filenames, manifests, or logs. No deduplication, screening, or evidence extraction occurred. F4C2 was not executed.

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
