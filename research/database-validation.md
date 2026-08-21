# Database-Specific Validation

**Validation date:** 2026-08-20
**Phase:** Database-Specific Validation
**Methodological authority:** [`protocol.md`](./protocol.md)
**Pilot calibration authority:** [`search-log.md`](./search-log.md)
**Search specification:** [`systematic-search-design.md`](./systematic-search-design.md)

## Scope and Boundary

This document validates access conditions, official documentation, searchable fields, syntax feasibility, and translation strategy for the six protocol databases. It does not execute the systematic literature search.

The vendor sites were accessed from this environment without institutional credentials, proxy configuration, or database API keys. A database page returning a generic HTTP response was not treated as authenticated database access. Counts, records, abstracts, exports, screening decisions, and evidence extraction were not collected.

### Representative branches

The following small set was used for translation feasibility only:

| Branch | Why selected | Pilot/design basis |
|---|---|---|
| F1 | Traditional software-engineering terminology with multiple synonyms and explicit software qualification. | `P1-F1`, `P2-F1`, `systematic-search-design.md` F1 |
| F5A | Recent coding-agent population terminology with software/repository qualification. | `P1-F5`, `P2-F5`, `systematic-search-design.md` F5A |
| F6A2 | Coding-agent repository retrieval/navigation terminology. | `systematic-search-design.md` F6A2 |
| F6C1 | Coding-agent clarification/elicitation terminology and a multi-block Boolean structure. | `systematic-search-design.md` F6C1 |
| F3C | Calibrated supplementary allocation/interdependence branch. | `P4-F3`, `systematic-search-design.md` F3C |
| F4A | Known-noisy requirements ambiguity/completeness terms where field qualification is important. | `P7-F4A`, `systematic-search-design.md` F4A |

These are retrieval diagnostics. They are not evidence samples and were not selected to support an interpretation of Work Items.

## Access Summary

| Database | Access status | Access mode observed | Authentication/subscription | Advanced search | Export | Metadata/abstracts | Outcome |
|---|---|---|---|---|---|---|---|
| IEEE Xplore | Access unavailable | Official help page loaded only as a shell; database request returned HTTP 418 from this environment. | Not verified. | Not verified. | Not verified. | Not verified. | Requires access resolution. |
| ACM Digital Library | Access unavailable | Official ACM library pages returned HTTP 403; no authenticated search session. | Not verified. | Not verified. | Not verified. | Not verified. | Requires access resolution. |
| Scopus | Subscription/authentication required | Scopus redirected to its product/home surface and was not usable for an authenticated search session. | Required; no institutional session available. | Documented, not live-executed. | Not verified in this session. | Not verified in this session. | Requires access resolution. |
| Web of Science | Subscription/authentication required | Product request redirected to the Clarivate login flow. | Required; no institutional session available. | Not verified live. | Not verified. | Not verified. | Requires access resolution. |
| ScienceDirect | Access unavailable | Product/search requests returned HTTP 403/400; Elsevier support pages were reachable. | Not verified. | Not verified. | Not verified. | Not verified. | Requires access resolution. |
| SpringerLink | Access unavailable | Search URL presented a JavaScript/cookie challenge rather than a usable results interface. | Not verified. | Not verified. | Not verified. | Not verified. | Requires access resolution. |

No database was silently replaced. The status records this run's operational access, not the general availability of the products on the public web.

## Official Documentation Consulted

| Database | Official source | What was verified | What remained unverified |
|---|---|---|---|
| IEEE Xplore | [IEEE Xplore Help: Searching IEEE Xplore](https://ieeexplore.ieee.org/Xplorehelp/searching-ieee-xplore) | Official help endpoint exists and identifies the searching help area. | Page content was rendered as a shell; field codes, operators, export limits, and live interface behavior could not be confirmed. |
| ACM Digital Library | [ACM Digital Library subscriber resources](https://libraries.acm.org/digital-library/acm-digital-library) | Official ACM library destination was identified. | The official page returned 403; advanced-search fields, operators, limits, and export behavior were not confirmed. |
| Scopus | [How can I best use the Advanced search?](https://service.elsevier.com/app/answers/detail/a_id/11365/) | Boolean operators, grouping/precedence, `TITLE`, `ABS`, `TITLE-ABS`, `TITLE-ABS-KEY`, `KEY`, wildcards/proximity guidance, document type, language, and publication-year field codes are documented. | Live interface acceptance, export allowance for this account, and institutional result/export caps were not tested. |
| Web of Science | [Web of Science Help Center](https://webofscience.help.clarivate.com/en-us/Content/search-operators.html) | Official help destination and product login flow were identified. | The requested operator page did not expose article content in this environment; exact field, wildcard, proximity, export, and filter syntax remains unverified. |
| ScienceDirect | [ScienceDirect Support Center](https://service.elsevier.com/app/home/supporthub/sciencedirect/) | Official support center and access/download support areas were reachable. | The product search interface was blocked; exact field syntax, operators, limits, and export behavior remain unverified. |
| SpringerLink | [SpringerLink search surface](https://link.springer.com/search) and [Springer Nature support](https://support.springernature.com/) | Official search domain was identified. | Search was challenge-gated; official field/operator guidance and export limits were not confirmed. |

## Capability Matrix

`Verified` means confirmed from an accessible official source or live interface. `Not verified` is deliberately not a negative capability claim.

| Capability | IEEE | ACM | Scopus | Web of Science | ScienceDirect | SpringerLink |
|---|---|---|---|---|---|---|
| Boolean AND / OR / NOT | Not verified | Not verified | Verified: `AND`, `OR`, `AND NOT` | Not verified | Not verified | Not verified |
| Exact phrases | Not verified | Not verified | Verified/documented; quoted phrase examples | Not verified | Not verified | Not verified |
| Parentheses/grouping | Not verified | Not verified | Verified/documented; grouping and precedence described | Not verified | Not verified | Not verified |
| Wildcards/truncation | Not verified | Not verified | Partly documented; exact wildcard behavior should be checked in the live interface | Not verified | Not verified | Not verified |
| Proximity | Not verified | Not verified | Verified/documented: `W/n` and `PRE/n` | Not verified | Not verified | Not verified |
| Title search | Not verified | Not verified | Verified: `TITLE(...)` | Not verified | Not verified | Not verified |
| Abstract search | Not verified | Not verified | Verified: `ABS(...)` | Not verified | Not verified | Not verified |
| Keyword search | Not verified | Not verified | Verified: `KEY(...)`, `AUTHKEY(...)`, and `INDEXTERMS(...)` | Not verified | Not verified | Not verified |
| Combined title/abstract/keyword | Not verified | Not verified | Verified: `TITLE-ABS-KEY(...)` | Not verified | Not verified | Not verified |
| Publication year filter | Not verified | Not verified | Verified: `PUBYEAR` with `IS`, `BEF`, `AFT`; live filter not tested | Not verified | Not verified | Not verified |
| Document-type filter | Not verified | Not verified | Verified/documented: `DOCTYPE(...)` | Not verified | Not verified | Not verified |
| Language filter | Not verified | Not verified | Verified/documented: `LANGUAGE(...)` | Not verified | Not verified | Not verified |

### Scopus-specific verified syntax

The official Scopus support page documents `TITLE-ABS-KEY(...)` as the combined title, abstract, and keyword field, `TITLE(...)`, `ABS(...)`, and `KEY(...)` as field expressions, Boolean `AND`, `OR`, and `AND NOT`, quoted phrases, `W/n` and `PRE/n` proximity, `PUBYEAR`, `DOCTYPE`, and `LANGUAGE`. It also states that there is no explicit query-length limit, recommends no more than 50 Boolean operators for performance, and documents operator precedence. The systematic branches selected here are below that recommendation, but this is not a decision to freeze them.

For the other databases, the current run established only that a documented or interface-level translation must be rechecked in an authenticated live session. Expected field labels from the design document, such as IEEE metadata fields, Web of Science `TS`, or product-specific advanced-search controls, are not promoted to verified syntax here.

## Database Records

### IEEE Xplore

#### Access

**Access unavailable.** The official database host returned HTTP 418 and did not provide a usable search session. No authentication state or subscription entitlement could be tested. Advanced search, abstracts, bibliographic metadata, exports, and export limits are therefore **not verified**.

#### Official documentation consulted

The official [IEEE Xplore Help searching page](https://ieeexplore.ieee.org/Xplorehelp/searching-ieee-xplore) was consulted. It rendered only a help shell in this environment, so no syntax claim beyond the existence of the official help destination is made.

#### Search interface

Not usable in this session. A live advanced-search form, query parser response, result count, and record sample were not obtained.

#### Supported fields

The design's preferred title, abstract, and author-keyword strategy remains a preparation target, not a validated IEEE syntax result. Title, abstract, keyword, combined metadata, year, and document-type controls require authenticated interface verification.

#### Boolean syntax

Not verified.

#### Phrase syntax

Not verified.

#### Wildcards

Not verified.

#### Proximity operators

Not verified.

#### Filters

Year and document-type filtering are not verified. Language filtering is not verified.

#### Export capabilities

Not verified. No export was attempted.

#### Query-length or interface constraints

Not verified.

#### Representative query translations

The following are interface-level translations preserving the conceptual blocks. They are not executable IEEE strings until the live advanced-search field names and parser are checked.

```text
F1: (software development OR software engineering OR programming)
    AND ("software task" OR "software development task" OR "work unit"
         OR "work item" OR "issue description" OR ticket OR "user story")

F5A: ("coding agent" OR "AI coding agent" OR "agentic coding")
     AND ("software development" OR "software engineering" OR "repository-level task")

F6C1: ("coding agent" OR "software engineering agent" OR "interactive coding agent")
      AND ("clarification-seeking" OR "requirement elicitation" OR "underspecified instructions")
```

The execution strategy should use separate title, abstract, and keyword expressions if the interface exposes them; otherwise, use the documented advanced-search form rather than guessing field syntax. Long branches should be split only after a parser test.

#### Diagnostic behavior

No diagnostic query was submitted. The access response prevented syntax and grouping observation.

#### Known-item behavior if checked

Not verified for F1 seeds, including Licorish and MacDonell and Ramírez-Mora et al. No item was retrieved or inspected.

#### Limitations

Access and live syntax are unresolved. IEEE should not be used for systematic execution from this environment without an authenticated session and a recorded parser test.

#### Execution readiness

**Requires access resolution.** After access, run syntax/grouping diagnostics and one-item DOI/title checks before freezing any IEEE query.

### ACM Digital Library

#### Access

**Access unavailable.** Official ACM Digital Library/library pages returned HTTP 403. No authenticated search session, advanced search, metadata record, abstract, or export was available.

#### Official documentation consulted

The official [ACM Digital Library subscriber-resources page](https://libraries.acm.org/digital-library/acm-digital-library) was attempted. The request was blocked with HTTP 403, so ACM-specific operators and limits remain unverified.

#### Search interface

Not usable in this session. No query parser or result page was available.

#### Supported fields

Title, abstract, author-supplied keyword, and combined metadata searching are design targets only. Their ACM field names and whether advanced search exposes all of them require live verification.

#### Boolean syntax

Not verified.

#### Phrase syntax

Not verified.

#### Wildcards

Not verified.

#### Proximity operators

Not verified.

#### Filters

Year, publication/content type, and language controls are not verified.

#### Export capabilities

Not verified. No export was attempted.

#### Query-length or interface constraints

Not verified.

#### Representative query translations

These preserve the same concepts as the other database adaptations but are not claimed as ACM parser syntax:

```text
F1: ("software development" OR "software engineering" OR programming)
    AND ("software task" OR "software development task" OR "work unit"
         OR "work item" OR "issue description" OR ticket OR "user story")

F6A2: ("coding agent" OR "software engineering agent" OR "SWE agent")
      AND ("repository exploration" OR "structural code retrieval" OR "repository navigation")

F3C [supplementary]: ("software development" OR "crowdsourcing software development")
      AND ("task allocation" OR "work allocation" OR "task interdependence" OR "parallel tasks")
```

Use separate advanced-search fields if offered. Do not assume ACM accepts Scopus field codes or Scopus proximity syntax.

#### Diagnostic behavior

No diagnostic query was submitted because the ACM search surface was inaccessible.

#### Known-item behavior if checked

Not verified for Raharjana et al., Schwedt and Ströder, or the coding-agent seeds. No records were inspected.

#### Limitations

Both access and syntax are unresolved. ACM indexing of arXiv versions must also not be assumed, as noted in the systematic-search design.

#### Execution readiness

**Requires access resolution.** An authenticated session must verify field controls, grouping, phrase behavior, export, and known-item indexing.

### Scopus

#### Access

**Subscription/authentication required.** The public product route was reachable but did not provide an authenticated search session. No institutional entitlement was available in this run. Official syntax documentation was accessible.

#### Official documentation consulted

The official [Scopus Advanced search support page](https://service.elsevier.com/app/answers/detail/a_id/11365/) was accessible. It documents Boolean operators, grouping and precedence, proximity, field codes, year, document type, language, and keyword fields.

#### Search interface

Not executed. The support page confirms the Advanced Search model, but the live form and account-level result/export behavior were not available.

#### Supported fields

Verified from the official support page: `TITLE`, `ABS`, `TITLE-ABS`, `TITLE-ABS-KEY`, `KEY`, `AUTHKEY`, and `INDEXTERMS`. The page also documents `PUBYEAR`, `DOCTYPE`, and `LANGUAGE` filters.

#### Boolean syntax

Verified/documented: `AND`, `OR`, and `AND NOT`. Parentheses are supported and recommended for explicit grouping. The documented precedence is `OR`, proximity, `AND`, then `AND NOT`; explicit parentheses are required for conceptual blocks.

#### Phrase syntax

Quoted phrases are documented by official examples, including `TITLE-ABS-KEY("heart attack")`.

#### Wildcards

The support page refers to wildcard use but exact behavior for every wildcard form was not live-tested. Wildcard-heavy terms must be checked before execution.

#### Proximity operators

Verified/documented: `W/n` and `PRE/n`. Neither is required for the representative translations, so no proximity behavior was tested.

#### Filters

Verified/documented: `PUBYEAR`, `DOCTYPE`, and `LANGUAGE`. No year, language, subject-area, or document-type filter was applied in this validation. The design's broad historical/recent split remains a later execution decision.

#### Export capabilities

Not verified because no authenticated result set was available. Export limits must be checked against the institution/account and recorded before collection.

#### Query-length or interface constraints

The official page states no explicit query-length or Boolean-count limit, while recommending at most 50 Boolean operators for optimal performance. The representative queries are below that recommendation. Account/session constraints remain unverified.

#### Representative query translations

These are the most operationally specific translations in this run because Scopus syntax is documented:

```text
F1:
TITLE-ABS-KEY(("software development" OR "software engineering" OR programming)
  AND ("software task" OR "software development task" OR "work unit" OR "work item"
       OR "issue description" OR ticket OR "user story"))

F5A:
TITLE-ABS-KEY(("coding agent" OR "AI coding agent" OR "agentic coding")
  AND ("software development" OR "software engineering" OR "repository-level task"))

F6A2:
TITLE-ABS-KEY(("coding agent" OR "software engineering agent" OR "SWE agent")
  AND ("repository exploration" OR "structural code retrieval" OR "repository navigation"))

F6C1:
TITLE-ABS-KEY(("coding agent" OR "software engineering agent" OR "interactive coding agent")
  AND ("clarification-seeking" OR "requirement elicitation" OR "underspecified instructions"))

F3C [supplementary]:
TITLE-ABS-KEY(("software development" OR "crowdsourcing software development")
  AND ("task allocation" OR "work allocation" OR "task interdependence" OR "parallel tasks"))

F4A [noisy]:
TITLE-ABS-KEY(("software requirements" OR "requirements engineering")
  AND ("requirements ambiguity" OR "ambiguity detection" OR "requirements completeness"
       OR "requirements coverage" OR "traceability completeness"))
```

Use separate `TITLE(...)` checks for precision-sensitive terms and exact known-item title checks. Do not add filters or split queries until the access session confirms result counts and export behavior.

#### Diagnostic behavior

No diagnostic query was submitted. Official syntax was validated from documentation only; no result count or record sample exists.

#### Known-item behavior if checked

Not verified. The F1, F5A, F6A2, and F6C1 pilot seeds were not queried in Scopus.

#### Limitations

Institutional access, live parser behavior, result counts, abstracts, metadata completeness, and export limits remain unresolved. The documented 50-Boolean recommendation is operational guidance, not an export or corpus limit.

#### Execution readiness

**Requires access resolution.** Syntax preparation is feasible, but systematic-query preparation cannot be frozen until an authenticated session confirms the live interface and exports.

### Web of Science

#### Access

**Subscription/authentication required.** The product route redirected to the official Clarivate login flow. No institutional Web of Science session was available.

#### Official documentation consulted

The official [Web of Science search-operators help URL](https://webofscience.help.clarivate.com/en-us/Content/search-operators.html) and [Web of Science Help Center](https://webofscience.help.clarivate.com/en-us/Content/wos-core-collection/wos-core-collection.htm) were consulted. The help route exposed the official help shell rather than the requested article content in this environment. Therefore, no exact Web of Science operator or field capability is marked verified here.

#### Search interface

Not usable without authentication. The login redirect is an access diagnostic, not a search execution.

#### Supported fields

The systematic design's `TS` Topic and `TI` title strategy remains provisional. Whether Topic includes the expected title, abstract, author-keyword, and Keywords Plus behavior must be checked in the authenticated interface and edition/index used.

#### Boolean syntax

Not verified from accessible official content or live parser.

#### Phrase syntax

Not verified.

#### Wildcards

Not verified.

#### Proximity operators

Not verified.

#### Filters

Database edition/indexes, year, document type, and language controls were not available for verification.

#### Export capabilities

Not verified. Institutional export quotas and batch limits must be checked in the authenticated account.

#### Query-length or interface constraints

Not verified.

#### Representative query translations

The following use the design's provisional Topic/title field labels only as translation notation. They are not frozen WoS query strings:

```text
F1:
TS=(("software development" OR "software engineering" OR programming)
    AND ("software task" OR "software development task" OR "work unit"
         OR "work item" OR "issue description" OR ticket OR "user story"))

F5A:
TS=(("coding agent" OR "AI coding agent" OR "agentic coding")
    AND ("software development" OR "software engineering" OR "repository-level task"))

F6C1:
TS=(("coding agent" OR "software engineering agent" OR "interactive coding agent")
    AND ("clarification-seeking" OR "requirement elicitation" OR "underspecified instructions"))
```

If `TS` is confirmed, use title-only `TI` sensitivity variants for F5A/F6A2 lineage terms and F4A noisy phrases. Do not transfer Scopus wildcards or proximity operators into WoS without a parser test.

#### Diagnostic behavior

No diagnostic query was submitted. The login redirect prevented parser and grouping tests.

#### Known-item behavior if checked

Not verified for the F1, F5A, F6A2, or F6C1 seeds.

#### Limitations

Authentication, subscription edition/index, syntax, field semantics, and exports are unresolved. Web of Science is not executable for this project from the current session.

#### Execution readiness

**Requires access resolution.** After access, verify Topic composition, exact phrases, wildcards/proximity, filters, and export batches.

### ScienceDirect

#### Access

**Access unavailable.** ScienceDirect search/product requests returned HTTP 403/400 from this environment. Elsevier's support center was reachable, but no product result page or authenticated session was obtained.

#### Official documentation consulted

The official [ScienceDirect Support Center](https://service.elsevier.com/app/home/supporthub/sciencedirect/) was consulted, including its access and download support categories. The official search surface was also attempted but did not return a usable interface. Exact ScienceDirect query syntax is therefore not verified.

#### Search interface

Not usable in this session. No advanced-search form, field selector, result count, or record sample was available.

#### Supported fields

Title, abstract, and keywords are the planned fields from the systematic design, but their live controls and parser syntax are not verified.

#### Boolean syntax

Not verified.

#### Phrase syntax

Not verified.

#### Wildcards

Not verified.

#### Proximity operators

Not verified.

#### Filters

Year, article/content type, journal/conference context, and language filters are not verified.

#### Export capabilities

Not verified. No result export or full-text download was attempted.

#### Query-length or interface constraints

Not verified.

#### Representative query translations

These are field-selector plans, not ScienceDirect syntax:

```text
F1: Title/Abstract/Keywords:
    ("software development" OR "software engineering" OR programming)
    AND ("software task" OR "software development task" OR "work unit"
         OR "work item" OR "issue description" OR ticket OR "user story")

F6A2: Title/Abstract/Keywords:
    ("coding agent" OR "software engineering agent" OR "SWE agent")
    AND ("repository exploration" OR "structural code retrieval" OR "repository navigation")

F4A: Title/Abstract/Keywords:
    ("software requirements" OR "requirements engineering")
    AND ("requirements ambiguity" OR "ambiguity detection" OR "requirements completeness"
         OR "requirements coverage" OR "traceability completeness")
```

If the interface cannot express a combined field, run separate title, abstract, and keyword variants and preserve their provenance. No unrestricted full-text default is authorized by the design.

#### Diagnostic behavior

No diagnostic query was submitted. Access errors prevented syntax and Boolean-grouping observation.

#### Known-item behavior if checked

Not verified for Forward and Lethbridge, Briand, Krishna et al., or any selected coding-agent seed.

#### Limitations

Access, advanced field controls, parser syntax, result metadata, article-type filters, and export limits remain unresolved. ScienceDirect must not be treated as validated because the Elsevier support center itself was reachable.

#### Execution readiness

**Requires access resolution.** The preferred strategy is a title/abstract/keyword interface search, with separate smaller variants if the live form imposes limits.

### SpringerLink

#### Access

**Access unavailable.** The official SpringerLink search URL returned a JavaScript/cookie challenge. No search form, result count, metadata record, abstract, or export was obtained.

#### Official documentation consulted

The official [SpringerLink search surface](https://link.springer.com/search) and [Springer Nature support home](https://support.springernature.com/) were consulted. The search surface was challenge-gated and the support route did not expose a usable database-search guide in this environment. Exact SpringerLink syntax is not verified.

#### Search interface

Not usable in this session.

#### Supported fields

Title, abstract, and keyword fields are design targets only. Content type and year controls require live verification.

#### Boolean syntax

Not verified.

#### Phrase syntax

Not verified.

#### Wildcards

Not verified.

#### Proximity operators

Not verified.

#### Filters

Content type, year, journal/book chapter/conference proceedings, language, and version status are not verified.

#### Export capabilities

Not verified. No export was attempted.

#### Query-length or interface constraints

Not verified.

#### Representative query translations

These preserve the conceptual blocks while avoiding an unverified Springer-specific parser:

```text
F1: ("software development" OR "software engineering" OR programming)
    AND ("software task" OR "software development task" OR "work unit"
         OR "work item" OR "issue description" OR ticket OR "user story")

F5A: ("coding agent" OR "AI coding agent" OR "agentic coding")
     AND ("software development" OR "software engineering" OR "repository-level task")

F3C [supplementary]: ("software development" OR "crowdsourcing software development")
     AND ("task allocation" OR "work allocation" OR "task interdependence" OR "parallel tasks")
```

Use the live advanced-search field selectors if available. Split by field or by conceptual synonym group only if the interface requires it; retain the same branch and query-version provenance.

#### Diagnostic behavior

No diagnostic query was submitted. The JavaScript/cookie challenge prevented query execution.

#### Known-item behavior if checked

Not verified for Wong and Lau, Lucassen et al., or any coding-agent seed.

#### Limitations

Access, syntax, field semantics, version coverage, content-type filters, and export limits remain unresolved. SpringerLink coverage of preprints or accepted manuscripts must not be assumed.

#### Execution readiness

**Requires access resolution.** A live session must verify whether the search supports the intended fields and whether smaller field-specific queries are required.

## Diagnostic Query Policy and Attempts

### Queries executed

**None.** No database returned a usable authenticated search interface, so no diagnostic query was submitted and no result count or record sample was inspected. Consequently, no systematic-search ID (`S1-*`) was created and no source-registry entry was made.

### Bounded diagnostic attempts

The following IDs identify planned access/syntax attempts, not executed searches. They are included to make the boundary auditable.

| Validation ID | Database | Conceptual branch | Exact intended diagnostic query | Purpose | Fields/filters | Result count | Results inspected | Known item | Limitation |
|---|---|---|---|---|---|---|---:|---|---|
| DBV-IEEE-01 | IEEE Xplore | F5A | `("coding agent" OR "AI coding agent") AND ("software engineering" OR "repository-level task")` | Test Boolean grouping and phrase handling. | Default metadata fields; no filters. | Not displayed; not submitted. | 0 | Not verified | HTTP 418/help shell. |
| DBV-ACM-01 | ACM Digital Library | F1 | `("software task" OR "software development task") AND ("software engineering" OR programming)` | Test mature terminology and software qualification. | Intended title/abstract/keyword fields; no filters. | Not displayed; not submitted. | 0 | Not verified | HTTP 403. |
| DBV-SCOPUS-01 | Scopus | F6A2 | `TITLE-ABS-KEY(("coding agent" OR "software engineering agent") AND ("repository exploration" OR "repository navigation"))` | Test documented field nesting and grouped AND/OR. | `TITLE-ABS-KEY`; no filters. | Not displayed; not submitted. | 0 | Not verified | No authenticated session. |
| DBV-WOS-01 | Web of Science | F6C1 | `TS=(("coding agent" OR "software engineering agent") AND ("clarification-seeking" OR "requirement elicitation"))` | Test Topic grouping and phrase behavior. | Intended `TS`; no filters. | Not displayed; not submitted. | 0 | Not verified | Login redirect. |
| DBV-SD-01 | ScienceDirect | F4A | `("software requirements" OR "requirements engineering") AND ("requirements ambiguity" OR "requirements completeness")` | Test field restriction against known noisy terminology. | Intended title/abstract/keywords; no filters. | Not displayed; not submitted. | 0 | Not verified | HTTP 403/400. |
| DBV-SPRINGER-01 | SpringerLink | F3C | `("software development" OR "crowdsourcing software development") AND ("task allocation" OR "task interdependence")` | Test supplementary branch grouping and phrase handling. | Intended title/abstract/keyword fields; no filters. | Not displayed; not submitted. | 0 | Not verified | JavaScript/cookie challenge. |

The attempts did not retrieve literature and must not be interpreted as zero-result searches.

## Known-Item Checks

No known-item query was executed. All statuses below are `Not verified`, not `Missed` or `Not indexed`.

| Representative branch | IEEE | ACM | Scopus | WoS | ScienceDirect | SpringerLink |
|---|---|---|---|---|---|---|
| F1: Licorish and MacDonell; Ramírez-Mora et al. | Not verified | Not verified | Not verified | Not verified | Not verified | Not verified |
| F5A: SWE-chat; Change2Task; AIDev | Not verified | Not verified | Not verified | Not verified | Not verified | Not verified |
| F6A2: OwlPath; SWE-Replay; SWE-agent | Not verified | Not verified | Not verified | Not verified | Not verified | Not verified |
| F6C1: Ask or Assume?; ClarEval; Dialogue SWE-Bench | Not verified | Not verified | Not verified | Not verified | Not verified | Not verified |
| F3C: Khanfor; Stol and Fitzgerald; Saremi and Yang | Not verified | Not verified | Not verified | Not verified | Not verified | Not verified |
| F4A: Bano; Rempel and Mader | Not verified | Not verified | Not verified | Not verified | Not verified | Not verified |

Because no item was queried, there is no miss to investigate and no query was altered to force retrieval.

## Adaptation Strategy and Equivalence

The common conceptual intent is a title/abstract/keyword or topic search with explicit Boolean blocks, followed by title-only sensitivity checks for noisy or exact-lineage terms. The literal translations differ as follows:

| Database | Adaptation strategy | Translation status |
|---|---|---|
| IEEE Xplore | Separate title, abstract, and author-keyword expressions if exposed; otherwise use the advanced-search field selectors. Split long synonym blocks only after parser testing. | Limited support; live syntax not verified. |
| ACM Digital Library | Prefer separate title/abstract/author-keyword fields when exposed. Do not transfer Scopus field codes. | Limited support; live syntax not verified. |
| Scopus | One `TITLE-ABS-KEY(...)` expression for ordinary branches; `TITLE(...)` sensitivity variants; split only for live-interface performance or export constraints. | Adapted translation; syntax documented, access unresolved. |
| Web of Science | One `TS(...)` Topic expression if confirmed; `TI(...)` sensitivity variants. Do not assume Topic is unrestricted full text. | Limited support; `TS`/`TI` still require live confirmation. |
| ScienceDirect | Use advanced title/abstract/keyword selectors; use separate smaller field queries if no combined field is available. | Limited support; live syntax not verified. |
| SpringerLink | Use available title/abstract/keyword selectors; use multiple smaller queries if interface length or parser behavior requires it. | Limited support; live syntax not verified. |

No database was shown to require a conceptual change. However, five databases cannot currently support a claim of executable literal translation, and Scopus cannot yet support account-level export readiness. Database-specific syntax corrections must be logged as query-version events before systematic execution.

### Search-equivalence matrix

| Conceptual branch | IEEE | ACM | Scopus | WoS | ScienceDirect | SpringerLink |
|---|---|---|---|---|---|---|
| F1 traditional software work units | Limited support | Limited support | Adapted translation | Limited support | Limited support | Limited support |
| F5A coding-agent population | Limited support | Limited support | Adapted translation | Limited support | Limited support | Limited support |
| F6A2 repository retrieval/navigation | Limited support | Limited support | Adapted translation | Limited support | Limited support | Limited support |
| F6C1 clarification-seeking | Limited support | Limited support | Adapted translation | Limited support | Limited support | Limited support |
| F3C supplementary allocation/interdependence | Limited support | Limited support | Adapted translation | Limited support | Limited support | Limited support |
| F4A noisy requirements ambiguity/completeness | Limited support | Limited support | Adapted translation | Limited support | Limited support | Limited support |

`Adapted translation` means that official syntax is documented sufficiently to write a candidate database expression. It does not mean access, results, known-item retrieval, or export has been validated. `Limited support` means the conceptual translation is prepared but the database's literal syntax and fields remain unverified.

## F6B1 and F6B2 Decision Boundary

Database validation did not change the methodological status of either branch:

- **F6B1: Requires further calibration.** No database diagnostic was executed, so this run provides no new retrieval-method evidence about distinguishing planning from generic project planning or decomposition.
- **F6B2: Requires further calibration.** No database diagnostic was executed, so this run provides no new retrieval-method evidence about distinguishing agent-side functional decomposition/delegation from human/project decomposition.

There is no observed database-specific noise or retrieval-method issue because no result sample was available. A focused pre-execution calibration step remains necessary after access is resolved, especially for terminology instability and the planning/decomposition boundary. This does not reopen the completed Pilot phase and does not promote either branch to Primary.

## Inconsistencies and Open Method Issues

No inconsistency was discovered in the conceptual branch inventory or in the stated F6B1/F6B2 statuses. One operational gap remains visible and is consistent with the design's own unresolved-issues section: the design names expected field strategies for several products but intentionally leaves exact live syntax, access, and export limits as `TBD`. This validation confirms that those items remain unresolved; it does not justify editing the design document.

The following items require resolution before query freeze:

- institutional authentication or an approved access route for all six protocol databases;
- live parser tests for Boolean grouping, phrase handling, wildcards, proximity, field composition, and filters;
- database edition/index and coverage recording for Web of Science;
- account-specific export limits and metadata/abstract availability;
- known-item checks using publication/version-aware identifiers;
- focused calibration for F6B1 and F6B2;
- explicit split and rerun logging if any interface cannot accept a representative branch as one query.

No database substitution is proposed. Possible alternatives, if access remains unavailable, require a later human methodological decision and protocol evolution.

## Validation Outcome Per Database

| Database | Outcome | Reason |
|---|---|---|
| IEEE Xplore | Requires access resolution | No usable database session; syntax, fields, exports, and known items unverified. |
| ACM Digital Library | Requires access resolution | Official pages and product access blocked; operational capabilities unverified. |
| Scopus | Requires access resolution | Official syntax is documented, but authenticated search, metadata, known items, and exports are unavailable. |
| Web of Science | Requires access resolution | Official product redirects to login; live fields, syntax, edition, and exports unverified. |
| ScienceDirect | Requires access resolution | Product search blocked; support content does not establish live query capabilities. |
| SpringerLink | Requires access resolution | Search challenge prevents field, syntax, result, and export validation. |

## Validation Boundary Confirmations

- No systematic search corpus was collected.
- No complete result set for any systematic branch was retrieved or exported.
- No source registry was populated.
- No screening or evidence extraction occurred.
- No included/excluded status was assigned.
- No evidence synthesis or Work Item characteristic was derived.
- Diagnostic attempts were not counted as zero-result literature searches.
- No systematic query was frozen or executed.

## Overall Exit Decision

**Database-specific validation complete with access contingencies requiring resolution**
