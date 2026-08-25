# Research Readiness Checkpoint

**Checkpoint date:** 2026-08-25
**Protocol authority:** Research Protocol v1.1  
**Repository state:** `main`, clean worktree at the checkpoint start; no protocol, query, or search-log changes made by this checkpoint.

## Executive Status

The research is in the post-freeze, tiered-retrieval phase. The research questions, provisional Work Item definition, evidence-stream boundaries, frozen query inventory, database-validation records, and Protocol v1.1 execution policy are established. The Scopus Primary retrieval closure gate is met; cross-database calibration remains open.

**Current decision:** Not ready for calibration deduplication, screening, evidence extraction, synthesis, or Work Item-characteristic derivation.

## Completed Milestones

| Area | Status | Evidence |
|---|---|---|
| Method and protocol | Complete | [`protocol.md`](./protocol.md), [`research-plan.md`](../research-plan.md) |
| Research questions and provisional definition | Frozen as provisional | [`research-questions.md`](./research-questions.md), [`protocol.md`](./protocol.md) |
| Query design | Frozen; 28 branches, 22 Primary and 6 Supplementary | [`systematic-queries.md`](./systematic-queries.md), [`systematic-search-design.md`](./systematic-search-design.md) |
| Scopus route | Operational; Primary core retrieval complete | [`database-validation.md`](./database-validation.md), [`systematic-search-log.md`](./systematic-search-log.md) |
| Additional-database feasibility | Evaluated; no additional route currently qualifies for calibration | [`database-validation.md`](./database-validation.md) |
| IEEE F1 historical retrieval | Complete and reconciled as two independent query pieces; Protocol v1 provenance retained | [`systematic-search-log.md`](./systematic-search-log.md), [`manifests/ieee/`](./manifests/ieee/) |
| Practitioner evidence | Nine pilot records captured across Aider, Claude Code, Codex, and Hacker News; no themes derived | [`../practitioner-evidence/methodology.md`](../practitioner-evidence/methodology.md) |
| Authoritative evidence | ISO/IEC/IEEE 29148:2018, SWEBOK V4.0a, and ISO/IEC 25010:2023 inventoried; no empirical conclusions derived | [`authoritative-sources.md`](./authoritative-sources.md), [`theoretical-framework.md`](./theoretical-framework.md) |
| Work-unit comparison | Ten models described without ranking or suitability claims | [`../comparisons/work-unit-models.md`](../comparisons/work-unit-models.md) |
| Review pipeline | Contracts and tooling prepared; synthetic fixtures/tests only | [`systematic-review-pipeline.md`](./systematic-review-pipeline.md), [`tools/`](./tools/), [`tests/`](./tests/) |

## Current Phase And Non-Activities

The active phase is retrieval closure and feasibility resolution. No real academic record has been deduplicated, screened, quality-assessed, extracted, or synthesized. The synthetic pipeline has not processed real records. No candidate Work Item characteristic, hypothesis, stopping rule, or database-contribution conclusion has been derived.

The following remain deliberately unchanged: Protocol v1.1, the frozen queries, the branch inventory, eligibility criteria, contradictory-evidence policy, and historical execution provenance.

## Scopus Primary Closure

Protocol v1.1 requires all 22 Scopus Primary branches before calibration (Protocol v1.1, tiered execution step 1). The search log documents completed Scopus retrievals for all Primary branches, including all four required F7C variants.

`F3C` is Supplementary in the frozen inventory and must not be counted as a missing Primary branch. The completed zero-result branches are retained as completed retrievals where the log provides their zero-result reconciliation; zero is not treated as an execution failure.

**Scopus Primary status: complete, 22 of 22 branches evidenced as completed.** The 25 required active Scopus variants are reconciled, including all four deliberate F7C variants. No overall unique Scopus corpus count is reported because no cross-branch deduplication has occurred.

The older execution-readiness handoff value for F2A is superseded by the later authoritative search-log completion record. The search log records the final reconciled execution state; neither value is treated as a unique corpus count.

## Database Feasibility And Role

| Database | Feasibility status | Eligible for seven-branch calibration now? | Unresolved dependency |
|---|---|---:|---|
| Scopus | Operational systematic-core route | Core source, not an additional calibration gate | Primary core complete; preserve private raw data and public-safe manifests |
| Web of Science Core Collection | Blocked: API Expanded entitlement unavailable; not excluded from future targeted use | No | Authorized qualifying API or another officially documented equivalent route |
| IEEE Xplore | Official route and corrected F1 retrieval demonstrated, but seven-branch feasibility gate is not closed | No | Complete seven-branch feasibility/calibration decision with the required field, identifier, capture, reconciliation, and licensing evidence |
| ACM Digital Library | Conditional targeted/gap-filling source; complete bulk capture not demonstrated | No | Authorized Premium export, official systematic API, or authorized complete reconciled capture |
| ScienceDirect | Unsuitable as current systematic API route | No | Authorized route with aligned field semantics and complete retrieval above the documented result ceiling |
| Springer Nature Link | Unsuitable as current systematic API route | No | Field-equivalent, stable, complete authorized route and separate licensed-data review |

Feasibility validation events are not systematic corpus retrievals and their records are not eligible for deduplication or screening.

## IEEE Decision Paths

### Path A: IEEE qualifies

The qualification decision must be based on the seven frozen calibration branches: `F2A`, `F4B`, `F5A`, `F6A1`, `F6C1`, `F7A`, and `F7D`. The historical IEEE F1 retrieval is reusable only as historical Protocol v1 provenance and does not substitute for those seven branches.

After Scopus Primary closure and a qualifying IEEE decision, the next sequence is:

1. Execute the remaining IEEE calibration branches through the authorized official route.
2. Reconcile reported counts, captured records, pagination, identifiers, field semantics, hashes, and private raw provenance for every branch.
3. Close the eligible Scopus-plus-IEEE calibration retrieval set.
4. Activate normalization, deduplication, and title/abstract calibration screening.
5. Analyze marginal, RQ, contradiction/boundary, coding-agent-specific, and branch-sensitive database coverage.
6. Freeze the stopping and expansion rule.
7. Perform only the conditional expansions justified by that rule.
8. Complete systematic screening after retrieval expansion closes.

### Path B: IEEE does not qualify

The Scopus core is still required to close. Once it is closed, the current protocol does not define an automatic substitute calibration route for a zero-qualified additional database. The next action is therefore a documented methodological decision by the researcher about whether to amend or clarify the prospective calibration procedure. No calibration corpus, final screening, extraction, synthesis, or characteristic derivation should begin until that decision is recorded under the amendment boundary.

## Data, Provenance, Privacy, And Licensing Audit

### Public/private boundary

The intended boundary is technically documented: record-level licensed files belong under ignored `research/raw-local/` paths, while public manifests and provenance-only sidecars remain public. The current public tree and reachable public refs contain no record-level Scopus or IEEE raw files; the Scopus sidecar and manifest inventories are reconciled in [`scopus-public-data-policy.md`](./scopus-public-data-policy.md).

Current `.gitignore` rules protect future local raw files. Public-ref history inspection found no reachable record-level Scopus or IEEE raw paths; this does not make claims about unrelated external clones, caches, or unreachable objects.

### Provenance

Completed retrieval log entries generally record Query ID, branch, database, query version, date, fields, filters, reported count, capture status, reconciliation, raw-artifact location, and manifest reference. Public manifests are the intended provenance-only artifacts. No unique cross-query count has been claimed.

### Secrets and personal information

The search log documents that API keys were not written to raw responses, sidecars, filenames, or logs. No researcher identity, institution, account identifier, proxy, or authentication detail is included in the public research artifacts inspected. This does not remove the need for a final secret scan after the raw-data boundary is repaired.

### Stream separation

Academic retrieval, authoritative sources, practitioner pilots, and descriptive work-unit models remain separate. Practitioner material and standards have not been pooled with scientific evidence or converted into Work Item requirements.

## Blockers And Activation Decision

**Blocking findings:**

1. IEEE is not yet qualified for the seven-branch calibration.
2. If IEEE fails qualification, the current protocol provides no automatic zero-qualified-secondary-database calibration rule.

**Non-blocking maintenance findings:**

- The older F2A readiness-handoff count (`23439`) is superseded by the later authoritative search-log completion record (`23444`); neither value is a unique corpus count.
- A manifest audit must distinguish forbidden record-level object keys from legitimate textual values such as export-format descriptions.

**Activation decision:** Do not activate the real review pipeline. Do not deduplicate, screen, extract, synthesize, or derive characteristics.

## Exact Next Executable Stage

The immediate executable research stage is **IEEE feasibility resolution** for the seven frozen calibration branches. Scopus Primary retrieval closure and the public/private boundary audit are complete. No calibration retrieval set is closed, and no real deduplication, screening, extraction, or synthesis may begin until the IEEE decision and any zero-qualified-secondary-database methodological decision are recorded.

This checkpoint identifies additional blockers before IEEE resolution; it does not claim that IEEE is the only remaining activation dependency.
