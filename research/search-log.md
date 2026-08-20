# Search Log

This document is the durable record of pilot searches and, later, systematic searches conducted under [`research/protocol.md`](./protocol.md). Pilot searches validate and refine terminology, query families, database coverage, precision, recall, and feasibility; they do not establish research findings or Work Item characteristics.

Pilot Round 1 was conducted on 2026-08-20 using arXiv search/API endpoints and OpenAlex discovery. No systematic literature review search has begun.

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

## Pilot Round 1

The first round tested only Family 1 and Family 5. Search counts are the counts reported by the source at the time of searching; they are not estimates of the total literature. The inspected samples were limited to relevance and terminology assessment, not final screening.

### P1-F1-01

- **Search ID:** `P1-F1-01`
- **Date:** `2026-08-20`
- **Evidence stream:** Scientific discovery
- **Database / source:** OpenAlex Works API
- **Query:** `("work unit" OR "work item" OR task OR issue OR ticket OR "user story" OR "change request") AND (software OR "software development" OR programming)`
- **Fields searched:** OpenAlex full-text search
- **Filters:** None; `per-page=10`
- **Result count:** `1` reported by OpenAlex
- **Results inspected:** The single returned record and its metadata/abstract
- **Clearly relevant results:** None confidently identified; the result was a 2013 University of Minho master's dissertation about agile and traditional project management, not a focused study of software work units.
- **Clearly irrelevant patterns:** Project-management and organizational-governance material dominated the only full-text match; the combined all-term full-text interpretation was too restrictive to be useful as a discovery query.
- **Terminology discovered:** Agile software development, work-management, task/work management
- **Candidate seed sources:** None
- **Query adjustment:** `original query → OpenAlex full-text interpretation required all terms and returned one off-target dissertation → test the same concept family in arXiv's all-field search and then narrow by software-task phrases → determine whether database syntax, rather than terminology, caused the retrieval failure`
- **Rationale:** The provisional query must be tested before assuming that a low result count indicates good precision.
- **Notes:** OpenAlex API record: [W2126352330](https://openalex.org/W2126352330). The API's `fulltext.search` behavior is not equivalent to a Boolean title/abstract database query, so this result is a syntax/coverage diagnostic only.

### P1-F1-02

- **Search ID:** `P1-F1-02`
- **Date:** `2026-08-20`
- **Evidence stream:** Scientific discovery
- **Database / source:** arXiv API
- **Query:** `(all:"work unit" OR all:"work item" OR all:task OR all:issue OR all:ticket OR all:"user story" OR all:"change request") AND (all:software OR all:"software development" OR all:programming)`
- **Fields searched:** arXiv `all` fields, including indexed title/abstract/text metadata
- **Filters:** None; first 10 sorted by relevance
- **Result count:** `28,976` reported by arXiv
- **Results inspected:** First 10 result records and abstracts
- **Clearly relevant results:** No high-confidence work-unit study in the first ten; the top records included broad software-development collaboration, developer experience, and project/process topics.
- **Clearly irrelevant patterns:** The unquoted terms `task`, `issue`, and `software` produced broad software-engineering and general issue/project results. The search was too noisy for practical first-pass screening.
- **Terminology discovered:** software development workflow, software development tasks, software tasks, issue tracking systems, issue descriptions, task type, task completion performance
- **Candidate seed sources:** The query exposed useful adjacent terminology but no seed was promoted from this sample without a narrower search.
- **Query adjustment:** `original query → 28,976 results and broad task/issue noise → combine precise phrases such as "software task", "software development task", and "issue description" with software/programming → reduce ambiguous single-word terms while retaining issue-based literature`
- **Rationale:** `task` and `issue` are useful vocabulary but cannot stand alone in the initial pilot query.
- **Notes:** arXiv query endpoint: [search URL](https://export.arxiv.org/api/query?search_query=all:%28%22work%20unit%22%20OR%20%22work%20item%22%20OR%20task%20OR%20issue%20OR%20ticket%20OR%20%22user%20story%22%20OR%20%22change%20request%22%29%20AND%20all:%28software%20OR%20%22software%20development%22%20OR%20programming%29&start=0&max_results=10&sortBy=relevance). This is a discovery observation, not an exclusion of the noisy terms from future separate searches.

### P1-F1-03

- **Search ID:** `P1-F1-03`
- **Date:** `2026-08-20`
- **Evidence stream:** Scientific discovery
- **Database / source:** arXiv API
- **Query:** `(all:"software task" OR all:"software development task" OR all:"issue description") AND (all:software OR all:programming)`
- **Fields searched:** arXiv `all` fields
- **Filters:** None; first 10 sorted by relevance
- **Result count:** `200` reported by arXiv
- **Results inspected:** First 10 result records and abstracts; full source-page inspection was deferred for the listed candidates
- **Clearly relevant results:** `Exploring the links between software development task type, team attitudes and task completion performance` (Licorish and MacDonell) studies about 30,000 software development tasks in the IBM Jazz repository; `Descriptions of issues and comments for predicting issue success in software projects` (Ramírez-Mora, Oktaba, and Gómez-Adorno) studies issue descriptions/comments across issue-tracking systems and identifies bugs, improvements, and new features as issue types.
- **Clearly irrelevant patterns:** Some results used software tasks only as a generic setting for LLM evaluation, energy use, or cognitive-load measurement rather than studying how software work units are represented or executed.
- **Terminology discovered:** software development task type, task completion performance, issue-tracking systems, issue descriptions and comments, issue success, bug/improvement/new-feature issues, software development tasks
- **Candidate seed sources:** [Licorish and MacDonell, arXiv:2104.12131](https://arxiv.org/abs/2104.12131), journal reference Information and Software Technology 97 (2018), DOI [10.1016/j.infsof.2017.12.005](https://doi.org/10.1016/j.infsof.2017.12.005), inspected; [Ramírez-Mora, Oktaba, and Gómez-Adorno, arXiv:2006.01358](https://arxiv.org/abs/2006.01358), journal reference Journal of Systems and Software 168 (2020), DOI [10.1016/j.jss.2020.110663](https://doi.org/10.1016/j.jss.2020.110663), inspected.
- **Query adjustment:** No further F1 adjustment in this round.
- **Rationale:** The narrower phrase family produced identifiable software-task and issue-description literature while retaining terminology needed for later comparison.
- **Notes:** The sources were inspected through their arXiv records and abstracts. Their relevance here is as terminology/seed discovery; no Work Item claim was evaluated.

### P1-F5-01

- **Search ID:** `P1-F5-01`
- **Date:** `2026-08-20`
- **Evidence stream:** Coding-agent-specific scientific discovery
- **Database / source:** OpenAlex Works API
- **Query:** `("coding agent*" OR "code agent*" OR "software engineering agent*" OR "autonomous software engineering" OR "AI programming assistant*" OR "agentic software development")`
- **Fields searched:** OpenAlex full-text search
- **Filters:** None; `per-page=10`
- **Result count:** `0` reported by OpenAlex
- **Results inspected:** No records returned
- **Clearly relevant results:** None
- **Clearly irrelevant patterns:** None returned; the zero count is not evidence that the terminology is absent.
- **Terminology discovered:** None from this query
- **Candidate seed sources:** None
- **Query adjustment:** `original query → OpenAlex full-text search returned zero because the combined expression appears to require all terms → test exact phrase searches in arXiv and keep software-engineering-agent and SWE-agent families separate → accommodate database-specific Boolean behavior`
- **Rationale:** The protocol requires database-specific adaptation and warns against interpreting a low result count as high precision.
- **Notes:** This OpenAlex result was a query-behavior diagnostic. It should not be compared directly with arXiv counts.

### P1-F5-02

- **Search ID:** `P1-F5-02`
- **Date:** `2026-08-20`
- **Evidence stream:** Coding-agent-specific scientific discovery
- **Database / source:** arXiv API
- **Query:** `all:"coding agent"`
- **Fields searched:** arXiv `all` fields
- **Filters:** None; first 10 sorted by relevance
- **Result count:** `1,001` reported by arXiv
- **Results inspected:** First 10 result records and abstracts; full arXiv pages inspected for selected records
- **Clearly relevant results:** Coding-agent and software-engineering-agent records appeared near the top, including `Software Delegation Contracts`, `Building an Internal Coding Agent at Zup`, `LoopsBench`, `Failure as a Process`, `Change2Task`, and `SWE-chat`.
- **Clearly irrelevant patterns:** The exact phrase retrieved adjacent compiler, systems, infrastructure, and broad AI-agent work; coding-agent wording is recent and not consistently used as the primary title term.
- **Terminology discovered:** coding agents, AI coding agents, CLI coding agents, coding-agent workloads, coding-agent sessions, software delegation contracts, software engineering tasks, repository-level tasks
- **Candidate seed sources:** [SWE-chat: Coding Agent Interactions From Real Users in the Wild](https://arxiv.org/abs/2604.20779), preprint record inspected; [Change2Task: From Repository Changes to Executable Coding Agent Tasks and Environments](https://arxiv.org/abs/2607.28591), preprint record inspected; [Failure as a Process: An Anatomy of CLI Coding Agent Trajectories](https://arxiv.org/abs/2607.09510), preprint record inspected. Publication status for these records was not independently established in this pilot beyond their arXiv records.
- **Query adjustment:** `all:"coding agent" → 1,001 results with useful recent terminology but adjacent systems/AI noise → test all:"software engineering agent" and all:"SWE-agent" separately → distinguish the broader current label from the established benchmark/system label`
- **Rationale:** The broad phrase is useful for discovery but should not be treated as a complete vocabulary or a homogeneous agent category.
- **Notes:** arXiv query endpoint: [search URL](https://export.arxiv.org/api/query?search_query=all:%22coding%20agent%22&start=0&max_results=10&sortBy=relevance). Records were inspected as metadata and abstracts, not accepted as evidence.

### P1-F5-03

- **Search ID:** `P1-F5-03`
- **Date:** `2026-08-20`
- **Evidence stream:** Coding-agent-specific scientific discovery
- **Database / source:** arXiv API
- **Query:** `all:"software engineering agent"`
- **Fields searched:** arXiv `all` fields
- **Filters:** None; first 10 sorted by relevance
- **Result count:** `100` reported by arXiv
- **Results inspected:** First 10 result records and abstracts; full arXiv page inspected for the SWE-agent seed identified through the related terminology search
- **Clearly relevant results:** `Unified Software Engineering Agent as AI Software Engineer` uses `Unified Software Engineering agent`, `AI Software Engineer`, `USEagent`, `USEbench`, and repository-level software-engineering tasks; `SeaView` explicitly uses `SWE agents` and studies their trajectories; other results use software-engineering agents for context, environment, recovery, and benchmark evaluation.
- **Clearly irrelevant patterns:** The phrase also retrieved embodied-controller and general agent infrastructure papers. The term does not by itself guarantee repository-level coding work.
- **Terminology discovered:** software engineering agents, SWE agents, SWE-agent, Unified Software Engineering agent, AI Software Engineer, repository-level software engineering tasks, agent trajectories, agent-environment interaction
- **Candidate seed sources:** [SWE-agent: Agent-Computer Interfaces Enable Automated Software Engineering](https://arxiv.org/abs/2405.15793), John Yang et al., submitted 2024, arXiv record inspected; the page identifies software-engineering and AI subjects and the SWE-bench evaluation, but this pilot does not independently establish a peer-reviewed venue. [Unified Software Engineering Agent as AI Software Engineer](https://arxiv.org/abs/2506.14683), Leonhard Applis et al., 2025, arXiv record and abstract inspected; the record says it was to appear at ICSE 2026, which should be verified during later screening.
- **Query adjustment:** No further F5 adjustment in this round.
- **Rationale:** This exact phrase materially reduced the arXiv result set and exposed a distinct `SWE agents`/`AI Software Engineer` vocabulary without collapsing it into autocomplete or conversational-assistant terminology.
- **Notes:** The query was used for terminology and seed discovery only. The search result does not establish that these agent labels denote one uniform class.

### P1-F5-04

- **Search ID:** `P1-F5-04`
- **Date:** `2026-08-20`
- **Evidence stream:** Coding-agent-specific scientific discovery
- **Database / source:** arXiv API
- **Query:** `all:"SWE-agent"`
- **Fields searched:** arXiv `all` fields
- **Filters:** None; first 10 sorted by relevance
- **Result count:** `119` reported by arXiv
- **Results inspected:** First 10 result records and abstracts; full arXiv page inspected for `SWE-agent: Agent-Computer Interfaces Enable Automated Software Engineering`
- **Clearly relevant results:** The result set uses `SWE-Agent`, `SWE-agents`, `SWE-bench`, agent frameworks, issue resolution, repository exploration, trajectories, and verification. The inspected SWE-agent paper describes an agent-computer interface for repository navigation, code editing, and test execution, and evaluates it on SWE-bench and HumanEvalFix.
- **Clearly irrelevant patterns:** The named system is also used in papers about training, economic experimentation, self-evolution, evaluation diagnostics, and other agent infrastructure; the label identifies a research lineage, not a single task scope.
- **Terminology discovered:** SWE-agent, SWE-agents, mini-SWE-agent, agent-computer interface (ACI), SWE-bench, issue resolution, repository navigation, trajectories, agent scaffold, tool-mediated trajectory
- **Candidate seed sources:** [SWE-agent: Agent-Computer Interfaces Enable Automated Software Engineering](https://arxiv.org/abs/2405.15793), John Yang, Carlos E. Jimenez, Alexander Wettig, Kilian Lieret, Shunyu Yao, Karthik Narasimhan, and Ofir Press, 2024, arXiv record inspected; [SWE-bench: Can Language Models Resolve Real-World GitHub Issues?](https://arxiv.org/abs/2310.06770), Carlos E. Jimenez, John Yang, Alexander Wettig, Shunyu Yao, Kexin Pei, Ofir Press, and Karthik Narasimhan, 2023 arXiv submission revised 2024, record inspected and identified as ICLR 2024 in the source comments; [Understanding Software Engineering Agents: A Study of Thought-Action-Result Trajectories](https://arxiv.org/abs/2506.18824), Islem Bouzenia and Michael Pradel, 2025, discovered and abstract inspected; the record states acceptance at ASE 2025.
- **Query adjustment:** No further F5 adjustment in this round.
- **Rationale:** `SWE-agent` is a high-yield lineage term for software-engineering-agent research, but its results still require task-scope screening.
- **Notes:** Search endpoint: [arXiv SWE-agent query](https://export.arxiv.org/api/query?search_query=all:%22SWE-agent%22&start=0&max_results=10&sortBy=relevance). The source records contain abstracts and publication-status metadata; no claims were added to the literature files.

## Query Evolution Records

The material changes observed in this round are preserved here in the required form:

- `("work unit" OR "work item" OR task OR issue OR ticket OR "user story" OR "change request") AND (software OR "software development" OR programming) → OpenAlex full-text interpretation returned 1 off-target record → test arXiv all-field search, then phrase-focused search → distinguish database syntax failure from terminology failure and reduce single-word noise`
- `arXiv broad Family 1 query with task/issue/ticket terms → 28,976 results dominated by generic software/project material → ("software task" OR "software development task" OR "issue description") AND (software OR programming) → retain relevant software-task and issue-description vocabulary while making initial screening feasible`
- `("coding agent*" OR "code agent*" OR "software engineering agent*" OR "autonomous software engineering" OR "AI programming assistant*" OR "agentic software development") in OpenAlex full-text search → 0 results under the API's combined-term behavior → exact arXiv phrase searches for "coding agent", "software engineering agent", and "SWE-agent" → preserve separate database-adapted families rather than inferring absence from zero retrieval`
- `all:"coding agent" → 1,001 results with useful recent records and adjacent systems noise → all:"software engineering agent" and all:"SWE-agent" → distinguish broad coding-agent language from SWE-agent/software-engineering-agent research lineage`

No query was removed because it returned contradictory or unexpected material. No query was frozen as a systematic search string.

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
| software development task | software work definition | P1-F1-02, P1-F1-03 | Traditional software engineering | add as synonym | Appeared in titles and abstracts for task-type, completion, and repository studies. |
| software task | software work definition | P1-F1-03 | Traditional software engineering | add as synonym | More precise than unqualified `task`, but still broad across evaluation and developer studies. |
| issue description | issue/work representation | P1-F1-02, P1-F1-03 | Issue-tracking research | add as synonym | Promising phrase for studies of textual work descriptions; retain separate from generic `issue`. |
| issue-tracking system | issue/work representation | P1-F1-03 | Traditional software engineering | retain as contextual term | Identifies the repository/tool context in which issues are studied. |
| task type | software work classification | P1-F1-03 | Traditional software engineering | add as synonym | Used with task completion performance and categories of development work. |
| task completion performance | completion/outcome terminology | P1-F1-03 | Traditional software engineering | add as outcome term | Outcome phrase, not a Work Item characteristic. |
| coding agent | coding-agent vocabulary | P1-F5-02 | Recent coding-agent research | retain and test separately | High-yield broad phrase with adjacent systems and infrastructure noise. |
| AI coding agent | coding-agent vocabulary | P1-F5-02 | Recent coding-agent research | add as synonym | Appeared in recent arXiv records alongside coding-agent workloads and sessions. |
| software engineering agent | coding-agent vocabulary | P1-F5-03 | Recent software-engineering-agent research | add as synonym | More focused than `coding agent` but still includes non-repository and infrastructure settings. |
| SWE agent / SWE-agent | coding-agent vocabulary | P1-F5-03, P1-F5-04 | Benchmarks and agent systems | add as synonym | Established research-lineage term; test hyphenation and plural variants separately. |
| AI Software Engineer | coding-agent vocabulary | P1-F5-03 | Unified agent framing | investigate separately | Appears in a paper describing a unified agent across coding, testing, and patching. |
| agent-computer interface (ACI) | agent execution environment | P1-F5-04 | SWE-agent system paper | add as contextual term | Specific interface terminology associated with repository navigation, editing, and execution. |
| SWE-bench | coding-agent evaluation | P1-F5-04 | GitHub issue resolution benchmark | retain as contextual term | Benchmark name, not a general synonym for coding agents. |
| agent trajectory / tool-mediated trajectory | agent execution trace | P1-F5-03, P1-F5-04 | Agent evaluation and analysis | add as contextual term | Used to describe multi-step agent/environment interaction. |

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
