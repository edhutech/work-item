# Search Log

This document is the durable record of pilot searches and, later, systematic searches conducted under [`research/protocol.md`](./protocol.md). Pilot searches validate and refine terminology, query families, database coverage, precision, recall, and feasibility; they do not establish research findings or Work Item characteristics.

Pilot Round 1 was conducted on 2026-08-20 using arXiv search/API endpoints and OpenAlex discovery. Pilot Round 2 calibration was conducted on 2026-08-20 using arXiv, OpenAlex, and Crossref APIs. Pilot Round 3 database-field calibration was conducted on 2026-08-20 using arXiv, OpenAlex, and Crossref APIs. No systematic literature review search has begun.

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
- `P2 F1 phrase family → arXiv retrieval confirmed 272 results across the four provisional terms, with mixed task, issue, and evaluation contexts → retain phrase-level tests and compare database behavior → test consistency without freezing a combined systematic query`
- `P2 F1 phrase family → Crossref bibliographic count returned 1,692,352 records with no sample inspection → use fielded or separate Crossref phrase queries later → treat the count as an API-noise diagnostic only`
- `P2 F5 phrase family → arXiv combined provisional terms returned 1,154 records and exposed agentic aliases → retain separate exact terms plus a combined discovery query → preserve distinctions between coding agents, SWE agents, and adjacent systems`
- `P2 F5 phrase family → Crossref bibliographic count returned 627,049 records and sample retrieval received HTTP 429 → defer broad Crossref sampling and use DOI lookups/fielded queries → do not interpret the rate limit or count as evidence about terminology coverage`
- `P2 F5 phrase family → OpenAlex full-text query returned 561 records including published and preprint candidates but cross-family noise → test title/abstract field behavior in a later iteration → keep OpenAlex discovery separate from systematic precision estimates`
- `P2 F1 provisional vocabulary → arXiv all-field phrase query returned 272 records and known F1 seeds → retain phrase-level coverage without freezing the combined query`
- `P2 F1 provisional vocabulary → Crossref unfielded bibliographic query returned 1,692,352 records with no sample → use fielded or separate phrase requests → treat Crossref as DOI discovery until field behavior is validated`
- `P2 F5 provisional vocabulary → arXiv OR query returned 1,154 records and retrieved current agentic aliases → retain separate phrase queries plus a combined discovery query`
- `P2 F5 provisional vocabulary → Crossref returned 627,049 count-only records and HTTP 429 on sample retrieval → use exact title queries or DOI lookups → do not infer recall from the broad count`
- `P2 F5 provisional vocabulary → OpenAlex full-text query returned 561 records including published and preprint sources but cross-family noise → test title/abstract filters → keep OpenAlex as discovery support rather than a final precision measure`
- `P3 F1 field calibration → arXiv title-only phrase query returned 23 records and title/abstract phrase query returned 136 → retain both variants for sensitivity/precision comparison → do not freeze one field selection without a relevance set`
- `P3 F1 field calibration → OpenAlex title searches returned 2,001 software-task and 858 issue-description records → keep phrase searches separate → do not compare counts directly with arXiv`
- `P3 F1 field calibration → Crossref title counts returned 3,032,498 for software development task and 731,632 for issue description, without usable samples → require narrower sample requests or DOI lookup`
- `P3 F5 field calibration → arXiv title-only phrase query returned 431 records and title/abstract phrase query returned 1,003 → preserve the title/abstract tradeoff as provisional`
- `P3 F5 field calibration → OpenAlex title searches returned 3,622 coding-agent and 866 software-engineering-agent records → keep labels separate and treat counts as discovery diagnostics`
- `P3 F5 field calibration → Crossref coding-agent title query returned HTTP 429 while software-engineering-agent title count returned 1,048,935 → do not infer terminology coverage from either operational result`

No query was removed because it returned contradictory or unexpected material. No query was frozen as a systematic search string.

## Pilot Round 2 Calibration

This round tested the provisional vocabulary selected from Pilot Round 1 across arXiv, OpenAlex, and Crossref. Counts are source-reported and not directly comparable because the APIs search different fields and apply different relevance/indexing behavior. The terms remain provisional and are not validated or frozen systematic terminology.

### P2-F1-01

- **Search ID:** `P2-F1-01`
- **Date:** `2026-08-20`
- **Evidence stream:** Scientific discovery
- **Database / source:** arXiv API
- **Query:** `all:"software development task" OR all:"software task" OR all:"issue description" OR all:"issue-tracking system"`
- **Fields searched:** arXiv `all` fields
- **Filters:** None; first 10 sorted by relevance
- **Result count:** `272` reported by arXiv
- **Results inspected:** First 10 result records and abstracts; selected source pages inspected in the round
- **Clearly relevant results:** The result set consistently returned software-development-task, issue-description, and issue-tracking studies, including the previously identified Jazz task study and newer issue-description/repair work.
- **Clearly irrelevant patterns:** LLM evaluation, energy/accuracy, cognitive-load, and generic issue-tracking studies appeared alongside work-definition material. The terms retrieve a useful neighborhood, not a single homogeneous topic.
- **Terminology discovered:** outer-loop software-development tasks, issue description response, issue tracking systems, issue-resolution, software-development task evaluation
- **Candidate seed sources:** Previously identified [Licorish and MacDonell](https://arxiv.org/abs/2104.12131) and [Ramírez-Mora et al.](https://arxiv.org/abs/2006.01358) remained retrievable. [SIADAFIX: issue description response for adaptive program repair](https://arxiv.org/abs/2510.16059) was discovered as a newer issue-description term; its source page was not fully inspected in this round.
- **Query adjustment:** `P1 phrase-focused F1 family → 272 results across the four provisional terms with recurring but mixed software-task contexts → retain the four terms as separate phrase tests across databases → avoid treating the combined retrieval set as one evidence domain`
- **Rationale:** The terms consistently retrieve relevant vocabulary, but the sample still requires task-scope screening.
- **Notes:** arXiv search endpoint: [P2-F1-01](https://export.arxiv.org/api/query?search_query=all:%28%22software%20development%20task%22%20OR%20%22software%20task%22%20OR%20%22issue%20description%22%20OR%20%22issue-tracking%20system%22%29&start=0&max_results=10&sortBy=relevance). No Work Item characteristic was assessed.

### P2-F1-02

- **Search ID:** `P2-F1-02`
- **Date:** `2026-08-20`
- **Evidence stream:** Scientific discovery
- **Database / source:** Crossref Works API
- **Query:** `software development task software task issue description issue-tracking system`
- **Fields searched:** Crossref bibliographic query fields
- **Filters:** `rows=0` count-only request
- **Result count:** `1,692,352` reported by Crossref
- **Results inspected:** No records; count-only request
- **Clearly relevant results:** Not assessed in this count-only calibration.
- **Clearly irrelevant patterns:** The volume indicates that Crossref's bibliographic query semantics are too broad for precision assessment with this unfielded combined query.
- **Terminology discovered:** No new term from the count-only request
- **Candidate seed sources:** None from this request
- **Query adjustment:** `combined provisional F1 terms → 1,692,352 Crossref records under bibliographic query behavior → use fielded/title/abstract syntax or separate phrase queries in later Crossref calibration → avoid using this count as a precision or recall estimate`
- **Rationale:** Crossref is useful for DOI discovery, but this query form is not yet suitable for an interpretable combined search.
- **Notes:** Crossref returned a count but no records because `rows=0` was used. A later request for sample records should use narrower or fielded queries; no result count was estimated from the count-only response.

### P2-F1-03

- **Search ID:** `P2-F1-03`
- **Date:** `2026-08-20`
- **Evidence stream:** Scientific discovery
- **Database / source:** OpenAlex Works API
- **Query:** `"software development task" "issue description"`
- **Fields searched:** OpenAlex full-text search
- **Filters:** `per-page=5`; selected metadata fields
- **Result count:** `44` reported by OpenAlex
- **Results inspected:** Five returned metadata records and titles; [Agentless](https://arxiv.org/abs/2407.01489) was opened and its abstract inspected as an off-target but useful terminology source.
- **Clearly relevant results:** The query surfaced `Demystifying LLM-Based Software Engineering Agents`, `Agentless`, `MarsCode Agent`, and `Human-In-the-Loop Software Development Agents`; these are relevant to agent/task terminology but not a clean F1-only sample.
- **Clearly irrelevant patterns:** OpenAlex full-text matching connected the F1 phrases to coding-agent papers through shared discussion of software-development tasks and issue descriptions. This demonstrates cross-family leakage rather than F1 precision.
- **Terminology discovered:** autonomous LLM agents, agentless approach, localization, repair, patch validation, insufficient/misleading issue descriptions
- **Candidate seed sources:** [Demystifying LLM-Based Software Engineering Agents](https://doi.org/10.1145/3715754), Chunqiu Steven Xia et al., 2025, published Proceedings of the ACM on Software Engineering; metadata and abstract were inspected through Crossref. [Agentless](https://arxiv.org/abs/2407.01489), Xia et al., 2024 arXiv preprint, source page and abstract inspected.
- **Query adjustment:** `OpenAlex F1 phrase search → 44 results but top records crossed into coding-agent literature through shared task/issue language → keep F1 and F5 retrieval separate and record cross-family leakage → do not assume a term belongs to only one research stream`
- **Rationale:** The result demonstrates why source context and evidence stream must be recorded during screening.
- **Notes:** OpenAlex reported `44` for the full-text query. The returned `Demystifying...` article is a useful cross-family seed, not an F1 work-unit result.

### P2-F5-01

- **Search ID:** `P2-F5-01`
- **Date:** `2026-08-20`
- **Evidence stream:** Coding-agent-specific scientific discovery
- **Database / source:** arXiv API
- **Query:** `all:"software engineering agent" OR all:"SWE-agent" OR all:"coding agent" OR all:"AI coding agent"`
- **Fields searched:** arXiv `all` fields
- **Filters:** None; first 10 sorted by relevance
- **Result count:** `1,154` reported by arXiv
- **Results inspected:** First 10 result records and abstracts; [AIDev](https://arxiv.org/abs/2602.09185) was opened and its source page/abstract inspected.
- **Clearly relevant results:** The sample included AI coding agents, software-engineering agents, agent-authored pull requests, coding-agent workloads, and software-delegation contracts. `AIDev` explicitly lists `AI Coding Agent`, `Agentic Coding`, `Agentic Software Engineering`, and `Agentic Engineering` as related terms.
- **Clearly irrelevant patterns:** The combined family includes human-centered position papers, systems/infrastructure, compiler work, repository studies, and general agent evaluation. The four terms retrieve a broad research neighborhood.
- **Terminology discovered:** agentic coding, agentic software engineering, agentic engineering, Agentic-PRs, AI agent, coding-agent workloads, software delegation contract
- **Candidate seed sources:** [AIDev: Studying AI Coding Agents on GitHub](https://arxiv.org/abs/2602.09185), Hao Li, Haoxiang Zhang, and Ahmed E. Hassan, 2026 arXiv record with DOI [10.1145/3793302.3797249](https://doi.org/10.1145/3793302.3797249), inspected; [Software Delegation Contracts: Measuring Reviewability in AI Coding-Agent Work](https://arxiv.org/abs/2606.17099), Vincent Schmalbach, 2026 arXiv record and abstract inspected.
- **Query adjustment:** `P1 separate F5 phrase searches → 1,154 results when the four provisional terms are combined → retain separate phrase queries plus a combined discovery query → preserve distinctions between coding assistants, coding agents, and software-engineering agents during screening`
- **Rationale:** The combined query improves discovery of current aliases but is too heterogeneous to serve as a final systematic string.
- **Notes:** arXiv search endpoint: [P2-F5-01](https://export.arxiv.org/api/query?search_query=all:%28%22software%20engineering%20agent%22%20OR%20%22SWE-agent%22%20OR%20%22coding%20agent%22%20OR%20%22AI%20coding%20agent%22%29&start=0&max_results=10&sortBy=relevance). The listed terms remain provisional.

### P2-F5-02

- **Search ID:** `P2-F5-02`
- **Date:** `2026-08-20`
- **Evidence stream:** Coding-agent-specific scientific discovery
- **Database / source:** Crossref Works API
- **Query:** `software engineering agent SWE-agent coding agent AI coding agent`
- **Fields searched:** Crossref bibliographic query fields
- **Filters:** `rows=0` count-only request
- **Result count:** `627,049` reported by Crossref
- **Results inspected:** No records; count-only request. A sample-record request for the same broad query returned HTTP 429 and was not retried as evidence.
- **Clearly relevant results:** Not assessed from this request.
- **Clearly irrelevant patterns:** The very large count and rate limit show that this unfielded Crossref query is unsuitable for precision measurement.
- **Terminology discovered:** No new term from the count-only request
- **Candidate seed sources:** None from this request; known candidates were retrieved through OpenAlex/arXiv and Crossref DOI lookups.
- **Query adjustment:** `combined provisional F5 terms → 627,049 Crossref records and a 429 on sample retrieval → use exact phrase/title/abstract queries separately in later Crossref work → do not treat Crossref's broad count as comparable to arXiv/OpenAlex`
- **Rationale:** The source is useful for DOI metadata after candidate discovery, but this query form is not calibrated for sample inspection.
- **Notes:** The HTTP 429 is preserved as an operational limitation, not interpreted as absence of literature.

### P2-F5-03

- **Search ID:** `P2-F5-03`
- **Date:** `2026-08-20`
- **Evidence stream:** Coding-agent-specific scientific discovery
- **Database / source:** OpenAlex Works API, with source-page and DOI inspection
- **Query:** `"software engineering agent" "SWE-agent" "coding agent"`
- **Fields searched:** OpenAlex full-text search
- **Filters:** `per-page=5`; selected metadata fields
- **Result count:** `561` reported by OpenAlex
- **Results inspected:** Five returned metadata records; [Agentless](https://arxiv.org/abs/2407.01489), [UTBoost](https://aclanthology.org/2025.acl-long.189/), and [Demystifying LLM-Based Software Engineering Agents](https://doi.org/10.1145/3715754) were inspected through source pages or DOI metadata.
- **Clearly relevant results:** The sample included a published ACM software-engineering article, SWE-agent and Agentless preprints, SWE-Gym, and a published ACL coding-agent evaluation paper. This suggests the provisional terms retrieve both preprint and peer-reviewed/published material.
- **Clearly irrelevant patterns:** The full-text query still mixes agent systems, training/evaluation frameworks, issue-resolution benchmarks, and repository-level studies; exact terminology does not define a single experimental population.
- **Terminology discovered:** LLM-based software engineering agents, software-engineering AI agents, SWE-Gym, coding-agent evaluation, agentless software engineering
- **Candidate seed sources:** [Demystifying LLM-Based Software Engineering Agents](https://doi.org/10.1145/3715754), Chunqiu Steven Xia, Yinlin Deng, Soren Dunn, and Lingming Zhang, published 2025 in *Proceedings of the ACM on Software Engineering*, DOI inspected; [UTBoost: Rigorous Evaluation of Coding Agents on SWE-Bench](https://aclanthology.org/2025.acl-long.189/), Boxi Yu, Yuxuan Zhu, Pinjia He, and Daniel Kang, ACL 2025 conference paper, DOI [10.18653/v1/2025.acl-long.189](https://doi.org/10.18653/v1/2025.acl-long.189), source page inspected; [Agentless](https://arxiv.org/abs/2407.01489), preprint source page inspected.
- **Query adjustment:** `OpenAlex combined phrase search → 561 full-text matches with relevant published and preprint records plus cross-family noise → test title/abstract fields and exact phrases separately in the next database-specific iteration → preserve the current query as discovery-only`
- **Rationale:** OpenAlex provides useful cross-source discovery, but its full-text matching should not be used as a final precision estimate.
- **Notes:** OpenAlex query metadata reported all three phrases as required full-text terms. The source-level publication statuses were recorded only for inspected candidates; no evidence synthesis was performed.

## Pilot Round 3 Database-Field Calibration

This round compared title-only and title/abstract-style field behavior for the provisional Family 1 and Family 5 vocabulary. Counts are source-reported and not directly comparable. Crossref title-query counts were obtained with `rows=0`; sample requests were either truncated by the retrieval tool or rate-limited, so no precision estimate is made.

### P3-F1-01

- **Search ID:** `P3-F1-01`
- **Date:** `2026-08-20`
- **Evidence stream:** Scientific discovery
- **Database / source:** arXiv API
- **Query:** `ti:"software development task" OR ti:"software task" OR ti:"issue description" OR ti:"issue-tracking system"`
- **Fields searched:** arXiv title fields
- **Filters:** None; first 10 sorted by relevance
- **Result count:** `23` reported by arXiv
- **Results inspected:** First 10 result records and abstracts
- **Clearly relevant results:** The title-only set retained software-task and issue-description vocabulary; individual known-seed retrieval was not verified from the recorded sample.
- **Clearly irrelevant patterns:** Some titles concerned repair, evaluation, or generic issue tracking rather than work definition.
- **Terminology discovered:** No new term beyond the provisional F1 vocabulary.
- **Candidate seed sources:** Licorish & MacDonell: `Not verified`; Ramírez-Mora et al.: `Not verified`.
- **Query adjustment:** `all-field phrase query → explicit title-only phrase query → compare precision signal against title/abstract-inclusive syntax before any systematic adaptation`
- **Rationale:** Title restriction reduced the result set substantially but may miss studies whose relevant terminology occurs only in abstracts.
- **Notes:** This was a field-behavior calibration, not a final systematic query.

### P3-F1-02

- **Search ID:** `P3-F1-02`
- **Date:** `2026-08-20`
- **Evidence stream:** Scientific discovery
- **Database / source:** arXiv API
- **Query:** `ti:"software development task" OR abs:"software development task" OR ti:"software task" OR abs:"software task" OR ti:"issue description" OR abs:"issue description" OR ti:"issue-tracking system" OR abs:"issue-tracking system"`
- **Fields searched:** arXiv title and abstract fields
- **Filters:** None; first 10 sorted by relevance
- **Result count:** `136` reported by arXiv
- **Results inspected:** First 10 result records and abstracts
- **Clearly relevant results:** The expanded field set recovered additional software-task and issue-description records beyond title-only retrieval.
- **Clearly irrelevant patterns:** Abstract matching reintroduced adjacent repair, evaluation, and general software-engineering noise.
- **Terminology discovered:** No new term beyond the provisional F1 vocabulary.
- **Candidate seed sources:** Licorish & MacDonell: `Not verified`; Ramírez-Mora et al.: `Not verified`. No new seed was promoted from the limited sample.
- **Query adjustment:** `title-only phrase query → title OR abstract phrase query → retain both as sensitivity/precision calibration variants rather than selecting one prematurely`
- **Rationale:** The count increase indicates a recall/precision tradeoff, but the pilot sample is insufficient to quantify either measure.
- **Notes:** arXiv field syntax was tested explicitly; no Work Item characteristic was assessed.

### P3-F1-03

- **Search ID:** `P3-F1-03`
- **Date:** `2026-08-20`
- **Evidence stream:** Scientific discovery
- **Database / source:** OpenAlex Works API
- **Query:** `title.search:"software task"`
- **Fields searched:** OpenAlex title search
- **Filters:** None; selected metadata fields
- **Result count:** `2,001` reported by OpenAlex
- **Results inspected:** Returned metadata sample was used for field-behavior inspection; no complete relevance assessment was attempted.
- **Clearly relevant results:** Title-field matching retrieved a large software-task neighborhood.
- **Clearly irrelevant patterns:** The count remains broad and includes task-evaluation and general software-development work.
- **Terminology discovered:** No new term.
- **Candidate seed sources:** None promoted from this count-focused field test.
- **Query adjustment:** `OpenAlex full-text F1 query → title search for software task → test separate exact title phrases because title search remains broad`
- **Rationale:** OpenAlex title search is operationally distinct from full-text search and should not inherit the earlier full-text interpretation.
- **Notes:** Result count is a source diagnostic, not a precision or recall estimate.

### P3-F1-04

- **Search ID:** `P3-F1-04`
- **Date:** `2026-08-20`
- **Evidence stream:** Scientific discovery
- **Database / source:** OpenAlex Works API
- **Query:** `title.search:"issue description"`
- **Fields searched:** OpenAlex title search
- **Filters:** None; selected metadata fields
- **Result count:** `858` reported by OpenAlex
- **Results inspected:** Returned metadata sample was used for field-behavior inspection; no complete relevance assessment was attempted.
- **Clearly relevant results:** Title matching produced an issue-description literature neighborhood relevant to issue-based work representation.
- **Clearly irrelevant patterns:** The phrase also covers repair, issue mining, and other uses outside task definition.
- **Terminology discovered:** No new term.
- **Candidate seed sources:** None promoted from this count-focused field test.
- **Query adjustment:** `OpenAlex title software task → separate title issue-description query → retain separate F1 phrase tests for later screening`
- **Rationale:** Separate phrase counts expose different coverage and avoid treating F1 vocabulary as interchangeable.
- **Notes:** Result count is not comparable with the arXiv counts.

### P3-F1-05

- **Search ID:** `P3-F1-05`
- **Date:** `2026-08-20`
- **Evidence stream:** Scientific discovery
- **Database / source:** Crossref Works API
- **Query:** `query.title=software development task`
- **Fields searched:** Crossref title query
- **Filters:** `rows=0` count-only request
- **Result count:** `3,032,498` reported by Crossref
- **Results inspected:** No records; the sample response was truncated by the retrieval tool.
- **Clearly relevant results:** Not assessed.
- **Clearly irrelevant patterns:** The very large title-query count requires verification of Crossref query semantics before interpretation.
- **Terminology discovered:** No new term.
- **Candidate seed sources:** None.
- **Query adjustment:** `unfielded combined Crossref query → title query for software development task → use narrower exact-title requests or DOI lookup before drawing coverage conclusions`
- **Rationale:** Fielding changed the query form but did not yet produce an interpretable candidate sample.
- **Notes:** Count-only result; no precision or recall estimate.

### P3-F1-06

- **Search ID:** `P3-F1-06`
- **Date:** `2026-08-20`
- **Evidence stream:** Scientific discovery
- **Database / source:** Crossref Works API
- **Query:** `query.title=issue description`
- **Fields searched:** Crossref title query
- **Filters:** `rows=0` count-only request
- **Result count:** `731,632` reported by Crossref
- **Results inspected:** No records; sample retrieval was not used as evidence.
- **Clearly relevant results:** Not assessed.
- **Clearly irrelevant patterns:** The count is too broad to establish title precision.
- **Terminology discovered:** No new term.
- **Candidate seed sources:** None.
- **Query adjustment:** `Crossref title software development task → separate title issue-description query → retain separate phrase requests and verify samples under rate limits`
- **Rationale:** Separate fielded queries are preferable to the unfielded combined query, but still require sample inspection.
- **Notes:** Count-only result; no precision or recall estimate.

### P3-F5-01

- **Search ID:** `P3-F5-01`
- **Date:** `2026-08-20`
- **Evidence stream:** Coding-agent-specific scientific discovery
- **Database / source:** arXiv API
- **Query:** `ti:"software engineering agent" OR ti:"SWE-agent" OR ti:"coding agent" OR ti:"AI coding agent"`
- **Fields searched:** arXiv title fields
- **Filters:** None; first 10 sorted by relevance
- **Result count:** `431` reported by arXiv
- **Results inspected:** First 10 result records and abstracts
- **Clearly relevant results:** Title-only retrieval retained coding-agent and software-engineering-agent records, including SWE-agent lineage terminology.
- **Clearly irrelevant patterns:** Some results were adjacent agent systems or broad AI evaluation rather than coding-agent work.
- **Terminology discovered:** No new term beyond the provisional F5 vocabulary.
- **Candidate seed sources:** SWE-agent: `Not verified`; SWE-bench: `Not verified`; Agentless: `Not verified`; AIDev: `Not verified`; Understanding Software Engineering Agents: `Not verified`. No new seed was promoted from the limited sample.
- **Query adjustment:** `combined all-field F5 query → title-only phrase query → compare against abstract-inclusive syntax`
- **Rationale:** Title restriction provides a narrower discovery signal while risking omission of papers using agent terminology only in abstracts.
- **Notes:** No agent-category conclusion was drawn.

### P3-F5-02

- **Search ID:** `P3-F5-02`
- **Date:** `2026-08-20`
- **Evidence stream:** Coding-agent-specific scientific discovery
- **Database / source:** arXiv API
- **Query:** `ti:"software engineering agent" OR abs:"software engineering agent" OR ti:"SWE-agent" OR abs:"SWE-agent" OR ti:"coding agent" OR abs:"coding agent" OR ti:"AI coding agent" OR abs:"AI coding agent"`
- **Fields searched:** arXiv title and abstract fields
- **Filters:** None; first 10 sorted by relevance
- **Result count:** `1,003` reported by arXiv
- **Results inspected:** First 10 result records and abstracts
- **Clearly relevant results:** The expanded field set recovered a wider current coding-agent and SWE-agent literature neighborhood.
- **Clearly irrelevant patterns:** Abstract matching increased systems, infrastructure, benchmark, and general-agent noise.
- **Terminology discovered:** No new term beyond the provisional F5 vocabulary.
- **Candidate seed sources:** SWE-agent: `Not verified`; SWE-bench: `Not verified`; Agentless: `Not verified`; AIDev: `Not verified`; Understanding Software Engineering Agents: `Not verified`. No new seed was promoted from the limited sample.
- **Query adjustment:** `title-only F5 query → title OR abstract phrase query → retain both variants for calibration rather than freezing a final string`
- **Rationale:** The larger result set indicates broader coverage but does not establish improved recall without a relevance set.
- **Notes:** No Work Item characteristic was assessed.

### P3-F5-03

- **Search ID:** `P3-F5-03`
- **Date:** `2026-08-20`
- **Evidence stream:** Coding-agent-specific scientific discovery
- **Database / source:** OpenAlex Works API
- **Query:** `title.search:"coding agent"`
- **Fields searched:** OpenAlex title search
- **Filters:** None; selected metadata fields
- **Result count:** `3,622` reported by OpenAlex
- **Results inspected:** Returned metadata sample was used for field-behavior inspection; no complete relevance assessment was attempted.
- **Clearly relevant results:** Title matching retrieved a substantial coding-agent terminology neighborhood.
- **Clearly irrelevant patterns:** The count includes broad agent, coding, and evaluation contexts and is not a clean coding-agent corpus.
- **Terminology discovered:** No new term.
- **Candidate seed sources:** None promoted from this count-focused test.
- **Query adjustment:** `OpenAlex full-text F5 query → title search for coding agent → test software-engineering-agent title wording separately`
- **Rationale:** A title field is more interpretable than the earlier all-term full-text behavior, but remains broad.
- **Notes:** Result count is not comparable with arXiv.

### P3-F5-04

- **Search ID:** `P3-F5-04`
- **Date:** `2026-08-20`
- **Evidence stream:** Coding-agent-specific scientific discovery
- **Database / source:** OpenAlex Works API
- **Query:** `title.search:"software engineering agent"`
- **Fields searched:** OpenAlex title search
- **Filters:** None; selected metadata fields
- **Result count:** `866` reported by OpenAlex
- **Results inspected:** Returned metadata sample was used for field-behavior inspection; no complete relevance assessment was attempted.
- **Clearly relevant results:** The title field retained a narrower software-engineering-agent neighborhood than the coding-agent query.
- **Clearly irrelevant patterns:** Agent infrastructure and evaluation papers remained present.
- **Terminology discovered:** No new term.
- **Candidate seed sources:** None promoted from this count-focused test.
- **Query adjustment:** `OpenAlex title coding agent → separate title software engineering agent query → preserve both labels as non-equivalent provisional terms`
- **Rationale:** The differing counts support separate terminology calibration, not a conclusion that one label has better recall.
- **Notes:** Result count is not comparable with arXiv.

### P3-F5-05

- **Search ID:** `P3-F5-05`
- **Date:** `2026-08-20`
- **Evidence stream:** Coding-agent-specific scientific discovery
- **Database / source:** Crossref Works API
- **Query:** `query.title=coding agent`
- **Fields searched:** Crossref title query
- **Filters:** `rows=0` count-only request
- **Result count:** Not available; Crossref returned HTTP `429 Too Many Requests`
- **Results inspected:** None
- **Clearly relevant results:** Not assessed.
- **Clearly irrelevant patterns:** Rate limiting prevented field-level evaluation.
- **Terminology discovered:** No new term.
- **Candidate seed sources:** None.
- **Query adjustment:** `Crossref broad F5 query → title coding-agent query → pause repeated sampling and use DOI lookup or a later rate-limited request`
- **Rationale:** The operational failure cannot be interpreted as terminology absence or low retrieval.
- **Notes:** HTTP 429 was preserved as an access limitation.

### P3-F5-06

- **Search ID:** `P3-F5-06`
- **Date:** `2026-08-20`
- **Evidence stream:** Coding-agent-specific scientific discovery
- **Database / source:** Crossref Works API
- **Query:** `query.title=software engineering agent`
- **Fields searched:** Crossref title query
- **Filters:** `rows=0` count-only request
- **Result count:** `1,048,935` reported by Crossref
- **Results inspected:** No records; sample output was truncated by the retrieval tool.
- **Clearly relevant results:** Not assessed.
- **Clearly irrelevant patterns:** The count is too broad to support title precision claims.
- **Terminology discovered:** No new term.
- **Candidate seed sources:** None.
- **Query adjustment:** `Crossref title coding agent rate-limited → title software engineering agent count → require narrower requests and explicit sample inspection before using Crossref for screening`
- **Rationale:** The successful count confirms endpoint availability but not useful field semantics.
- **Notes:** Count-only result; no precision or recall estimate.

No Round 3 query was frozen as a systematic search string. The title-only versus title/abstract arXiv comparison is a calibration signal only; the OpenAlex and Crossref counts require further sample-level validation.

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

Record terminology discovered during pilot searches. The eight terms selected from Pilot Round 1 below are provisional vocabulary for calibration, not validated or final terminology. Do not treat a term as a Work Item characteristic merely because it appears frequently in search results.

| Term | Related concept | Source / Search ID | Context | Action | Notes |
|---|---|---|---|---|---|
| software development task | software work definition | P1-F1-02, P1-F1-03, P2-F1-01, P3-F1-01, P3-F1-02 | Traditional software engineering | test provisionally across sources | Appeared in titles and abstracts for task-type, completion, repository, and evaluation studies; not validated as final terminology. |
| software task | software work definition | P1-F1-03, P2-F1-01, P3-F1-01, P3-F1-02 | Traditional software engineering | test provisionally across sources | More precise than unqualified `task`, but still broad across evaluation and developer studies. |
| issue description | issue/work representation | P1-F1-02, P1-F1-03, P2-F1-01, P3-F1-01, P3-F1-02 | Issue-tracking research | test provisionally across sources | Promising phrase for studies of textual work descriptions; retain separate from generic `issue`. |
| issue-tracking system | issue/work representation | P1-F1-03, P2-F1-01, P3-F1-01, P3-F1-02 | Issue-tracking research | test provisionally across sources | Identifies the repository/tool context in which issues are studied; not validated as final terminology. |
| task type | software work classification | P1-F1-03 | Traditional software engineering | add as synonym | Used with task completion performance and categories of development work. |
| task completion performance | completion/outcome terminology | P1-F1-03 | Traditional software engineering | add as outcome term | Outcome phrase, not a Work Item characteristic. |
| coding agent | coding-agent vocabulary | P1-F5-02, P2-F5-01, P3-F5-01, P3-F5-02 | Recent coding-agent research | test provisionally across sources | High-yield broad phrase with adjacent systems and infrastructure noise; not validated as final terminology. |
| AI coding agent | coding-agent vocabulary | P1-F5-02, P2-F5-01, P3-F5-01, P3-F5-02 | Recent coding-agent research | test provisionally across sources | Appeared in recent records alongside coding-agent workloads, sessions, and agent-authored pull requests. |
| software engineering agent | coding-agent vocabulary | P1-F5-03, P2-F5-01, P3-F5-01, P3-F5-02 | Recent software-engineering-agent research | test provisionally across sources | More focused than `coding agent` but still includes non-repository and infrastructure settings. |
| SWE agent / SWE-agent | coding-agent vocabulary | P1-F5-03, P1-F5-04, P2-F5-01, P3-F5-01, P3-F5-02 | Benchmarks and agent systems | test provisionally across sources | Research-lineage term; test hyphenation and plural variants separately rather than treating it as final. |
| AI Software Engineer | coding-agent vocabulary | P1-F5-03 | Unified agent framing | investigate separately | Appears in a paper describing a unified agent across coding, testing, and patching. |
| agent-computer interface (ACI) | agent execution environment | P1-F5-04 | SWE-agent system paper | add as contextual term | Specific interface terminology associated with repository navigation, editing, and execution. |
| SWE-bench | coding-agent evaluation | P1-F5-04 | GitHub issue resolution benchmark | retain as contextual term | Benchmark name, not a general synonym for coding agents. |
| agent trajectory / tool-mediated trajectory | agent execution trace | P1-F5-03, P1-F5-04 | Agent evaluation and analysis | add as contextual term | Used to describe multi-step agent/environment interaction. |
| agentic coding | coding-agent vocabulary | P2-F5-01, P3-F5-01 | Recent coding-agent research | investigate separately | Appeared as a related term in AIDev and the Round 3 arXiv sample; not yet tested as a standalone search phrase. |
| agentic software engineering | coding-agent vocabulary | P2-F5-01, P3-F5-01 | Recent coding-agent research | investigate separately | Appeared as a related term in AIDev and the Round 3 arXiv sample; may overlap with software-engineering-agent terminology. |
| Agentic-PRs | coding-agent activity/data | P2-F5-01, P3-F5-01 | GitHub repository studies | investigate separately | Term used for agent-authored pull requests; source and population boundaries need later screening. |
| software delegation contract | coding-agent work framing | P2-F5-01, P3-F5-01 | Coding-agent task/review study | retain as contextual term | A source-specific term for a study's unit of analysis; not a Work Item characteristic or final vocabulary. |
| agentless software engineering | coding-agent comparison vocabulary | P2-F5-03, P3-F5-03 | Agentless versus agent-based systems | retain as contextual term | Useful for separating autonomous-agent claims from non-agent workflow baselines. |
| SWE-Gym | coding-agent training/evaluation | P2-F5-03, P3-F5-03 | Agent training/evaluation | retain as contextual term | Benchmark/framework name, not a general synonym for coding agents. |

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
