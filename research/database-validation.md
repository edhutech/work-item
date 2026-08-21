# Database-Specific Validation

**Validation date:** 2026-08-20
**Phase:** Database-Specific Validation
**Methodological authority:** [`protocol.md`](./protocol.md)
**Search-design authority:** [`systematic-search-design.md`](./systematic-search-design.md)
**Pilot calibration authority:** [`search-log.md`](./search-log.md)

## Scope And Boundary

This artifact records human verification of access, search capability, field behavior, metadata visibility, and export capability for the six protocol databases. It records operational database capability only. It does not execute the systematic search, freeze systematic queries, collect a research corpus, screen records, extract evidence, or synthesize findings.

Access provenance is recorded only with generic labels. No institution, account, researcher, authentication identifier, proxy, or local access detail is recorded.

## Diagnostic Query Classification

All searches performed during human verification were **Database-validation diagnostic searches**. They were not systematic-search executions, corpus records, screened records, included sources, or evidence. Their result counts must not be reused as systematic-search result counts.

Files exported during these diagnostic tests are verification artifacts only. They were not incorporated into the research corpus.

## Verified Database Records

### Scopus

- **Access:** Institutional authenticated access.
- **Search capability:** Advanced Search was accessible. `TITLE-ABS-KEY(...)`, field codes, Boolean operators, and visible proximity operators including `PRE/` and `W/` worked or were available. The diagnostic search for `"software engineering agent"` executed successfully and returned document records. Abstracts were accessible in the result workflow.
- **Export capability:** Bulk CSV export worked. The interface stated that up to 20,000 documents can be exported in CSV. Available fields included citation and bibliographic information, abstracts, author keywords, indexed keywords, DOI, publication stage, document type, EID, and other metadata.
- **Operational classification:** `Operational`.
- **Material limitation:** Institutional authenticated access is required for the observed route. Export size and batching must still be recorded for each systematic execution.

The diagnostic records are not part of the systematic corpus.

### Web of Science Core Collection

- **Access:** Institutional authenticated access. Core Collection was accessible without requiring a separate personal login for database access.
- **Search capability:** Advanced Search was accessible. `TS=(...)` worked. The diagnostic query `TS=("software engineering agent")` executed successfully. Document records and abstracts were accessible.
- **Export capability:** Export was available, with an interface-stated maximum of 1,000 records per batch. Direct Excel export failed during this observed session. Export by email succeeded. Email Full Record export can include authors, title, source, abstract, document type, year, DOI when available, Web of Science unique identifier (`UT`), categories, references, and additional bibliographic metadata.
- **Operational classification:** `Operational with documented export limitation`.
- **Material limitation:** Direct Excel export failed in the observed session. Email Full Record export succeeded and does not block systematic retrieval, but export batching and format handling must be planned and logged.

The diagnostic records are not part of the systematic corpus.

### ScienceDirect

- **Access:** Institutional authenticated access.
- **Search capability:** Advanced Search was accessible. Search fields included `Title, abstract or author-specified keywords`, title, journal/book title, authors, affiliation, references, ISSN/ISBN, publication year, and other bibliographic fields. Separate abstract-only and author-keyword-only fields were not visible. The combined Title/Abstract/Author Keywords field worked. The diagnostic search for `"software engineering agent"` executed successfully, returned results, and displayed abstracts. Institutional full-text access was visible for at least part of the collection.
- **Export capability:** Citation export worked. Exported data included title, authors, publication, year, volume/issue where available, DOI, URL, abstract, and keywords.
- **Operational classification:** `Operational with reduced field granularity`.
- **Material limitation:** Database-specific systematic queries must use the combined Title/Abstract/Author Keywords field rather than assume independent Scopus-style fields.

The diagnostic records are not part of the systematic corpus.

### IEEE Xplore

- **Access:** Public. No institutional subscription was used during verification.
- **Search capability:** Advanced Search and Command Search were accessible. Searchable fields included All Metadata, Full Text & Metadata, Full Text Only, Document Title, Abstract, Author Keywords, IEEE Terms, DOI, authors, publication title, and other metadata fields. Command Search displayed `AND`, `OR`, `NOT`, `NEAR`, and `ONEAR`. The interface stated a maximum of 25 search terms per search clause. The diagnostic search for `"software engineering agent"` executed successfully and returned results with visible abstracts.
- **Export capability:** Citation/result export worked without registration or sign-in. Plain-text citation records included title, authors, venue, year, DOI, abstract, keywords, and URL.
- **Operational classification:** `Operational`.
- **Material limitations:** Some full-text records remain subscription-restricted, while Open Access records are accessible. Full-text subscription status is a later retrieval issue, not a systematic-identification blocker. Query branches may need database-specific splitting to respect the 25-terms-per-clause constraint.

The diagnostic records are not part of the systematic corpus.

### IEEE Metadata API support boundary

Local support for the IEEE Xplore Metadata API is prepared in [`tools/ieee_metadata.py`](./tools/ieee_metadata.py). The utility is setup-only in this change: no API request was made, no systematic query was executed, and no API result or corpus record was created. The local credential is read only from `IEEE_API_KEY`; it is not stored, printed, logged, placed in URLs saved to disk, or preserved in raw artifacts.

The IEEE web Command Search execution remains authoritative. The API is a separate executable representation and is not approved as a substitute for web systematic retrieval. The candidate validation case is `S1-F2A-IEEE-01-v1.1`, with an observed web result-count target of `4798`; count equality alone is insufficient. The prepared validation gate also requires the web field strategy, the candidate API representation, and a deterministic sample comparison using stable article numbers and/or DOIs.

The web field strategy is `Document Title`, `Abstract`, and `Author Keywords`. API field behavior is not assumed equivalent: `index_terms` may include more than Author Keywords. Unless exact Author Keywords-only semantics are demonstrated, API replacement remains unresolved and unapproved. API retrieval, if later approved, preserves untouched JSON responses under `research/raw/systematic-search/`, reports `totalfound`, reconciles raw counts, and does not retrieve full text, screen, deduplicate, extract evidence, or synthesize findings.

### Scopus Search API support boundary

Support is available in [`tools/scopus_search.py`](./tools/scopus_search.py). Scopus API connectivity and bounded equivalence validation were completed with HTTP 200; the API credential was not printed, logged, or stored, and no corpus record was created. The utility reads `ELSEVIER_API_KEY` only for the `X-ELS-APIKey` request header.

The frozen Scopus web query expressions in [`systematic-queries.md`](./systematic-queries.md) remain authoritative. The utility accepts the exact frozen `TITLE-ABS-KEY(...)` expression and does not translate, simplify, or regenerate it. Query `S1-F1-SCOPUS-01-v1` completed the validation gate: the frozen query representation was identical, the Scopus Web count and API `totalResults` were both `2596`, and the 10-record validation samples matched exactly by EID, DOI, and EID+DOI pair (`10/10`). Web/API sample order differed because records were tied on publication date; identical ordering is not required for equivalence and this difference was not treated as a retrieval-equivalence failure.

On this basis, Scopus Search API retrieval is validated for the frozen Scopus `TITLE-ABS-KEY` query representation and may now be used as the retrieval mechanism for frozen Scopus systematic queries. Each retrieval must preserve its exact frozen query, Query ID, API-reported total, request pagination, and immutable raw API provenance. This validation is specific to Scopus and does not generalize to IEEE Xplore or other databases. The validation was bounded: no full retrieval, systematic corpus artifact, screening, or deduplication occurred.

Raw API response bytes are preserved unchanged under `research/raw/systematic-search/` with immutable pagination metadata sidecars. Retrieval reconciles captured entries to API `totalResults`, fails on incomplete pagination, performs no execution-time deduplication, screening, or evidence extraction, and uses conservative pacing. No systematic API execution occurred in this setup.

### Scopus pagination and view hardening

The completed F1 run sent no explicit Scopus `view` or field-selection parameter. Its `25` records/request came from the utility's explicit `count=25`, producing `ceil(2596 / 25) = 104` pages; the run does not establish that `COMPLETE` was selected by the API. The preserved response fields cover the current identification metadata contract, but do not include abstracts.

The utility now uses the validated Scopus default route: it omits `view`, allowing Scopus to select `STANDARD`, and defaults to `count=200`. Explicit `view=STANDARD` is also supported at up to 200 records/request. `view=COMPLETE` is an opt-in mode limited to 25 records/request and is not required for systematic identification; it may be entitlement-restricted. STANDARD and COMPLETE response fields are not claimed to be equivalent. If richer metadata such as abstracts is needed later, that is a separate enrichment concern rather than a reason to force COMPLETE during search retrieval.

Pagination policy is deterministic: `pagination=auto` uses cursor pagination from the first request, while explicit `pagination=offset` remains available for result sets at or below the 5,000-record offset boundary. Cursor mode preserves cursor provenance, detects repeated cursors, rejects premature short/empty pages, and reconciles captured entries against API `totalResults`. It fails rather than silently truncating a result set beyond the offset boundary. No deduplication or screening is performed during either mode.

### ACM Digital Library

- **Access:** Public - Basic Edition. No Premium institutional access was used during verification.
- **Search capability:** Advanced Search was accessible. Fields included Anywhere, Title, Publication Title, Author, Abstract, Full Text, Author Affiliation, Author Keyword, DOI, and additional fields. The interface documented `AND`, `OR`, `NOT`, exact phrases in double quotation marks, wildcards `*` and `?`, publication-date filters, and query syntax. An Abstract-specific diagnostic query for `"software engineering agent"` executed successfully and produced a distinct result set. Result metadata and abstracts were visible.
- **Export capability:** Bulk citation export was not available in Basic Edition. The interface stated: `To export citations, you must have Premium access.` Bulk download of citations and search results is listed as a Premium feature.
- **Operational classification:** `Usable with material bulk-export limitation`.
- **Material limitations:** Advanced systematic searching and field-specific searching are viable. Reproducible metadata capture at systematic-search scale requires a method decision before ACM systematic branches are executed. No workaround is authorized or selected in this run. Scraping is not proposed, and Premium access is not assumed or recommended.

The diagnostic records are not part of the systematic corpus.

### Springer Nature Link

- **Access:** Public search access. A free account was required for downloading search-result CSV in the observed workflow. No paid or institutional subscription was required for the verified search-and-export workflow.
- **Search capability:** Advanced Search was accessible. Fields included Keywords, Title, Author(s) or Editor(s), journal, and publication date. The interface documented `AND`, `OR`, `NOT`, parentheses, and exact phrases in quotation marks. Official support documentation states that the Keywords field searches across the document, including title, abstract, and body text, while excluding supplementary files. No separate abstract-only field was visible. The diagnostic query `"software engineering agent"` executed successfully and returned results.
- **Export capability:** Search results could be downloaded as CSV. The observed CSV contained bibliographic metadata useful for identification and deduplication, but less metadata and abstract/keyword depth than Scopus or Web of Science.
- **Operational classification:** `Operational with reduced field and export metadata granularity`.
- **Material limitations:** The Keywords field is broader than Title/Abstract/Keywords because it also searches body text. This must be considered when adapting queries and interpreting result-count differences. A free account is required for the observed CSV export workflow.

The diagnostic records are not part of the systematic corpus.

## Updated Readiness Matrix

| Database | Access | Advanced search | Field control | Export | Main limitation | Overall readiness |
|---|---|---|---|---|---|---|
| Scopus | Institutional authenticated | Verified | Strong | CSV, up to 20,000 documents | Institutional-access dependency | Operational |
| Web of Science Core Collection | Institutional authenticated | Verified | Strong | Email Full Record succeeded; 1,000 per batch stated | Direct Excel error observed | Operational with documented export limitation |
| ScienceDirect | Institutional authenticated | Verified | Moderate | Citation export verified | Combined Title/Abstract/Author Keywords field | Operational with reduced field granularity |
| IEEE Xplore | Public | Verified | Strong | Verified without account | 25 terms per clause; paid full text for some records | Operational |
| ACM Digital Library | Public Basic Edition | Verified | Strong | Bulk export unavailable in Basic Edition | Premium required for bulk citation/results export | Usable with material bulk-export limitation |
| Springer Nature Link | Public; free account required for observed CSV export | Verified | Moderate | CSV via free account | Keywords searches body text; reduced metadata export | Operational with reduced field and export metadata granularity |

## Access Contingency Reassessment

The previous status, `Access contingencies partially resolved; human access verification required`, is superseded by this completed human verification.

Five databases have an operational search-and-export path, with documented limitations. ACM has operational advanced and field-specific search, but Basic Edition does not provide bulk citation/result export. ACM is not removed and no substitute database is introduced. No paid subscription is assumed or required at this stage.

The six-database environment is operationally sufficient to move toward systematic-query freeze, subject to the separate ACM bulk-export workflow decision and the ordinary database-specific query, batching, and export planning required by the search design. This record does not begin query freeze.

## Minimum Viable Database-Set Assessment

The six-database design remains methodologically justified as an operationally viable set, not because of its database count alone. Its coverage combines:

- IEEE Xplore and ACM Digital Library for computer-science and software-engineering conferences, journals, workshops, HCI, requirements, and coding-agent literature;
- Scopus and Web of Science for broad citation-index coverage, multidisciplinary discovery, and database overlap;
- ScienceDirect for Elsevier journal and conference content, including software engineering, requirements, maintenance, and empirical work;
- Springer Nature Link for Springer journals, books, proceedings, and related software-engineering literature;
- recent coding-agent literature, while recognizing that recent terminology and indexing may be uneven across databases.

Observed overlap among the databases is useful for deduplication and coverage comparison, but overlap does not establish equivalent coverage. Publisher-specific and conference routes remain non-interchangeable. The export limitations, reduced field granularity, and ACM metadata-capture issue affect execution planning and interpretation of result counts, but they do not currently require a protocol database-set revision.

### Distinct Readiness Questions

- **Search-query viability:** Viable across all six databases. Each provides an accessible advanced or equivalent search interface, and the required Boolean/field strategies can be adapted to observed controls.
- **Result-export viability:** Viable for five databases. ACM search is viable, but reproducible systematic-scale metadata capture remains unresolved because Basic Edition lacks bulk citation/result export. Web of Science requires batching and email/format handling; other limitations are documented in the matrix.
- **Later full-text access:** Not a current database-identification blocker. Paid full text is not required for database identification or search validation. Open Access versions, preprints, author manuscripts, institutional repositories, and other legitimate routes may later be used where allowed. Studies with inaccessible full texts must be handled according to the screening/full-text protocol when that phase begins.

The minimum viable database set therefore remains the six protocol databases. No database substitution or protocol change is made in this run.

## ACM Systematic Result-Capture Workflow

**Investigation date:** 2026-08-20

This section resolves the capture design only. It does not execute an ACM systematic query, collect a systematic result count, or collect a corpus. Any record viewed while checking this workflow remains `Operational validation only`.

### Evidence and capability boundary

The prior human verification established that Basic Edition exposes Advanced Search, the validated Title, Abstract, and Author Keyword fields, Boolean and phrase search, wildcards, result records, abstracts, and bibliographic detail. The interface also explicitly states that citation export requires Premium access and that bulk search-result citation download is a Premium feature. These observations are retained as platform observations rather than treated as a corpus result.

The following ACM mechanisms were checked conceptually against the public Digital Library interface and ACM library-resource information:

| Mechanism | Basic Edition finding | Capture consequence |
|---|---|---|
| Individual record page | Record metadata, abstract, DOI where present, and ACM record navigation are visible | A record can be transcribed or copied individually, subject to the live-page check below |
| Formatted citation, BibTeX, RIS, citation-manager integration | No Basic Edition bulk route was verified; no documented Basic Edition batch route was found | Must not be assumed as a systematic export mechanism |
| Bulk result/citation export | Not available; Premium requirement is explicit in the interface | Does not provide a Basic Edition workflow |
| ACM bibliographic API or metadata endpoint for arbitrary search-result export | No public, documented ACM API suitable for this purpose was identified in the inspected official material | Do not substitute an undocumented endpoint or unofficial crawler |
| Search-result URL, pagination, page size, saved-search persistence | Search and result navigation are available, but reproducible pagination/page-size persistence was not established without executing a systematic query | Must be verified in a human pilot before execution; URLs and page numbers must be captured as evidence, not inferred |

Sources inspected: [ACM Digital Library](https://dl.acm.org/), [ACM Digital Library resources](https://libraries.acm.org/digital-library-resources), and ACM’s [authorized-user terms](https://www.acm.org/publications/policies/terms-for-authorized-users). The ACM resource pages were not machine-readable from this environment; their non-availability here is not evidence that an undocumented API exists. The explicit Premium message and the earlier human interface verification remain the controlling evidence for export capability.

### Completed human operational verification

The researcher completed a separate **Database-validation diagnostic search** in ACM Basic Edition. It was not a frozen systematic query, and the inspected records remain operational-validation records only. The diagnostic result set reported 44 results. With 20 records per page, ACM displayed the deterministic ranges `1-20 of 44`, `21-40 of 44`, and `41-44 of 44`; pages 1, 2, and 3 were navigated successfully. The interface also exposed page sizes of 10, 20, and 50. This verifies an explicit exhaustive pagination sequence for the observed result set, without generalizing the observed count or page behavior beyond that verification.

The diagnostic result URL preserved the selected field and search expression. It is therefore suitable as supplementary operational provenance, but it does not replace the frozen Query ID, exact frozen query, execution timestamp, or recorded interface state.

Result-list rows exposed useful raw metadata, depending on record type: content/document type, publication date/year, title, authors where applicable, publication or venue information, page information where applicable, DOI where available, abstract or snippet text, and a direct ACM record link. Individual diagnostic article/paper pages supplied stable ACM URLs, title, author or authors, publication/venue, publication date, DOI-style identifier where available, and abstract. A diagnostic `PROCEEDING` record also opened at a stable `/doi/proceedings/{identifier}` ACM locator and exposed proceeding title, publication year/type, publisher, conference information, ISBN, publication date, abstract, and internal contents. These examples validate record-type handling only; they are not evidence records.

Not every record type exposes the same fields in the list view. DOI and author data are therefore optional raw fields, not universal list-view requirements. The stable ACM record URL is the mandatory fallback locator when DOI is absent or not applicable.

### Candidate workflows

| Candidate | Cost | Completeness and structure | Provenance and reproducibility | Burden, failure modes, and risk | Decision |
|---|---|---|---|---|---|
| **Basic Edition manual, page-by-page and record-by-record capture** | Free; account requirement unknown | Can capture the full set only if every result page is traversed and every displayed record is captured. Structured fields are limited to what the page exposes, but can include title, authors, publication, year, DOI, ACM URL/identifier, abstract when visible, page number, and capture order | Strong when each row stores Search ID, query ID, execution timestamp, reported count, page URL, page number, ordinal, and ACM locator. The ACM row remains the identification record | High. Transcription errors, changed ordering, duplicate display rows, stale URLs, interrupted sessions, and missed pages are possible; high effort across 33 queries. Count/page reconciliation and position records mitigate these risks | **Preferred no-cost workflow**, human-verified |
| **Basic Edition individual record inspection plus DOI enrichment** | Free or service-specific limits; account requirement unknown | ACM still identifies each record. Crossref can return one DOI record and RIS/BibTeX/CSL representations; OpenAlex can return DOI-linked bibliographic metadata. Neither service can recover ACM records that were not captured or records without DOI | ACM raw fields and ACM locator remain authoritative; enrichment is a separate nullable layer with source, request date, response status, and match key | Moderate to high. DOI absence, malformed DOI, version mismatch, missing abstracts, stale or conflicting metadata, rate limits, and false DOI matches require explicit failure states. DOI coverage cannot be presumed sufficient | Permitted enrichment after capture, never a replacement retrieval path |
| **Premium bulk citation/result export** | Requires paid Premium access; availability to the researcher is unknown | Explicitly intended to export search-result citations in bulk and is the most direct route to complete structured capture, subject to export limits/batching and count reconciliation | Strong if the original ACM query, count, export batch, and raw files are preserved | Low to moderate, but export truncation, batch limits, format changes, and account entitlement remain risks | **Fallback** if Basic manual capture fails the pilot or paid access is independently approved |
| **Unofficial HTTP extraction, scraping, or browser automation** | Unknown | Could appear complete but has no verified completeness guarantee and may omit dynamically loaded or access-controlled records | Weak unless ACM permits it and the capture can be independently audited | Maintenance, throttling, terms/access uncertainty, changed markup, silent omissions, and possible circumvention of Premium restrictions | Rejected for this run; no implementation or recommendation |

### Preferred workflow and execution controls

The preferred workflow is **Basic Edition manual, page-by-page and record-by-record capture**, with optional DOI enrichment only after the ACM capture passes integrity checks. The completed diagnostic verification establishes this as a reproducible no-cost systematic-identification workflow: result totals are visible, page ranges are deterministic for the observed configuration, page size is selectable, complete pagination is navigable, stable individual-record URLs are available, and deeper record inspection supplies metadata when the list view is incomplete. Manual capture remains high-burden and more error-prone than native bulk export, so the controls below are mandatory rather than optional. The observed 44-result diagnostic count must never be recorded as a systematic-search result count.

For each later frozen Query ID, the operator will:

1. Record the frozen Query ID, exact ACM interface expression, selected fields, filters, execution date and time, access edition, and the ACM-reported total result count before capturing records.
2. Save the ACM search-result locator and record the active result ordering/sort state, page size, first/last page, and every visited page locator. If ACM does not expose stable page URLs, preserve a permitted raw page/PDF or equivalent interface capture named by Query ID and page number; do not rely on a reconstructed URL.
3. Traverse pages sequentially without changing sorting, filters, or page size. Capture one raw row per displayed ACM result, including the frozen Query ID, execution timestamp, result position or equivalent page/position provenance, raw title, and stable ACM record URL. Capture DOI, ACM identifier, ISBN, authors/editors, publication/venue, publication date, content type, page information, abstract, and other raw bibliographic metadata when available or applicable.
4. Mark duplicate display rows rather than deleting them. Preserve missing DOI, missing author, malformed identifier, and inaccessible-page states explicitly.
5. Reconcile page coverage: expected pages from the reported count and page size, visited pages, rows captured, duplicate display rows, and any interruption or rerun. A rerun receives a new capture timestamp and is compared to the original; it does not overwrite it.
6. Stage the unchanged ACM rows as raw retrieval evidence. Only after that stage passes the checks below may an optional enrichment process run, followed later by deduplication under the protocol.

Minimum raw fields are: `acm_query_id`, `acm_execution_timestamp`, `acm_reported_result_count`, `acm_result_locator`, `acm_sort_state`, `acm_page_size`, `acm_page_number`, `acm_result_position`, `acm_raw_title`, and `acm_record_url`. Optional/applicable fields include `acm_raw_authors_or_editors`, `acm_raw_publication`, `acm_raw_publication_date`, `acm_raw_content_type`, `acm_raw_doi`, `acm_raw_identifier`, `acm_raw_isbn`, `acm_raw_abstract`, and `enrichment_status`. A DOI is not required for raw corpus staging when the stable ACM URL is present. Raw values are never overwritten by normalized or enriched values.

The integrity condition is not merely “rows were copied.” For each later frozen query, execute the exact frozen query, record the Query ID and execution date/time, record the reported ACM total, record the active sort/order state, use one consistent page size, traverse every displayed page, preserve each result position, capture the minimum raw fields, and record missing optional identifiers rather than dropping records. Before deduplication, the number of captured raw ACM results must equal the original ACM-reported result count. Duplicate interpretation is deferred. An interrupted or failed capture remains explicitly marked incomplete and is not presented as complete; if the index may have changed before resumption, preserve the new execution provenance rather than silently continuing the old capture. The following counts remain separate: ACM reported query-result count, raw captured ACM records, normalized/enriched records, duplicate-display count, deduplicated records, screened records, and included studies. An unresolved reconciliation, malformed batch, failed page, or failed enrichment is a blocking exception for that Query ID, not a reason to silently drop a record.

### Secondary metadata boundary

**Crossref** is the preferred enrichment candidate when an ACM DOI is present. Crossref documents a public REST API for DOI/work metadata and DOI content negotiation for one record at a time, including CSL JSON, RIS, and BibTeX: [REST API](https://www.crossref.org/documentation/retrieve-metadata/rest-api/) and [content negotiation](https://www.crossref.org/documentation/retrieve-metadata/content-negotiation/). It can provide title, contributors, venue, dates, container, pages/article number, abstract when deposited, and other deposited metadata, but deposits are incomplete and fields can differ from ACM. A DOI miss or disagreement is recorded as `not enriched`, not repaired by a title search that could discover a replacement record.

**OpenAlex** is a secondary alternative for DOI-linked enrichment. Its work endpoint exposes DOI, title, authors, publication/source information, dates, identifiers, abstract reconstruction where available, and OpenAlex identifiers; the endpoint is documented in the [OpenAlex API reference](https://docs.openalex.org/api-entities/works). It is an index, not ACM, and its coverage, version linking, field transformations, and update timing can differ. It is therefore useful only when the ACM DOI or an independently captured ACM identifier already exists. An ACM record without DOI is not sent to OpenAlex by title as a discovery search; it remains an ACM-only raw record unless a human-approved exact identifier match is documented.

Enrichment must store the service, request timestamp, lookup key, response status, matched identifier, and field-level success/failure. It must never add a record, remove a record, replace ACM provenance, or change the original ACM result count. DOI coverage is unknown until the ACM capture is performed, so no claim of unbiased enrichment coverage is made.

### Premium assessment and limitations

Premium specifically enables the bulk citation/search-result export that Basic Edition lacks. It would materially reduce transcription burden and improve structured metadata capture, but it is not methodologically necessary because the manual workflow and its page/count controls were human-verified. Paid access is therefore **not required by the selected workflow** and must not be assumed. If Premium is later used, preserve the same Query ID, execution timestamp, ACM reported count, export batch boundaries, raw files, and reconciliation controls; Premium does not remove the need to check truncation or batch completeness.

No automation is authorized by this decision. Any future technical automation would require a separate human review of ACM terms, documented access rules, robots/access constraints where relevant, rate limits, incomplete-capture risk, and maintenance burden. It must not circumvent Premium restrictions.

### Operational status

ACM search capability, frozen-query compatibility, deterministic complete-result pagination for the observed diagnostic configuration, stable record locators, article/paper metadata capture, and proceeding metadata capture are human-verified. Basic Edition still has no native bulk citation export; Premium export remains an optional fallback. No paid access is required to proceed. Manual workload and human-error risk remain high relative to native export, but they are controlled by page coverage, count reconciliation, ordering, position, locator, raw-field, interruption, and rerun records rather than treated as an unresolved access blocker.

No frozen ACM query requires revision as a result of this verification. The limitation is operational only. No scraping, crawler, or browser automation is authorized merely to bypass Premium export restrictions.

All searches and records inspected during this verification are **Database-validation diagnostic searches and records**. They are not systematic-search executions, systematic result counts, corpus records, screened records, included studies, evidence, or research findings. No diagnostic record may be promoted silently into the systematic corpus.

## F6B1 And F6B2 Boundary

- **F6B1:** `Requires further calibration`.
- **F6B2:** `Requires further calibration`.

Database access verification does not change either status and no focused calibration was performed. The now-verified database environment removes access as a general obstacle to their later focused calibration, but the conceptual and retrieval calibration remains outstanding and must be performed later under the search design.

## Full-Text Boundary

Systematic identification/search validation is distinct from later full-text retrieval. Paid full-text access is not currently required to proceed with database identification or search validation. Full-text acquisition for studies surviving later screening is a later-stage issue. Legitimate Open Access versions, preprints, author manuscripts, institutional repositories, and other permitted routes may be considered then. Inaccessible full texts must be handled under the screening/full-text protocol. No individual papers were bought or retrieved during this run.

## Boundary Confirmations

- All human searches in this record remain Database-validation diagnostic searches only.
- Diagnostic result counts are not systematic-search result counts.
- Diagnostic exports are verification artifacts and were not incorporated into the systematic corpus.
- No systematic corpus was collected.
- No systematic-query freeze began.
- No screening, evidence extraction, or synthesis occurred.
- No Work Item characteristics or research conclusions were derived.
- F6B1 and F6B2 remain `Requires further calibration`.
- The protocol database set was not changed and no database was silently substituted.

## Privacy Audit

The artifact contains no institution names, institution-specific access domains, proxy URLs, library portal URLs, institutional or personal email addresses, personal account identifiers, authentication tokens, usernames, researcher names, screenshots, local identifying paths, or IP addresses. Access provenance is limited to generic labels such as `Institutional authenticated access`, `Public`, and `Public Basic Edition`.

## Overall Exit Decision

No systematic search was executed, no systematic corpus was collected, no screening or evidence extraction occurred, no synthesis occurred, and no commit was made.

**ACM result-capture workflow resolved; database set ready for systematic execution**
