# Scopus Public-Data Boundary

## Policy

Scopus raw database content is licensed research data and is local/private. It
must not be added to this public repository. This applies to Scopus Search API
responses, Scopus Web exports, abstracts, author or affiliation metadata, and
other record-level Scopus content.

Public Git may contain frozen queries, protocol and methodological decisions,
execution provenance, database-reported counts, run identifiers, pagination or
partition information, reconciliation results, raw artifact filenames, and
cryptographic checksums. Public manifests must not contain record-level
Scopus metadata.

This policy changes publication handling, not the frozen search strategy,
retrieval policy, screening boundary, or no-deduplication rule.

## Current Inventory

The current `main` tree contains the following tracked Scopus artifacts:

| Category | Files | Git/LFS | Record-level content | Current public exposure |
| --- | ---: | --- | --- | --- |
| Scopus API response JSON | 164 | Git blobs | Yes | Public in current tree |
| Scopus API metadata sidecars | 164 | Git blobs | No, provenance only | Public in current tree |
| Scopus Web CSV exports | 2 | Git LFS | Yes | Public in current tree through LFS pointers and objects |

The tracked API responses cover F1, F2B, F2C, F3A, and F3B. The two tracked
CSV files are the F2A Scopus Web partitions. No other database policy is
changed by this document.

Ten reachable historical commits contain Scopus raw paths. Deleting a raw
file in a new commit would remove it from the tip tree only; the content would
remain recoverable from earlier commits, Git objects, hosting caches, clones,
or LFS storage.

## F3C Local Provenance

The uncommitted F3C artifacts remain local and are not deleted or moved by
this change. They comprise two complete runs and two bounded probes:

- `20260822T234914Z`: 8 response JSON files and 8 sidecars; complete 180-record run.
- `20260822T235149Z`: 8 response JSON files and 8 sidecars; repeat complete 180-record run recorded latest in the search log.
- `bounded-20260822T234902Z`: 1 response JSON file and 1 sidecar; bounded probe.
- `bounded-20260822T235137Z`: 1 response JSON file and 1 sidecar; repeat bounded probe.

The 18 F3C response JSON files are local/private. The 18 sidecars contain
provenance fields only and contain no record-level Scopus metadata. The legacy
`research/raw/systematic-search/*SCOPUS*` pattern is now ignored for future
untracked local files; already tracked files remain tracked and untouched.

## Public Manifest Contract

The Scopus utility writes one JSON manifest after a successful complete
retrieval. The public manifest contains:

- `manifest_version`, `query_id`, `branch`, and `query_version`;
- database, retrieval mechanism, run identifier, and status;
- database-reported `totalResults` and `raw_captured_records`;
- API call count and reconciliation status;
- page number, offset, returned count, and inclusive range for each page;
- each local response and sidecar filename, byte size, and SHA-256 checksum;
- `raw_storage: local-private`.

The manifest contains no query text, abstracts, titles, authors,
affiliations, identifiers, or other record-level fields. Frozen query text
remains in the existing systematic query artifact.

Default public manifest location: `research/manifests/scopus/`.

Default local/private raw location: `research/raw-local/scopus/`.

## Remediation Plan

This plan is prepared but not executed.

1. Freeze and review the current-tree inventory and the manifest/checksum
   records before any history operation.
2. Remove tracked Scopus response JSON and Scopus Web CSV files from the
   current tree in a dedicated change, while retaining methodological logs,
   provenance-only sidecars where permitted, and public manifests.
3. For LFS CSVs, remove the tracked pointers from the tree and separately
   identify the corresponding LFS object IDs and hosting retention state.
4. Use a history-rewrite tool with an explicit path list to remove raw Scopus
   content from every affected historical commit, including API JSON and Web
   CSV paths. A new deletion commit is insufficient.
5. Coordinate the rewrite with all collaborators and the hosting service.
   Rewriting shared history requires a force update; use `--force-with-lease`
   only after the expected remote state has been verified. This task does not
   perform that update.
6. Apply any hosting-specific LFS object purge or repository garbage
   collection request after the rewritten references are published. Removing
   pointers alone does not guarantee removal of retained LFS objects.
7. Verify the rewritten repository with path inventories, `git rev-list
   --objects --all`, LFS object inventory, secret scanning, public-artifact
   content scanning, manifest checksum checks, tests, and a fresh clone.
8. Confirm that no raw Scopus JSON, CSV, abstract, author, affiliation, or
   other record-level content remains reachable from the public refs or LFS
   storage before treating remediation as complete.

No history rewrite, force-push, current-tree raw deletion, or LFS purge is
authorized by this preparation change.
