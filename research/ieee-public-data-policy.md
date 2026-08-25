# IEEE Public-Data Boundary

## Decision

The IEEE Xplore Citation-and-Abstract exports are record-level content and are
not clearly authorized for public redistribution under the authoritative IEEE
material reviewed for this audit. They are therefore local/private. This
decision changes publication handling only; it does not invalidate the
historical retrieval or change its queries, counts, reconciliation, or
methodological status.

## Authoritative evidence

- [IEEE Xplore API Terms of Use](https://developer.ieee.org/API_Terms_of_Use2)
  grants a limited license for non-commercial educational, research, or
  scientific activity within the licensee's institution; it reserves rights
  not expressly granted, prohibits distribution of Content to third parties,
  prohibits bulk presentation, and prohibits forms harvestable by humans or
  machines. This is direct API-term language and is controlling for API
  Content, not a claim that the web export has identical terms.
- [IEEE Xplore API use cases](https://developer.ieee.org/docs/read/IEEE_Xplore_Metadata_API_Overview)
  identifies metadata indexing and text-and-data-mining use cases, with
  eligibility and subscription conditions. It does not grant a public
  redistribution license.
- [IEEE Xplore API data fields](https://developer.ieee.org/docs/read/Metadata_API_responses)
  identifies titles, authors, author terms, DOI, article numbers,
  publication metadata, and abstracts as returned Content. This establishes
  that these fields are record-level IEEE Content; it does not grant
  redistribution permission.
- [IEEE Xplore Help](https://ieeexplore.ieee.org/Xplorehelp/)
  documents the Xplore help system and export workflow. The available export
  documentation establishes that citation export is a retrieval feature, not
  a public-license grant. Export permission is not treated as redistribution
  permission.

The web Citation-and-Abstract export terms did not provide an identifiable,
express public redistribution grant in the authoritative material located.
Silence and the ability to search, view, export, or access content are not
treated as permission.

## Classification

Under the audit decision standard, the categories are:

| Content category | Classification | Basis |
| --- | --- | --- |
| Bibliographic citation metadata | C — Public redistribution authorization not established | No express public grant located; API terms reserve ungranted rights and restrict third-party distribution of Content. |
| DOI and stable identifiers | C — Public redistribution authorization not established | The API documentation identifies DOI/article number fields, but documentation is not a redistribution license. |
| Author names | C — Public redistribution authorization not established | Identified as returned Content; no public redistribution grant located. |
| Titles | C — Public redistribution authorization not established | Identified as returned Content; no public redistribution grant located. |
| Publication metadata | C — Public redistribution authorization not established | Identified as returned Content; no public redistribution grant located. |
| Author keywords/terms | C — Public redistribution authorization not established | Identified as returned Content; no public redistribution grant located. |
| Abstracts | D — Public redistribution clearly restricted | IEEE API terms expressly restrict third-party distribution and bulk/harvestable presentation of Content; abstracts are explicitly returned Content. |
| Complete Citation-and-Abstract export files | D — Public redistribution clearly restricted | They contain abstracts and bulk record-level Content; the API terms prohibit bulk and third-party distribution where applicable, and no web-export public grant was established. |
| Systematic-search result sets or bulk exports | D — Public redistribution clearly restricted | They are bulk record-level exports; no express public redistribution authorization was located. |

The classifications do not claim that every individual field has identical
copyright status. They state the safe repository boundary supported by the
evidence. A future written IEEE permission or applicable field-specific public
license would require a fresh review.

## Repository boundary

- IEEE raw/export files remain in `research/raw-local/ieee/` and are ignored by
  Git.
- Public manifests contain provenance, filenames, sizes, SHA-256 values,
  counts, reconciliation, export mechanism and format, and page provenance;
  they contain no titles, authors, identifiers, keywords, abstracts, or other
  record-level fields.
- The public search log points to the private/local raw location and manifests.
- The five restricted raw paths were removed from the current public main tree
  and are not reachable from the inspected current public refs. Public
  provenance manifests remain. Raw IEEE content is local/private under the
  ignored `research/raw-local/ieee/` path.
- This public-ref statement does not claim physical destruction from intentional
  local recovery artifacts, stale external clones, hosting caches, backups, or
  unreachable Git objects.

## Completed Public-Ref Remediation

Git evidence for the current public refs establishes that the approved
remediation removed the five restricted raw paths from public reachability. The
purge scope was the five exact paths matching:

`research/raw/systematic-search/S1-F1-IEEE-01-v1.1__run-20260821T134155__page-*.txt`

`research/raw/systematic-search/S1-F1-IEEE-02-v1.1__run-20260821T155348__page-*.txt`

The remediation was limited to those raw paths. Stale clones or intentional
local recovery artifacts remain outside the public-ref claim and must not be
used to infer that every historical Git object or hosting cache was physically
destroyed.
