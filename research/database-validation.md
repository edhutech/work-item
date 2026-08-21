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

## ACM Unresolved Operations

ACM advanced systematic searching is viable, and field-specific searching is viable. Bulk result export is not available in Basic Edition. Before executing ACM systematic branches, a reproducible metadata-capture method must be chosen. This is a later operational or methodological decision. No workaround is authorized or selected in this run. Scraping is not proposed, and Premium access is not assumed.

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

**Access contingencies resolved except ACM bulk-export workflow; resolve before systematic execution**

No systematic search was executed, no systematic corpus was collected, no screening or evidence extraction occurred, no synthesis occurred, and no commit was made.
