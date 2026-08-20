# Search Log

This document is the durable record of pilot searches and, later, systematic searches conducted under [`research/protocol.md`](./protocol.md). Pilot searches validate and refine terminology, query families, database coverage, precision, recall, and feasibility; they do not establish research findings or Work Item characteristics.

No searches have been conducted in this repository yet.

## Purpose

Use this log to preserve the search strategy, observations, failed attempts, terminology changes, and decisions needed to reproduce the pilot-search phase and later systematic searching.

## Pilot Objectives

Pilot searches should assess whether they:

- Retrieve clearly relevant literature.
- Produce excessive irrelevant results or recognizable noise patterns.
- Reveal missing terminology, synonyms, aliases, or older terms.
- Expose differences between traditional software-engineering and coding-agent terminology.
- Require database-specific query adaptations.
- Identify useful seed sources for backward and forward snowballing.

Searches must not be optimized to support the Work Item idea. Relevant contradictory literature is equally valuable. A query is not successful merely because it returns many results; retrieval quality, coverage, and feasibility matter more than raw result count.

## Search Families

These are provisional discovery families derived from the concept groups in [`research/protocol.md`](./protocol.md). They are intentionally separate rather than one giant query. The query templates are starting points for pilot searches, not frozen systematic search strings.

### Family 1: Software Work Units And Work Definition

Concepts: software work units, work unit, task, work item, issue, ticket, user story, change request, job to be done, work definition.

Provisional template:

`("work unit" OR "work item" OR task OR issue OR ticket OR "user story" OR "change request") AND (software OR software development OR programming)`

### Family 2: Requirements, Specifications, User Stories, And Acceptance Criteria

Concepts: requirements engineering, requirements, specifications, user stories, acceptance criteria, task descriptions, documentation.

Provisional template:

`(requirements OR "requirements engineering" OR specification* OR "user stor*" OR "acceptance criteria" OR "task description*") AND (software OR software development)`

### Family 3: Task Decomposition And Task Descriptions

Concepts: task decomposition, work decomposition, task breakdown, planning, task description, software development task, execution.

Provisional template:

`("task decomposition" OR "work decomposition" OR "task breakdown" OR planning OR "task description*") AND (software OR programming OR "software development")`

### Family 4: Information Sufficiency, Ambiguity, Cognitive Load, And Documentation Overhead

Concepts: ambiguity, clarity, completeness, information sufficiency, missing context, information overload, cognitive load, documentation overhead.

Provisional template:

`(ambiguity OR clarity OR completeness OR "information sufficiency" OR "missing context" OR "information overload" OR "cognitive load" OR "documentation overhead") AND (software OR programming OR "software development")`

### Family 5: Coding Agents And Software-Engineering Agents

Concepts: coding agents, code agents, software-engineering agents, autonomous software engineering, AI programming assistants, agentic software development.

Provisional template:

`("coding agent*" OR "code agent*" OR "software engineering agent*" OR "autonomous software engineering" OR "AI programming assistant*" OR "agentic software development")`

Keep this family separate from traditional software-engineering families when combining them would hide terminology or reduce useful coverage.

### Family 6: Coding-Agent Context, Planning, Clarification, And Autonomy

Concepts: context management, repository understanding, long context, agent planning, clarification seeking, autonomy, context pollution.

Provisional template:

`("coding agent*" OR "software engineering agent*" OR "code agent*") AND ("context management" OR "repository understanding" OR "long context" OR planning OR clarification OR autonomy OR "context pollution")`

### Family 7: Verification, Completion, Rework, And Task Success

Concepts: software verification, validation, completion, acceptance, rework, review findings, task success.

Provisional template:

`("software verification" OR validation OR completion OR acceptance OR rework OR "review finding*" OR "task success") AND (software OR programming OR "coding agent*" OR "software engineering agent*")`

## Search Log Template

Copy this template for each pilot or systematic search. Use a stable Search ID and record unsuccessful, noisy, and abandoned searches as well as useful searches.

### Search Entry

- **Search ID:** `TBD`
- **Date:** `TBD`
- **Evidence stream:** `TBD`
- **Database / source:** `TBD`
- **Query:** `TBD`
- **Fields searched:** `TBD`
- **Filters:** `TBD`
- **Result count:** `TBD`
- **Results inspected:** `TBD`
- **Clearly relevant results:** `TBD`
- **Clearly irrelevant patterns:** `TBD`
- **Terminology discovered:** `TBD`
- **Candidate seed sources:** `TBD`
- **Query adjustment:** `TBD`
- **Rationale:** `TBD`
- **Notes:** `TBD`

Record database-specific syntax, access limitations, publication-status observations, and whether a result was inspected by a human, a coding agent, or both in `Notes` or the relevant fields. Any coding-agent assistance must preserve the evidence used for its recommendation and receive human resolution when the decision is ambiguous or consequential.

## Terminology Registry

Record terminology discovered during pilot searches. Do not treat a term as a Work Item characteristic merely because it appears frequently in search results.

| Term | Related concept | Source / Search ID | Context | Action | Notes |
|---|---|---|---|---|---|

## Query Evolution

Record every material query change, including changes that reduce retrieval quality or are abandoned. Use this format:

`original query → observation → revised query → rationale`

### Query Change Record

- **Date:** `TBD`
- **Search family:** `TBD`
- **Original query:** `TBD`
- **Observation:** `TBD`
- **Revised query:** `TBD`
- **Rationale:** `TBD`
- **Affected database(s):** `TBD`
- **Search IDs:** `TBD`

Do not silently replace an earlier query. Preserve the original query, its result count, and the reason for revision so unsuccessful and noisy approaches remain traceable.

## Pilot Exit Criteria

Pilot searching may end when all of the following are documented:

- Major concept families have been tested.
- Terminology is sufficiently stable for systematic searching, including relevant differences between traditional software engineering and coding-agent terminology.
- Obvious high-value literature can be retrieved through the tested families.
- Irrelevant-result patterns are understood well enough to document likely noise.
- Database-specific query adaptations are documented.
- Approximate query breadth is manageable for the planned screening process.
- Further pilot iterations produce little meaningful terminology change.

Pilot exit does not mean that the literature review is complete, that the final search strings are permanently fixed, or that any Work Item characteristic has been supported. The systematic search protocol and any later changes remain subject to the traceability and evolution rules in [`research/protocol.md`](./protocol.md).
