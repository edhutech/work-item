# Search Log

This document is the durable record of pilot searches and, later, systematic searches conducted under [`research/protocol.md`](./protocol.md). Pilot searches validate and refine terminology, query families, database coverage, precision, recall, and feasibility; they do not establish research findings or Work Item characteristics.

Pilot Round 1 was conducted on 2026-08-20 using arXiv search/API endpoints and OpenAlex discovery. Pilot Round 2 calibration was conducted on 2026-08-20 using arXiv, OpenAlex, and Crossref APIs. Pilot Round 3 database-field calibration was conducted on 2026-08-20 using arXiv, OpenAlex, and Crossref APIs. Pilot Round 4 terminology calibration for Families 2 and 3 was conducted on 2026-08-20 using arXiv, OpenAlex, and DOI/publisher metadata. Pilot Round 5 focused calibration for Family 3 was conducted on 2026-08-20 using subgroup-specific arXiv and OpenAlex searches plus Crossref metadata verification. Pilot Round 6 tested the proposed F3-A/F3-B/F3-C split on 2026-08-20 using focused arXiv and OpenAlex searches. No systematic literature review search has begun.

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

## Pilot Round 4 Family 2 Calibration

This round tested phrase-focused requirements, specifications, user-story, acceptance-criteria, and task-description terminology. arXiv title-only and all-field counts are source-reported and not directly comparable. OpenAlex searches were used for discovery and metadata inspection; its full-text semantics and counts are not precision estimates. Candidate records were promoted only when their title, abstract, DOI metadata, or publisher record was inspected sufficiently to establish relevance to Family 2 terminology.

### P4-F2-01

- **Search ID:** `P4-F2-01`
- **Date:** `2026-08-20`
- **Evidence stream:** Scientific discovery
- **Database / source:** arXiv API
- **Query:** `all:"software requirements" OR all:"requirements specification" OR all:"user story" OR all:"acceptance criteria" OR all:"task description"`
- **Fields searched:** arXiv `all` fields
- **Filters:** None; first 10 sorted by relevance
- **Result count:** `1,782` reported by arXiv
- **Results inspected:** First 10 records and abstracts
- **Clearly relevant results:** The sample contained software requirements specification, requirements engineering, functional and non-functional requirements, SRS quality/stability, user stories, and acceptance testing material. `Using LLMs in Software Requirements Specifications: An Empirical Evaluation` was identifiable as an RE 2024 paper from the record and DOI.
- **Clearly irrelevant patterns:** Generic project documents, AI/LLM requirement-generation papers, ethical user stories, and requirements in non-software or domain-specific contexts appeared together. `task description` was not a clean software-work representation term in this combined all-field sample.
- **Terminology discovered:** software requirements specification (SRS), functional requirements, non-functional requirements, requirements engineering, acceptance testing criteria, ethical user stories, requirements validation, requirements classification
- **Candidate seed sources:** Madhava Krishna, Bhagesh Gaur, Arsh Verma, and Pankaj Jalote, `Using LLMs in Software Requirements Specifications: An Empirical Evaluation`, 2024, IEEE International Requirements Engineering Conference (RE), DOI [10.1109/RE59067.2024.00056](https://doi.org/10.1109/RE59067.2024.00056); inspected arXiv record, abstract, journal reference, and DOI.
- **Query adjustment:** `F2 provisional combined phrase query → 1,782 results with distinct SRS, user-story, acceptance-testing, and unrelated task-description contexts → retain exact phrases but test title-only and software-engineering intersections separately → avoid treating requirements, stories, criteria, and task descriptions as interchangeable`
- **Rationale:** The initial discovery search exposed multiple established traditions, but the combined result set was heterogeneous and not suitable for a single relevance interpretation.
- **Notes:** arXiv endpoint: [P4-F2-01](https://export.arxiv.org/api/query?search_query=all:%22software%20requirements%22%20OR%20all:%22requirements%20specification%22%20OR%20all:%22user%20story%22%20OR%20all:%22acceptance%20criteria%22%20OR%20all:%22task%20description%22&start=0&max_results=10&sortBy=relevance). Metadata/abstract inspection only; no Work Item characteristic was assessed.

### P4-F2-02

- **Search ID:** `P4-F2-02`
- **Date:** `2026-08-20`
- **Evidence stream:** Scientific discovery
- **Database / source:** arXiv API
- **Query:** `ti:"software requirements" OR ti:"requirements specification" OR ti:"user story" OR ti:"acceptance criteria" OR ti:"task description"`
- **Fields searched:** arXiv title fields
- **Filters:** None; first 10 sorted by relevance
- **Result count:** `133` reported by arXiv
- **Results inspected:** First 10 records and abstracts
- **Clearly relevant results:** Title-only retrieval retained software requirements specifications, requirements-specification stability/quality, and user-story-related records; it reduced some abstract-only cross-domain matches.
- **Clearly irrelevant patterns:** Student/project specification documents, security specifications, and unrelated uses of `acceptance` remained. Title-only retrieval also risks missing papers that study an artifact without naming it in the title.
- **Terminology discovered:** requirements specification document, software requirements specification document, natural-language requirements, requirements artifact
- **Candidate seed sources:** J. del Sagrado and I. M. del Águila, `Stability prediction of the software requirements specification`, 2018 journal article (arXiv record 2024), *Software Quality Journal*, DOI [10.1007/s11219-017-9362-x](https://doi.org/10.1007/s11219-017-9362-x); inspected arXiv abstract and publication metadata. The record explicitly concerns requirements-specification documents and requirements metrics.
- **Query adjustment:** `F2 all-field phrase query → 1,782 results → title-only phrase query → 133 results with a narrower but incomplete artifact signal → retain title-only as a precision-oriented variant and title/abstract/all-field variants for sensitivity`
- **Rationale:** Round 3 established that title-only and title/abstract retrieval are different strategies; this family confirms the same tradeoff for requirements artifacts.
- **Notes:** arXiv title syntax was explicit. The result count is a source diagnostic, not an estimate of relevant literature.

### P4-F2-03

- **Search ID:** `P4-F2-03`
- **Date:** `2026-08-20`
- **Evidence stream:** Scientific discovery
- **Database / source:** arXiv API
- **Query:** `all:"acceptance criteria" AND all:"software engineering"`
- **Fields searched:** arXiv `all` fields
- **Filters:** None; first 10 sorted by relevance
- **Result count:** `30` reported by arXiv
- **Results inspected:** First 10 records and abstracts; the ICSE candidate record and DOI metadata were inspected
- **Clearly relevant results:** The sample included acceptance criteria in requirements engineering, user stories, BDD/Gherkin, requirement coverage, and software-engineering-agent evaluation. `From Bugs to Benefits: Improving User Stories by Leveraging Crowd Knowledge with CrUISE-AC` directly connected user stories and generated acceptance criteria and identified an ICSE 2025 publication.
- **Clearly irrelevant patterns:** General user-acceptance criteria, cost-model acceptance criteria, autonomous-driving testing, and unrelated AI evaluation remained despite the software-engineering term.
- **Terminology discovered:** acceptance testing criteria, Gherkin acceptance criteria, Behavior-Driven Development (BDD), requirement coverage, requirement-aligned acceptance criteria, acceptance-criteria generation
- **Candidate seed sources:** Stefan Schwedt and Thomas Ströder, `From Bugs to Benefits: Improving User Stories by Leveraging Crowd Knowledge with CrUISE-AC`, 2025, ICSE, pp. 1385–1395, DOI [10.1109/icse55347.2025.00217](https://doi.org/10.1109/icse55347.2025.00217); arXiv abstract and DOI/publisher metadata inspected. This is a candidate for later screening of the relationship between user stories, issue knowledge, and acceptance criteria.
- **Query adjustment:** `all:"acceptance criteria" → broad mixed acceptance language → all:"acceptance criteria" AND all:"software engineering" → isolate a smaller software-engineering neighborhood while preserving BDD, requirements, and agent-evaluation noise`
- **Rationale:** The conjunction materially improved manageability but did not make `acceptance criteria` a homogeneous requirements term.
- **Notes:** The query is useful for separate acceptance-criteria calibration, not for collapsing acceptance criteria into general requirements.

### P4-F2-04

- **Search ID:** `P4-F2-04`
- **Date:** `2026-08-20`
- **Evidence stream:** Scientific discovery
- **Database / source:** arXiv API
- **Query:** `all:"user story" AND all:"software engineering"`
- **Fields searched:** arXiv `all` fields
- **Filters:** None; first 10 sorted by relevance
- **Result count:** `71` reported by arXiv
- **Results inspected:** First 10 records and abstracts; selected publisher metadata was inspected through DOI records
- **Clearly relevant results:** Records addressed agile requirements artifacts, user-story quality, user-story sets, NLP over user stories, and user-story generation. `User Story Tutor` explicitly described story readability and effort estimation; `Exploring LLMs Impact on Student-Created User Stories and Acceptance Testing in Software Development` linked user stories to acceptance testing and scope.
- **Clearly irrelevant patterns:** Blockchain methods, ethical user stories, privacy requirements, and domain-specific user-story applications appeared alongside general agile requirements research.
- **Terminology discovered:** agile requirements artifact, user-story set, user-story quality, INVEST, story readability, story points, user-story management, acceptance testing
- **Candidate seed sources:** I. K. Raharjana, D. Siahaan, and C. Fatichah, `User Stories and Natural Language Processing: A Systematic Literature Review`, 2021, *IEEE Access* 9, 53811–53826, DOI [10.1109/access.2021.3070606](https://doi.org/10.1109/access.2021.3070606); publisher DOI metadata and OpenAlex record inspected. G. Neo et al., `User Story Tutor (UST) to Support Agile Software Developers`, 2024, CSEDU, DOI [10.5220/0012619200003693](https://doi.org/10.5220/0012619200003693); arXiv record, abstract, and DOI metadata inspected.
- **Query adjustment:** `all:"user story" → broad user-story discovery → all:"user story" AND all:"software engineering" → retain agile/user-story terms while documenting domain-specific and ethical-story noise`
- **Rationale:** User-story literature is a recognizable research tradition, but it includes quality, tooling, NLP, education, domain requirements, and planning/estimation subtraditions that require separate screening.
- **Notes:** The systematic review seed is a discovery candidate, not yet extracted evidence. No claim was made about the suitability of user stories for coding agents.

### P4-F2-05

- **Search ID:** `P4-F2-05`
- **Date:** `2026-08-20`
- **Evidence stream:** Scientific discovery
- **Database / source:** OpenAlex Works API
- **Query:** `"requirements quality" software`
- **Fields searched:** OpenAlex full-text search
- **Filters:** `per-page=10`; selected metadata fields
- **Result count:** `3,193` reported by OpenAlex
- **Results inspected:** Ten returned metadata records and titles; DOI metadata for the systematic-review and requirements-quality candidates was inspected
- **Clearly relevant results:** `Challenges of Software Requirements Quality Assurance and Validation: A Systematic Literature Review`, `Requirements quality control: a unifying framework`, and papers on natural-language requirements quality were identifiable. The result set exposed a quality/assessment tradition separate from artifact-name searches.
- **Clearly irrelevant patterns:** Generic quality models, project success, and coding-agent papers sharing the word `quality` appeared in the full-text set.
- **Terminology discovered:** requirements quality assurance, requirements validation, requirements quality control, natural-language requirements quality, requirements quality assessment
- **Candidate seed sources:** I. Atoum et al., `Challenges of Software Requirements Quality Assurance and Validation: A Systematic Literature Review`, 2021, *IEEE Access* 9, 137613–137634, DOI [10.1109/access.2021.3117989](https://doi.org/10.1109/access.2021.3117989); publisher DOI metadata and OpenAlex record inspected. P. W. T. Wong and J. L. H. H. K. Lau, `Requirements quality control: a unifying framework`, 2005, *Requirements Engineering*, DOI [10.1007/s00766-005-0018-1](https://doi.org/10.1007/s00766-005-0018-1); OpenAlex metadata inspected, publisher access was unavailable.
- **Query adjustment:** `artifact phrases → recurring quality-related titles and terminology → "requirements quality" software → test quality/assessment as a separate F2 subfamily → do not fold quality terminology into requirements/specification synonyms`
- **Rationale:** The search established a distinct quality-assurance/validation research tradition relevant to later calibration of artifact properties, without treating those properties as conclusions.
- **Notes:** OpenAlex full-text count is not a relevance estimate. The Springer DOI request returned HTTP 429 during publisher retrieval; this access limitation was not interpreted as absence of the source.

### P4-F2-06

- **Search ID:** `P4-F2-06`
- **Date:** `2026-08-20`
- **Evidence stream:** Scientific discovery
- **Database / source:** OpenAlex Works API
- **Query:** `"user story" software`
- **Fields searched:** OpenAlex full-text search
- **Filters:** `per-page=10`; selected metadata fields
- **Result count:** `12,093` reported by OpenAlex
- **Results inspected:** Ten returned metadata records and titles; DOI metadata for the systematic-review, quality-framework, and practice-study candidates was inspected
- **Clearly relevant results:** The sample included `Improving agile requirements: the Quality User Story framework and tool`, `The Use and Effectiveness of User Stories in Practice`, `User Stories and Natural Language Processing: A Systematic Literature Review`, user-story management, and planning-poker studies.
- **Clearly irrelevant patterns:** Books, general agile planning, education/tooling, and unrelated full-text matches inflated the result set.
- **Terminology discovered:** Quality User Story, agile requirements, user-story management, user-story effectiveness, user-story practice
- **Candidate seed sources:** Garm Lucassen, Fabiano Dalpiaz, Jan Martijn E. M. van der Werf, and Sjaak Brinkkemper, `Improving agile requirements: the Quality User Story framework and tool`, 2016, *Requirements Engineering*, DOI [10.1007/s00766-016-0250-x](https://doi.org/10.1007/s00766-016-0250-x); Crossref metadata, OpenAlex metadata, and DOI target were inspected, but the publisher returned HTTP 429. Garm Lucassen et al., `The Use and Effectiveness of User Stories in Practice`, 2016, Springer LNCS chapter, DOI [10.1007/978-3-319-30282-9_14](https://doi.org/10.1007/978-3-319-30282-9_14); OpenAlex metadata inspected, full text unavailable.
- **Query adjustment:** `arXiv user-story/SE intersection → OpenAlex full-text user-story/software discovery → preserve Quality User Story and user-story effectiveness as separate candidate terms while recording broad OpenAlex noise`
- **Rationale:** OpenAlex surfaced established titles and terminology not present in the small arXiv sample, but the count and full-text semantics prevent precision interpretation.
- **Notes:** This search was discovery/metadata calibration only. No Work Item characteristic was derived.

## Pilot Round 4 Family 3 Calibration

This round tested decomposition and task-description phrases separately from Family 2 artifact terminology. The results show that `task decomposition` is common outside software engineering; software-specific intersections and source screening are necessary. `task granularity` also primarily retrieved parallel-computing/runtime scheduling material rather than decomposition of development work.

### P4-F3-01

- **Search ID:** `P4-F3-01`
- **Date:** `2026-08-20`
- **Evidence stream:** Scientific discovery
- **Database / source:** arXiv API
- **Query:** `all:"task decomposition" OR all:"work decomposition" OR all:"task breakdown" OR all:"software development task" OR all:"task description"`
- **Fields searched:** arXiv `all` fields
- **Filters:** None; first 10 sorted by relevance
- **Result count:** `1,011` reported by arXiv
- **Results inspected:** First 10 records and abstracts
- **Clearly relevant results:** The sample contained software-development-task literature and `Tasks Decomposition Approaches in Crowdsourcing Software Development`, which explicitly studies decomposition practices in a software-development setting. It also surfaced software-development workflow and task-evaluation terminology.
- **Clearly irrelevant patterns:** General AI task decomposition, robotics/control, multi-agent reinforcement learning, NLP task descriptions, annotation decomposition, and LLM software-task evaluation dominated much of the sample.
- **Terminology discovered:** task decomposition approaches, crowdsourcing software development, task preparation, manageable tasks, software-development task type, outer-loop software-development tasks
- **Candidate seed sources:** Abdullah Khanfor, `Tasks Decomposition Approaches in Crowdsourcing Software Development`, 2023, arXiv preprint, DOI [10.48550/arxiv.2302.05099](https://doi.org/10.48550/arxiv.2302.05099); arXiv record and abstract inspected. The abstract explicitly describes breaking projects into manageable software tasks, preparing tasks, and reviewing submissions.
- **Query adjustment:** `F3 provisional combined phrase query → 1,011 results with strong general-AI/planning noise → require a software-development intersection and inspect title/abstract context → distinguish software task decomposition from generic AI task decomposition`
- **Rationale:** The initial discovery query was useful for finding aliases but was too heterogeneous for direct screening.
- **Notes:** arXiv endpoint: [P4-F3-01](https://export.arxiv.org/api/query?search_query=all:%22task%20decomposition%22%20OR%20all:%22work%20decomposition%22%20OR%20all:%22task%20breakdown%22%20OR%20all:%22software%20development%20task%22%20OR%20all:%22task%20description%22&start=0&max_results=10&sortBy=relevance). No conclusion about decomposition effects was drawn.

### P4-F3-02

- **Search ID:** `P4-F3-02`
- **Date:** `2026-08-20`
- **Evidence stream:** Scientific discovery
- **Database / source:** arXiv API
- **Query:** `ti:"task decomposition" OR ti:"work decomposition" OR ti:"task breakdown" OR ti:"software development task" OR ti:"task description"`
- **Fields searched:** arXiv title fields
- **Filters:** None; first 10 sorted by relevance
- **Result count:** `92` reported by arXiv
- **Results inspected:** First 10 records and abstracts
- **Clearly relevant results:** Title-only retrieval retained software-development-task records, including the Jazz task-type study, but did not make `task decomposition` itself common in software-engineering titles.
- **Clearly irrelevant patterns:** General task decomposition, software-task evaluation, energy/accuracy, and cognitive-load studies remained. A title match did not guarantee decomposition of development work.
- **Terminology discovered:** task type, task completion performance, software development tasks, software task evaluation
- **Candidate seed sources:** Sherlock A. Licorish and Stephen G. MacDonell, `Exploring the links between software development task type, team attitudes and task completion performance: Insights from the Jazz repository`, 2017/2018, *Information and Software Technology* 97, DOI [10.1016/j.infsof.2017.12.005](https://doi.org/10.1016/j.infsof.2017.12.005); arXiv record, abstract, and DOI metadata inspected. It is a seed for software-task classification/context, not a direct decomposition study.
- **Query adjustment:** `F3 all-field phrase query → title-only phrase query → 92 results but persistent task-evaluation and general-AI noise → retain title-only for terminology sensitivity, not as a sufficient software-decomposition filter`
- **Rationale:** Field restriction reduces breadth but cannot substitute for a software-development/decomposition relevance screen.
- **Notes:** The source record identifies the journal publication and a dataset of approximately 30,000 software-development tasks; that observation is recorded only for seed relevance.

### P4-F3-03

- **Search ID:** `P4-F3-03`
- **Date:** `2026-08-20`
- **Evidence stream:** Scientific discovery
- **Database / source:** arXiv API
- **Query:** `all:"task decomposition" AND all:"software development"`
- **Fields searched:** arXiv `all` fields
- **Filters:** None; first 10 sorted by relevance
- **Result count:** `5` reported by arXiv
- **Results inspected:** All five records and abstracts
- **Clearly relevant results:** `Tasks Decomposition Approaches in Crowdsourcing Software Development` was directly relevant to F3. Other records concerned end-to-end software-development agents, multi-agent software development, and software-agent surveys where decomposition is an architectural/planning term.
- **Clearly irrelevant patterns:** The intersection still included agent architecture and benchmark work rather than human/team task decomposition; one result was a general code-generation-agent survey.
- **Terminology discovered:** task decomposition and collaboration, end-to-end software development, requirement-driven task decomposition, multi-agent software development
- **Candidate seed sources:** Zhengran Zeng et al., `Benchmarking and Studying the LLM-based Agent System in End-to-End Software Development`, 2025, arXiv preprint, arXiv:2511.04064; record and abstract inspected. It is a coding-agent-specific contextual seed because the abstract names task-decomposition strategy as an agent-system variable, not because it establishes a general software task decomposition model. Khanfor's 2023 crowdsourcing paper remained the direct traditional-SE seed.
- **Query adjustment:** `broad F3 phrase query → general-AI and robotics noise → all:"task decomposition" AND all:"software development" → five inspectable records with a smaller but mixed software-development neighborhood`
- **Rationale:** The conjunction was the most useful revised arXiv search for separating generic task decomposition from software-development contexts.
- **Notes:** This search bridges traditional software development and coding-agent-specific terminology; the evidence streams remain distinct during later screening.

### P4-F3-04

- **Search ID:** `P4-F3-04`
- **Date:** `2026-08-20`
- **Evidence stream:** Scientific discovery
- **Database / source:** arXiv API
- **Query:** `all:"task granularity" AND all:"software"`
- **Fields searched:** arXiv `all` fields
- **Filters:** None; first 10 sorted by relevance
- **Result count:** `5` reported by arXiv
- **Results inspected:** All five records and abstracts
- **Clearly relevant results:** The query showed that `task granularity` is an established software/computing phrase, but the inspected records focused on parallel-program execution, scheduling, profiling, and runtime granularity rather than decomposition of software-development work.
- **Clearly irrelevant patterns:** HPC scheduling, parallel QR factorization, task-parallel runtime performance, and Android execution profiling dominated the sample.
- **Terminology discovered:** task granularity, fine-grained tasks, minimum effective task granularity, task-based execution
- **Candidate seed sources:** None promoted. The records were useful negative calibration evidence for the phrase's ambiguity, not candidate literature on development-work decomposition.
- **Query adjustment:** `F3 decomposition phrases → recurring size/granularity language → all:"task granularity" AND all:"software" → inspect separately and keep out of broad work-decomposition searches unless paired with development/task-planning context`
- **Rationale:** The phrase may be useful for later conceptual searching, but this pilot did not establish that it ordinarily denotes software-development task size.
- **Notes:** No conclusion about an optimal or preferred granularity was made.

### P4-F3-05

- **Search ID:** `P4-F3-05`
- **Date:** `2026-08-20`
- **Evidence stream:** Scientific discovery
- **Database / source:** OpenAlex Works API
- **Query:** `"task decomposition" software`
- **Fields searched:** OpenAlex full-text search
- **Filters:** `per-page=10`; selected metadata fields
- **Result count:** `6,164` reported by OpenAlex
- **Results inspected:** Ten returned metadata records and titles
- **Clearly relevant results:** The sample included `Two's company, three's a crowd: a case study of crowdsourcing software development`, software-task decomposition/parallelism material, and software development task records.
- **Clearly irrelevant patterns:** Artificial intelligence, dialogue management, robotics, compiler construction, HPC, and general task-based systems dominated the result set.
- **Terminology discovered:** crowdsourcing software development, task allocation, software development task allocation, design rule hierarchies, parallelism in software development tasks
- **Candidate seed sources:** Klaas-Jan Stol and Brian Fitzgerald, `Two's company, three's a crowd: a case study of crowdsourcing software development`, 2014, ICSE, pp. 187–198, DOI [10.1145/2568225.2568249](https://doi.org/10.1145/2568225.2568249); Crossref metadata, OpenAlex metadata, and DOI target were inspected, but the publisher request returned HTTP 429. C. Treude and M.-A. Storey, `Design Rule Hierarchies and Parallelism in Software Development Tasks`, 2009, ASE, DOI [10.1109/ase.2009.53](https://doi.org/10.1109/ase.2009.53); OpenAlex metadata and DOI target were inspected, but the publisher request returned HTTP 429.
- **Query adjustment:** `arXiv software-development intersection → OpenAlex full-text task-decomposition/software discovery → retain task allocation, crowdsourcing, and parallelism as distinct contextual terms while treating the count as non-interpretable`
- **Rationale:** OpenAlex found traditional software-engineering work not visible in the small arXiv sample, but its broad full-text semantics require title/abstract and source screening later.
- **Notes:** Crossref was not queried for a broad count in Round 4 because prior rounds demonstrated that such counts are not interpretable and sample requests may be rate-limited. DOI/publisher HTTP 429 responses are recorded as access limitations.

### P4-F3-06

- **Search ID:** `P4-F3-06`
- **Date:** `2026-08-20`
- **Evidence stream:** Scientific discovery
- **Database / source:** OpenAlex Works API
- **Query:** `"software task decomposition"`
- **Fields searched:** OpenAlex full-text search
- **Filters:** `per-page=10`; selected metadata fields
- **Result count:** `5` reported by OpenAlex
- **Results inspected:** All five returned metadata records and titles
- **Clearly relevant results:** The exact phrase retrieved the Khanfor crowdsourcing paper and a small set of unrelated or adjacent software-development/agent records. This supports testing the exact phrase as a narrow discovery variant.
- **Clearly irrelevant patterns:** Mission reliability, education, and general software/agent records remained even under the exact phrase because OpenAlex matches full text rather than requiring the phrase to define the title or study object.
- **Terminology discovered:** software task decomposition, decomposition approaches, requirement-driven software engineering tasks
- **Candidate seed sources:** Khanfor, `Tasks Decomposition Approaches in Crowdsourcing Software Development`, 2023, arXiv preprint, DOI [10.48550/arxiv.2302.05099](https://doi.org/10.48550/arxiv.2302.05099); OpenAlex record and arXiv source page/abstract inspected.
- **Query adjustment:** `OpenAlex broad task-decomposition/software search → 6,164 mixed records → exact "software task decomposition" → 5 records and one direct seed → retain as a narrow discovery query, not a validated systematic string`
- **Rationale:** Exact phrase searching materially improved manageability and surfaced a direct F3 seed, but the sample is too small and source semantics remain uncertain.
- **Notes:** Counts are not comparable with arXiv. No Work Item characteristic or decomposition-effect conclusion was derived.

No Round 4 query was frozen as a systematic search string. The evidence supports separate F2 artifact/quality subfamilies and a software-context-qualified F3 decomposition family, while leaving title-only versus title/abstract choices for later source-specific searching.

## Pilot Round 7 Family 4 Calibration

Pilot Round 7 was conducted on 2026-08-20 using OpenAlex Works API discovery and metadata/abstract inspection. The round was limited to Family 4. No F6 or F7 searches were executed. OpenAlex `search` in these requests performs broad full-text matching; reported counts are therefore retrieval diagnostics, not estimates of the relevant literature. The inspected records were used for terminology, venue, publication-status, noise, and seed calibration only. No Work Item characteristic, causal conclusion, hypothesis, or optimal information amount was derived.

The four provisional groups did not behave as one homogeneous search family. Requirements ambiguity/completeness, developer information seeking, programmer mental workload, information overload, and documentation relevance/maintenance exposed different literatures, populations, constructs, and outcome measures. This supports retaining separate branches for later systematic-search design.

### P7-F4A-01

- **Search ID:** `P7-F4A-01`
- **Date:** `2026-08-20`
- **Evidence stream:** Scientific discovery
- **Database / source:** OpenAlex Works API
- **Query:** `requirements ambiguity`
- **Fields searched:** OpenAlex broad full-text search
- **Filters:** `per-page=10`; selected metadata, abstracts, DOI, authors, and primary-location fields
- **Result count:** `831,451` reported by OpenAlex
- **Results inspected:** First-page records, abstracts where available, DOI and venue metadata
- **Clearly relevant results:** The sample contained a requirements-engineering review of ambiguity, requirements-specification ambiguity, natural-language requirements ambiguity, ambiguity detection, and ambiguity-resolution records. Relevant titles included `Addressing the challenges of requirements ambiguity: A review of empirical literature`, `Ambiguity in Requirements Specification`, `Identifying Nocuous Ambiguities in Natural Language Requirements`, `Requirements for tools for ambiguity identification and measurement in natural language requirements specifications`, `Analysing anaphoric ambiguity in natural language requirements`, and `Detecting Ambiguities in Requirements Documents Using Inspections`.
- **Clearly irrelevant patterns:** Psycholinguistics, organizational communication, regulatory/legal requirements, and generic natural-language ambiguity were also retrieved. The broad full-text count was dominated by incidental matches outside software requirements.
- **Terminology discovered:** requirements ambiguity, natural-language requirements, requirements specification, ambiguity identification and measurement, ambiguity detection, ambiguity resolution, anaphoric ambiguity, lexical/semantic/syntactic ambiguity, nocuous ambiguity.
- **Candidate seed sources:** Muneera Bano, `Addressing the challenges of requirements ambiguity: A review of empirical literature`, 2015, IEEE EmpiRE workshop, DOI [10.1109/empire.2015.7431303](https://doi.org/10.1109/empire.2015.7431303), published proceedings record; Daniel M. Berry and Erik Kamsties, `Ambiguity in Requirements Specification`, 2004, book chapter in *Perspectives on Software Requirements*, DOI [10.1007/978-1-4615-0465-8_2](https://doi.org/10.1007/978-1-4615-0465-8_2), published; Francis Chantree, Bashar Nuseibeh, Anne de Roeck, and Alistair Willis, `Identifying Nocuous Ambiguities in Natural Language Requirements`, 2006, IEEE RE, DOI [10.1109/re.2006.31](https://doi.org/10.1109/re.2006.31), published; Nadzeya Kiyavitskaya, Nicola Zeni, Luisa Mich, and Daniel M. Berry, `Requirements for tools for ambiguity identification and measurement in natural language requirements specifications`, 2008, *Requirements Engineering*, DOI [10.1007/s00766-008-0063-7](https://doi.org/10.1007/s00766-008-0063-7), published; Erik Kamsties, Daniel M. Berry, and Barbara Paech, `Detecting Ambiguities in Requirements Documents Using Inspections`, 2001, source record with an inspectable author-hosted version but no DOI identified in this pilot.
- **Query adjustment:** `requirements ambiguity → 831,451 broad full-text matches with a strong requirements-ambiguity neighborhood but substantial linguistic and non-software noise → test completeness/quality and traceability terminology with a software-requirements qualifier`
- **Rationale:** The initial query established a coherent requirements-engineering branch, but `ambiguity` alone cannot distinguish requirements ambiguity from general linguistic ambiguity or ambiguity in other requirement domains.
- **Notes:** The records are discovery candidates, not extracted evidence. Ambiguity in requirements/specifications is kept distinct from ambiguity in source code, APIs, project uncertainty, and natural-language research outside executable software work.

### P7-F4A-02

- **Search ID:** `P7-F4A-02`
- **Date:** `2026-08-20`
- **Evidence stream:** Scientific discovery
- **Database / source:** OpenAlex Works API
- **Query:** `requirements completeness software`
- **Fields searched:** OpenAlex broad full-text search
- **Filters:** `per-page=10`; selected metadata and abstracts
- **Result count:** `1,948,484` reported by OpenAlex
- **Results inspected:** First-page records, abstracts where available, DOI and venue metadata
- **Clearly relevant results:** `Preventing Defects: The Impact of Requirements Traceability Completeness on Software Quality`, Patrick Rempel and Parick Mader, 2016, *IEEE Transactions on Software Engineering*, DOI [10.1109/TSE.2016.2622264](https://doi.org/10.1109/TSE.2016.2622264), published version, was a direct completeness/quality seed. `Requirements Engineering: A Good Practice Guide`, Ian Sommerville and Pete Sawyer, 1997, Lancaster University e-print, was a terminology source with an accepted-version record.
- **Clearly irrelevant patterns:** Most first-page records were software-package or scientific-computing descriptions such as Quantum ESPRESSO, VOSviewer, NMRPipe, Bioconductor, FieldTrip, MEGA3, and PsychoPy. The broad count cannot support precision claims.
- **Terminology discovered:** requirements traceability completeness, requirements coverage, requirements quality, requirements quality assessment, defect prevention, software quality.
- **Candidate seed sources:** Patrick Rempel and Parick Mader, `Preventing Defects: The Impact of Requirements Traceability Completeness on Software Quality`, 2016, *IEEE Transactions on Software Engineering*, DOI [10.1109/TSE.2016.2622264](https://doi.org/10.1109/TSE.2016.2622264), published; Ian Sommerville and Pete Sawyer, `Requirements Engineering: A Good Practice Guide`, 1997, Lancaster University e-print, stable URL not resolved in this pilot, accepted-version record.
- **Query adjustment:** `requirements completeness software → 1,948,484 broad full-text matches and package-description noise → ("requirements completeness" OR "requirements traceability completeness" OR "requirements coverage" OR "requirements quality") AND ("software requirements" OR "software engineering") → preserve completeness, coverage, traceability, and quality as related but non-interchangeable branches`
- **Rationale:** The revised terminology is more useful for later fielded searching than the phrase `information sufficiency`; it also exposes a measurable traceability/completeness tradition. The query remains discovery-only because OpenAlex full-text semantics still produce substantial noise.
- **Notes:** This branch overlaps F2 requirements/specifications and should be cross-screened rather than duplicated automatically.

### P7-F4B-01

- **Search ID:** `P7-F4B-01`
- **Date:** `2026-08-20`
- **Evidence stream:** Scientific discovery
- **Database / source:** OpenAlex Works API
- **Query:** `developer information needs`
- **Fields searched:** OpenAlex broad full-text search
- **Filters:** `per-page=10`; selected metadata and abstracts
- **Result count:** `608,914` reported by OpenAlex
- **Results inspected:** First-page records, abstracts where available, DOI and venue metadata
- **Clearly relevant results:** `API-Related Developer Information Needs in Stack Overflow`, Mingwei Liu et al., 2021, *IEEE Transactions on Software Engineering*, DOI [10.1109/TSE.2021.3120203](https://doi.org/10.1109/TSE.2021.3120203), published; `Categorizing developer information needs in software ecosystems`, Nicole Haenni et al., 2013, ACM ecosystem-architecture workshop, DOI [10.1145/2501585.2501586](https://doi.org/10.1145/2501585.2501586), published; `A Quantitative Analysis of Developer Information Needs in Software Ecosystems`, Nicole Haenni et al., 2014, ECSA workshop, DOI [10.1145/2642803.2642815](https://doi.org/10.1145/2642803.2642815), published; `Two Decades of Empirical Research on Developers' Information Needs`, Abir Bouraffa and Walid Maalej, 2020, ICSE workshop, DOI [10.1145/3387940.3391485](https://doi.org/10.1145/3387940.3391485), published; and `Information Needs in Collocated Software Development Teams`, Amy J. Ko, Robert DeLine, and Gina Venolia, 2007, ICSE, DOI [10.1109/ICSE.2007.45](https://doi.org/10.1109/ICSE.2007.45), published.
- **Clearly irrelevant patterns:** Scientific-software package papers, health/research reporting, and generic developer uses dominated other records. `developer` is not a sufficient software-development qualifier.
- **Terminology discovered:** developer information needs, API-related information needs, information seeking, software ecosystems, collocated software development teams, relevant information, empirical classification, knowledge sources.
- **Candidate seed sources:** Mingwei Liu et al., `API-Related Developer Information Needs in Stack Overflow`, 2021, *IEEE Transactions on Software Engineering*, DOI [10.1109/TSE.2021.3120203](https://doi.org/10.1109/TSE.2021.3120203), published; Nicole Haenni et al., `Categorizing developer information needs in software ecosystems`, 2013, ACM workshop, DOI [10.1145/2501585.2501586](https://doi.org/10.1145/2501585.2501586), published; Nicole Haenni et al., `A Quantitative Analysis of Developer Information Needs in Software Ecosystems`, 2014, ECSA workshop, DOI [10.1145/2642803.2642815](https://doi.org/10.1145/2642803.2642815), published; Abir Bouraffa and Walid Maalej, `Two Decades of Empirical Research on Developers' Information Needs`, 2020, ICSE workshop, DOI [10.1145/3387940.3391485](https://doi.org/10.1145/3387940.3391485), published; Amy J. Ko, Robert DeLine, and Gina Venolia, `Information Needs in Collocated Software Development Teams`, 2007, ICSE, DOI [10.1109/ICSE.2007.45](https://doi.org/10.1109/ICSE.2007.45), published.
- **Query adjustment:** `developer information needs → 608,914 matches with identifiable software-information-needs literature but substantial scientific-software and reporting noise → test information seeking/information foraging/program comprehension with developer/programmer/software-engineer and maintenance/debugging/coding qualifiers`
- **Rationale:** `information sufficiency` did not appear as the strongest established label in this initial search. Developer information needs and information seeking provide a more established research neighborhood for whether available information supports software work.
- **Notes:** This branch concerns human developers and software teams; transfer to coding agents is not assumed.

### P7-F4B-02

- **Search ID:** `P7-F4B-02`
- **Date:** `2026-08-20`
- **Evidence stream:** Scientific discovery
- **Database / source:** OpenAlex Works API
- **Query:** `information seeking software developers`
- **Fields searched:** OpenAlex broad full-text search
- **Filters:** `per-page=10`; selected metadata and abstracts
- **Result count:** `194,775` reported by OpenAlex
- **Results inspected:** First-page records, abstracts where available, DOI and venue metadata
- **Clearly relevant results:** `An Exploratory Study of How Developers Seek, Relate, and Collect Relevant Information during Software Maintenance Tasks`, Andrew J. Ko, Brad A. Myers, Michael Coblenz, and Htet Htet Aung, 2006, *IEEE Transactions on Software Engineering*, DOI [10.1109/TSE.2006.116](https://doi.org/10.1109/TSE.2006.116), published; `Collaboration, Information Seeking and Communication: An Observational Study of Software Developers' Work Practices`, Márcio Kuroki Gonçalves, Víctor M. González, and Leidson R. B. de Souza, 2020, DOI [10.3217/jucs-017-14-1913](https://doi.org/10.3217/jucs-017-14-1913), OpenAlex submitted-version record, publication status requiring verification; and `Recommendation Systems for Software Engineering`, Martin P. Robillard, Robert J. Walker, and Thomas Zimmermann, 2009, *IEEE Software*, DOI [10.1109/MS.2009.161](https://doi.org/10.1109/MS.2009.161), published.
- **Clearly irrelevant patterns:** R, BEAST, PHENIX, MRtrix3, Open Babel, and other software-package papers; broader social or methodological papers were also retrieved.
- **Terminology discovered:** developer information seeking, information foraging, program comprehension, software maintenance tasks, relevant information, communication, recommendation systems for software engineering.
- **Candidate seed sources:** Andrew J. Ko, Brad A. Myers, Michael Coblenz, and Htet Htet Aung, `An Exploratory Study of How Developers Seek, Relate, and Collect Relevant Information during Software Maintenance Tasks`, 2006, *IEEE Transactions on Software Engineering*, DOI [10.1109/TSE.2006.116](https://doi.org/10.1109/TSE.2006.116), published; Márcio Kuroki Gonçalves, Víctor M. González, and Leidson R. B. de Souza, `Collaboration, Information Seeking and Communication: An Observational Study of Software Developers' Work Practices`, 2020, DOI [10.3217/jucs-017-14-1913](https://doi.org/10.3217/jucs-017-14-1913), submitted-version status in OpenAlex and not treated as established publication evidence; Martin P. Robillard, Robert J. Walker, and Thomas Zimmermann, `Recommendation Systems for Software Engineering`, 2009, *IEEE Software*, DOI [10.1109/MS.2009.161](https://doi.org/10.1109/MS.2009.161), published.
- **Query adjustment:** `developer information needs → information seeking software developers → 194,775 matches with a direct maintenance/program-comprehension neighborhood but persistent package-paper noise → retain information seeking, information foraging, program comprehension, and relevant information as separate candidate terms`
- **Rationale:** The revision produced a more actionable software-development information-needs neighborhood than the phrase `information sufficiency`. It does not establish that any amount or type of information is sufficient or optimal.
- **Notes:** F4-B has meaningful overlap with F3 issue/task descriptions and F6 context/clarification, but its object is the information need or seeking process rather than the work-unit representation or agent context-management mechanism.

### P7-F4C-01

- **Search ID:** `P7-F4C-01`
- **Date:** `2026-08-20`
- **Evidence stream:** Scientific discovery
- **Database / source:** OpenAlex Works API
- **Query:** `cognitive load software development`
- **Fields searched:** OpenAlex broad full-text search
- **Filters:** `per-page=10`; selected metadata and abstracts
- **Result count:** `326,198` reported by OpenAlex
- **Results inspected:** First-page records, abstracts where available, DOI and venue metadata
- **Clearly relevant results:** The sample exposed cognitive-load theory, collaborative cognitive load, mental effort, and software-design-process records, but most direct cognitive-load results were educational or general human-factors literature. `A field study of the software design process for large systems`, Bill Curtis, Herb Krasner, and Neil Iscoe, 1988, *Communications of the ACM*, DOI [10.1145/50087.50089](https://doi.org/10.1145/50087.50089), published, was a relevant adjacent software-development field study, not a direct cognitive-load experiment.
- **Clearly irrelevant patterns:** Neuroscience, child development, green-space research, educational programming, digital learning, and unrelated uses of `development` dominated the sample.
- **Terminology discovered:** cognitive load theory, intrinsic load, extraneous load, collaborative cognitive load, working memory, mental effort, instructional guidance, software design process.
- **Candidate seed sources:** Bill Curtis, Herb Krasner, and Neil Iscoe, `A field study of the software design process for large systems`, 1988, *Communications of the ACM*, DOI [10.1145/50087.50089](https://doi.org/10.1145/50087.50089), published, candidate only as an adjacent software-work context. No direct professional developer cognitive-load seed was promoted from this broad sample.
- **Query adjustment:** `cognitive load software development → 326,198 broad matches dominated by education, neuroscience, and unrelated development contexts → test mental workload/cognitive workload with programmer/developer/software-engineer and program-comprehension/programming/debugging/coding qualifiers`
- **Rationale:** The initial phrase is too broad and risks transferring educational cognitive-load concepts to professional software development without a professional developer population.
- **Notes:** Human cognitive load is distinct from computational, runtime, system, or model context load. Educational programming studies remain potentially useful for construct and measurement discovery but are not automatically professional-development evidence.

### P7-F4C-02

- **Search ID:** `P7-F4C-02`
- **Date:** `2026-08-20`
- **Evidence stream:** Scientific discovery
- **Database / source:** OpenAlex Works API
- **Query:** `mental workload programming`
- **Fields searched:** OpenAlex broad full-text search
- **Filters:** `per-page=10`; selected metadata and abstracts
- **Result count:** `184,829` reported by OpenAlex
- **Results inspected:** First-page records, abstracts where available, DOI and venue metadata
- **Clearly relevant results:** `Quantifying programmers' mental workload during program comprehension based on cerebral blood flow measurement: a controlled experiment`, Takao Nakagawa, Yasutaka Kamei, Hidetake Uwano, Akito Monden, Kenichi Matsumoto, and Daniel M. Germán, 2014, DOI [10.1145/2591062.2591098](https://doi.org/10.1145/2591062.2591098), published version, directly studies programmer mental workload during program comprehension. `State of science: mental workload in ergonomics`, Mark S. Young, Karel Brookhuis, Christopher D. Wickens, and Peter A. Hancock, 2014, *Ergonomics*, DOI [10.1080/00140139.2014.956151](https://doi.org/10.1080/00140139.2014.956151), published, is a measurement/concept review. `NASA TLX: Software for assessing subjective mental workload`, Alex Cao, Keshav Chintamani, Abhilash K. Pandya, and R. Darin Ellis, 2009, *Behavior Research Methods*, DOI [10.3758/brm.41.1.113](https://doi.org/10.3758/brm.41.1.113), published, is a measurement-instrument seed.
- **Clearly irrelevant patterns:** COVID-19 mental-health studies, driving workload, traffic monitoring, health-care workers, generic EEG/fNIRS papers, and education-staff studies were common.
- **Terminology discovered:** mental workload, cognitive workload, cognitive load, programmers' mental workload, program comprehension, subjective workload, NASA-TLX, physiological measures, cerebral blood flow.
- **Candidate seed sources:** Takao Nakagawa et al., `Quantifying programmers' mental workload during program comprehension based on cerebral blood flow measurement: a controlled experiment`, 2014, DOI [10.1145/2591062.2591098](https://doi.org/10.1145/2591062.2591098), published; Mark S. Young et al., `State of science: mental workload in ergonomics`, 2014, *Ergonomics*, DOI [10.1080/00140139.2014.956151](https://doi.org/10.1080/00140139.2014.956151), published; Alex Cao et al., `NASA TLX: Software for assessing subjective mental workload`, 2009, *Behavior Research Methods*, DOI [10.3758/brm.41.1.113](https://doi.org/10.3758/brm.41.1.113), published.
- **Query adjustment:** `cognitive load software development → broad education and neuroscience retrieval → mental workload programming → direct programmer program-comprehension experiment plus workload-measurement terminology → retain mental workload and program comprehension as primary calibration terms and cognitive load as a related construct requiring population screening`
- **Rationale:** The revised query found a coherent professional-programmer measurement neighborhood, but the evidence remains about human cognitive burden and cannot be inferred to coding-agent behavior.
- **Notes:** The sample does not resolve whether information volume, information structure, task complexity, or other factors produce the measured workload. That causal question remains open for later screening.

### P7-F4C-03

- **Search ID:** `P7-F4C-03`
- **Date:** `2026-08-20`
- **Evidence stream:** Scientific discovery
- **Database / source:** OpenAlex Works API
- **Query:** `information overload software engineering`
- **Fields searched:** OpenAlex broad full-text search
- **Filters:** `per-page=10`; selected metadata and abstracts
- **Result count:** `112,829` reported by OpenAlex
- **Results inspected:** First-page records, abstracts where available, DOI and venue metadata
- **Clearly relevant results:** `Structuring computer-mediated communication systems to avoid information overload`, 1985, *Communications of the ACM*, DOI [10.1145/3894.3895](https://doi.org/10.1145/3894.3895), published, directly concerns structuring communication systems to avoid overload. `Dealing with information overload: a comprehensive review`, 2023, *Frontiers in Psychology*, DOI [10.3389/fpsyg.2023.1122200](https://doi.org/10.3389/fpsyg.2023.1122200), published, is general information-overload background rather than software-engineering evidence. `ImageJ2: ImageJ for the next generation of scientific image data`, 2017, *BMC Bioinformatics*, DOI [10.1186/s12859-017-1934-z](https://doi.org/10.1186/s12859-017-1934-z), published, was adjacent because it discusses technical complexity and a developer community, not a direct overload study.
- **Clearly irrelevant patterns:** Information-systems theory, productivity paradox, software-defined networking, scientific software packages, and general information-overload psychology dominated the sample.
- **Terminology discovered:** information overload, computer-mediated communication, technical complexity, developer community, project documentation, awareness of changes, information-systems development.
- **Candidate seed sources:** `Structuring computer-mediated communication systems to avoid information overload`, 1985, *Communications of the ACM*, DOI [10.1145/3894.3895](https://doi.org/10.1145/3894.3895), published; retained as adjacent information-overload terminology, not as direct professional software-development evidence.
- **Query adjustment:** `information overload software engineering → 112,829 broad matches with one communication-systems record and extensive information-systems/package noise → test information overload software developers separately to check whether a developer-specific neighborhood is recoverable`
- **Rationale:** The explicit special question about information overload required a targeted calibration because the cognitive-load query did not distinguish overload from workload or educational load.
- **Notes:** The search did not establish a coherent software-engineering-specific information-overload corpus in the inspected sample.

### P7-F4C-04

- **Search ID:** `P7-F4C-04`
- **Date:** `2026-08-20`
- **Evidence stream:** Scientific discovery
- **Database / source:** OpenAlex Works API
- **Query:** `information overload software developers`
- **Fields searched:** OpenAlex broad full-text search
- **Filters:** `per-page=10`; selected metadata and abstracts
- **Result count:** `39,683` reported by OpenAlex
- **Results inspected:** First-page records, abstracts where available, DOI and venue metadata
- **Clearly relevant results:** `Awareness in the Wild: Why Communication Breakdowns Occur`, 2007, DOI [10.1109/ICGSE.2007.13](https://doi.org/10.1109/ICGSE.2007.13), published, concerns global software teams, communication breakdowns, and developers' awareness of implementation changes. `The user-developer communication process: a critical case study`, 2002, *Information Systems Journal*, DOI [10.1046/j.1365-2575.2003.00138.x](https://doi.org/10.1046/j.1046/j.1365-2575.2003.00138.x), published metadata record, was adjacent systems-development communication evidence. No inspected record directly measured information overload among professional software developers.
- **Clearly irrelevant patterns:** IT productivity, scientific software, simulation tools, networking/security, and distributed-network architecture dominated the sample.
- **Terminology discovered:** communication breakdowns, awareness of changes, global software teams, project documentation, user-developer communication, systems development.
- **Candidate seed sources:** `Awareness in the Wild: Why Communication Breakdowns Occur`, 2007, DOI [10.1109/ICGSE.2007.13](https://doi.org/10.1109/ICGSE.2007.13), published, retained as adjacent communication/context seed rather than information-overload evidence.
- **Query adjustment:** `information overload software engineering → broad information-systems and computing noise → information overload software developers → 39,683 matches but no direct overload study in the inspected sample → do not use information overload as a primary F4-C term without a later focused database search or snowballing from human-factors/communication seeds`
- **Rationale:** The second targeted check did not produce a developer-specific overload literature sufficient for primary retrieval. This is a calibration limitation, not evidence that information overload is absent.
- **Notes:** This search overlaps F3 descriptions/communication and F6 context/awareness. It should not be merged with mental workload without construct-level screening.

### P7-F4D-01

- **Search ID:** `P7-F4D-01`
- **Date:** `2026-08-20`
- **Evidence stream:** Scientific discovery
- **Database / source:** OpenAlex Works API
- **Query:** `documentation overhead software`
- **Fields searched:** OpenAlex broad full-text search
- **Filters:** `per-page=10`; selected metadata and abstracts
- **Result count:** `60,700` reported by OpenAlex
- **Results inspected:** First-page records, abstracts where available, DOI and venue metadata
- **Clearly relevant results:** `A Realistic Empirical Evaluation of the Costs and Benefits of UML in Software Maintenance`, W. J. Dzidek et al., 2008, *IEEE Transactions on Software Engineering*, DOI [10.1109/TSE.2008.15](https://doi.org/10.1109/TSE.2008.15), published, directly exposes cost/benefit language around documentation-like design artifacts. Scientific-software records also exposed documentation as part of software dissemination, but not documentation overhead as a measured construct.
- **Clearly irrelevant patterns:** R, MRtrix3, ProteoWizard, InterProScan, SciPy, PLINK, ITensor, Q-Chem, and other software-package papers dominated the top results. `documentation overhead` itself was not a stable title-level research label in this sample.
- **Terminology discovered:** documentation, software manuals, software framework/library, software maintenance, UML, costs and benefits, documentation usefulness.
- **Candidate seed sources:** W. J. Dzidek et al., `A Realistic Empirical Evaluation of the Costs and Benefits of UML in Software Maintenance`, 2008, *IEEE Transactions on Software Engineering*, DOI [10.1109/TSE.2008.15](https://doi.org/10.1109/TSE.2008.15), published.
- **Query adjustment:** `documentation overhead software → 60,700 broad package-description matches and no stable overhead terminology → test documentation effort/cost/maintenance with software-maintenance, developer, codebase, and legacy-software qualifiers`
- **Rationale:** The starting phrase did not retrieve a coherent documentation-burden literature. Cost, effort, relevance, usefulness, and maintenance are more plausible branches to test separately.
- **Notes:** No conclusion was drawn that documentation is beneficial or harmful.

### P7-F4D-02

- **Search ID:** `P7-F4D-02`
- **Date:** `2026-08-20`
- **Evidence stream:** Scientific discovery
- **Database / source:** OpenAlex Works API
- **Query:** `documentation effort software maintenance`
- **Fields searched:** OpenAlex broad full-text search
- **Filters:** `per-page=10`; selected metadata and abstracts
- **Result count:** `136,114` reported by OpenAlex
- **Results inspected:** First-page records, abstracts where available, DOI and venue metadata
- **Clearly relevant results:** `The relevance of software documentation, tools and technologies`, Andrew Forward and Timothy C. Lethbridge, 2002, DOI [10.1145/585058.585065](https://doi.org/10.1145/585058.585065), published; `Characteristics of application software maintenance`, Bennet P. Lientz, E. Burton Swanson, and Gerry Edward Tompkins, 1978, *Communications of the ACM*, DOI [10.1145/359511.359522](https://doi.org/10.1145/359511.359522), published; `A field study of the software design process for large systems`, Bill Curtis, Herb Krasner, and Neil Iscoe, 1988, *Communications of the ACM*, DOI [10.1145/50087.50089](https://doi.org/10.1145/50087.50089), published; and `A survey of software refactoring`, Tom Mens and Tom Tourwé, 2004, *IEEE Transactions on Software Engineering*, DOI [10.1109/TSE.2004.1265817](https://doi.org/10.1109/TSE.2004.1265817), published, exposed documentation relevance, maintenance, legacy-code, and change-cost vocabulary.
- **Clearly irrelevant patterns:** Quantum ESPRESSO, Bioconductor, Perseus, scientific software-package descriptions, case-study guidelines, and review-methodology records remained prominent. The query did not isolate documentation effort as a single outcome.
- **Terminology discovered:** software documentation, documentation relevance, documentation tools and technologies, documentation maintenance, application software maintenance, legacy software, maintenance effort, refactoring, costs and benefits.
- **Candidate seed sources:** Andrew Forward and Timothy C. Lethbridge, `The relevance of software documentation, tools and technologies`, 2002, DOI [10.1145/585058.585065](https://doi.org/10.1145/585058.585065), published; Bennet P. Lientz, E. Burton Swanson, and Gerry Edward Tompkins, `Characteristics of application software maintenance`, 1978, *Communications of the ACM*, DOI [10.1145/359511.359522](https://doi.org/10.1145/359511.359522), published; Tom Mens and Tom Tourwé, `A survey of software refactoring`, 2004, *IEEE Transactions on Software Engineering*, DOI [10.1109/TSE.2004.1265817](https://doi.org/10.1109/TSE.2004.1265817), published; Bill Curtis, Herb Krasner, and Neil Iscoe, `A field study of the software design process for large systems`, 1988, *Communications of the ACM*, DOI [10.1145/50087.50089](https://doi.org/10.1145/50087.50089), published.
- **Query adjustment:** `documentation overhead software → documentation effort software maintenance → 136,114 broad matches with stronger documentation-relevance and maintenance vocabulary but continued package-paper noise → retain documentation relevance/usefulness, maintenance, effort/cost, and costs/benefits as separate branches`
- **Rationale:** `documentation effort` and `documentation maintenance` are more useful discovery terms than `documentation overhead`, but the revised search still requires fielded database searching and source-level screening.
- **Notes:** The source sample does not establish a general documentation cost/benefit direction or an overhead threshold.

## Query Evolution Records: Pilot Round 7

- `requirements ambiguity → 831,451 OpenAlex broad full-text matches containing a recognizable requirements-ambiguity neighborhood plus linguistic and non-software noise → requirements completeness software → test completeness, traceability, coverage, and quality terminology separately → distinguish requirements ambiguity from completeness and quality rather than treating them as synonyms` (`P7-F4A-01`, `P7-F4A-02`; OpenAlex).
- `developer information needs → 608,914 broad matches with direct developer-information-needs papers plus scientific-software noise → information seeking software developers → test information seeking, information foraging, program comprehension, and relevant-information terms → use information-needs/seeking terminology rather than assuming information sufficiency is established` (`P7-F4B-01`, `P7-F4B-02`; OpenAlex).
- `cognitive load software development → 326,198 matches dominated by education, neuroscience, and unrelated development uses → mental workload programming → isolate a professional-programmer program-comprehension experiment and workload measurement vocabulary → distinguish human mental workload from educational cognitive load and runtime/computational load` (`P7-F4C-01`, `P7-F4C-02`; OpenAlex).
- `information overload software engineering → 112,829 broad information-systems/computing matches with one adjacent communication-systems seed → information overload software developers → 39,683 matches with communication/awareness material but no direct overload study in the inspected sample → do not make information overload a primary term without further focused calibration` (`P7-F4C-03`, `P7-F4C-04`; OpenAlex).
- `documentation overhead software → 60,700 matches dominated by software-package descriptions → documentation effort software maintenance → 136,114 matches with documentation relevance, maintenance, and cost/benefit vocabulary → test documentation relevance/usefulness, effort/cost, and maintenance as separate branches rather than treating overhead as established terminology` (`P7-F4D-01`, `P7-F4D-02`; OpenAlex).

No query was removed because it returned contradictory material. Terms were downgraded because of noise or construct mismatch, not because they failed to support an interpretation.

## Terminology Registry Updates From Pilot Round 7

The registry was updated only for terms discovered or materially recalibrated in this round. These are search labels, not Work Item characteristics.

| Term or phrase | Action | Calibration note |
|---|---|---|
| requirements ambiguity | retain as primary F4-A term | Coherent requirements-engineering literature; qualify against natural-language and non-software ambiguity. |
| ambiguity identification and measurement | retain as contextual term | Useful for operationalization discovery in requirements literature; not equivalent to execution ambiguity. |
| requirements completeness | test provisionally | Retrieved completeness/quality work, but broad full-text noise was high. |
| requirements traceability completeness | retain as contextual term | More specific and measurable terminology than generic information sufficiency. |
| requirements coverage | test provisionally | Related to completeness but not interchangeable; requires separate screening. |
| requirements quality / quality assessment | retain as contextual term | Established quality-assurance neighborhood; overlaps F2. |
| information sufficiency | downgrade; test only with software-development qualifier | Not the strongest phrase in inspected software-engineering records; use developer information needs and information seeking instead. |
| developer information needs | retain as primary F4-B term | Direct software-engineering and ecosystem literature was identifiable. |
| information seeking | retain as primary F4-B term | Direct developer-maintenance and team-work studies were found. |
| information foraging | test provisionally | Related developer-information tradition; needs software-development qualification. |
| program comprehension | retain as contextual term | Connects information needs and mental workload; not equivalent to information sufficiency. |
| missing context | test with software-development qualifier | No direct F4 search was needed after information-needs results; retain as a contextual phrase and do not assume it is established terminology. |
| cognitive load | split from information overload; retain as a related term with population screening | P8 confirms a professional-programmer mental-workload branch, while broad cognitive-load retrieval remains measurement- and population-sensitive. |
| mental workload / cognitive workload | retain as primary F4-C measurement terms | Programmer program-comprehension experiment and measurement literature were retrieved. |
| NASA-TLX / subjective workload | retain as measurement terms | Measurement vocabulary, not a software-work property. |
| information overload | exclude as primary F4-C term; retain as supplementary discovery/context term | P8's developer-qualified search remained extremely noisy and did not retrieve a direct professional software-development overload study in the inspected sample. |
| documentation overhead | exclude as primary search term | Initial search was dominated by package-description papers and did not establish a stable term. |
| documentation effort / documentation cost | test provisionally | More productive cost/effort wording, but not a homogeneous literature. |
| documentation relevance / usefulness | retain as primary F4-D terms | P8 title-restricted retrieval was relatively clean and exposed documentation relevance, quality, usefulness, task navigation, and "how much is enough" terminology. |
| documentation maintenance | retain as primary F4-D contextual term | Connects documentation with software maintenance and legacy-code work. |
| costs and benefits of UML/documentation | investigate separately | Useful artifact-cost framing; not interchangeable with documentation burden. |

## F4 Calibration Assessment

The labels below are search-method labels only. They do not classify any Work Item characteristic.

### F4-A: Ambiguity, Clarity, Completeness, And Information Quality

- **Conceptual coherence:** High for requirements ambiguity, completeness, traceability, coverage, and quality assessment, but these are related constructs rather than one measure. Ambiguity detection/measurement is a recognizable requirements-engineering tradition.
- **Retrieval coherence:** Moderate. Exact requirements phrases retrieve a useful neighborhood, while broad `clarity`, `quality`, `software`, and completeness full-text searches produce package, linguistic, regulatory, and general-quality noise.
- **Software-development relevance:** High for requirements/specification studies; lower for generic language ambiguity and non-software requirements.
- **Overlap:** Strong with F2 requirements, specifications, user stories, and acceptance criteria. The distinction for F4 is the information-quality property or measurement problem, not another artifact inventory. Some issue-description and quality studies also overlap F3 and F1.
- **Search status:** `Primary`

### F4-B: Information Sufficiency And Context

- **Conceptual coherence:** Moderate to high after recalibration toward developer information needs, information seeking, information foraging, and program comprehension. `Information sufficiency` itself was not established as the dominant phrase.
- **Retrieval coherence:** Moderate. Developer qualifiers improve relevance, but software-package and scientific-software records remain common. Maintenance-task and developer-information-needs phrases provide more inspectable retrieval neighborhoods.
- **Software-development relevance:** High for the inspected Ko, Haenni, Bouraffa/Maalej, API-needs, and team-information sources; directness varies by maintenance, ecosystem, API, and team setting.
- **Overlap:** Moderate with F3 issue/task descriptions and F6 context management, clarification, and repository understanding. F4-B should focus on information needs/seeking/comprehension rather than agent context mechanisms.
- **Search status:** `Primary`

### F4-C: Cognitive Load And Information Overload

- **Conceptual coherence:** Split. Mental workload/cognitive workload and program comprehension form a recognizable human-factors/software-development branch. Information overload is broader and was not coherent as a professional software-engineering construct in the inspected samples.
- **Retrieval coherence:** Moderate for `mental workload` plus programmer/program-comprehension qualifiers; poor for broad `cognitive load` and `information overload` searches.
- **Software-development relevance:** Direct professional-programmer evidence was found for mental workload during program comprehension. Educational programming and general HCI evidence require separate population labels. Direct professional developer evidence for information overload was not identified in this pilot sample.
- **Overlap:** Moderate with F3 task complexity/description work and F6 context management; strong conceptual separation is needed from computational/runtime load and coding-agent context load.
- **Search status:** `Requires further calibration` for the combined subgroup; `Primary` for a mental-workload/program-comprehension branch and `Supplementary` for information overload.

### F4-D: Documentation Cost, Overhead, And Information Volume

- **Conceptual coherence:** Moderate only after replacing `documentation overhead` with documentation relevance/usefulness, documentation effort/cost, documentation maintenance, and artifact cost/benefit branches. The original overhead phrase was not established by the inspected sample.
- **Retrieval coherence:** Low to moderate. Documentation effort/maintenance searches expose relevant software-maintenance literature but remain dominated by scientific software-package descriptions and general maintenance work.
- **Software-development relevance:** Moderate. Forward/Lethbridge and UML maintenance cost/benefit work are relevant; many retrieved papers treat documentation as part of distributing scientific software rather than as a developer-work information burden.
- **Overlap:** Strong with F2 documentation/requirements artifacts and moderate with F1/F3 work descriptions and task representations. The F4 distinction is cost, usefulness, maintenance, or information-volume treatment, not artifact presence alone.
- **Search status:** `Supplementary`

## Candidate Seed Source Summary

The following candidates were inspected sufficiently for F4 terminology/venue relevance. They are not yet included evidence and no findings are synthesized here.

| Source | Year and status | DOI or stable URL | Search ID | F4 relevance |
|---|---:|---|---|---|
| Bano, `Addressing the challenges of requirements ambiguity: A review of empirical literature` | 2015, published IEEE EmpiRE proceedings | [10.1109/empire.2015.7431303](https://doi.org/10.1109/empire.2015.7431303) | `P7-F4A-01` | Requirements-ambiguity review and terminology seed. |
| Berry and Kamsties, `Ambiguity in Requirements Specification` | 2004, published book chapter | [10.1007/978-1-4615-0465-8_2](https://doi.org/10.1007/978-1-4615-0465-8_2) | `P7-F4A-01` | Requirements-specification ambiguity framing. |
| Chantree et al., `Identifying Nocuous Ambiguities in Natural Language Requirements` | 2006, published IEEE RE paper | [10.1109/re.2006.31](https://doi.org/10.1109/re.2006.31) | `P7-F4A-01` | Ambiguity taxonomy/detection terminology. |
| Kiyavitskaya et al., `Requirements for tools for ambiguity identification and measurement in natural language requirements specifications` | 2008, published *Requirements Engineering* article | [10.1007/s00766-008-0063-7](https://doi.org/10.1007/s00766-008-0063-7) | `P7-F4A-01` | Measurement and tool-requirement terminology. |
| Rempel and Mader, `Preventing Defects: The Impact of Requirements Traceability Completeness on Software Quality` | 2016, published *IEEE TSE* article | [10.1109/TSE.2016.2622264](https://doi.org/10.1109/TSE.2016.2622264) | `P7-F4A-02` | Completeness/traceability quality branch. |
| Liu et al., `API-Related Developer Information Needs in Stack Overflow` | 2021, published *IEEE TSE* article | [10.1109/TSE.2021.3120203](https://doi.org/10.1109/TSE.2021.3120203) | `P7-F4B-01` | Developer information-needs classification in a software ecosystem. |
| Bouraffa and Maalej, `Two Decades of Empirical Research on Developers' Information Needs` | 2020, published ICSE workshop paper | [10.1145/3387940.3391485](https://doi.org/10.1145/3387940.3391485) | `P7-F4B-01` | Mapping/review seed for developer information-needs terminology. |
| Ko et al., `Information Needs in Collocated Software Development Teams` | 2007, published ICSE paper | [10.1109/ICSE.2007.45](https://doi.org/10.1109/ICSE.2007.45) | `P7-F4B-01` | Team information needs and software-development context. |
| Ko et al., `An Exploratory Study of How Developers Seek, Relate, and Collect Relevant Information during Software Maintenance Tasks` | 2006, published *IEEE TSE* article | [10.1109/TSE.2006.116](https://doi.org/10.1109/TSE.2006.116) | `P7-F4B-02` | Information seeking during maintenance tasks. |
| Nakagawa et al., `Quantifying programmers' mental workload during program comprehension based on cerebral blood flow measurement: a controlled experiment` | 2014, published version | [10.1145/2591062.2591098](https://doi.org/10.1145/2591062.2591098) | `P7-F4C-02` | Direct professional-programmer workload measurement. |
| Young et al., `State of science: mental workload in ergonomics` | 2014, published *Ergonomics* review | [10.1080/00140139.2014.956151](https://doi.org/10.1080/00140139.2014.956151) | `P7-F4C-02` | Workload construct and measurement background. |
| Cao et al., `NASA TLX: Software for assessing subjective mental workload` | 2009, published *Behavior Research Methods* article | [10.3758/brm.41.1.113](https://doi.org/10.3758/brm.41.1.113) | `P7-F4C-02` | Measurement-instrument terminology. |
| `Structuring computer-mediated communication systems to avoid information overload` | 1985, published *Communications of the ACM* article | [10.1145/3894.3895](https://doi.org/10.1145/3894.3895) | `P7-F4C-03` | Adjacent information-overload/communication-system terminology; not direct developer evidence. |
| Forward and Lethbridge, `The relevance of software documentation, tools and technologies` | 2002, published version | [10.1145/585058.585065](https://doi.org/10.1145/585058.585065) | `P7-F4D-02` | Documentation relevance/usefulness branch. |
| Dzidek et al., `A Realistic Empirical Evaluation of the Costs and Benefits of UML in Software Maintenance` | 2008, published *IEEE TSE* article | [10.1109/TSE.2008.15](https://doi.org/10.1109/TSE.2008.15) | `P7-F4D-01` | Artifact cost/benefit and maintenance branch. |
| Lientz, Swanson, and Tompkins, `Characteristics of application software maintenance` | 1978, published *Communications of the ACM* article | [10.1145/359511.359522](https://doi.org/10.1145/359511.359522) | `P7-F4D-02` | Maintenance context for documentation effort/cost searches. |

## Overlap With Previous Families

- **F2:** F4-A ambiguity, completeness, traceability, coverage, and requirements quality are heavily represented in requirements/specification literature already encountered in F2. F4 should not duplicate artifact searches; it should search the quality, ambiguity, completeness, and measurement constructs applied to those artifacts.
- **F3:** Developer information seeking, program comprehension, issue descriptions, communication breakdowns, and task context overlap F3 descriptions and execution. The object distinction is information need/seeking or cognitive burden versus decomposition or description structure.
- **F1:** Issue-description and software-task studies can include textual quality, completeness, or success measures. Those sources should be cross-listed when the information-quality property is central, while preserving F1's work-unit object and F4's information-quality object.
- **F6 boundary:** Information seeking and awareness may connect to context management or clarification, but F6 was not searched in this round and no F6 conclusion is made.
- **F7 boundary:** No verification, completion, rework, or task-success searches were executed in this round.

## Database And Access Limitations

- Only OpenAlex was used for this round's searches. IEEE Xplore, ACM Digital Library, Scopus, Web of Science, ScienceDirect, SpringerLink, arXiv, and Google Scholar were not systematically searched in Round 7.
- OpenAlex broad full-text counts were extremely large and are not comparable across queries or databases. Counts must not be interpreted as prevalence, precision, recall, or field maturity.
- Metadata often exposed DOI, venue, publication year, and version status, but abstracts were unavailable for some older records. Full-text inspection was not completed for candidate seeds.
- Publisher pages and DOI targets were not independently opened for every candidate. Publication statuses recorded here are based on the inspected OpenAlex metadata and must be verified during later screening.
- Crossref was not used for broad discovery because previous rounds documented unfielded-count noise and rate limits; DOI links were retained for later publication verification.
- The inspected samples were first-page discovery samples, not exhaustive relevance samples. No snowballing was performed in Round 7.

## Special Calibration Questions

1. **Is `information sufficiency` useful terminology, or does the literature use other concepts?** The inspected software-engineering retrieval did not establish `information sufficiency` as the dominant term. More productive discovered terms were `developer information needs`, `information seeking`, `information foraging`, `relevant information`, `program comprehension`, and task/maintenance context. `Information sufficiency` should remain a provisional, software-development-qualified term rather than the primary term.
2. **Is `missing context` an established research term or mainly informal wording?** Round 7 did not execute a dedicated `missing context` search. It was not established by the inspected samples as a dominant F4-B label. Retain it for a focused, software-development-qualified test, but treat it as provisional and investigate through information-needs, program-comprehension, repository-understanding, and clarification terminology.
3. **Does `cognitive load` yield relevant professional software-development literature?** Broad `cognitive load` retrieval was education- and neuroscience-heavy. A revised `mental workload programming` search identified a direct professional-programmer program-comprehension experiment and workload-measurement literature. Therefore, relevant professional literature is retrievable, but `mental workload`/`cognitive workload` plus programmer/program-comprehension qualifiers are more reliable than unqualified `cognitive load`.
4. **Is `information overload` studied meaningfully in software engineering?** The inspected samples did not reveal a coherent professional software-engineering information-overload corpus. They yielded adjacent computer-mediated communication, awareness, documentation, information-systems, and general overload literature. The term is useful for a supplementary human-factors/communication branch, not currently a primary software-engineering search term.
5. **Is `documentation overhead` useful terminology, or are concepts such as documentation effort/cost/maintenance more established?** `Documentation overhead` produced package-description noise and no stable direct literature in the sample. `Documentation relevance`, `documentation usefulness`, `documentation maintenance`, `documentation effort`, `documentation cost`, and software-maintenance costs/benefits were more useful discovered terms. These should remain separate branches because they may denote different constructs.
6. **Does F4 need to remain split into multiple subfamilies for systematic-search design?** Yes. F4-A and F4-B are distinct requirements-quality and developer-information-needs traditions. F4-C must split mental workload/program comprehension from information overload, and F4-D should split documentation relevance/usefulness from effort/cost/maintenance. A single F4 query would combine incompatible populations, outcomes, and noise sources.

## Recommended Search Status

| Subgroup | Status | Methodological reason |
|---|---|---|
| F4-A | `Primary` | Coherent requirements ambiguity/completeness/quality traditions with manageable phrase-level branches after qualification, despite F2 overlap. |
| F4-B | `Primary` | Developer information-needs/seeking/program-comprehension literature is identifiable, while `information sufficiency` remains secondary terminology. |
| F4-C | `Requires further calibration` | Mental workload is promising and information overload is weak/noisy; the provisional combined subgroup should be split before systematic design. |
| F4-D | `Supplementary` | Documentation relevance/maintenance/cost traditions are relevant but heterogeneous, and `documentation overhead` is not established as a primary term. |

## Remaining Uncertainty

- Whether requirements ambiguity/completeness measures transfer from requirements artifacts to smaller issue/task descriptions remains unresolved.
- Whether developer information-needs studies operationalize having enough information, or instead study seeking behavior, source selection, or comprehension, requires full-text extraction.
- The causal relationship among information amount, information structure, task complexity, and human workload was not tested in this calibration round.
- The boundary between information overload, communication breakdown, documentation maintenance, and context-navigation effort remains unsettled.
- Professional software-development populations are underrepresented in the broad cognitive-load and information-overload retrieval samples.
- Coding-agent-specific evidence was not sought in F4 Round 7; transfer from human software-development studies remains an open methodological question.
- Database coverage, field syntax, later versions, duplicate publications, and full-text access need verification in the systematic-search phase.

## F4 Exit Decision

**F4 should be split into distinct search subfamilies before systematic-search design**

The methodological reason is that the pilot found multiple recognizable but non-equivalent traditions rather than one retrievable information-quality corpus: requirements ambiguity/completeness, developer information needs and seeking, programmer mental workload/program comprehension, information overload/communication, and documentation relevance/effort/maintenance. Splitting these branches is necessary to preserve construct, population, object, outcome, and evidence-stream distinctions and to prevent broad retrieval noise from determining the search space.

No Work Item characteristics or research conclusions were derived. Round 7 did not establish that less information, more information, additional context, documentation, or any particular amount or quality of information is preferable. F6 and F7 were not executed. No systematic search strings were frozen, and no commit was made.

## Pilot Round 5 Family 3 Focused Calibration

Round 5 tested Family 3 as separate conceptual subgroups rather than one combined OR query: decomposition, task preparation and descriptions, granularity, dependency/interdependence and allocation, and crowdsourcing software development. Counts are source-reported diagnostics, not relevance estimates. Known-item status is recorded against the inspected sample: `Retrieved` means the named seed appeared in the retrieved records, `Missed` means it was not retrieved by the tested query, and `Not verified` means the available sample or field behavior did not establish its status.

### P5-F3-01

- **Search ID:** `P5-F3-01`
- **Date:** `2026-08-20`
- **Evidence stream:** Scientific discovery
- **Database / source:** arXiv API
- **Query:** `ti:"task decomposition" AND ti:"software development"`
- **Fields searched:** arXiv title fields
- **Filters:** None; first 10 sorted by relevance
- **Result count:** `1` reported by arXiv
- **Results inspected:** The single returned record and abstract
- **Clearly relevant results:** `Tasks Decomposition Approaches in Crowdsourcing Software Development` was retrieved and directly concerns decomposing software projects, preparing tasks, and reviewing submissions in a crowdsourcing setting.
- **Clearly irrelevant patterns:** None in the single-record sample.
- **Terminology discovered:** tasks decomposition approaches, software project decomposition, preparing tasks, manageable tasks
- **Candidate seed sources:** Abdullah Khanfor, `Tasks Decomposition Approaches in Crowdsourcing Software Development`, 2023, arXiv preprint, DOI [10.48550/arxiv.2302.05099](https://doi.org/10.48550/arxiv.2302.05099); retrieved and abstract inspected. Known seeds: Khanfor `Retrieved`; Stol and Fitzgerald `Missed`; Treude and Storey `Missed`.
- **Query adjustment:** `all:"task decomposition" AND all:"software development" → five mixed records in P4 → ti:"task decomposition" AND ti:"software development" → one direct software-development seed → use title-only as a high-precision known-item check, not as a recall-complete query`
- **Rationale:** The qualifier materially reduced noise and retrieved the direct F3 seed, but its narrowness risks missing work that uses different title terminology.
- **Notes:** arXiv endpoint: [P5-F3-01](https://export.arxiv.org/api/query?search_query=ti:%22task%20decomposition%22%20AND%20ti:%22software%20development%22&start=0&max_results=10&sortBy=relevance). `Tasks Decomposition` plural wording was matched by the source's title search semantics; this was not treated as a terminology equivalence conclusion.

### P5-F3-02

- **Search ID:** `P5-F3-02`
- **Date:** `2026-08-20`
- **Evidence stream:** Scientific discovery
- **Database / source:** arXiv API
- **Query:** `all:"task preparation" AND all:software`
- **Fields searched:** arXiv `all` fields
- **Filters:** None; first 10 sorted by relevance
- **Result count:** `2` reported by arXiv
- **Results inspected:** Both records and abstracts
- **Clearly relevant results:** None. The query returned IoT dataset task preparation and Android task automation, not preparation of software-development work.
- **Clearly irrelevant patterns:** Multisensory learning-task preparation and mobile task automation dominated the complete result set.
- **Terminology discovered:** task preparation as a general task-execution/automation phrase; no reusable software-work term established. Known seeds: Khanfor `Missed` (abstract uses `preparing tasks`, not the exact phrase); Stol and Fitzgerald `Missed`; Treude and Storey `Missed`.
- **Candidate seed sources:** None.
- **Query adjustment:** `"task preparation" AND software → two non-F3 records → do not expand the phrase as a primary F3 synonym; test source-specific wording such as "preparing tasks" only through decomposition/crowdsourcing contexts`
- **Rationale:** A small result set here represented domain mismatch, not calibrated precision.
- **Notes:** The result count is not evidence that the phrase is absent from software-engineering literature outside arXiv.

### P5-F3-03

- **Search ID:** `P5-F3-03`
- **Date:** `2026-08-20`
- **Evidence stream:** Scientific discovery
- **Database / source:** arXiv API
- **Query:** `all:"software development task" AND all:planning`
- **Fields searched:** arXiv `all` fields
- **Filters:** None; first 10 sorted by relevance
- **Result count:** `6` reported by arXiv
- **Results inspected:** All six records and abstracts
- **Clearly relevant results:** The sample contained software-development-agent planning and coding-plan generation, including `Human-In-the-Loop Software Development Agents`, which describes engineers guiding coding plans for software tasks. This is coding-agent-specific planning terminology, not traditional decomposition evidence.
- **Clearly irrelevant patterns:** Agent architectures, bug fixing, repository automation, generic software-task evaluation, and issue-resolution systems appeared with the planning term.
- **Terminology discovered:** coding plans, planning for future actions, multi-stage software development, issue-to-source-code workflow
- **Candidate seed sources:** Wannita Takerngsaksiri et al., `Human-In-the-Loop Software Development Agents`, 2024 arXiv preprint, arXiv [2411.12924](https://arxiv.org/abs/2411.12924), record and abstract inspected; candidate because it explicitly studies coding-plan generation for software-development tasks. Known seeds: Khanfor `Missed`; Stol and Fitzgerald `Not verified`; Treude and Storey `Missed`.
- **Query adjustment:** `"software development task" AND planning → six mixed software-task and agent-planning records → retain only as a separate planning/agent subfamily and do not use planning as a decomposition synonym`
- **Rationale:** Planning connects to F3, but the inspected literature used it for agent workflow or project activity rather than necessarily dividing development work.
- **Notes:** This record is coding-agent-specific scientific discovery and must remain separate from traditional software-engineering evidence during later screening.

### P5-F3-04

- **Search ID:** `P5-F3-04`
- **Date:** `2026-08-20`
- **Evidence stream:** Scientific discovery
- **Database / source:** arXiv API
- **Query:** `all:"software development task" AND all:description`
- **Fields searched:** arXiv `all` fields
- **Filters:** None; first 10 sorted by relevance
- **Result count:** `8` reported by arXiv
- **Results inspected:** All eight records and abstracts
- **Clearly relevant results:** `Descriptions of issues and comments for predicting issue success in software projects` directly studies textual descriptions of software tasks in issue-tracking systems. This confirms `issue descriptions` as a more established representation phrase than the generic `task description` in this sample.
- **Clearly irrelevant patterns:** API documentation, LLM code-task descriptions, automotive software, adversarial prompts, and code-understanding benchmarks appeared alongside issue-description research.
- **Terminology discovered:** textual descriptions of issues, issue descriptions and comments, issue-tracking systems, task descriptions as natural-language inputs
- **Candidate seed sources:** Sandra L. Ramírez-Mora, Hanna Oktaba, and Helena Gómez-Adorno, `Descriptions of issues and comments for predicting issue success in software projects`, 2020, *Journal of Systems and Software* 168, DOI [10.1016/j.jss.2020.110663](https://doi.org/10.1016/j.jss.2020.110663); arXiv record, abstract, journal reference, and DOI inspected. This is a representation/description seed, not a direct decomposition seed. Known seeds: Khanfor `Missed`; Stol and Fitzgerald `Missed`; Treude and Storey `Missed`.
- **Query adjustment:** `"software development task" AND description → eight mixed records → retain "issue description"/"issue descriptions and comments" as the higher-yield representation branch and keep generic "task description" contextual`
- **Rationale:** The search found relevant work-definition representations, but the term `description` also retrieves documentation and AI input studies.
- **Notes:** The source was already a Family 1 candidate; it is cross-listed here only for F3 description calibration.

### P5-F3-05

- **Search ID:** `P5-F3-05`
- **Date:** `2026-08-20`
- **Evidence stream:** Scientific discovery
- **Database / source:** arXiv API
- **Query:** `all:"task granularity" AND all:"software development"`
- **Fields searched:** arXiv `all` fields
- **Filters:** None; first 10 sorted by relevance
- **Result count:** `0` reported by arXiv
- **Results inspected:** No records
- **Clearly relevant results:** None; no direct software-development work-granularity record was retrieved.
- **Clearly irrelevant patterns:** No records were returned, so no sample-level noise could be assessed.
- **Terminology discovered:** None beyond prior `task granularity` and `fine-grained tasks` observations. Known seeds: Khanfor `Missed`; Stol and Fitzgerald `Missed`; Treude and Storey `Missed`.
- **Candidate seed sources:** None.
- **Query adjustment:** `all:"task granularity" AND all:software → five runtime/HPC-oriented records in P4 → all:"task granularity" AND all:"software development" → zero records → do not interpret zero as absence and do not retain as a primary F3 query without another qualifier`
- **Rationale:** The added qualifier removed the known runtime noise but also produced no inspectable software-development sample.
- **Notes:** Zero retrieval is a database/query diagnostic only.

### P5-F3-06

- **Search ID:** `P5-F3-06`
- **Date:** `2026-08-20`
- **Evidence stream:** Scientific discovery
- **Database / source:** arXiv API
- **Query:** `all:"software task" AND all:granularity`
- **Fields searched:** arXiv `all` fields
- **Filters:** None; first 10 sorted by relevance
- **Result count:** `0` reported by arXiv
- **Results inspected:** No records
- **Clearly relevant results:** None.
- **Clearly irrelevant patterns:** No records were returned; the query did not reproduce P4's runtime sample.
- **Terminology discovered:** None. Known seeds: Khanfor `Missed`; Stol and Fitzgerald `Missed`; Treude and Storey `Missed`.
- **Candidate seed sources:** None.
- **Query adjustment:** `all:"software task" AND granularity → zero records → retain granularity only as a separately investigated concept and avoid treating the zero as evidence of terminology absence`
- **Rationale:** The phrase did not yield a useful software-development task-size sample in arXiv.
- **Notes:** The query's narrowness and arXiv coverage are limitations.

### P5-F3-07

- **Search ID:** `P5-F3-07`
- **Date:** `2026-08-20`
- **Evidence stream:** Scientific discovery
- **Database / source:** arXiv API
- **Query:** `all:"task dependency" AND all:"software development"`
- **Fields searched:** arXiv `all` fields
- **Filters:** None; first 10 sorted by relevance
- **Result count:** `3` reported by arXiv
- **Results inspected:** All three records and abstracts
- **Clearly relevant results:** `DependEval` concerns repository dependency understanding, project structure, repository construction, and multi-file editing, but not decomposition of development work. No direct task-dependency study was found.
- **Clearly irrelevant patterns:** Repository/code dependency benchmarking, agentic bug localization, and dialogue-system task dependency dominated the sample.
- **Terminology discovered:** repository dependency understanding, repository construction, multi-file editing; these are code/repository dependency terms, not confirmed work-decomposition terms. Known seeds: Khanfor `Missed`; Stol and Fitzgerald `Missed`; Treude and Storey `Missed`.
- **Candidate seed sources:** None promoted; `DependEval` was inspected as a boundary/noise example rather than an F3 seed.
- **Query adjustment:** `"task dependency" AND "software development" → three records dominated by repository or dialogue dependencies → keep dependency out of broad F3 searches unless paired with task decomposition, planning, or work-allocation context`
- **Rationale:** The qualifier did not distinguish dependencies between development tasks from dependencies in software artifacts or AI task systems.
- **Notes:** No inference was made about whether task dependencies matter for a Work Item.

### P5-F3-08

- **Search ID:** `P5-F3-08`
- **Date:** `2026-08-20`
- **Evidence stream:** Scientific discovery
- **Database / source:** arXiv API
- **Query:** `all:"task interdependence" AND all:software`
- **Fields searched:** arXiv `all` fields
- **Filters:** None; first 10 sorted by relevance
- **Result count:** `3` reported by arXiv
- **Results inspected:** All three records and abstracts
- **Clearly relevant results:** `Perceptions of Task Interdependence in Software Development: An Industrial Case Study` directly studies technical and allocation-based dependencies between tasks in a software team. The term belongs to a work-design/team-organization tradition rather than a pure decomposition tradition.
- **Clearly irrelevant patterns:** Psychological safety, diversity, and team-performance studies used task interdependence as a work-design construct.
- **Terminology discovered:** task interdependence, technical dependencies between components, task allocation in teamwork, work design factor
- **Candidate seed sources:** Mayara Benício de Barros Souza, Fabio Q. B. da Silva, and Carolyn Seaman, `Perceptions of Task Interdependence in Software Development: An Industrial Case Study`, 2023, arXiv preprint, [arXiv:2304.09849](https://arxiv.org/abs/2304.09849); record and abstract inspected. Candidate because it explicitly defines and studies interdependence among software-development tasks. Known seeds: Khanfor `Missed`; Stol and Fitzgerald `Missed`; Treude and Storey `Missed`.
- **Query adjustment:** `task dependency → repository/dialogue dependency noise → task interdependence AND software → three records with one direct software-team study → retain as a contextual work-structure branch, not a decomposition synonym`
- **Rationale:** `task interdependence` is more productive than `task dependency` for finding software-team work-structure research, but it may concern allocation and team perceptions rather than task creation.
- **Notes:** This is traditional software-engineering/team research; transfer to coding agents is not assumed.

### P5-F3-09

- **Search ID:** `P5-F3-09`
- **Date:** `2026-08-20`
- **Evidence stream:** Scientific discovery
- **Database / source:** arXiv API
- **Query:** `all:"task allocation" AND all:"software development"`
- **Fields searched:** arXiv `all` fields
- **Filters:** None; first 10 sorted by relevance
- **Result count:** `9` reported by arXiv
- **Results inspected:** First 9 records and abstracts
- **Clearly relevant results:** The sample contained global software-development task allocation, distributed development, Scrum-based allocation, and role-based allocation. `A Survey on the State of the Practice in Distributed Software Development: Criteria for Task Allocation` provides a clearly software-engineering-specific allocation vocabulary.
- **Clearly irrelevant patterns:** General author-task allocation and non-software task allocation appeared at the end of the result set, but software-development context was strong in the inspected records.
- **Terminology discovered:** global software development, distributed software development, task distribution, work allocation, task allocation criteria, role-based task allocation
- **Candidate seed sources:** Ansgar Lamersdorf, Jürgen Münch, and Dieter Rombach, `A Survey on the State of the Practice in Distributed Software Development: Criteria for Task Allocation`, 2009, IEEE ICGSE, pp. 41–50, DOI [10.1109/ICGSE.2009.12](https://doi.org/10.1109/ICGSE.2009.12); arXiv record, abstract, Crossref metadata, and DOI inspected. Ansgar Lamersdorf, Jürgen Münch, and Dieter Rombach, `A Decision Model for Supporting Task Allocation Processes in Global Software Development`, 2009, Springer, pp. 332–346, DOI [10.1007/978-3-642-02152-7_25](https://doi.org/10.1007/978-3-642-02152-7_25); arXiv record, abstract, and Crossref metadata inspected. Known seeds: Khanfor `Missed`; Stol and Fitzgerald `Not verified`; Treude and Storey `Missed`.
- **Query adjustment:** `task allocation AND software development → nine records with a coherent global/distributed software-development allocation branch → retain as a separate allocation subfamily and do not equate allocation with decomposition`
- **Rationale:** Allocation retrieves software-engineering work, but it generally concerns assigning existing work to people/sites/roles rather than forming subtasks.
- **Notes:** These are candidate seeds for later screening, not evidence for any preferred work organization.

### P5-F3-10

- **Search ID:** `P5-F3-10`
- **Date:** `2026-08-20`
- **Evidence stream:** Scientific discovery
- **Database / source:** arXiv API
- **Query:** `all:"crowdsourcing software development" AND all:task`
- **Fields searched:** arXiv `all` fields
- **Filters:** None; first 10 sorted by relevance
- **Result count:** `7` reported by arXiv
- **Results inspected:** All seven records and abstracts
- **Clearly relevant results:** The sample covered decomposition, task scheduling, task failure, task life cycles, and parallel task upload in crowdsourced software development. `Impact of Task Cycle Pattern on Project Success in Software Crowdsourcing` explicitly uses terminology about decomposing and uploading parallel tasks.
- **Clearly irrelevant patterns:** Scheduling, market dynamics, worker selection, and task-failure prediction dominated several records; these are process/market contexts rather than task-boundary terminology.
- **Terminology discovered:** task life cycle, task cycle pattern, parallel tasks, task scheduling, task failure, task arrival, decomposing and uploading tasks
- **Candidate seed sources:** Razieh Saremi, Marzieh Lotfalian Saremi, Sanam Jena, Robert Anzalone, and Ahmed Bahabry, `Impact of Task Cycle Pattern on Project Success in Software Crowdsourcing`, 2021, HCI 2021, [arXiv:2103.10355](https://arxiv.org/abs/2103.10355); record and abstract inspected. Razieh Lotfalian Saremi and Ye Yang, `Empirical Analysis on Parallel Tasks in Crowdsourcing Software Development`, 2015, IEEE/ACM ASE Workshop, pp. 28–34, DOI [10.1109/asew.2015.22](https://doi.org/10.1109/asew.2015.22); OpenAlex title/metadata and Crossref metadata inspected. Known seeds: Khanfor `Retrieved`; Stol and Fitzgerald `Missed` in the arXiv sample; Treude and Storey `Missed`.
- **Query adjustment:** `crowdsourcing software development AND task → seven records across decomposition, scheduling, lifecycle, and worker-market topics → retain crowdsourcing as a source/domain qualifier and split decomposition from scheduling/failure branches`
- **Rationale:** Crowdsourcing produced the most coherent traditional F3 neighborhood, but its task concepts are tightly coupled to external-worker allocation and marketplace operations.
- **Notes:** Findings from crowdsourcing are not generalized to coding agents in this calibration round.

### P5-F3-11

- **Search ID:** `P5-F3-11`
- **Date:** `2026-08-20`
- **Evidence stream:** Scientific discovery
- **Database / source:** OpenAlex Works API
- **Query:** `title.search:"task decomposition"`
- **Fields searched:** OpenAlex title search
- **Filters:** `per-page=10`; selected metadata fields
- **Result count:** `612` reported by OpenAlex
- **Results inspected:** First 10 titles and metadata records
- **Clearly relevant results:** No direct software-development decomposition record appeared in the inspected first page; the query is useful as a noise baseline.
- **Clearly irrelevant patterns:** Cognitive science, multi-agent AI, dialogue systems, neural networks, reinforcement learning, and general decision-making dominated.
- **Terminology discovered:** No new F3-specific term. Known seeds: Khanfor `Not verified`; Stol and Fitzgerald `Missed`; Treude and Storey `Missed` in the inspected sample.
- **Candidate seed sources:** None.
- **Query adjustment:** `OpenAlex title task decomposition → 612 records dominated by non-software domains → require software-development/crowdsourcing title context and use exact-title known-item checks`
- **Rationale:** Title restriction alone did not make generic decomposition software-specific.
- **Notes:** OpenAlex title counts are not comparable with arXiv and are not relevance estimates.

### P5-F3-12

- **Search ID:** `P5-F3-12`
- **Date:** `2026-08-20`
- **Evidence stream:** Scientific discovery
- **Database / source:** OpenAlex Works API
- **Query:** `title.search:"task interdependence"`
- **Fields searched:** OpenAlex title search
- **Filters:** `per-page=10`; selected metadata fields
- **Result count:** `374` reported by OpenAlex
- **Results inspected:** First 10 titles and metadata records
- **Clearly relevant results:** The inspected records established a broad work-design and organizational-behavior tradition; the arXiv software-development industrial case was not present in the first page.
- **Clearly irrelevant patterns:** Team performance, job design, knowledge sharing, psychological safety, and organizational behavior dominated.
- **Terminology discovered:** No new software-specific term beyond `task interdependence` and work design. Known seeds: Khanfor `Missed`; Stol and Fitzgerald `Missed`; Treude and Storey `Missed`; Barros Souza et al. `Not verified` in the inspected first page.
- **Candidate seed sources:** None new.
- **Query adjustment:** `arXiv task interdependence AND software → direct software-team record → OpenAlex title task interdependence → broad work-design corpus → retain OpenAlex only for separate contextual expansion`
- **Rationale:** The fielded source difference shows that software qualifiers are essential for this term.
- **Notes:** OpenAlex did not provide an interpretable software-specific count through this title query.

### P5-F3-13

- **Search ID:** `P5-F3-13`
- **Date:** `2026-08-20`
- **Evidence stream:** Scientific discovery
- **Database / source:** OpenAlex Works API
- **Query:** `title.search:"task allocation"`
- **Fields searched:** OpenAlex title search
- **Filters:** `per-page=10`; selected metadata fields
- **Result count:** `5,944` reported by OpenAlex
- **Results inspected:** First 10 titles and metadata records
- **Clearly relevant results:** None in the inspected first page; prior arXiv retrieval demonstrates that adding `software development` is necessary to expose the global software-development allocation branch.
- **Clearly irrelevant patterns:** Robotics, distributed computing, mobile edge computing, and multi-agent systems dominated.
- **Terminology discovered:** No new F3-specific term. Known seeds: Khanfor `Missed`; Stol and Fitzgerald `Missed`; Treude and Storey `Missed`; Lamersdorf et al. `Not verified` in the inspected first page.
- **Candidate seed sources:** None new.
- **Query adjustment:** `OpenAlex title task allocation → 5,944 records dominated by robotics/computing → use software-development qualifier and venue/context restrictions rather than generic task-allocation title searches`
- **Rationale:** `task allocation` is productive only when explicitly tied to software development, global software development, or crowdsourcing.
- **Notes:** Count is a discovery diagnostic only.

### P5-F3-14

- **Search ID:** `P5-F3-14`
- **Date:** `2026-08-20`
- **Evidence stream:** Scientific discovery
- **Database / source:** OpenAlex Works API
- **Query:** `title.search:"crowdsourcing software development"`
- **Fields searched:** OpenAlex title search
- **Filters:** `per-page=10`; selected metadata fields
- **Result count:** `27` reported by OpenAlex
- **Results inspected:** First 10 titles and metadata records; Crossref metadata was retrieved for selected candidates
- **Clearly relevant results:** The first page contained software-crowdsourcing research, including Stol and Fitzgerald's ICSE paper, parallel tasks, project-description length, task selection, and project/task success.
- **Clearly irrelevant patterns:** The result set was substantially more coherent than generic decomposition or allocation searches, though it still included broad crowdsourcing concerns and worker-selection studies.
- **Terminology discovered:** project description length, expected duration, task selection, parallel tasks in crowdsourcing software development, competition-based crowdsourcing software development
- **Candidate seed sources:** Klaas-Jan Stol and Brian Fitzgerald, `Two's company, three's a crowd: a case study of crowdsourcing software development`, 2014, ICSE, DOI [10.1145/2568225.2568249](https://doi.org/10.1145/2568225.2568249); OpenAlex and Crossref metadata inspected, publisher page access returned HTTP 429. Razieh Lotfalian Saremi and Ye Yang, `Empirical Analysis on Parallel Tasks in Crowdsourcing Software Development`, 2015, IEEE/ACM ASEW, DOI [10.1109/asew.2015.22](https://doi.org/10.1109/asew.2015.22); title, OpenAlex metadata, Crossref metadata, and venue metadata inspected. David Gefen, Gavriel Gefen, and Erran Carmel, `How project description length and expected duration affect bidding and project success in crowdsourcing software development`, 2016, *Journal of Systems and Software* 116, 75–84, DOI [10.1016/j.jss.2015.03.039](https://doi.org/10.1016/j.jss.2015.03.039); title, OpenAlex metadata, and Crossref metadata inspected because it directly exposes project-description terminology.
- **Query adjustment:** `OpenAlex title task decomposition/all-field crowdsourcing searches → mixed or noisy results → title.search:"crowdsourcing software development" → 27-record coherent domain corpus → retain as a domain-qualified subfamily for later screening`
- **Rationale:** The domain phrase materially improves conceptual coherence, while still requiring separation of decomposition, allocation, scheduling, and marketplace outcomes.
- **Notes:** Known seeds: Stol and Fitzgerald `Retrieved`; Khanfor `Not verified` from the first OpenAlex page because its title does not contain the exact crowdsourcing phrase; Treude and Storey `Missed`.

### P5-F3-15

- **Search ID:** `P5-F3-15`
- **Date:** `2026-08-20`
- **Evidence stream:** Scientific discovery
- **Database / source:** OpenAlex Works API
- **Query:** `title.search:"task preparation"`
- **Fields searched:** OpenAlex title search
- **Filters:** `per-page=10`; selected metadata fields
- **Result count:** `99` reported by OpenAlex
- **Results inspected:** First 10 titles and metadata records
- **Clearly relevant results:** None. The title corpus was not software-development task preparation.
- **Clearly irrelevant patterns:** Cognitive neuroscience, task switching, executive function, and motor preparation dominated.
- **Terminology discovered:** No reusable software-development terminology. Known seeds: Khanfor `Missed`; Stol and Fitzgerald `Missed`; Treude and Storey `Missed`.
- **Candidate seed sources:** None.
- **Query adjustment:** `arXiv task preparation AND software → two automation/AI records → OpenAlex title task preparation → 99 neuroscience/psychology records → downgrade task preparation to source-specific wording rather than a primary F3 term`
- **Rationale:** Both source checks indicate that the exact phrase is not a reliable standalone software-work search term.
- **Notes:** OpenAlex count is not a relevance estimate.

Round 5 did not freeze a systematic search string. It supports splitting F3 into distinct search subfamilies: software-project decomposition/crowdsourcing; software-development task descriptions/issues; planning and coding-agent task workflows; allocation/interdependence; and a separately investigated granularity branch. `task preparation` and unqualified `task granularity` should not be primary terms without stronger source-specific evidence.

### Round 5 Query Evolution Records

- **Date:** `2026-08-20`
- **Search family:** Family 3 decomposition
- **Original query:** `all:"task decomposition" AND all:"software development"`
- **Observation:** Five records were software-development-related but mixed traditional crowdsourcing decomposition with agent architecture and software-agent surveys.
- **Revised query:** `ti:"task decomposition" AND ti:"software development"`
- **Rationale:** Use title restriction for a precise known-item check while preserving the broader query for sensitivity.
- **Affected database(s):** arXiv
- **Search IDs:** `P4-F3-03`, `P5-F3-01`

- **Date:** `2026-08-20`
- **Search family:** Family 3 task preparation
- **Original query:** `all:"task preparation" AND all:software`
- **Observation:** Two results concerned IoT dataset preparation and Android task automation; no software-development work preparation was found.
- **Revised query:** retain `task preparation` only as a source-specific phrase and test `preparing tasks` within decomposition/crowdsourcing contexts
- **Rationale:** Exact phrase is not reusable enough for a primary F3 search term.
- **Affected database(s):** arXiv and OpenAlex
- **Search IDs:** `P5-F3-02`, `P5-F3-15`

- **Date:** `2026-08-20`
- **Search family:** Family 3 planning and descriptions
- **Original query:** `"software development task"`
- **Observation:** Planning and description qualifiers produced different literatures: coding plans/agent workflows versus issue descriptions and comments.
- **Revised query:** keep `"software development task" AND planning` and `"software development task" AND description` as separate branches
- **Rationale:** Do not combine planning and textual representation terms when their inspected samples address different objects.
- **Affected database(s):** arXiv
- **Search IDs:** `P5-F3-03`, `P5-F3-04`

- **Date:** `2026-08-20`
- **Search family:** Family 3 granularity
- **Original query:** `all:"task granularity" AND all:software`
- **Observation:** P4 returned runtime/HPC and parallel-computing literature; adding `software development` returned zero records.
- **Revised query:** `all:"task granularity" AND all:"software development"` and `all:"software task" AND all:granularity`
- **Rationale:** Test whether development context recovers relevant work without runtime noise; preserve both zero-result variants.
- **Affected database(s):** arXiv
- **Search IDs:** `P4-F3-04`, `P5-F3-05`, `P5-F3-06`

- **Date:** `2026-08-20`
- **Search family:** Family 3 dependency/allocation
- **Original query:** `"task dependency" AND "software development"`
- **Observation:** Three results mixed repository dependencies, agentic localization, and dialogue-system task dependency.
- **Revised query:** `"task interdependence" AND software`; separately test `"task allocation" AND "software development"`
- **Rationale:** Interdependence retrieved a direct software-team work-design study, while allocation retrieved a distinct global/distributed software-development tradition; neither should be collapsed into decomposition.
- **Affected database(s):** arXiv
- **Search IDs:** `P5-F3-07`, `P5-F3-08`, `P5-F3-09`

- **Date:** `2026-08-20`
- **Search family:** Family 3 crowdsourcing
- **Original query:** `"crowdsourcing software development" AND task`
- **Observation:** Seven records covered decomposition, lifecycle, parallel tasks, scheduling, worker selection, and task failure.
- **Revised query:** `title.search:"crowdsourcing software development"`
- **Rationale:** A domain-qualified title search produced a manageable 27-record corpus for later subgroup screening; it must still be split by decomposition, allocation, scheduling, and marketplace concepts.
- **Affected database(s):** arXiv and OpenAlex
- **Search IDs:** `P5-F3-10`, `P5-F3-14`

- **Date:** `2026-08-20`
- **Search family:** Family 3 field calibration
- **Original query:** `title.search:"task decomposition"`, `title.search:"task interdependence"`, and `title.search:"task allocation"`
- **Observation:** OpenAlex title searches returned 612, 374, and 5,944 records respectively, with generic AI/organizational/robotics noise; title.search for crowdsourcing software development returned 27 and was substantially more coherent.
- **Revised query:** use explicit software-development, global-software-development, or crowdsourcing-software-development qualifiers and venue/context filters
- **Rationale:** Field restriction alone does not resolve ambiguous terminology; domain qualifiers are necessary for later source-specific designs.
- **Affected database(s):** OpenAlex
- **Search IDs:** `P5-F3-11`, `P5-F3-12`, `P5-F3-13`, `P5-F3-14`

### Round 5 Calibration Assessment

- **Decomposition terminology:** A coherent but narrow software-specific vocabulary is available around `task decomposition approaches`, `software project decomposition`, `preparing tasks`, and `crowdsourcing software development`. The direct title-qualified arXiv check retrieved Khanfor, while generic decomposition remained dominated by AI and other domains. This supports a distinct decomposition subfamily, not one combined F3 string.
- **Granularity terminology:** `task granularity` remains too contaminated by runtime/HPC/parallel-computing meanings. Adding `software development` produced zero arXiv records and `software task AND granularity` also produced zero; it should not be a primary term until another source or qualifier establishes a usable development-work corpus.
- **Task preparation terminology:** `task preparation` was not reusable in the tested sources. It retrieved neuroscience and task-automation material; `preparing tasks` appeared naturally in the Khanfor source but was not independently validated as a field-wide term.
- **Dependency/allocation terminology:** `task interdependence` retrieved a direct software-team study but belongs primarily to work-design/team-organization research. `task allocation` retrieved a coherent global/distributed software-development branch. Both should remain contextual or separate subfamilies rather than being treated as decomposition synonyms.
- **Crowdsourcing literature:** This tradition provides the most useful F3 domain qualifier and exposes decomposition, preparing tasks, parallel tasks, task lifecycle, scheduling, allocation, and project-description terminology. Its marketplace and external-worker setting must remain explicit during later screening; no transfer to coding agents was inferred.
- **Final methodological status:** `F3 should be split into distinct search subfamilies before systematic-search design`
- **Reason:** Decomposition, task descriptions/issues, planning/coding-agent workflows, allocation/interdependence, and crowdsourcing work form distinguishable retrieval neighborhoods. Granularity and exact task-preparation wording are not currently reliable primary terms, while generic decomposition/allocation searches retain major cross-domain noise.

## Pilot Round 6 Family 3 Subfamily Calibration

Round 6 tested three provisional F3 subfamilies: F3-A, software-project decomposition and planning; F3-B, software-development task descriptions and issue representations; and F3-C, allocation, interdependence, and crowdsourced software work. The purpose was to test whether the split improves interpretability, not to freeze systematic strings or infer Work Item characteristics. Counts are source-reported diagnostics, not relevance estimates. Seed status is recorded per subfamily and per inspected sample.

### F3-A: Decomposition And Planning

#### Search Entry

- **Search ID:** `P6-F3A-01`
- **Date:** `2026-08-20`
- **Evidence stream:** `traditional software engineering and coding-agent terminology`
- **Database / source:** `arXiv`
- **Query:** `all:"task decomposition" AND all:"software development"`
- **Fields searched:** `all`
- **Filters:** `none`
- **Result count:** `5`
- **Results inspected:** `5` titles and metadata/abstract records
- **Clearly relevant results:** Khanfor's `Tasks Decomposition Approaches in Crowdsourcing Software Development`; adjacent coding-agent and software-agent records using decomposition as an architectural or planning term.
- **Clearly irrelevant patterns:** General agent architecture/surveys and non-traditional software-task uses of decomposition.
- **Terminology discovered:** `task decomposition approaches`, `software project decomposition`, `task decomposition and collaboration`, and `requirement-driven task decomposition` remain distinct traditional-SE versus coding-agent contexts.
- **Candidate seed sources:** Khanfor `Retrieved`; Zeng et al. `Retrieved` as a coding-agent contextual seed; Stol and Fitzgerald `Missed`; Treude and Storey `Missed`.
- **Query adjustment:** Retain as the sensitivity-oriented F3-A variant; do not treat the mixed sample as one homogeneous decomposition literature.
- **Rationale:** The query recovers a direct traditional-SE seed but also exposes a separate agent-planning neighborhood, supporting a shared subfamily with explicit context branches.
- **Notes:** The count is not a precision estimate. Decomposition in coding-agent papers may describe system architecture rather than human or project work decomposition.

#### Search Entry

- **Search ID:** `P6-F3A-02`
- **Date:** `2026-08-20`
- **Evidence stream:** `known-item/title precision check`
- **Database / source:** `arXiv`
- **Query:** `ti:"task decomposition" AND ti:"software development"`
- **Fields searched:** `title`
- **Filters:** `none`
- **Result count:** `1`
- **Results inspected:** `1` title and abstract record
- **Clearly relevant results:** Khanfor's crowdsourcing software-development decomposition paper.
- **Clearly irrelevant patterns:** None in the one-record sample.
- **Terminology discovered:** No new term; title restriction confirms the narrow phrase `task decomposition approaches in crowdsourcing software development`.
- **Candidate seed sources:** Khanfor `Retrieved`; Zeng et al. `Missed` under this title-restricted variant; Stol and Fitzgerald `Missed`; Treude and Storey `Missed`.
- **Query adjustment:** Keep as a narrow title/known-item diagnostic, not as the systematic F3-A query.
- **Rationale:** Title restriction improves precision for the direct seed but would miss coding-agent planning literature and other relevant records whose titles use different decomposition terminology.
- **Notes:** The result count is not a recall estimate.

### F3-B: Task Descriptions And Issue Representations

#### Search Entry

- **Search ID:** `P6-F3B-01`
- **Date:** `2026-08-20`
- **Evidence stream:** `issue-tracking and software-work representation`
- **Database / source:** `arXiv`
- **Query:** `all:"issue description" AND all:"software project"`
- **Fields searched:** `all`
- **Filters:** `none`
- **Result count:** `7`
- **Results inspected:** `7` titles and metadata/abstract records
- **Clearly relevant results:** Issue-description, issue-assignment, and software-project records; the sample supports a textual representation/management neighborhood distinct from decomposition.
- **Clearly irrelevant patterns:** Some generic project-management and issue-classification material without a work-description focus.
- **Terminology discovered:** `issue description`, `issue descriptions`, `issue comments`, `issue success`, and `software project`.
- **Candidate seed sources:** Ramírez-Mora et al. `Not verified` in the inspected seven-record sample; Khanfor `Not applicable to this subfamily`; Stol and Fitzgerald `Not applicable to this subfamily`; Treude and Storey `Not applicable to this subfamily`.
- **Query adjustment:** Retain singular/plural issue-description variants with software-project or issue-tracking context; do not import decomposition terms into F3-B.
- **Rationale:** The query is more specific to the representation of software work than generic `task description`, while still requiring screening for issue-management outcomes versus description content.
- **Notes:** Exact bibliographic known-item verification was not established from this seven-record sample; prior metadata inspection confirms Ramírez-Mora et al. as the principal F3-B seed.

#### Search Entry

- **Search ID:** `P6-F3B-02`
- **Date:** `2026-08-20`
- **Evidence stream:** `exact-phrase failure check`
- **Database / source:** `arXiv`
- **Query:** `all:"issue descriptions and comments"`
- **Fields searched:** `all`
- **Filters:** `none`
- **Result count:** `0`
- **Results inspected:** `0`
- **Clearly relevant results:** None.
- **Clearly irrelevant patterns:** None.
- **Terminology discovered:** The exact plural phrase is not reliable arXiv-indexed terminology even though it occurs in the Ramírez-Mora et al. title.
- **Candidate seed sources:** Ramírez-Mora et al. `Missed`; Khanfor `Not applicable to this subfamily`; Stol and Fitzgerald `Not applicable to this subfamily`; Treude and Storey `Not applicable to this subfamily`.
- **Query adjustment:** Use component terms such as `issue description`, `issue comments`, and software-project/issue-tracking context rather than this exact phrase.
- **Rationale:** The zero-result check documents a database/indexing limitation and prevents the title phrase from being treated as a stable systematic synonym.
- **Notes:** A zero result does not establish absence of the literature.

### F3-C: Allocation, Interdependence, And Crowdsourced Work

#### Search Entry

- **Search ID:** `P6-F3C-01`
- **Date:** `2026-08-20`
- **Evidence stream:** `crowdsourced software work and coordination`
- **Database / source:** `arXiv`
- **Query:** `all:"crowdsourcing software development" AND all:task`
- **Fields searched:** `all`
- **Filters:** `none`
- **Result count:** `7`
- **Results inspected:** `7` titles and metadata/abstract records
- **Clearly relevant results:** Crowdsourced decomposition, task scheduling, task failure, task life cycle, parallel-task upload, and task-allocation records.
- **Clearly irrelevant patterns:** Little obvious domain noise in the sample, but the records vary between decomposition, marketplace operations, scheduling, and external-worker coordination.
- **Terminology discovered:** `task allocation`, `task scheduling`, `task life cycle`, `task cycle pattern`, `parallel tasks`, and `project description length`.
- **Candidate seed sources:** Khanfor `Retrieved`; Saremi et al. `Retrieved`; Saremi and Yang `Retrieved`; Stol and Fitzgerald `Missed` in the arXiv sample; Treude and Storey `Missed`; Lamersdorf et al. `Not applicable to this subfamily's crowdsourcing branch`.
- **Query adjustment:** Retain crowdsourcing as a domain-qualified supplementary branch and screen decomposition, allocation, scheduling, and marketplace studies separately.
- **Rationale:** This is the most coherent traditional-SE F3 neighborhood tested, but its work-unit concepts are tightly coupled to external-worker and marketplace conditions.
- **Notes:** Coherence does not justify transferring findings or terminology to coding-agent work.

#### Search Entry

- **Search ID:** `P6-F3C-02`
- **Date:** `2026-08-20`
- **Evidence stream:** `domain-qualified title discovery`
- **Database / source:** `OpenAlex`
- **Query:** `title.search:"crowdsourcing software development"`
- **Fields searched:** `title`
- **Filters:** `none`
- **Result count:** `27`
- **Results inspected:** First-page title/metadata records, including known crowdsourcing, parallel-task, and project-description sources
- **Clearly relevant results:** Stol and Fitzgerald's crowdsourcing case study; Saremi and Yang's parallel-task study; project-description and task-success studies.
- **Clearly irrelevant patterns:** The corpus remains heterogeneous across marketplace, scheduling, worker selection, project success, and decomposition.
- **Terminology discovered:** No new primary term; title-qualified crowdsourcing is a useful discovery boundary, not a decomposition synonym.
- **Candidate seed sources:** Stol and Fitzgerald `Retrieved`; Saremi and Yang `Retrieved`; Khanfor `Not verified` from the inspected first-page sample; Treude and Storey `Missed`; Lamersdorf et al. `Not applicable to this crowdsourcing branch`.
- **Query adjustment:** Keep as a supplementary discovery corpus for backward/forward snowballing, with explicit subtopic screening.
- **Rationale:** The manageable corpus confirms coverage of the crowdsourcing tradition but does not resolve whether allocation and decomposition belong in one systematic F3 branch.
- **Notes:** OpenAlex title counts are not relevance or recall estimates; publisher access for some records remained limited by HTTP 429.

### Round 6 Query Evolution Records

- **Date:** `2026-08-20`
- **Search family:** `F3-A decomposition and planning`
- **Original query:** `all:"task decomposition" AND all:"software development"`
- **Observation:** The five-record sample combined a direct crowdsourcing decomposition source with coding-agent architecture/planning sources.
- **Revised query:** `ti:"task decomposition" AND ti:"software development"`
- **Rationale:** Use title restriction only as a narrow known-item precision check; preserve the broader query and separate traditional-SE and coding-agent contexts during screening.
- **Affected database(s):** `arXiv`
- **Search IDs:** `P6-F3A-01`, `P6-F3A-02`

- **Date:** `2026-08-20`
- **Search family:** `F3-B task descriptions and issue representations`
- **Original query:** `all:"issue description" AND all:"software project"`
- **Observation:** The seven-record sample supported issue-description/project literature, while the exact known title phrase was not established as an indexed phrase.
- **Revised query:** `all:"issue descriptions and comments"`
- **Rationale:** Test the title phrase directly, then retain component terms after the zero-result failure rather than treating the phrase as a systematic synonym.
- **Affected database(s):** `arXiv`
- **Search IDs:** `P6-F3B-01`, `P6-F3B-02`

- **Date:** `2026-08-20`
- **Search family:** `F3-C crowdsourced software work`
- **Original query:** `all:"crowdsourcing software development" AND all:task`
- **Observation:** The seven-record sample was coherent but heterogeneous across decomposition, allocation, scheduling, lifecycle, and marketplace operations.
- **Revised query:** `title.search:"crowdsourcing software development"`
- **Rationale:** Bound a manageable discovery corpus for screening and snowballing, while classifying allocation and decomposition separately and retaining the branch as supplementary.
- **Affected database(s):** `arXiv` and `OpenAlex`
- **Search IDs:** `P6-F3C-01`, `P6-F3C-02`

### Round 6 Calibration Assessment

- **F3-A status:** `Primary`. The split preserves a direct traditional-SE decomposition branch and a distinct coding-agent planning branch without conflating their units of analysis.
- **F3-B status:** `Primary`. Issue descriptions/comments form a separate work-representation branch, although the exact title phrase is not a reliable indexed query.
- **F3-C status:** `Supplementary`. The crowdsourcing corpus is coherent enough for discovery and snowballing, but allocation, scheduling, marketplace, and external-worker conditions are not interchangeable with decomposition or coding-agent work.
- **Overlap assessment:** F3-A and F3-C overlap where crowdsourcing papers discuss decomposition and parallel tasks; F3-B overlaps Family 1 and Family 2 through issue/work labels and requirements-like text. These are screening overlaps, not grounds for one combined F3 query.
- **Terminology update:** Promote no new unqualified synonym. Retain `task decomposition`, `software project decomposition`, `coding plans`, `issue description`, `issue comments`, and domain-qualified `crowdsourcing software development` as provisional branches; keep `task preparation` and `task granularity` downgraded or excluded as previously recorded.
- **Final methodological status:** `F3 subfamily structure sufficiently calibrated for systematic-search design`
- **Reason:** The six checks produced interpretable, non-identical retrieval neighborhoods and documented their overlaps, seed limitations, and source-specific terminology. This permits systematic-search design without freezing final strings or asserting Work Item support.

### Round 4 Query Evolution Records

- **Date:** `2026-08-20`
- **Search family:** Family 2
- **Original query:** `all:"software requirements" OR all:"requirements specification" OR all:"user story" OR all:"acceptance criteria" OR all:"task description"`
- **Observation:** `1,782` results mixed SRS documents, requirements engineering, user stories, acceptance testing, domain-specific material, and generic task-description contexts.
- **Revised query:** `ti:"software requirements" OR ti:"requirements specification" OR ti:"user story" OR ti:"acceptance criteria" OR ti:"task description"`
- **Rationale:** Compare title-only precision signal with all-field sensitivity; do not treat the reduced count as a relevance estimate.
- **Affected database(s):** arXiv
- **Search IDs:** `P4-F2-01`, `P4-F2-02`

- **Date:** `2026-08-20`
- **Search family:** Family 2
- **Original query:** `all:"acceptance criteria"`
- **Observation:** Acceptance language was expected to include general user acceptance, cost estimation, and non-software domains.
- **Revised query:** `all:"acceptance criteria" AND all:"software engineering"`
- **Rationale:** Add a software-engineering context term while preserving the observed residual noise; use this as a separate acceptance-criteria calibration family.
- **Affected database(s):** arXiv
- **Search IDs:** `P4-F2-03`

- **Date:** `2026-08-20`
- **Search family:** Family 2
- **Original query:** `all:"user story"`
- **Observation:** User-story results include agile requirements, user-story quality, NLP, education, domain-specific stories, and planning/estimation.
- **Revised query:** `all:"user story" AND all:"software engineering"`
- **Rationale:** Retain the established agile requirements tradition while documenting that user stories are not one homogeneous artifact or research question.
- **Affected database(s):** arXiv
- **Search IDs:** `P4-F2-04`

- **Date:** `2026-08-20`
- **Search family:** Family 2
- **Original query:** artifact-name phrases only
- **Observation:** OpenAlex discovery repeatedly exposed a separate requirements quality, assurance, and validation literature that artifact-name searches could miss.
- **Revised query:** `"requirements quality" software`
- **Rationale:** Test quality/structure terminology separately rather than adding `quality` as an unqualified synonym for requirements or specifications.
- **Affected database(s):** OpenAlex
- **Search IDs:** `P4-F2-05`

- **Date:** `2026-08-20`
- **Search family:** Family 3
- **Original query:** `all:"task decomposition" OR all:"work decomposition" OR all:"task breakdown" OR all:"software development task" OR all:"task description"`
- **Observation:** `1,011` results were dominated by general AI, robotics, reinforcement learning, annotation, and task-evaluation literature.
- **Revised query:** `all:"task decomposition" AND all:"software development"`
- **Rationale:** Require a software-development context and screen agent-architecture results separately from traditional software-work decomposition.
- **Affected database(s):** arXiv
- **Search IDs:** `P4-F3-01`, `P4-F3-03`

- **Date:** `2026-08-20`
- **Search family:** Family 3
- **Original query:** `task size/granularity terms treated as possible decomposition synonyms`
- **Observation:** `all:"task granularity" AND all:"software"` returned five records centered on HPC, parallel execution, scheduling, and runtime profiling.
- **Revised query:** retain `task granularity` only with explicit software-development planning/decomposition terms; exclude it from broad searches
- **Rationale:** The phrase is ambiguous between development-work size and execution/runtime granularity; the pilot provided no direct evidence that it commonly denotes the former.
- **Affected database(s):** arXiv
- **Search IDs:** `P4-F3-04`

- **Date:** `2026-08-20`
- **Search family:** Family 3
- **Original query:** `"task decomposition" software`
- **Observation:** OpenAlex reported `6,164` full-text matches with major AI, robotics, compiler, and HPC noise.
- **Revised query:** `"software task decomposition"`
- **Rationale:** Exact phrase retrieval reduced the OpenAlex set to five records and retained the direct crowdsourcing software-development seed, but OpenAlex full-text semantics still prevent interpreting the count as precision.
- **Affected database(s):** OpenAlex
- **Search IDs:** `P4-F3-05`, `P4-F3-06`

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
| software requirements specification (SRS) | requirements/specification artifact | P4-F2-01, P4-F2-02 | Requirements engineering | test with field restrictions | Recurring artifact phrase; distinguish the document from individual requirements and from user stories. |
| requirements specification document | requirements/specification artifact | P4-F2-02 | Requirements engineering | test provisionally | Title-only results used document wording; retain separately from generic `specification`. |
| natural-language requirements | requirements representation | P4-F2-02, P4-F2-05 | Requirements engineering | test provisionally | Appeared in requirements quality and specification contexts; may retrieve linguistic-quality studies. |
| requirements artifact | requirements representation | P4-F2-01, P4-F2-02 | Requirements engineering | retain as contextual term | Umbrella wording in studies comparing user stories, personas, and other representations; not a synonym for each artifact. |
| acceptance testing criteria | acceptance criteria/testing | P4-F2-01, P4-F2-03 | Requirements engineering and testing | test provisionally | More specific than general `acceptance criteria`; test separately from user acceptance and domain acceptance language. |
| Gherkin acceptance criteria | acceptance criteria/testing | P4-F2-03 | Behavior-Driven Development | test provisionally with BDD | Specific syntax/representation term; likely higher precision than unqualified acceptance criteria. |
| Behavior-Driven Development (BDD) | requirements/testing representation | P4-F2-03 | Agile requirements and acceptance testing | investigate separately | Provides a distinct scenario-based tradition around executable or structured acceptance criteria. |
| requirement coverage | requirements/acceptance evaluation | P4-F2-03 | Requirements validation and acceptance criteria | retain as contextual term | Evaluation term, not a synonym for acceptance criteria. |
| user-story set | user-story representation | P4-F2-04 | Agile requirements | test provisionally | Distinguishes collections of stories from an individual user story. |
| user-story quality | user-story quality assessment | P4-F2-04, P4-F2-06 | Agile requirements | test provisionally | Established-looking quality vocabulary; requires later source screening and should not be equated with requirements quality. |
| Quality User Story | user-story quality framework | P4-F2-06 | Agile requirements | investigate separately | Named framework/term in Lucassen et al.; retain as a distinct phrase rather than expanding generic `quality`. |
| INVEST | user-story quality heuristic | P4-F2-04 | Agile requirements | retain as contextual term | Appeared in inspected user-story work as a named heuristic; not treated as a universal quality model. |
| requirements quality assurance | requirements quality/validation | P4-F2-05 | Requirements engineering | test provisionally with validation | Distinct literature tradition around assurance and validation, not a replacement for requirements/specification terms. |
| requirements quality control | requirements quality/validation | P4-F2-05 | Requirements engineering | investigate separately | Framework-oriented phrase found in published metadata; likely useful for quality-assessment searches. |
| natural-language requirements quality | requirements quality/validation | P4-F2-05 | Requirements engineering | test provisionally | More precise than generic requirements quality for linguistic properties of requirement statements. |
| coding agent | coding-agent vocabulary | P1-F5-02, P2-F5-01, P3-F5-01, P3-F5-02 | Recent coding-agent research | test provisionally across sources | High-yield broad phrase with adjacent systems and infrastructure noise; not validated as final terminology. |
| AI coding agent | coding-agent vocabulary | P1-F5-02, P2-F5-01, P3-F5-01, P3-F5-02 | Recent coding-agent research | test provisionally across sources | Appeared in recent records alongside coding-agent workloads, sessions, and agent-authored pull requests. |
| software engineering agent | coding-agent vocabulary | P1-F5-03, P2-F5-01, P3-F5-01, P3-F5-02 | Recent software-engineering-agent research | test provisionally across sources | More focused than `coding agent` but still includes non-repository and infrastructure settings. |
| SWE agent / SWE-agent | coding-agent vocabulary | P1-F5-03, P1-F5-04, P2-F5-01, P3-F5-01, P3-F5-02 | Benchmarks and agent systems | test provisionally across sources | Research-lineage term; test hyphenation and plural variants separately rather than treating it as final. |
| AI Software Engineer | coding-agent vocabulary | P1-F5-03 | Unified agent framing | investigate separately | Appears in a paper describing a unified agent across coding, testing, and patching. |
| agent-computer interface (ACI) | agent execution environment | P1-F5-04, P9-F6D-02, P10-F6D1-01 | SWE-agent system paper | retain as architecture-specific contextual term | Specific interface terminology associated with repository navigation, editing, and execution; P9/P10 confirm it should not stand for autonomy generally. |
| SWE-bench | coding-agent evaluation | P1-F5-04, P9-F6A-02, P9-F6C-01, P9-F6C-02, P9-F6D-01, P9-F6D-02 | GitHub issue resolution benchmark | retain as contextual term | Benchmark name, not a general synonym for coding agents; P9 records its use as a benchmark setting and interaction-boundary source. |
| agent trajectory / tool-mediated trajectory | agent execution trace | P1-F5-03, P1-F5-04, P9-F6D-01, P10-F6D1-01, P10-F6D2-01 | Agent evaluation and analysis | retain as execution-record contextual term | Used to describe multi-step agent/environment interaction; P9/P10 explicitly separate trajectory records from reasoning quality and autonomy level. |
| agentic coding | coding-agent vocabulary | P2-F5-01, P3-F5-01 | Recent coding-agent research | investigate separately | Appeared as a related term in AIDev and the Round 3 arXiv sample; not yet tested as a standalone search phrase. |
| agentic software engineering | coding-agent vocabulary | P2-F5-01, P3-F5-01 | Recent coding-agent research | investigate separately | Appeared as a related term in AIDev and the Round 3 arXiv sample; may overlap with software-engineering-agent terminology. |
| Agentic-PRs | coding-agent activity/data | P2-F5-01, P3-F5-01 | GitHub repository studies | investigate separately | Term used for agent-authored pull requests; source and population boundaries need later screening. |
| software delegation contract | coding-agent work framing | P2-F5-01, P3-F5-01 | Coding-agent task/review study | retain as contextual term | A source-specific term for a study's unit of analysis; not a Work Item characteristic or final vocabulary. |
| agentless software engineering | coding-agent comparison vocabulary | P2-F5-03, P3-F5-03, P9-F6B-01, P9-F6C-01, P9-F6C-02, P9-F6D-01 | Agentless versus agent-based systems | retain as contextual term | Useful for separating autonomous-agent claims from non-agent workflow baselines and for identifying non-interactive benchmark boundaries. |
| SWE-Gym | coding-agent training/evaluation | P2-F5-03, P3-F5-03 | Agent training/evaluation | retain as contextual term | Benchmark/framework name, not a general synonym for coding agents. |
| task decomposition approaches | software work decomposition | P4-F3-01, P4-F3-03, P4-F3-06, P5-F3-01, P6-F3A-01, P6-F3A-02 | Crowdsourcing software development | test provisionally with software context | Title-qualified search retrieved the direct Khanfor seed; retain separately from generic AI task decomposition. |
| crowdsourcing software development | software work decomposition and allocation | P4-F3-01, P4-F3-03, P4-F3-05, P5-F3-10, P5-F3-14, P6-F3C-01, P6-F3C-02 | Crowdsourcing/project decomposition | retain as a domain-qualified supplementary subfamily | Produced a relatively coherent but heterogeneous corpus covering decomposition, parallel tasks, allocation, scheduling, lifecycle, and marketplace studies; retain for discovery and snowballing rather than assume primary F3 status. |
| task preparation | task description/decomposition | P4-F3-01, P5-F3-02, P5-F3-15 | Crowdsourcing software development | downgrade to source-specific wording | Exact phrase retrieved non-software task automation/neuroscience; Khanfor used `preparing tasks`, not the exact phrase. |
| manageable software tasks | task scope/decomposition | P4-F3-01 | Crowdsourcing software development | test provisionally | Context-bound phrase; do not generalize it beyond the inspected crowdsourcing literature. |
| preparing tasks | task description/decomposition | P5-F3-01 | Crowdsourcing software development | investigate separately | Natural wording in the Khanfor abstract; not tested as an independent broad search phrase. |
| software project decomposition | software work decomposition | P5-F3-01 | Crowdsourcing software development | test provisionally with domain qualifier | Phrase observed in the title/abstract context of the direct decomposition seed; keep separate from generic task decomposition. |
| coding plans | software development planning | P5-F3-03, P9-F6B-01 | Coding-agent-specific software development | investigate separately | Retrieved in agent workflow literature; distinct from traditional decomposition and from project planning. P9 separates explicit plans from implicit scaffold planning. |
| issue descriptions and comments | task description/work representation | P5-F3-04, P6-F3B-01, P6-F3B-02 | Issue-tracking research | test component terms with software context | The exact plural phrase returned zero in the Round 6 arXiv check; retain `issue description` and `issue comments` as component terms rather than treating the full phrase as stable. |
| textual descriptions of issues | task description/work representation | P5-F3-04 | Issue-tracking research | retain as contextual term | Representation phrase from a software-task study; not a decomposition synonym. |
| task decomposition and collaboration | software development planning | P4-F3-03 | Coding-agent-specific software development | investigate separately | Agent-architecture phrase; keep distinct from human/team task decomposition. |
| requirement-driven task decomposition | software development planning | P4-F3-03, P9-F6B-02 | End-to-end software-development agents | investigate separately | Recent agent-specific wording; publication status and transferability require later screening. P9 keeps it separate from F3 human/project decomposition and multi-agent delegation. |
| task interdependence | software task relationships/work design | P5-F3-08, P5-F3-12 | Software development teams | retain as contextual term | More productive than `task dependency` for a direct software-team study, but primarily a work-design/team-organization construct. |
| technical dependencies between components | software task relationships | P5-F3-08 | Software development teams | retain as contextual term | Appeared as one source's explanation of task interdependence; not equivalent to decomposition dependencies. |
| task allocation | software work division | P4-F3-05, P5-F3-09, P5-F3-13 | Software development and crowdsourcing | test provisionally with software context | Retrieves global/distributed software-development allocation when qualified; distinct from forming subtasks. |
| software development task allocation | software work division | P4-F3-05, P5-F3-09 | Software project management | test provisionally with field restrictions | More specific phrase exposed by OpenAlex/arXiv; distinguish allocation from decomposition. |
| global software development task allocation | software work division | P5-F3-09 | Global/distributed software development | test provisionally as separate branch | Coherent allocation tradition involving sites, roles, and distributed projects; not interchangeable with decomposition. |
| task allocation criteria | software work division | P5-F3-09 | Global software development | investigate separately | Explicit terminology in Lamersdorf et al.; likely concerns assignment decisions rather than task creation. |
| work allocation | software work division | P5-F3-09 | Global/distributed software development | test provisionally with software context | Related allocation wording found in global software-development literature. |
| design rule hierarchies | software task structure/dependencies | P4-F3-05 | Software development tasks | investigate separately | Appeared in a study of hierarchy and parallelism; likely a dependency/structure term rather than a general decomposition synonym. |
| parallelism in software development tasks | software task structure/dependencies | P4-F3-05, P5-F3-10, P5-F3-14 | Software development planning/crowdsourcing | retain as contextual term | Appeared with crowdsourced parallel tasks and task upload; not equivalent to task decomposition. |
| parallel tasks in crowdsourcing software development | software work division | P5-F3-10, P5-F3-14 | Crowdsourcing software development | investigate separately | More specific than generic parallelism; may concern task lifecycle/market scheduling as well as decomposition. |
| task granularity | task size/execution granularity | P4-F3-04, P5-F3-05, P5-F3-06 | Parallel computing and runtime systems | exclude from broad searches due to ambiguity | P4 retrieved runtime/HPC material; software-development qualifiers produced zero arXiv records. Do not use as a primary F3 term yet. |
| fine-grained tasks | task size/execution granularity | P4-F3-04 | Parallel computing and runtime systems | exclude from broad searches due to ambiguity | Strongly associated with parallel execution in the inspected sample; no development-work calibration evidence. |
| task life cycle | crowdsourced software work process | P5-F3-10 | Crowdsourcing software development | investigate separately | Process term found in task-cycle research; not synonymous with decomposition. |
| task cycle pattern | crowdsourced software work process | P5-F3-10 | Crowdsourcing software development | investigate separately | Source-specific process terminology connected to task arrival and sequencing. |
| task scheduling | crowdsourced software work process | P5-F3-10 | Crowdsourcing software development | retain as contextual term | Retrieves marketplace/process scheduling; distinguish from decomposition and allocation. |
| project description length | task/project description | P5-F3-14 | Crowdsourcing software development | investigate separately | Candidate representation/size-related terminology; evidence is domain-specific and not a decomposition synonym. |
| software development task type | software work classification | P4-F3-01, P4-F3-02, P4-F3-03 | Traditional software engineering | test provisionally across sources | Useful for classifying development work, but not itself a decomposition term. |
| outer-loop software-development tasks | software work classification | P4-F3-01 | Coding-agent and LLM evaluation | investigate separately | Recent phrase for bug fixing, review, and documentation activities; distinct from task decomposition. |

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

## Pilot Round 8 Family 4 Subfamily Validation

Pilot Round 8 was conducted on 2026-08-20 using focused OpenAlex Works API searches and individual DOI retrieval checks. The round tested the P7 split rather than recreating broad Family 4 queries. No F6 or F7 searches were executed. OpenAlex counts remain database diagnostics, not estimates of prevalence, precision, recall, or evidence strength. Search results were used for boundary and terminology validation only; no Work Item characteristic, causal conclusion, hypothesis, or optimal information amount was derived.

### P8-F4A-01

- **Search ID:** `P8-F4A-01`
- **Date:** `2026-08-20`
- **Database / source:** OpenAlex Works API
- **Query:** `title.search:"requirements ambiguity"`
- **Fields searched:** OpenAlex title search with selected metadata, DOI, venue, and abstract fields
- **Filters:** `per-page=10`
- **Result count:** `19` reported by OpenAlex
- **Results inspected:** First 10 title records and available abstracts/metadata
- **Clearly relevant results:** `Addressing the challenges of requirements ambiguity: A review of empirical literature`, Muneera Bano, 2015, IEEE EmpiRE, DOI [10.1109/empire.2015.7431303](https://doi.org/10.1109/empire.2015.7431303), published; `Requirement Ambiguity Not as Important as Expected--Results of an Empirical Evaluation`, Erik Jan Philippo et al., 2013, LNCS, DOI [10.1007/978-3-642-37422-7_5](https://doi.org/10.1007/978-3-642-37422-7_5), published; and `Requirements Ambiguity Detection and Explanation with LLMs: An Industrial Study`, Sarmad Bashir et al., 2025, IEEE ICSME, DOI [10.1109/icsme64153.2025.00063](https://doi.org/10.1109/icsme64153.2025.00063), published.
- **Noise:** Low in the inspected sample; most records concerned requirements ambiguity, detection, prevention, elicitation, or empirical evaluation.
- **Terminology retained:** requirements ambiguity, ambiguity detection, ambiguity explanation, ambiguity avoidance, requirements elicitation, empirical ambiguity evaluation.
- **Known-source checks:** Bano `Retrieved`; Berry and Kamsties, `Ambiguity in Requirements Specification`, `Missed`; Chantree et al., `Identifying Nocuous Ambiguities in Natural Language Requirements`, `Missed`; Kiyavitskaya et al., `Requirements for tools for ambiguity identification and measurement in natural language requirements specifications`, `Missed`; Kamsties, Berry, and Paech, `Detecting Ambiguities in Requirements Documents Using Inspections`, `Not verified` because the P7 candidate had no DOI and was not title-matched in this check.
- **Query adjustment:** None. The focused title-restricted query was sufficient to classify the ambiguity branch.
- **Rationale:** The P7 ambiguity neighborhood remains recognizable with low inspected noise, while missed known sources demonstrate that title restriction is not recall-complete.

### P8-F4A-02

- **Search ID:** `P8-F4A-02`
- **Date:** `2026-08-20`
- **Database / source:** OpenAlex Works API
- **Query:** `title.search:"requirements completeness"`
- **Fields searched:** OpenAlex title search with selected metadata, DOI, venue, and abstract fields
- **Filters:** `per-page=10`
- **Result count:** `20` reported by OpenAlex
- **Results inspected:** First 10 title records and available abstracts/metadata
- **Clearly relevant results:** `Are Your Requirements Complete?`, Donald Firesmith, 2005, *The Journal of Object Technology*, DOI [10.5381/jot.2005.4.1.c3](https://doi.org/10.5381/jot.2005.4.1.c3), published; `Generating Obstacle Conditions for Requirements Completeness`, Dalal Alrajeh et al., 2012, ICSE, DOI [10.1109/icse.2012.6227147](https://doi.org/10.1109/icse.2012.6227147), published; `Improving requirements completeness: automated assistance through large language models`, Dipeeka Luitel et al., 2024, *Requirements Engineering*, DOI [10.1007/s00766-024-00416-3](https://doi.org/10.1007/s00766-024-00416-3), published; and `Investigating Requirements Completeness Metrics...`, Tanu Singh and Manoj Kumar, 2021, DOI [10.1007/s13369-021-06269-0](https://doi.org/10.1007/s13369-021-06269-0), published.
- **Noise:** Low in the inspected sample, with duplicate conference/preprint records and some systems-engineering material.
- **Terminology retained:** requirements completeness, completeness metrics, obstacle conditions, scenarios, schemas, formal validation, empirical validation, automated completeness assistance.
- **Known-source checks:** Rempel and Mader, `Preventing Defects: The Impact of Requirements Traceability Completeness on Software Quality`, `Missed`; Sommerville and Sawyer, `Requirements Engineering: A Good Practice Guide`, `Not verified` because the P7 record had no DOI and no stable title record was retrieved in this check.
- **Query adjustment:** None. The focused title search was sufficient to classify completeness without a second query.
- **Rationale:** Completeness remains distinct from ambiguity, traceability, coverage, and information sufficiency, but is searchable as part of the same information-quality branch.

### P8-F4B-01

- **Search ID:** `P8-F4B-01`
- **Date:** `2026-08-20`
- **Database / source:** OpenAlex Works API
- **Query:** `title.search:"developer information needs"`
- **Fields searched:** OpenAlex title search with selected metadata, DOI, venue, and abstract fields
- **Filters:** `per-page=10`
- **Result count:** `7` reported by OpenAlex
- **Results inspected:** All 7 records and available abstracts/metadata
- **Clearly relevant results:** `API-Related Developer Information Needs in Stack Overflow`, Mingwei Liu et al., 2021, *IEEE Transactions on Software Engineering*, DOI [10.1109/TSE.2021.3120203](https://doi.org/10.1109/TSE.2021.3120203), published; `Categorizing developer information needs in software ecosystems`, Nicole Haenni et al., 2013, ACM workshop, DOI [10.1145/2501585.2501586](https://doi.org/10.1145/2501585.2501586), published; `A Quantitative Analysis of Developer Information Needs in Software Ecosystems`, Nicole Haenni et al., 2014, ECSA workshop, DOI [10.1145/2642803.2642815](https://doi.org/10.1145/2642803.2642815), published; `Two Decades of Empirical Research on Developers' Information Needs`, Abir Bouraffa and Walid Maalej, 2020, ICSE workshop, DOI [10.1145/3387940.3391485](https://doi.org/10.1145/3387940.3391485), published; and `Software Developers' Information Needs: Towards the Development of Intelligent Recommender Systems`, Adam Grzywaczewski et al., 2011, Electronic Workshops in Computing, DOI [10.14236/ewic/iubicom2011.8](https://doi.org/10.14236/ewic/iubicom2011.8), published/open-access record.
- **Noise:** Low to moderate; the exact title branch was cleaner than P7 full-text retrieval, but the records span ecosystem, API, team, and recommendation settings.
- **Terminology retained:** developer information needs, software developers' information needs, software ecosystem information, API-related needs, information sources, recommender systems.
- **Known-source checks:** Liu `Retrieved`; Haenni et al. 2013 `Retrieved`; Haenni et al. 2014 `Retrieved`; Bouraffa and Maalej `Retrieved`; Ko, DeLine, and Venolia, `Information Needs in Collocated Software Development Teams`, `Missed`.
- **Query adjustment:** None.
- **Rationale:** P8 confirms `developer information needs` as a stable software-engineering phrase, while its contexts remain heterogeneous.

### P8-F4B-02

- **Search ID:** `P8-F4B-02`
- **Date:** `2026-08-20`
- **Database / source:** OpenAlex Works API
- **Query:** `title.search:"information seeking" AND from_publication_date:2000-01-01 AND fulltext.search:"software developers"`
- **Fields searched:** OpenAlex title and full-text filters with selected metadata, DOI, venue, and abstract fields
- **Filters:** Publication date from 2000; `per-page=10`
- **Result count:** `99` reported by OpenAlex
- **Results inspected:** First 10 records and available abstracts/metadata
- **Clearly relevant results:** `An empirically-based characterization and quantification of information seeking through mailing lists during Open Source developers' software evolution`, Khaironi Yatim Sharif et al., 2014, *Information and Software Technology*, DOI [10.1016/j.infsof.2014.09.003](https://doi.org/10.1016/j.infsof.2014.09.003), published; `A Gaze-Based Exploratory Study on the Information Seeking Behavior of Developers on Stack Overflow`, Cole S. Peterson et al., 2019, CHI Extended Abstracts, DOI [10.1145/3290607.3312801](https://doi.org/10.1145/3290607.3312801), published; and `Collaboration, Information Seeking and Communication: An Observational Study of Software Developers' Work Practices`, Márcio Kuroki Gonçalves et al., 2020, DOI [10.3217/jucs-017-14-1913](https://doi.org/10.3217/jucs-017-14-1913), OpenAlex submitted/unpublished version.
- **Noise:** Moderate to high, including generic information-seeking and health/social-media information behavior studies.
- **Terminology retained:** information seeking, software evolution, mailing lists, Stack Overflow, gaze-based information seeking, collaboration, communication, observational developer behavior.
- **Known-source checks:** Ko, Myers, Coblenz, and Aung, `An Exploratory Study of How Developers Seek, Relate, and Collect Relevant Information during Software Maintenance Tasks`, `Missed`; Goncalves et al. `Retrieved`; Robillard, Walker, and Zimmermann, `Recommendation Systems for Software Engineering`, `Missed`.
- **Query adjustment:** None. This remains a sensitivity branch rather than a standalone sufficiency query.
- **Rationale:** Information seeking is coherent as an adjacent tradition, but it studies behavior and sources rather than directly measuring information sufficiency.

### P8-F4C-01

- **Search ID:** `P8-F4C-01`
- **Date:** `2026-08-20`
- **Database / source:** OpenAlex Works API
- **Query:** `mental workload programmers program comprehension`
- **Fields searched:** OpenAlex broad full-text search with selected metadata, DOI, venue, and abstract fields
- **Filters:** `per-page=10`
- **Result count:** `1,229` reported by OpenAlex
- **Results inspected:** First 10 records and available abstracts/metadata
- **Clearly relevant results:** `Quantifying programmers' mental workload during program comprehension based on cerebral blood flow measurement`, Takao Nakagawa et al., 2014, ICSE Companion Proceedings, DOI [10.1145/2591062.2591098](https://doi.org/10.1145/2591062.2591098), published; `Towards an affordable brain computer interface for the assessment of programmers' mental workload`, Makrina Viola Kosti et al., 2018, *International Journal of Human-Computer Studies*, DOI [10.1016/j.ijhcs.2018.03.002](https://doi.org/10.1016/j.ijhcs.2018.03.002), published; `Can EEG Be Adopted as a Neuroscience Reference for Assessing Software Programmers' Cognitive Load?`, Júlio Medeiros et al., 2021, *Sensors*, DOI [10.3390/s21072338](https://doi.org/10.3390/s21072338), published; and `Quality Evaluation of Modern Code Reviews Through Intelligent Biometric Program Comprehension`, Haytham Hijazi et al., 2022, *IEEE Transactions on Software Engineering*, DOI [10.1109/TSE.2022.3158543](https://doi.org/10.1109/TSE.2022.3158543), published.
- **Noise:** Very high despite qualifiers: programming education, AI, business-process comprehension, generic workload, and unrelated biometric studies remained.
- **Terminology retained:** mental workload, cognitive workload, programmers' cognitive load, program comprehension, cerebral blood flow, EEG, fNIRS, BCI, biometric assessment.
- **Known-source checks:** Nakagawa `Retrieved`; Young et al., `State of science: mental workload in ergonomics`, `Missed`; Cao et al., `NASA TLX: Software for assessing subjective mental workload`, `Missed`; Curtis, Krasner, and Iscoe, `A field study of the software design process for large systems`, `Missed`.
- **Query adjustment:** None. The query classified the professional-programmer workload branch, but is not a final systematic string.
- **Rationale:** Mental workload is retrievable through direct programmer/program-comprehension studies, but measurement and population screening are essential.

### P8-F4C-02

- **Search ID:** `P8-F4C-02`
- **Date:** `2026-08-20`
- **Database / source:** OpenAlex Works API
- **Query:** `information overload software developers`
- **Fields searched:** OpenAlex broad full-text search with selected metadata, DOI, venue, and abstract fields
- **Filters:** `per-page=10`
- **Result count:** `39,683` reported by OpenAlex
- **Results inspected:** First 10 records and available abstracts/metadata
- **Clearly relevant results:** `Awareness in the Wild: Why Communication Breakdowns Occur`, Daniela Damian et al., 2007, IEEE ICGSE, DOI [10.1109/ICGSE.2007.13](https://doi.org/10.1109/ICGSE.2007.13), published, was adjacent software-team communication evidence. `The productivity paradox of information technology`, Erik Brynjolfsson, 1993, *Communications of the ACM*, DOI [10.1145/163298.163309](https://doi.org/10.1145/163298.163309), published, was only indirectly related.
- **Noise:** Extreme; generic full-text matches, software papers, systems surveys, productivity work, and unrelated information uses dominated.
- **Terminology retained only as supplementary:** information overload, communication breakdowns, awareness, developer coordination, productivity paradox.
- **Known-source checks:** `Structuring computer-mediated communication systems to avoid information overload`, `Missed`; Damian et al., `Awareness in the Wild: Why Communication Breakdowns Occur`, `Not verified` because the individual DOI request returned OpenAlex HTTP 429 during P8.
- **Query adjustment:** None. The P7 developer-qualified overload query was reused as a boundary check and remained too noisy for further synonym expansion.
- **Rationale:** Cognitive/mental workload and information overload do not share a sufficiently coherent professional software-engineering retrieval neighborhood in this pilot.

### P8-F4D-01

- **Search ID:** `P8-F4D-01`
- **Date:** `2026-08-20`
- **Database / source:** OpenAlex Works API
- **Query:** `title.search:"software documentation"`
- **Fields searched:** OpenAlex title search with selected metadata, DOI, venue, and abstract fields
- **Filters:** `per-page=10`
- **Result count:** `493` reported by OpenAlex
- **Results inspected:** First 10 title records and available abstracts/metadata
- **Clearly relevant results:** `The relevance of software documentation, tools and technologies`, Andrew Forward and Timothy C. Lethbridge, 2002, ACM Document Engineering, DOI [10.1145/585058.585065](https://doi.org/10.1145/585058.585065), published; `Software Documentation Issues Unveiled`, Emad Aghajani et al., 2019, ICSE, DOI [10.1109/icse.2019.00122](https://doi.org/10.1109/icse.2019.00122), published; `Software documentation: how much is enough?`, Lionel Briand, 2003, ECSA, DOI [10.1109/csmr.2003.1192406](https://doi.org/10.1109/csmr.2003.1192406), published; `Extracting Development Tasks to Navigate Software Documentation`, Christoph Treude et al., 2014, *IEEE Transactions on Software Engineering*, DOI [10.1109/TSE.2014.2387172](https://doi.org/10.1109/TSE.2014.2387172), published; and `The Value of Software Documentation Quality`, Reinhold Plösch et al., 2014, QSIC, DOI [10.1109/qsic.2014.22](https://doi.org/10.1109/qsic.2014.22), published.
- **Noise:** Low in the inspected sample, with some adjacent documentation/NLP and document-engineering work.
- **Terminology retained:** software documentation, documentation relevance, documentation quality, documentation formats, documentation maintenance, traceability, task navigation, documentation usefulness, how much is enough.
- **Known-source checks:** Forward and Lethbridge `Retrieved`; Dzidek et al., `A Realistic Empirical Evaluation of the Costs and Benefits of UML in Software Maintenance`, `Not verified` because the individual DOI request returned OpenAlex HTTP 429; Lientz, Swanson, and Tompkins, `Characteristics of application software maintenance`, `Not verified` because the individual DOI request returned HTTP 429; Mens and Tourwe, `A survey of software refactoring`, `Retrieved` by individual DOI check but `Not applicable to this documentation-specific title branch` as a direct documentation seed.
- **Query adjustment:** None. The title branch was sufficient to validate documentation as a searchable F4 domain.
- **Rationale:** P8 improves the case for documentation as an F4 branch because the neighborhood includes relevance, quality, navigation, maintenance, and explicit information-volume wording rather than only package descriptions.

### P8-F4D-02

- **Search ID:** `P8-F4D-02`
- **Date:** `2026-08-20`
- **Database / source:** OpenAlex Works API
- **Query:** `documentation relevance software maintenance`
- **Fields searched:** OpenAlex broad full-text search with selected metadata, DOI, venue, and abstract fields
- **Filters:** `per-page=10`
- **Result count:** `66,105` reported by OpenAlex
- **Results inspected:** First 10 records and available abstracts/metadata
- **Clearly relevant results:** `The relevance of software documentation, tools and technologies`, Forward and Lethbridge, 2002, ACM Document Engineering, DOI [10.1145/585058.585065](https://doi.org/10.1145/585058.585065), published; `Quality analysis of source code comments`, Daniela Steidl et al., 2013, ICPC, DOI [10.1109/icpc.2013.6613836](https://doi.org/10.1109/icpc.2013.6613836), published.
- **Noise:** Extreme; generic maintenance, scientific-computing, research-methods, and testing papers dominated broad full-text retrieval.
- **Terminology retained:** documentation relevance, source-code comments, documentation quality analysis, traceability, documentation maintenance.
- **Known-source checks:** Forward and Lethbridge `Retrieved`; Dzidek et al. `Not verified` because the individual DOI request returned HTTP 429; Lientz et al. `Not verified` because the individual DOI request returned HTTP 429; Mens and Tourwe `Retrieved` individually but `Not applicable to this documentation-relevance branch`.
- **Query adjustment:** None. This was a deliberately noisy sensitivity check after the cleaner title search, not a candidate final search string.
- **Rationale:** The contrast with P8-F4D-01 confirms that field restriction is material for documentation retrieval.

## P8 Query Evolution Records

- `P7 broad requirements ambiguity/full-text neighborhood → P8 title.search:"requirements ambiguity" → 19 records with low inspected noise and direct ambiguity studies → retain title-qualified ambiguity branch; do not treat title restriction as recall-complete` (`P8-F4A-01`; OpenAlex).
- `P7 requirements completeness software/full-text query → P8 title.search:"requirements completeness" → 20 records with low inspected noise and completeness metrics/validation terminology → retain completeness as a separate F4-A quality branch while preserving F2 overlap` (`P8-F4A-02`; OpenAlex).
- `P7 developer information needs/full-text query → P8 title.search:"developer information needs" → 7 records, mostly direct software-ecosystem/API/team information-needs studies → validate exact phrase as a primary F4-B term` (`P8-F4B-01`; OpenAlex).
- `P7 information seeking software developers/full-text query → P8 title/full-text information-seeking query → 99 records with direct developer-seeking studies and moderate/high general information-seeking noise → retain as a sensitivity F4-B branch` (`P8-F4B-02`; OpenAlex).
- `P7 mental workload programming plus qualifiers → P8 mental workload programmers program comprehension → 1,229 records with direct professional-programmer workload studies but high measurement/education noise → retain mental workload/program comprehension as primary and require population screening` (`P8-F4C-01`; OpenAlex).
- `P7 information overload software developers → P8 same developer-qualified boundary check → 39,683 records with extreme noise and no direct overload study in the inspected sample → separate information overload from mental workload and retain only as supplementary/contextual terminology` (`P8-F4C-02`; OpenAlex).
- `P7 documentation overhead/effort broad queries → P8 title.search:"software documentation" → 493 records with low inspected noise and relevance/quality/navigation/"how much is enough" terminology → validate documentation as a primary F4-D branch while excluding documentation overhead as a primary phrase` (`P8-F4D-01`; OpenAlex).
- `P7 documentation effort/relevance broad query → P8 documentation relevance software maintenance → 66,105 noisy full-text matches → retain only as a sensitivity branch and require fielding in later systematic searching` (`P8-F4D-02`; OpenAlex).

No P8 query was silently replaced. No systematic search string was frozen.

## P8 Terminology Registry Recalibration

The existing P7 registry rows were updated in place where P8 materially changed their status. No duplicate canonical rows were added.

- `requirements ambiguity`: validated as a primary F4-A term by `P8-F4A-01`; title retrieval was low-noise but not recall-complete.
- `requirements completeness`: validated as a primary F4-A quality branch by `P8-F4A-02`; retain separate from ambiguity, traceability, and coverage.
- `developer information needs`: validated as a primary F4-B term by `P8-F4B-01`.
- `information seeking`: retained as a supplementary/sensitivity F4-B term by `P8-F4B-02`.
- `program comprehension`: retained as a bridge term across F4-B and F4-C; not equivalent to sufficiency or workload.
- `cognitive load`: separated from information overload; retain only with population and construct screening through `P8-F4C-01`.
- `mental workload` and `cognitive workload`: validated as primary F4-C1 terminology through `P8-F4C-01`.
- `information overload`: downgraded to supplementary/contextual and excluded from the primary F4-C branch through `P8-F4C-02`.
- `software documentation`: validated as a primary F4-D discovery term through `P8-F4D-01`.
- `documentation relevance`, `documentation quality`, `documentation usefulness`, `documentation maintenance`, and `task navigation`: retained as primary F4-D contextual terms through `P8-F4D-01` and `P8-F4D-02`, with field restrictions required.
- `documentation overhead`: remains excluded as a primary term; P8 did not restore it.
- `information sufficiency`, `missing context`, and generic `clarity`: remain downgraded/provisional and were not restored by P8.

## P8 Boundary Assessment

### F4-A: Ambiguity, Completeness, And Information Quality

- **Conceptual coherence:** High. P8 independently retrieved requirements ambiguity and requirements completeness studies, including reviews, empirical evaluation, detection, metrics, and automated assistance.
- **Retrieval coherence:** High for exact title-qualified phrases in the inspected samples; broad full-text quality searches remain noisy. Title restriction is a precision aid, not a recall-complete strategy.
- **Distinctness:** Meaningfully distinct from F2 artifact searches because the search object is ambiguity/completeness/quality measurement, while retaining legitimate F2 overlap.
- **Overlap:** Strong with F2 requirements/specifications; some overlap with F1/F3 issue or task descriptions when information quality is measured.
- **Population/transferability:** Requirements engineers, software engineers, and industrial-study participants; no coding-agent population was retrieved or inferred.
- **Search status:** `Primary`

### F4-B: Developer Information Needs And Context

- **Conceptual coherence:** High after replacing information sufficiency with developer information needs, information seeking, and related comprehension/context terms.
- **Retrieval coherence:** Moderate to high for exact developer-information-needs titles; moderate for information seeking because general information behavior remains.
- **Distinctness:** Distinct from F4-A quality properties because the object is what developers seek, need, use, or comprehend. Distinct from F3 when task descriptions are only information sources.
- **Overlap:** F1 issue/work-unit studies may provide information sources; F2 requirements/specifications may be sources; F3 descriptions and comprehension tasks overlap. F6 was not executed.
- **Population/transferability:** Professional developers, maintainers, open-source developers, ecosystem/API users, and software teams; transfer to coding agents remains untested.
- **Search status:** `Primary`

### F4-C1: Mental Workload And Cognitive Burden In Software Development

- **Conceptual coherence:** Moderate to high when restricted to mental workload/cognitive workload, programmer/developer populations, and program comprehension or code-review tasks.
- **Retrieval coherence:** Moderate. Direct professional-programmer studies were found, but education, neuroscience, biometric, and generic workload noise requires screening.
- **Distinctness:** Distinct from F4-B information behavior and from runtime/computational load or coding-agent context load.
- **Overlap:** F3 task complexity and program comprehension can be contexts; F2 requirements/specifications may be experimental material; F1 work units may be task settings.
- **Population/transferability:** Professional programmers/developers in direct studies plus separately labeled student/general human-factors populations.
- **Search status:** `Primary`

### F4-C2: Information Overload

- **Conceptual coherence:** Low for a professional software-development branch. Adjacent communication, awareness, information-systems, and general overload traditions exist, but no direct developer-overload neighborhood was established.
- **Retrieval coherence:** Low; the developer-qualified full-text search remained extremely noisy.
- **Distinctness:** Conceptually distinct from mental workload, but insufficiently coherent for a primary systematic branch.
- **Overlap:** Strong with F3 communication/task descriptions and possible F6 context/awareness topics; those families were not merged or searched in P8.
- **Population/transferability:** General users/teams and occasional developer contexts; direct professional developer overload evidence was not established.
- **Search status:** `Supplementary`

### F4-D: Documentation Effort, Cost, Maintenance, And Usefulness

- **Conceptual coherence:** Moderate to high after replacing documentation overhead with software documentation, relevance, quality/usefulness, maintenance, task navigation, and information-volume wording. Cost/effort remains a separate sub-branch.
- **Retrieval coherence:** High for title-qualified `software documentation`; low for broad documentation relevance/maintenance full-text retrieval. P8 validates field restriction as methodologically important.
- **Distinctness:** Distinct from F2 artifact presence because it concerns documentation usefulness, quality, navigation, maintenance, and cost/effort. It overlaps F2 where requirements/specifications are documentation artifacts.
- **Overlap:** F1 and F3 may study documentation attached to issues, tasks, or work units; cross-screen rather than collapse the object and property.
- **Population/transferability:** Developers, maintainers, software teams, document users, and scientific-software communities; context-specific transfer is required.
- **Search status:** `Primary`

## Calibrated F4 Structure For Later Systematic-Search Design

| Branch | Purpose | Provisional terminology | Major exclusions/noise | Population/transferability | F1/F2/F3 relationship | Status |
|---|---|---|---|---|---|---|
| F4-A Information-quality properties | Ambiguity, completeness, quality, coverage, and measurement of software-development information/artifacts | requirements ambiguity; ambiguity detection; requirements completeness; completeness metrics; requirements quality; requirements coverage; traceability completeness | Generic linguistic ambiguity; regulatory/legal requirements; source-code/API ambiguity unless explicitly in scope; broad quality/package matches | Requirements engineers and software engineers; no coding-agent transfer assumed | Strong F2 overlap; cross-list F1/F3 text-quality studies | `Primary` |
| F4-B Developer information needs and context | What developers seek, need, use, and comprehend during software work | developer information needs; information seeking; information foraging; program comprehension; relevant information; software evolution; task context | Generic information behavior; health/social-media studies; package papers; unqualified information sufficiency or missing context | Professional developers, maintainers, open-source developers, software teams; no coding-agent transfer assumed | Overlaps F1 sources, F2 artifacts, F3 descriptions; separate information behavior from representation | `Primary` |
| F4-C1 Mental workload and cognitive burden | Human workload associated with programming, comprehension, code review, or software work | mental workload; cognitive workload; programmers' cognitive load; program comprehension; subjective workload; NASA-TLX; EEG/fNIRS/BCI | Educational-only studies; generic HCI/neuroscience; computational/runtime load; agent context load | Professional programmers plus separately labeled student/general populations | Context may involve F1/F2/F3 tasks or artifacts; no population generalization | `Primary` |
| F4-C2 Information overload | Supplementary communication and information-system overload context | information overload; communication breakdowns; awareness; developer coordination | Broad information-systems, productivity, networking, package, and general psychology noise | General users/teams and occasional developer contexts; direct professional evidence not established | Possible F3/F6 overlap; do not merge with mental workload | `Supplementary` |
| F4-D Documentation information and burden | Documentation usefulness, quality, relevance, navigation, maintenance, effort, cost, and information-volume questions | software documentation; documentation relevance; documentation quality; documentation usefulness; documentation maintenance; task navigation; documentation effort/cost; "how much is enough" | documentation overhead; package descriptions; scientific software when no developer-work information question; broad maintenance/testing noise | Developers, maintainers, teams, document users, scientific-software communities; context-specific transfer | Strong F2 overlap and meaningful F1/F3 overlap | `Primary` |

## Decision On Cognitive Load Versus Information Overload

P8 supports two distinct branches, not one combined F4-C systematic-search subfamily. Mental workload/cognitive workload is a measurable human-factors/software-development branch with direct programmer program-comprehension studies, although retrieval is noisy and population-sensitive. Information overload retrieved mostly general information-systems, communication, productivity, and unrelated software literature; it remains supplementary rather than a primary professional software-engineering branch. This is a search-design decision only and does not establish any effect of either construct.

## Decision On Documentation As An F4 Branch

Documentation is directly relevant enough to remain a primary F4-D branch, but only after narrowing its purpose. P8 title retrieval was relatively coherent and exposed documentation relevance, quality, navigation, maintenance, and explicit amount/usefulness terminology. Broad documentation relevance/maintenance searches were noisy, so later systematic searching must separate documentation quality/usefulness, maintenance, effort/cost, and task navigation rather than use `documentation overhead` as a single umbrella term. This does not imply documentation is beneficial, harmful, necessary, or optimal.

## Remaining Uncertainty After P8

- Title searches validate terminology and neighborhood boundaries but do not establish recall across databases or records using different titles.
- Requirements-quality properties remain entangled with F2 artifacts; later screening must define the information-quality object without duplicating artifact-only searches.
- Developer information-needs studies may measure seeking behavior, source selection, or ecosystem/API knowledge rather than whether information is sufficient for a bounded task.
- Mental workload studies vary in task, instrumentation, expertise, and outcome; professional, student, general human-factors, and neuroscience populations require separate extraction.
- The pilot did not establish a direct professional software-development information-overload corpus; later supplementary snowballing may still find one.
- Documentation studies may concern production, maintenance, navigation, quality, or consumption, and these should not be collapsed into one burden construct.
- Four P8 DOI checks returned OpenAlex HTTP 429 for Damian et al., Forward/Lethbridge, Dzidek et al., and Lientz et al.; their individual P8 statuses remain `Not verified`, despite earlier P7 metadata where applicable.
- No coding-agent-specific F4 search was executed. Transfer from human software-engineering and human-factors studies to coding agents remains open.

## F4 Exit Decision

**F4 subfamily structure sufficiently calibrated for systematic-search design**

The methodological reason is that P8 confirmed stable, distinguishable retrieval neighborhoods for F4-A information-quality properties, F4-B developer information needs/context, F4-C1 mental workload/cognitive burden, and F4-D documentation information/usefulness/maintenance. It also tested and separated F4-C2 information overload as a supplementary branch rather than forcing it into the mental-workload search. The branches have documented terminology, field behavior, noise boundaries, population limits, known-source statuses, and overlaps with F1/F2/F3. F4 pilot exploration can close; this does not freeze final systematic strings or derive any Work Item characteristic.

No Work Item characteristics or research conclusions were derived. No claim was made that more, less, sufficient, or documented information is preferable. F6 and F7 were not executed. No commit was made.

## Pilot Round 9 Family 6 Calibration

Pilot Round 9 was conducted on 2026-08-20 using arXiv API discovery searches and metadata/abstract inspection. The round was limited to F6. arXiv counts are source-reported discovery diagnostics, not estimates of prevalence, precision, recall, or evidence strength. Recent preprints were retained for terminology calibration and labeled as preprints unless the record identified a venue or publication status. No systematic search string was frozen, no F7 search was executed, and no Work Item characteristic or causal conclusion was derived.

### F6-A: Context And Repository Understanding

#### P9-F6A-01

- **Search ID:** `P9-F6A-01`
- **Date:** `2026-08-20`
- **Evidence stream:** Coding-agent-specific scientific discovery
- **Database / source:** arXiv API
- **Query:** `all:"software engineering agent" AND all:context`
- **Fields searched:** arXiv `all` fields
- **Filters:** None; first 10 sorted by relevance
- **Result count:** `18` reported by arXiv
- **Results inspected:** First 10 titles, abstracts, authors, dates, and available venue/DOI metadata
- **Clearly relevant results:** `On Problems of Implicit Context Compression for Software Engineering Agents` studies context-length limits and implicit context compression in multi-step coding tasks; `SWE-MeM` uses adaptive memory management in long-horizon SWE agents; `Training Long-Context, Multi-Turn Software Engineering Agents with Reinforcement Learning` treats the agent as interacting with a stateful environment; `Confucius Code Agent` describes context management, persistent notes, and tool use for large codebases. `TOM-SWE` adds user intent, interaction history, and persistent user memory.
- **Clearly irrelevant patterns:** Broad context retrieval also found position/document-analysis work and system architecture papers where `context` referred to user intent, training data, or governance rather than repository information.
- **Terminology discovered:** `context compression`, `implicit context compression`, `long-context software engineering agents`, `memory management`, `persistent memory`, `stateful environment`, `context management`, `interaction history`, `user mental modeling`.
- **Candidate seed sources:** Kirill Gelvan et al., `On Problems of Implicit Context Compression for Software Engineering Agents`, 2026, arXiv preprint, [arXiv:2605.11051](https://arxiv.org/abs/2605.11051); Shuzheng Gao et al., `SWE-MeM: Learning Adaptive Memory Management for Long-Horizon Coding Agents`, 2026, arXiv preprint, [arXiv:2606.28434](https://arxiv.org/abs/2606.28434); Sherman Wong et al., `Confucius Code Agent: Scalable Agent Scaffolding for Real-World Codebases`, 2025/2026 version, arXiv preprint, [arXiv:2512.10398](https://arxiv.org/abs/2512.10398). These are context/memory architecture or evaluation seeds; publication status and full text require later verification.
- **Known-source checks:** SWE-agent `Not applicable to this exact context query`; SWE-bench `Not applicable to this exact context query`; Agentless `Not applicable to this exact context query`; AIDev `Not applicable to this exact context query`; Understanding Software Engineering Agents `Not applicable to this exact context query`.
- **Clearly relevant known lineage:** No prior F5 seed was directly retrieved in the inspected first-page sample; this is not a claim of absence.
- **Query adjustment:** `"software engineering agent" AND context` → `18` records with context, memory, user-state, and architecture meanings → test repository/retrieval-qualified wording rather than treating `context` as one construct.
- **Rationale:** The initial query showed that context is a recognizable but internally heterogeneous neighborhood.
- **Notes:** The query was useful for discovery, not for deciding whether more or less context is preferable. `TOM-SWE` concerns a dual-agent architecture and stateful/user context, not only repository context.

#### P9-F6A-02

- **Search ID:** `P9-F6A-02`
- **Date:** `2026-08-20`
- **Evidence stream:** Coding-agent-specific scientific discovery
- **Database / source:** arXiv API
- **Query:** `all:"software engineering agent" AND (all:"repository understanding" OR all:retrieval OR all:"repository context")`
- **Fields searched:** arXiv `all` fields
- **Filters:** None; first 10 sorted by relevance
- **Result count:** `4` reported by arXiv
- **Results inspected:** All 4 titles, abstracts, authors, dates, and available metadata
- **Clearly relevant results:** `Structurally Aligned Subtask-Level Memory for Software Engineering Agents` uses memory storage/retrieval/update aligned to functional decomposition and evaluates on SWE-bench Verified; `OwlPath` uses structural code retrieval and repository knowledge maps for SWE-bench Pro; `GHIssuemarket` uses a retrieval-augmented interface in a controlled SWE-agent environment.
- **Clearly irrelevant patterns:** The query still retrieved a broad intent-centric position paper; exact repository terminology was sparse compared with `context`, `memory`, and `retrieval` wording.
- **Terminology discovered:** `repository-level understanding`, `repository exploration`, `structural code retrieval`, `knowledge compression`, `software knowledge map`, `repository dependency understanding`, `retrieval-augmented generation`, `repository navigation`, `functional decomposition`.
- **Candidate seed sources:** Kangning Shen et al., `Structurally Aligned Subtask-Level Memory for Software Engineering Agents`, 2026, arXiv preprint, [arXiv:2602.21611](https://arxiv.org/abs/2602.21611); Bo Zhang et al., `OwlPath: Lossless Knowledge Compression for LLM Bug Repair`, 2026, arXiv preprint, [arXiv:2607.27249](https://arxiv.org/abs/2607.27249). Both are direct context/retrieval seeds; benchmark settings and status require later screening.
- **Known-source checks:** SWE-agent `Missed`; SWE-bench `Not applicable as a benchmark source rather than a context study`; Agentless `Not applicable to this repository-retrieval query`; AIDev `Not applicable`; Understanding Software Engineering Agents `Not applicable`. `SWE-agent` was not retrieved by this revised phrase query despite being a known repository-navigation source.
- **Query adjustment:** `"software engineering agent" AND context` → context query mixed memory, user state, and long-context training → `"software engineering agent" AND ("repository understanding" OR retrieval OR "repository context")` → four records and a narrower retrieval/navigation neighborhood.
- **Rationale:** The revision separates repository/code retrieval from general context and exposes that `repository understanding` is less frequent than operational terms such as retrieval, exploration, navigation, memory, and structural code access.
- **Notes:** `OwlPath` and `Structurally Aligned Subtask-Level Memory` are preprints in the inspected records. Their reported benchmark results are not generalized beyond their stated settings.

### F6-B: Planning And Task Decomposition

#### P9-F6B-01

- **Search ID:** `P9-F6B-01`
- **Date:** `2026-08-20`
- **Evidence stream:** Coding-agent-specific scientific discovery
- **Database / source:** arXiv API
- **Query:** `all:"software engineering agent" AND all:planning`
- **Fields searched:** arXiv `all` fields
- **Filters:** None; first 10 sorted by relevance
- **Result count:** `10` reported by arXiv
- **Results inspected:** All 10 titles, abstracts, authors, dates, and available venue metadata
- **Clearly relevant results:** `HyperAgent` explicitly separates Planner, Navigator, Code Editor, and Executor roles across SWE tasks; `PatchPilot` distinguishes agent-based planning from rule-based planning in software patching; `DCAS` distinguishes explicit pre-execution plans from implicit scaffold planning and describes a plan-source intervention; `TOM-SWE` includes planning among agent capabilities; `Agentless` is a direct boundary source because it removes autonomous future-action selection while retaining a fixed three-phase workflow.
- **Clearly irrelevant patterns:** Planning also referred to environment setup, training, or generic agent architecture. The result set did not make planning a uniform intervention or outcome variable.
- **Terminology discovered:** `explicit planning`, `implicit planning`, `plan-source intervention`, `planning structure`, `agent-based planning`, `rule-based planning`, `planner`, `multi-stage workflow`, `task plans`, `dependency-aware task plans`.
- **Candidate seed sources:** Kishanthan Thangarajah et al., `DCAS: Decoupling CLI Agent Scaffolding to Internalize Planning across Scaffolds`, 2026, arXiv preprint, [arXiv:2608.06113](https://arxiv.org/abs/2608.06113); Huy Nhat Phan et al., `HyperAgent: Generalist Software Engineering Agents to Solve Coding Tasks at Scale`, 2024/2025 version, arXiv preprint, [arXiv:2409.16299](https://arxiv.org/abs/2409.16299); Hongwei Li et al., `PatchPilot: A Cost-Efficient Software Engineering Agent with Early Attempts on Formal Verification`, 2025, arXiv preprint, [arXiv:2502.02747](https://arxiv.org/abs/2502.02747). These represent planning architecture and planning comparison traditions, not a settled planning-effect claim.
- **Known-source checks:** SWE-agent `Not applicable to this planning query`; SWE-bench `Not applicable`; Agentless `Retrieved` as a planning boundary/comparison source; AIDev `Not applicable`; Understanding Software Engineering Agents `Not applicable`.
- **Query adjustment:** None for this first focused query; the sample was sufficiently informative to justify a decomposition-qualified revision.
- **Rationale:** `planning` is visibly used as both an architectural module and an empirically manipulated or analyzed process, so planning architecture and planning effectiveness must remain separate during later screening.
- **Notes:** HyperAgent and PatchPilot are agent-system/benchmark studies; `Agentless` is not a coding-agent population equivalent to autonomous SWE agents and is retained as a comparator boundary.

#### P9-F6B-02

- **Search ID:** `P9-F6B-02`
- **Date:** `2026-08-20`
- **Evidence stream:** Coding-agent-specific scientific discovery
- **Database / source:** arXiv API
- **Query:** `all:"software engineering agent" AND (all:decomposition OR all:"coding plan" OR all:"task planning")`
- **Fields searched:** arXiv `all` fields
- **Filters:** None; first 10 sorted by relevance
- **Result count:** `3` reported by arXiv
- **Results inspected:** All 3 titles, abstracts, authors, dates, and available metadata
- **Clearly relevant results:** `Structurally Aligned Subtask-Level Memory` explicitly links retrieval/update to functional decomposition; `Effective Strategies for Asynchronous Software Engineering Agents` constructs dependency-aware task plans, delegates subtasks, and evaluates multi-agent coordination on PaperBench and Commit0; `Agent-Computer Observation Interfaces Enable Dynamic Computer Use` was adjacent interface/decomposition material rather than a direct software-task decomposition study.
- **Clearly irrelevant patterns:** The small set mixed agent functional decomposition, multi-agent delegation, and computer-use interface decomposition. Traditional F3 decomposition terms were not dominant.
- **Terminology discovered:** `functional decomposition`, `subtask-level`, `dependency-aware task plans`, `centralized task delegation`, `subtask execution`, `isolated workspaces`, `multi-agent coordination`, `branch-and-merge`.
- **Candidate seed sources:** Jiayi Geng and Graham Neubig, `Effective Strategies for Asynchronous Software Engineering Agents`, 2026, arXiv preprint, [arXiv:2603.21489](https://arxiv.org/abs/2603.21489); Kangning Shen et al., `Structurally Aligned Subtask-Level Memory for Software Engineering Agents`, 2026, arXiv preprint, [arXiv:2602.21611](https://arxiv.org/abs/2602.21611). The first is a multi-agent task delegation/planning seed; the second is a functional-decomposition/context seed.
- **Known-source checks:** SWE-agent `Missed`; SWE-bench `Not applicable`; Agentless `Not applicable`; AIDev `Not applicable`; Understanding Software Engineering Agents `Not applicable`.
- **Query adjustment:** `"software engineering agent" AND planning` → planning results mixed modules, fixed workflows, and explicit/implicit plans → `"software engineering agent" AND (decomposition OR "coding plan" OR "task planning")` → three records focused on functional decomposition, subtask delegation, and planning-related interfaces.
- **Rationale:** The revision shows that agent decomposition is retrievable, but it is not the same tradition as F3 human/project decomposition or issue decomposition. It should be screened as agent functional decomposition, delegation, or multi-agent coordination.
- **Notes:** The result count is too small to establish branch maturity. No claim was made about whether decomposition or multi-agent planning improves outcomes.

### F6-C: Clarification, Ambiguity Resolution, And Interactive Assistance

#### P9-F6C-01

- **Search ID:** `P9-F6C-01`
- **Date:** `2026-08-20`
- **Evidence stream:** Coding-agent-specific scientific discovery
- **Database / source:** arXiv API
- **Query:** `all:"coding agent" AND all:clarification`
- **Fields searched:** arXiv `all` fields
- **Filters:** None; first 10 sorted by relevance
- **Result count:** `8` reported by arXiv
- **Results inspected:** All 8 titles, abstracts, authors, dates, and available venue metadata
- **Clearly relevant results:** `Ask or Assume? Uncertainty-Aware Clarification-Seeking in Coding Agents` evaluates clarification seeking on underspecified SWE-bench Verified; `ClarEval` defines clarification metrics including Average Turns to Clarify and Key Question Coverage; `SWE-RPG` separates requirement clarification and implementation planning in repository-level trajectories; `ICAE-Bench` evaluates interactive project building from fuzzy product requirements. `UnderSpecBench` is a related safety/ambiguity boundary benchmark for DevOps coding agents.
- **Clearly irrelevant patterns:** `ProCAD` concerns text-to-CAD rather than repository-level software engineering; other results used clarification in domain-specific synthesis or specification settings.
- **Terminology discovered:** `clarification-seeking`, `uncertainty-aware clarification`, `requirement clarification`, `requirement elicitation`, `underspecified instructions`, `ambiguous instructions`, `interactive coding agents`, `dialogue-driven coding agents`, `user simulator`, `implicit requirement recovery`, `action-boundary violations`, `deferment`.
- **Candidate seed sources:** Nicholas Edwards and Sebastian Schuster, `Ask or Assume? Uncertainty-Aware Clarification-Seeking in Coding Agents`, 2026, arXiv preprint, [arXiv:2603.26233](https://arxiv.org/abs/2603.26233); Jialin Li et al., `ClarEval: A Benchmark for Evaluating Clarification Skills of Code Agents under Ambiguous Instructions`, 2026, arXiv preprint, [arXiv:2603.00187](https://arxiv.org/abs/2603.00187); Xin Zhou et al., `A Unified Issue Resolution Benchmark for Requirement Clarification, Planning, and Code Generation for Coding Agents`, 2026, arXiv preprint, [arXiv:2608.09072](https://arxiv.org/abs/2608.09072); Brendan King and Jeffrey Flanigan, `Dialogue SWE-Bench: A Benchmark for Dialogue-Driven Coding Agents`, 2026, arXiv preprint, [arXiv:2606.13995](https://arxiv.org/abs/2606.13995).
- **Known-source checks:** SWE-agent `Not applicable to this clarification query`; SWE-bench `Retrieved as the benchmark family underlying clarification variants, not as a clarification study`; Agentless `Retrieved as a non-interactive benchmark boundary source`; AIDev `Not applicable`; Understanding Software Engineering Agents `Not applicable`.
- **Query adjustment:** None. The exact `clarification` query returned a compact and directly relevant coding-agent neighborhood.
- **Rationale:** Clarification is now identifiable as a distinct, recent research branch, but its evidence base is benchmark-heavy and largely preprint-based in this pilot.
- **Notes:** Clarification capability must be distinguished from the benchmark's interaction design. Standard SWE-bench-style tasks generally do not provide a user dialogue channel; the newer variants explicitly add ambiguity, user simulation, or intermediate reference annotations.

#### P9-F6C-02

- **Search ID:** `P9-F6C-02`
- **Date:** `2026-08-20`
- **Evidence stream:** Coding-agent-specific scientific discovery
- **Database / source:** arXiv API
- **Query:** `all:"coding agent" AND (all:ambiguity OR all:"human-agent interaction" OR all:"interactive coding")`
- **Fields searched:** arXiv `all` fields
- **Filters:** None; first 10 sorted by relevance
- **Result count:** `34` reported by arXiv
- **Results inspected:** First 10 titles, abstracts, authors, dates, and available venue metadata
- **Clearly relevant results:** `Dialogue SWE-Bench` treats dialogue as a separate coding-agent capability; `ClarEval` injects missing goals, premises, and ambiguous terminology; `Humans are Missing from AI Coding Agent Research` frames task alignment, steerability, adaptability, and verifiability as interaction dimensions; `Software Delegation Contracts` studies assigned work under bounded authority and reviewability; `ICAE-Bench` adds a user simulator for fuzzy requirements.
- **Clearly irrelevant patterns:** The broader query included AppWorld's general interactive coding environment and specification/agentic-synthesis papers outside repository-level coding-agent clarification.
- **Terminology discovered:** `task alignment`, `steerability`, `adaptability`, `human-agent task-solving loop`, `dialogue quality`, `interactive project building`, `user simulator`, `bounded authority`, `delegation contract`, `specification refinement`, `underspecification`.
- **Candidate seed sources:** Zora Z. Wang et al., `Humans are Missing from AI Coding Agent Research`, 2026, arXiv position paper, [arXiv:2608.12355](https://arxiv.org/abs/2608.12355); Brendan King and Jeffrey Flanigan, `Dialogue SWE-Bench: A Benchmark for Dialogue-Driven Coding Agents`, 2026, arXiv preprint, [arXiv:2606.13995](https://arxiv.org/abs/2606.13995); Vincent Schmalbach, `Software Delegation Contracts: Measuring Reviewability in AI Coding-Agent Work`, 2026, arXiv empirical preprint, [arXiv:2606.17099](https://arxiv.org/abs/2606.17099). These extend clarification into interaction, authority, and reviewability; they should not be treated as equivalent constructs.
- **Known-source checks:** SWE-agent `Missed`; SWE-bench `Retrieved as a benchmark lineage/boundary, not an interactive study`; Agentless `Retrieved as a non-interactive comparator`; AIDev `Not applicable`; Understanding Software Engineering Agents `Not applicable`.
- **Query adjustment:** `"coding agent" AND clarification` → compact direct clarification neighborhood → add `ambiguity`, `human-agent interaction`, and `interactive coding` → 34 broader records exposing dialogue, alignment, steerability, authority, and substantial adjacent-domain noise.
- **Rationale:** The revision shows that `clarification` does not cover the full interaction literature; however, the added terms must remain separate because interaction quality, task alignment, authority, and ambiguity resolution are not synonyms.
- **Notes:** This branch is suitable for a dedicated systematic search only if benchmark interaction design and agent population are extracted explicitly.

### F6-D: Autonomy, Tool Use, And Agent-Environment Interaction

#### P9-F6D-01

- **Search ID:** `P9-F6D-01`
- **Date:** `2026-08-20`
- **Evidence stream:** Coding-agent-specific scientific discovery
- **Database / source:** arXiv API
- **Query:** `all:"software engineering agent" AND (all:autonomy OR all:"tool use" OR all:trajectory)`
- **Fields searched:** arXiv `all` fields
- **Filters:** None; first 10 sorted by relevance
- **Result count:** `39` reported by arXiv
- **Results inspected:** First 10 titles, abstracts, authors, dates, and available venue metadata
- **Clearly relevant results:** `Understanding Software Engineering Agents` analyzes 120 thought-action-result trajectories from RepairAgent, AutoCodeRover, and OpenHands; `SeaView` studies visualization of SWE-agent trajectories and environment/model problems; `Enconda-bench` evaluates process-level environment-configuration trajectories; `SWE-World` models the agent-environment loop; `Same Signal, Different Semantics` compares trajectory behavior across 126 configurations and 43 frameworks.
- **Clearly irrelevant patterns:** `autonomy` and `tool use` also retrieved training frameworks, generic agent infrastructure, and non-repository computer-use material. The same trajectory feature may not have the same interpretation across agent frameworks.
- **Terminology discovered:** `thought-action-result trajectory`, `agent trajectory`, `agent-environment interaction`, `tool-mediated trajectory`, `process-level trajectory evaluation`, `environment configuration`, `action space`, `framework effects`, `autonomous software engineering`, `multi-turn environment`.
- **Candidate seed sources:** Islem Bouzenia and Michael Pradel, `Understanding Software Engineering Agents: A Study of Thought-Action-Result Trajectories`, 2025, arXiv record stating ASE 2025 acceptance, [arXiv:2506.18824](https://arxiv.org/abs/2506.18824); Jiayi Kuang et al., `Process-Level Trajectory Evaluation for Environment Configuration in Software Engineering Agents`, 2025, arXiv preprint, [arXiv:2510.25694](https://arxiv.org/abs/2510.25694); Wei Ma et al., `Same Signal, Different Semantics: A Cross-Framework Behavioral Analysis of Software Engineering Agents`, 2026, arXiv preprint, [arXiv:2605.18332](https://arxiv.org/abs/2605.18332). These are trajectory/process-analysis seeds, not direct measures of a single autonomy construct.
- **Known-source checks:** SWE-agent `Retrieved` through the software-engineering-agent trajectory neighborhood; SWE-bench `Retrieved as the main benchmark context for several trajectory studies`; Agentless `Retrieved as an autonomy/tool-use boundary source`; AIDev `Not applicable to this trajectory query`; Understanding Software Engineering Agents `Retrieved`.
- **Query adjustment:** None. The combined autonomy/tool-use/trajectory query returned enough direct trajectory and environment terminology to assess the branch.
- **Rationale:** The literature operationalizes autonomy indirectly through whether an agent selects future actions, invokes tools, observes feedback, and continues in an environment. Trajectory analysis is a useful execution-record concept, but not automatically a measure of reasoning quality or autonomy level.
- **Notes:** `Same Signal, Different Semantics` is especially relevant to later construct validity because it reports framework-dependent behavior in the inspected abstract. This observation remains source-specific and is not generalized beyond that study.

#### P9-F6D-02

- **Search ID:** `P9-F6D-02`
- **Date:** `2026-08-20`
- **Evidence stream:** Coding-agent-specific scientific discovery
- **Database / source:** arXiv API
- **Query:** `all:"agent-computer interface" AND all:software`
- **Fields searched:** arXiv `all` fields
- **Filters:** None; first 10 sorted by relevance
- **Result count:** `3` reported by arXiv
- **Results inspected:** All 3 titles, abstracts, authors, dates, and available metadata
- **Clearly relevant results:** `SWE-agent: Agent-Computer Interfaces Enable Automated Software Engineering` directly describes an ACI for repository navigation, code editing, and test execution and evaluates on SWE-bench and HumanEvalFix.
- **Clearly irrelevant patterns:** The query also retrieved a healthcare operating-system interface and a general autonomous training interface. `Agent-computer interface` is therefore a useful but architecture-specific term, not a general autonomy synonym.
- **Terminology discovered:** `agent-computer interface (ACI)`, `repository navigation`, `code editing`, `test execution`, `interface design`, `tool-mediated execution`, `CLI scaffold`, `environment interface`.
- **Candidate seed sources:** John Yang et al., `SWE-agent: Agent-Computer Interfaces Enable Automated Software Engineering`, 2024, arXiv preprint record, [arXiv:2405.15793](https://arxiv.org/abs/2405.15793); the record is a core ACI seed and identifies SWE-bench/HumanEvalFix settings. Peer-reviewed status should be verified in later screening.
- **Known-source checks:** SWE-agent `Retrieved`; SWE-bench `Retrieved as the evaluation benchmark named by the seed`; Agentless `Not applicable to this ACI title query`; AIDev `Not applicable`; Understanding Software Engineering Agents `Not applicable to this ACI title query`.
- **Query adjustment:** `"software engineering agent" AND (autonomy OR "tool use" OR trajectory)` → broad trajectory/process neighborhood → `"agent-computer interface" AND software` → three records and a narrow architecture/interface check.
- **Rationale:** The revision isolates the established F5 interface term and demonstrates that it should be searched separately from autonomy and trajectory rather than used as a universal label.
- **Notes:** The ACI query is a known-item and architecture calibration, not a population-complete autonomy search.

## P9 Query Evolution Records

- **Date:** `2026-08-20`
- **Search family:** F6-A context and repository understanding
- **Original query:** `all:"software engineering agent" AND all:context`
- **Observation:** `18` records mixed context compression, memory, user state, long-context training, and repository/tool context.
- **Revised query:** `all:"software engineering agent" AND (all:"repository understanding" OR all:retrieval OR all:"repository context")`
- **Rationale:** Separate repository/code retrieval from general context and test whether `repository understanding` is an established author term.
- **Affected database(s):** arXiv
- **Search IDs:** `P9-F6A-01`, `P9-F6A-02`

- **Date:** `2026-08-20`
- **Search family:** F6-B planning and decomposition
- **Original query:** `all:"software engineering agent" AND all:planning`
- **Observation:** `10` records mixed planner modules, rule-based workflows, explicit plans, implicit scaffold behavior, and environment setup.
- **Revised query:** `all:"software engineering agent" AND (all:decomposition OR all:"coding plan" OR all:"task planning")`
- **Rationale:** Test agent functional decomposition and task delegation separately from generic planning architecture.
- **Affected database(s):** arXiv
- **Search IDs:** `P9-F6B-01`, `P9-F6B-02`

- **Date:** `2026-08-20`
- **Search family:** F6-C clarification and interactive assistance
- **Original query:** `all:"coding agent" AND all:clarification`
- **Observation:** `8` records formed a compact clarification/requirement-elicitation neighborhood, but did not cover dialogue, authority, or broader interaction terminology.
- **Revised query:** `all:"coding agent" AND (all:ambiguity OR all:"human-agent interaction" OR all:"interactive coding")`
- **Rationale:** Test adjacent author vocabulary while preserving clarification as a separate construct.
- **Affected database(s):** arXiv
- **Search IDs:** `P9-F6C-01`, `P9-F6C-02`

- **Date:** `2026-08-20`
- **Search family:** F6-D autonomy, tool use, and agent-environment interaction
- **Original query:** `all:"software engineering agent" AND (all:autonomy OR all:"tool use" OR all:trajectory)`
- **Observation:** `39` records exposed trajectory/process analysis, environment interaction, and framework-dependent behavior, but also broad agent infrastructure.
- **Revised query:** `all:"agent-computer interface" AND all:software`
- **Rationale:** Run a narrow known-lineage/interface check for ACI terminology rather than treating it as equivalent to autonomy or tool use.
- **Affected database(s):** arXiv
- **Search IDs:** `P9-F6D-01`, `P9-F6D-02`

No P9 query was silently replaced. No final systematic search string was frozen.

## P9 Terminology Registry Recalibration

The existing F5/F4/F3 rows remain canonical. P9 materially recalibrated the following existing rows in place: `agent-computer interface (ACI)` is retained as an architecture-specific F6-D term; `agent trajectory / tool-mediated trajectory` is retained as an execution-record term and explicitly not a reasoning-quality synonym; `SWE-bench` remains a benchmark-context term; `coding plans` and `requirement-driven task decomposition` remain separate from human/project decomposition; `program comprehension` remains an F4 bridge and was not promoted to repository understanding. New canonical terms discovered in P9 are listed once below.

| Term | Related concept | Source / Search ID | Context | Action | Notes |
|---|---|---|---|---|---|
| context compression | agent context maintenance | P9-F6A-01, P10-F6A1-01 | Software-engineering agents | test provisionally | Includes implicit context compression and long-horizon context bottlenecks; do not equate with context selection or amount. |
| implicit context compression | agent context maintenance | P9-F6A-01 | Software-engineering agents | investigate separately | Specific wording from a recent preprint; retain as a failure/method term. |
| memory management | agent context maintenance | P9-F6A-01, P9-F6A-02, P10-F6A1-01 | Long-horizon SWE agents | test provisionally | Covers storage, retrieval, update, and compression; distinct from repository retrieval. |
| persistent memory | agent context/state | P9-F6A-01 | SWE agents and user modeling | retain as contextual term | May refer to user state, repository/task state, or cross-session memory. |
| repository exploration | repository understanding | P9-F6A-02, P9-F6D-01, P10-F6A2-01, P10-F6D1-01 | Repository-level SWE tasks | retain as primary contextual term | Operational term more frequently visible than `repository understanding` in inspected records; P10 separates retrieval/navigation from environment interaction. |
| structural code retrieval | repository context selection | P9-F6A-02, P10-F6A2-01 | Code intelligence and SWE-bench Pro | test provisionally | Keep separate from generic code retrieval and memory. |
| knowledge compression | repository context representation | P9-F6A-02 | Repository retrieval | investigate separately | Source-specific/architecture term; includes structured repository maps. |
| software knowledge map | repository context representation | P9-F6A-02 | Structural repository retrieval | investigate separately | Architecture-specific term from OwlPath. |
| functional decomposition | agent task decomposition | P9-F6B-02, P10-F6B2-01 | SWE-agent memory/planning | test provisionally | Agent-side decomposition; not equivalent to F3 project decomposition or explicit planning. |
| explicit planning | agent planning | P9-F6B-01, P10-F6B1-01 | SWE-agent scaffolds | test provisionally | Plan as a first-class pre-execution artifact. |
| implicit planning | agent planning | P9-F6B-01, P10-F6B1-01 | SWE-agent scaffolds | test provisionally | Structural conventions in an agent loop; distinct from an explicit plan. |
| plan-source intervention | planning evaluation | P9-F6B-01 | Cross-scaffold agent evaluation | investigate separately | Evaluation vocabulary, not a planning synonym. |
| dependency-aware task plans | multi-agent planning | P9-F6B-02, P10-F6B2-01 | Multi-agent software development | test provisionally | Connects planning with delegation and integration; retain separate from decomposition. |
| centralized task delegation | multi-agent software development | P9-F6B-02 | PaperBench/Commit0-style environments | investigate separately | Delegation/coordination term, not clarification or autonomy itself. |
| clarification-seeking | agent interaction | P9-F6C-01, P10-F6C1-01 | Underspecified coding tasks | retain as primary F6-C term | More direct than generic `clarification`; preserve uncertainty-detection context. |
| requirement elicitation | agent interaction/specification refinement | P9-F6C-01, P9-F6C-02 | Ambiguous coding tasks | test provisionally | Adjacent requirements tradition; do not collapse with user dialogue quality. |
| underspecified instructions | ambiguity/interaction | P9-F6C-01, P9-F6C-02 | Coding-agent benchmarks | retain as primary contextual term | Benchmark/task condition, not a Work Item characteristic. |
| dialogue-driven coding agents | interactive coding | P9-F6C-02, P10-F6C1-01 | Dialogue SWE-Bench | test provisionally | Population/evaluation label; distinct from autonomous benchmark agents. |
| user simulator | interactive benchmark design | P9-F6C-01, P9-F6C-02 | Interactive coding benchmarks | retain as contextual term | Indicates that clarification is enabled by the evaluation design. |
| task alignment | human-agent interaction | P9-F6C-02 | Coding-agent interaction | test provisionally | Separate from clarification, steerability, and verification. |
| steerability | human-agent interaction | P9-F6C-02 | Human-centered coding agents | test provisionally | Interaction construct; not equivalent to autonomy. |
| bounded authority | agent autonomy/control | P9-F6C-02 | Delegated coding work | retain as contextual term | Describes authority boundaries without defining a scalar autonomy level. |
| action-boundary violation | underspecification safety | P9-F6C-01 | DevOps coding-agent benchmark | investigate separately | Safety outcome and benchmark-specific term. |
| process-level trajectory evaluation | agent execution analysis | P9-F6D-01, P10-F6D2-01 | SWE-agent environments | retain as primary contextual term | Evaluates intermediate execution records in addition to end outcomes. |
| agent-environment interaction | tool-mediated execution | P9-F6D-01, P10-F6D1-01 | SWE agents | retain as primary contextual term | Broader than tool use; includes observations, feedback, and stateful environments. |
| framework effects | agent trajectory validity | P9-F6D-01 | Cross-framework SWE-agent analysis | retain as contextual term | Relevant to transferability of trajectory metrics across scaffolds. |
| action space | agent interface/tool design | P9-F6D-01 | Agent-environment interaction | test provisionally | Keep separate from autonomy and ACI. |

## P9 Candidate Seed Sources

The following sources were inspected sufficiently for F6 terminology, population, setting, or benchmark relevance. They are candidate seeds for later screening, not included evidence or synthesized findings.

| Source | Year and status | DOI or stable URL | Search ID | F6 relevance |
|---|---:|---|---|---|
| Gelvan et al., `On Problems of Implicit Context Compression for Software Engineering Agents` | 2026, arXiv preprint | [arXiv:2605.11051](https://arxiv.org/abs/2605.11051) | `P9-F6A-01` | Context compression and multi-step agent failure terminology. |
| Gao et al., `SWE-MeM: Learning Adaptive Memory Management for Long-Horizon Coding Agents` | 2026, arXiv preprint | [arXiv:2606.28434](https://arxiv.org/abs/2606.28434) | `P9-F6A-01` | Adaptive memory management, trajectory state, SWE-bench Verified. |
| Wong et al., `Confucius Code Agent: Scalable Agent Scaffolding for Real-World Codebases` | 2025/2026, arXiv preprint/version | [arXiv:2512.10398](https://arxiv.org/abs/2512.10398) | `P9-F6A-01` | Large-codebase context management, persistent notes, tools, SWE-Bench-Pro. |
| Shen et al., `Structurally Aligned Subtask-Level Memory for Software Engineering Agents` | 2026, arXiv preprint | [arXiv:2602.21611](https://arxiv.org/abs/2602.21611) | `P9-F6A-02`, `P9-F6B-02` | Retrieval/memory granularity aligned to agent functional decomposition; SWE-bench Verified. |
| Zhang et al., `OwlPath: Lossless Knowledge Compression for LLM Bug Repair` | 2026, arXiv preprint | [arXiv:2607.27249](https://arxiv.org/abs/2607.27249) | `P9-F6A-02` | Structural repository retrieval and knowledge maps; SWE-bench Pro. |
| Thangarajah et al., `DCAS: Decoupling CLI Agent Scaffolding to Internalize Planning across Scaffolds` | 2026, arXiv preprint | [arXiv:2608.06113](https://arxiv.org/abs/2608.06113) | `P9-F6B-01` | Explicit versus implicit planning and cross-scaffold evaluation. |
| Phan et al., `HyperAgent: Generalist Software Engineering Agents to Solve Coding Tasks at Scale` | 2024/2025, arXiv preprint/version | [arXiv:2409.16299](https://arxiv.org/abs/2409.16299) | `P9-F6B-01` | Planner/Navigator/Editor/Executor multi-agent architecture; SWE-bench, RepoExec, Defects4J. |
| Li et al., `PatchPilot: A Cost-Efficient Software Engineering Agent with Early Attempts on Formal Verification` | 2025, arXiv preprint | [arXiv:2502.02747](https://arxiv.org/abs/2502.02747) | `P9-F6B-01` | Agent-based versus rule-based planning in patching; SWE-bench. |
| Geng and Neubig, `Effective Strategies for Asynchronous Software Engineering Agents` | 2026, arXiv preprint | [arXiv:2603.21489](https://arxiv.org/abs/2603.21489) | `P9-F6B-02` | Dependency-aware task plans, delegation, isolated workspaces; PaperBench and Commit0. |
| Edwards and Schuster, `Ask or Assume? Uncertainty-Aware Clarification-Seeking in Coding Agents` | 2026, arXiv preprint | [arXiv:2603.26233](https://arxiv.org/abs/2603.26233) | `P9-F6C-01` | Clarification-seeking on underspecified SWE-bench Verified variants. |
| Li et al., `ClarEval: A Benchmark for Evaluating Clarification Skills of Code Agents under Ambiguous Instructions` | 2026, arXiv preprint | [arXiv:2603.00187](https://arxiv.org/abs/2603.00187) | `P9-F6C-01`, `P9-F6C-02` | Clarification benchmark and ATC/KQC metrics. |
| Zhou et al., `A Unified Issue Resolution Benchmark for Requirement Clarification, Planning, and Code Generation for Coding Agents` | 2026, arXiv preprint | [arXiv:2608.09072](https://arxiv.org/abs/2608.09072) | `P9-F6C-01` | Intermediate clarification/planning references across repository-level tasks. |
| King and Flanigan, `Dialogue SWE-Bench: A Benchmark for Dialogue-Driven Coding Agents` | 2026, arXiv preprint | [arXiv:2606.13995](https://arxiv.org/abs/2606.13995) | `P9-F6C-01`, `P9-F6C-02` | Dialogue-enabled evaluation and user simulation. |
| Wang et al., `Humans are Missing from AI Coding Agent Research` | 2026, arXiv position paper | [arXiv:2608.12355](https://arxiv.org/abs/2608.12355) | `P9-F6C-02` | Human-agent interaction terminology: alignment, steerability, adaptability. |
| Bouzenia and Pradel, `Understanding Software Engineering Agents: A Study of Thought-Action-Result Trajectories` | 2025, arXiv record states ASE 2025 acceptance | [arXiv:2506.18824](https://arxiv.org/abs/2506.18824) | `P9-F6D-01` | Empirical trajectory analysis of RepairAgent, AutoCodeRover, and OpenHands. |
| Kuang et al., `Process-Level Trajectory Evaluation for Environment Configuration in Software Engineering Agents` | 2025, arXiv preprint | [arXiv:2510.25694](https://arxiv.org/abs/2510.25694) | `P9-F6D-01` | Process-level environment interaction and Enconda-bench. |
| Ma et al., `Same Signal, Different Semantics: A Cross-Framework Behavioral Analysis of Software Engineering Agents` | 2026, arXiv preprint | [arXiv:2605.18332](https://arxiv.org/abs/2605.18332) | `P9-F6D-01` | Framework sensitivity of trajectory behavior across 43 frameworks. |
| Yang et al., `SWE-agent: Agent-Computer Interfaces Enable Automated Software Engineering` | 2024, arXiv preprint record | [arXiv:2405.15793](https://arxiv.org/abs/2405.15793) | `P9-F6D-02` | ACI, repository navigation, editing, test execution; SWE-bench and HumanEvalFix. |

## P9 Calibration Assessment

### Conceptual coherence

- **F6-A:** Moderate to high after separating general context, memory/state, repository exploration, retrieval, and context compression. `Context management` is not a single construct in the inspected literature.
- **F6-B:** Moderate. Planning is recognizable, but explicit plans, implicit scaffold planning, functional decomposition, task delegation, and multi-agent coordination have different units of analysis.
- **F6-C:** Moderate and rapidly developing. Clarification-seeking, requirement elicitation, dialogue, ambiguity handling, and interaction quality form a related neighborhood but are not interchangeable.
- **F6-D:** High as an execution/interface neighborhood, but autonomy itself is not consistently operationalized as a common scalar or intervention. Tool use, ACI, environment interaction, and trajectory analysis should be distinct search concepts.

### Retrieval coherence

- **F6-A:** `context` retrieves a useful but heterogeneous neighborhood; repository-qualified revision was small and shifted toward retrieval, structural code access, and memory. `repository understanding` was less common than operational vocabulary.
- **F6-B:** `planning` is retrievable and produces agent architectures, workflow comparisons, and trajectory/training studies. Decomposition-qualified searching is smaller and tends toward functional decomposition or multi-agent delegation.
- **F6-C:** Exact clarification searching was the cleanest branch in this round. Broader interaction/ambiguity searching increases coverage but also retrieves adjacent CAD, general interactive agents, and specification work.
- **F6-D:** Trajectory and ACI searches retrieve recognizable SWE-agent research, but autonomy/tool-use terms retain broad agent infrastructure noise. ACI is high precision for a lineage, not high recall for all tool/environment work.

### Empirical maturity and evidence type

- **F6-A:** Mainly recent system descriptions, benchmark evaluations, and preprints; some direct empirical ablations/evaluations of memory or retrieval are visible, but publication status and replication require later screening.
- **F6-B:** Mainly architecture descriptions and benchmark comparisons, with newer cross-scaffold or planning-intervention work. Planning modules alone are not evidence of planning effectiveness.
- **F6-C:** A small but identifiable benchmark/empirical branch, currently dominated by recent preprints and custom benchmarks that explicitly add interaction or ambiguity.
- **F6-D:** More mature than F6-C in trajectory/interface terminology, including an ASE-accepted trajectory study record and cross-framework observational analysis, but construct validity remains framework- and environment-dependent.

### Agent-population scope

- Autocomplete and code-completion systems were not the dominant population in P9.
- Conversational coding assistants appear mainly in F6-C interaction/benchmark material and are not equivalent to autonomous SWE agents.
- Tool-using repository-level SWE agents, including SWE-agent, OpenHands, RepairAgent, AutoCodeRover, and related systems, dominate F6-A, F6-B, and F6-D.
- Autonomous/semi-autonomous agents are usually defined operationally by future-action selection, tool invocation, environment feedback, and multi-step execution rather than by a shared autonomy scale.
- Multi-agent software-development systems appear most clearly in F6-B through planner/delegator/subtask coordination; they should be labeled separately from single-agent scaffolds.

### Benchmark dependence and setting

- SWE-bench and SWE-bench Verified dominate repository-level bug-fixing and clarification variants in the inspected sample. SWE-bench Pro, SWE-Gym, HumanEvalFix, RepoExec, Defects4J, PaperBench, Commit0, and custom environments provide additional settings.
- Standard SWE-bench-style execution is generally issue-to-patch evaluation with repository/tool access and no ordinary user clarification loop. The exact interaction affordances must be extracted per benchmark rather than inferred from the benchmark name.
- Clarification studies use modified SWE-bench tasks, underspecified variants, user simulators, or new benchmarks such as ClarEval, SWE-RPG, Dialogue SWE-Bench, and ICAE-Bench. These settings cannot be silently pooled with non-interactive SWE-bench results.
- Trajectory studies often evaluate logs after or during execution. A trajectory feature is an execution-record descriptor; it is not automatically a reasoning-quality or autonomy measure.

### Relationship to prior families

- **F3:** F6-B overlaps `coding plans`, task decomposition, dependency-aware planning, task delegation, and multi-agent coordination. F3 human/project decomposition, issue description, allocation, and crowdsourcing traditions must remain distinct from agent functional decomposition and planning.
- **F4:** F6-A overlaps developer information needs, information seeking, program comprehension, documentation navigation, and context relevance. Human information-seeking evidence is an indirect bridge and not evidence about agent context behavior. F6-C overlaps ambiguity, requirements completeness, specification refinement, and missing information.
- **F5:** F6 relies on `coding agent`, `software engineering agent`, `SWE-agent`, `agent-computer interface`, `agent trajectory`, and `agentless software engineering`. F5 population distinctions must be retained during screening; labels do not define one homogeneous population.

## Answers To P9 Special Questions

1. **What terminology is most useful for coding-agent context?** The most useful inspected terms are `context management`, `memory management`, `context compression`, `repository exploration`, `structural code retrieval`, `repository navigation`, `repository-level understanding`, and `agent-environment interaction`. `Context` alone is too broad; `repository understanding` is recognizable but less operationally frequent than retrieval/navigation/memory terms.
2. **Does the literature distinguish context amount from context relevance/selection?** Yes, at least terminologically. Long-context/context-budget work addresses amount or retention constraints; retrieval, structural code retrieval, repository exploration, memory selection, and knowledge compression address selection, relevance, or representation. The pilot does not establish how these dimensions affect outcomes or whether one dominates.
3. **Is agent planning a coherent empirical research branch or primarily an architectural feature?** Both appear. Many papers describe planner modules or workflows architecturally, while DCAS and related work explicitly distinguish and intervene on planning behavior. The branch therefore requires separate extraction of architecture, intervention, and effectiveness evaluation.
4. **Is task decomposition studied directly for coding agents?** It is present under `functional decomposition`, `subtask-level`, `dependency-aware task plans`, `task delegation`, and multi-agent coordination. Direct coding-agent decomposition terminology is narrower than general `task decomposition`, and it should not be merged with F3 human/project decomposition.
5. **Is clarification/question-asking a meaningful coding-agent research branch?** Yes, a small recent benchmark/empirical branch is identifiable under `clarification-seeking`, `requirement elicitation`, `underspecified instructions`, and dialogue-driven coding agents. Its maturity and generality remain limited relative to repository-level autonomous benchmark research.
6. **Are current benchmarks structurally capable of evaluating clarification?** Standard issue-to-patch benchmarks generally do not provide a normal user dialogue channel. New variants and benchmarks explicitly add underspecification, user simulators, dialogue, or intermediate clarification references, so capability depends on benchmark design rather than benchmark name alone.
7. **How is autonomy described or operationalized?** Usually through operational properties: selecting future actions, invoking tools, observing environment feedback, modifying repositories, executing tests, and continuing across multiple steps. The inspected literature did not reveal a stable general scalar autonomy measure.
8. **Should tool/environment interaction remain with autonomy or become a separate branch?** It should be searched as a related but separate branch. Tool use and environment interaction are architectural/execution mechanisms that can occur without fully autonomous task authority; ACI, action space, environment interaction, and autonomy should be cross-linked rather than collapsed.
9. **Is trajectory analysis useful as a primary search concept or only contextual terminology?** It is useful as a primary execution-analysis concept for studies of action sequences, feedback, failures, and process-level evaluation. It is only contextual terminology when used to infer reasoning quality or autonomy without a validated construct and appropriate comparison.
10. **Does F6 need to be split differently before systematic-search design?** Yes. F6-A should distinguish context/memory management from repository retrieval/navigation; F6-B should distinguish planning architecture/effectiveness from functional decomposition/delegation; F6-C should distinguish clarification-seeking from broader dialogue/interaction; F6-D should distinguish autonomy from tool/environment interface and trajectory analysis.

## Recommended F6 Search Status

| Branch | Status | Methodological reason |
|---|---|---|
| F6-A Context and repository understanding | `Requires further calibration` | Recognizable but internally split between context/memory maintenance and repository retrieval/navigation; `context` is broad and repository terminology is operationally heterogeneous. |
| F6-B Planning and task decomposition | `Requires further calibration` | Planning is both architecture and empirical process; agent functional decomposition/delegation is distinct from F3 decomposition and needs separate search branches. |
| F6-C Clarification, ambiguity resolution, and interactive assistance | `Primary` | Compact direct clarification terminology and dedicated recent benchmarks were retrieved, with explicit interaction-design boundaries to record. |
| F6-D Autonomy, tool use, and agent-environment interaction | `Requires further calibration` | Trajectory and ACI neighborhoods are clear, but autonomy, tool use, interface design, and process analysis are not one construct and need separation before systematic searching. |

## F6 Remaining Uncertainty

- Whether `context management`, memory management, retrieval, and repository navigation are studied as separable interventions or merely as parts of agent scaffolds requires full-text extraction.
- Whether context quantity and context relevance are measured independently is unresolved in this pilot; the terminology distinction is clearer than the experimental separation.
- The balance between planning architecture descriptions and planning-effectiveness studies is not established from abstracts alone.
- Agent functional decomposition may be a memory/indexing mechanism, a planner representation, a delegation mechanism, or an evaluation label; these uses should not be pooled.
- Clarification literature may be growing rapidly, but most inspected records were recent preprints and custom benchmarks rather than mature replicated studies.
- Standard benchmark interaction constraints may explain why clarification is sparse in older coding-agent studies; absence of observed clarification is not evidence of inability or irrelevance.
- Autonomy lacks a common operational scale in the inspected sample. Tool access, authority boundaries, user interaction, model behavior, scaffold behavior, and environment feedback may all contribute separately.
- Trajectory features may be framework-dependent; transfer across models, scaffolds, tools, repositories, and benchmarks requires explicit validation.
- Database coverage was limited to arXiv in P9. IEEE Xplore, ACM Digital Library, Scopus, Web of Science, ScienceDirect, SpringerLink, and Google Scholar were not searched in this round. arXiv discovery is useful for rapidly evolving preprints but cannot establish venue coverage or publication completeness.
- Full texts were not retrieved for the candidate sources in this pilot. Publication status, duplicate versions, later peer-reviewed versions, methods, datasets, and limitations require later screening.
- The search date is 2026-08-20 and recent records may change status or version; later searches must preserve version links and publication-status distinctions.

## F6 Exit Decision

**F6 should be split into distinct search subfamilies before systematic-search design**

The methodological reason is that the pilot retrieved several related but non-equivalent neighborhoods: context/memory maintenance, repository retrieval/navigation, planning architecture, planning effectiveness, functional decomposition/delegation, clarification-seeking, dialogue/interaction, autonomy, tool/environment interfaces, and trajectory/process analysis. The required split preserves construct, agent population, benchmark interaction affordances, unit of analysis, and evidence maturity. F6-C is already sufficiently coherent to serve as a primary branch, but the overall family should not proceed as one combined search family.

No Work Item characteristics or research conclusions were derived. P9 did not define optimal context, favor more or less context, claim that planning, clarification, or autonomy is beneficial, or generalize benchmark results beyond their studied conditions. F7 was not executed. No systematic search strings were frozen. No commit was made.

## Pilot Round 10 Family 6 Split Validation

Pilot Round 10 was conducted on 2026-08-20 using focused arXiv API searches selected from P9 terminology. The purpose was to validate a restructured F6 search family, not to repeat broad discovery. Counts are source-reported diagnostics and are not estimates of prevalence, precision, recall, or evidence strength. The searches remained limited to coding-agent-specific terminology and recent records; preprints are labeled as such and are not treated as equivalent to peer-reviewed publications. No F7 search was executed, no systematic search string was frozen, and no Work Item characteristic or research conclusion was derived.

### P10-F6A1: Context Quantity, Long-Context Behavior, And Memory Management

#### P10-F6A1-01

- **Search ID:** `P10-F6A1-01`
- **Date:** `2026-08-20`
- **Evidence stream:** Coding-agent-specific scientific discovery
- **Database / source:** arXiv API
- **Query:** `all:"software engineering agent" AND (all:"long-context" OR all:"context compression" OR all:"memory management")`
- **Fields searched:** arXiv `all` fields
- **Filters:** None; first 10 sorted by relevance
- **Result count:** `5` reported by arXiv
- **Results inspected:** All 5 titles, abstracts, authors, dates, and available venue metadata
- **Clearly relevant results:** `On Problems of Implicit Context Compression for Software Engineering Agents` focuses on context-length limits and compression in multi-step coding; `SWE-MeM` studies adaptive memory management under limited context budgets; `Training Long-Context, Multi-Turn Software Engineering Agents with Reinforcement Learning` treats long-context multi-turn SWE interaction; `Confucius Code Agent` combines long-context reasoning, persistent notes, and tool stacks; the OpenHands SDK exposes memory management as an agent component.
- **Clearly irrelevant patterns:** The small result set still combines context-window constraints, history compression, persistent memory, stateful interaction, and production-agent architecture. These are related but not one intervention or outcome.
- **Terminology discovered:** `long-context`, `context length limitations`, `context budget`, `context compression`, `memory management`, `interaction history`, `persistent notes`, `long-horizon`, `multi-turn SWE agent`.
- **Known-source checks:** SWE-agent `Not applicable`; SWE-bench `Not applicable as a benchmark rather than a context study`; Agentless `Not applicable`; AIDev `Not applicable`; Understanding Software Engineering Agents `Not applicable`; SWE-MeM `Retrieved`; Confucius Code Agent `Retrieved`; `On Problems of Implicit Context Compression` `Retrieved`; OpenHands Software Agent SDK `Retrieved`.
- **Candidate seed sources:** Xingyao Wang et al., `The OpenHands Software Agent SDK: A Composable and Extensible Foundation for Production Agents`, 2025, arXiv preprint with arXiv record stating MLSys 2026 acceptance, [arXiv:2511.03690](https://arxiv.org/abs/2511.03690). This is a new architecture/context seed; later screening must distinguish SDK description from controlled memory evaluation.
- **Query adjustment:** None. The focused query returned a small, recognizable context-quantity/memory neighborhood, although its constructs remain heterogeneous.
- **Rationale:** P9's general `context` result was narrowed successfully without collapsing context budget, compression, and memory into a single effect claim.
- **Notes:** This branch concerns the amount/retention/maintenance side of context. It does not establish that a larger or smaller context is preferable.

### P10-F6A2: Repository Retrieval, Selection, Exploration, And Navigation

#### P10-F6A2-01

- **Search ID:** `P10-F6A2-01`
- **Date:** `2026-08-20`
- **Evidence stream:** Coding-agent-specific scientific discovery
- **Database / source:** arXiv API
- **Query:** `all:"software engineering agent" AND (all:"repository navigation" OR all:"structural code retrieval" OR all:"repository exploration")`
- **Fields searched:** arXiv `all` fields
- **Filters:** None; first 10 sorted by relevance
- **Result count:** `2` reported by arXiv
- **Results inspected:** Both titles, abstracts, authors, dates, and available metadata
- **Clearly relevant results:** `SWE-Replay` treats repository exploration as a decision point in agent trajectories and evaluates on SWE-bench Verified, SWE-bench Pro, and Multilingual; `OwlPath` studies structural code retrieval, multi-hop repository relations, knowledge maps, and retrieval tests on SWE-bench Pro.
- **Clearly irrelevant patterns:** No clearly unrelated result appeared in the complete two-record sample. The low count may reflect exact phrase sparsity rather than a small literature.
- **Terminology discovered:** `repository exploration`, `structural code retrieval`, `repository navigation`, `multi-hop dependencies`, `knowledge map`, `structural queries`, `issue-related symbols`, `repository exploration decision points`.
- **Known-source checks:** SWE-agent `Missed`; SWE-bench `Not applicable as a benchmark source`; Agentless `Not applicable`; AIDev `Not applicable`; Understanding Software Engineering Agents `Not applicable`; OwlPath `Retrieved`; SWE-Replay `Retrieved`; Structurally Aligned Subtask-Level Memory `Missed`; Confucius Code Agent `Not applicable to this retrieval-focused query`.
- **Candidate seed sources:** Yifeng Ding and Lingming Zhang, `SWE-Replay: Efficient Test-Time Scaling for Software Engineering Agents`, 2026, arXiv preprint, [arXiv:2601.22129](https://arxiv.org/abs/2601.22129). Its repository-exploration terminology and cross-benchmark setting make it a new retrieval/navigation seed; it is not treated as a general context-quantity source.
- **Query adjustment:** None. The exact operational terms produced a narrow, coherent repository-retrieval neighborhood.
- **Rationale:** P10 supports separating repository retrieval/selection/navigation from context quantity and memory management. The branch is smaller and more terminology-sensitive, so later searching should include component terms and field variants rather than rely on this exact string.
- **Notes:** The low count is a query and indexing limitation, not evidence that repository understanding is rare. `Repository understanding` itself remained less visible than operational retrieval/navigation terms.

### P10-F6B1: Planning As An Explicit Or Implicit Agent Process

#### P10-F6B1-01

- **Search ID:** `P10-F6B1-01`
- **Date:** `2026-08-20`
- **Evidence stream:** Coding-agent-specific scientific discovery
- **Database / source:** arXiv API
- **Query:** `all:"software engineering agent" AND (all:"explicit planning" OR all:"implicit planning" OR all:"plan-source intervention")`
- **Fields searched:** arXiv `all` fields
- **Filters:** None; first 10 sorted by relevance
- **Result count:** `1` reported by arXiv
- **Results inspected:** The single title, abstract, authors, date, and available metadata
- **Clearly relevant results:** `DCAS` explicitly distinguishes an explicit pre-execution plan from implicit scaffold planning and uses a plan-source intervention in cross-scaffold evaluation.
- **Clearly irrelevant patterns:** None in the single-record sample, but the narrow vocabulary misses papers that describe planning through `planner`, workflow, decomposition, or trajectory terms.
- **Terminology discovered:** `explicit planning`, `implicit planning`, `planning structure`, `plan-source intervention`, `scaffold-specific behavior`, `planning-aware trajectories`.
- **Known-source checks:** SWE-agent `Not applicable to this exact planning-term query`; SWE-bench `Not applicable`; Agentless `Missed`; AIDev `Not applicable`; Understanding Software Engineering Agents `Not applicable`; DCAS `Retrieved`; HyperAgent `Missed`; PatchPilot `Missed`.
- **Candidate seed sources:** No new seed promoted. DCAS remains the P9 planning-intervention seed and is retained for later screening.
- **Query adjustment:** None. The query was intentionally a terminology boundary check, not a broad planning search.
- **Rationale:** The result validates a distinct planning vocabulary but also shows that exact terms are too narrow for recall. Planning remains a candidate primary branch only when architecture, intervention, and effectiveness are extracted separately.
- **Notes:** One result is not evidence of a mature literature. It is evidence that explicit/implicit planning is a recognizable author distinction in at least one recent coding-agent study.

### P10-F6B2: Functional Decomposition, Subtasks, And Delegation

#### P10-F6B2-01

- **Search ID:** `P10-F6B2-01`
- **Date:** `2026-08-20`
- **Evidence stream:** Coding-agent-specific scientific discovery
- **Database / source:** arXiv API
- **Query:** `all:"software engineering agent" AND (all:"functional decomposition" OR all:"subtask-level" OR all:"task delegation")`
- **Fields searched:** arXiv `all` fields
- **Filters:** None; first 10 sorted by relevance
- **Result count:** `2` reported by arXiv
- **Results inspected:** Both titles, abstracts, authors, dates, and available metadata
- **Clearly relevant results:** `Structurally Aligned Subtask-Level Memory` connects storage/retrieval/update to functional decomposition; `Effective Strategies for Asynchronous Software Engineering Agents` uses dependency-aware task plans, centralized task delegation, concurrent subtasks, isolated workspaces, and integration across PaperBench and Commit0.
- **Clearly irrelevant patterns:** No unrelated record appeared in the complete sample, but the two sources address different objects: memory indexing by functional subtask versus multi-agent delegation and coordination.
- **Terminology discovered:** `functional decomposition`, `subtask-level memory`, `dependency-aware task plans`, `centralized task delegation`, `subtask execution`, `isolated workspaces`, `multi-agent coordination`, `branch-and-merge`.
- **Known-source checks:** SWE-agent `Missed`; SWE-bench `Not applicable`; Agentless `Not applicable`; AIDev `Not applicable`; Understanding Software Engineering Agents `Not applicable`; Structurally Aligned Subtask-Level Memory `Retrieved`; Effective Strategies for Asynchronous Software Engineering Agents `Retrieved`; HyperAgent `Missed`; DCAS `Missed`.
- **Candidate seed sources:** No new seed promoted. The two P9 seeds remain the direct sources for this branch, with separate labels for memory/indexing and multi-agent delegation.
- **Query adjustment:** None. The query returned a small but recognizable agent-side decomposition/delegation neighborhood.
- **Rationale:** The branch is distinct from F3 human/project decomposition and from explicit planning, but the two retrieved traditions should not be pooled without a sub-branch or extraction distinction.
- **Notes:** The search does not establish that decomposition improves outcomes. Multi-agent systems and single-agent functional decomposition are separate populations/settings.

### P10-F6C1: Clarification-Seeking And Requirement Elicitation

#### P10-F6C1-01

- **Search ID:** `P10-F6C1-01`
- **Date:** `2026-08-20`
- **Evidence stream:** Coding-agent-specific scientific discovery
- **Database / source:** arXiv API
- **Query:** `all:"coding agent" AND (all:"clarification-seeking" OR all:"requirement elicitation" OR all:"dialogue-driven")`
- **Fields searched:** arXiv `all` fields
- **Filters:** None; first 10 sorted by relevance
- **Result count:** `3` reported by arXiv
- **Results inspected:** All 3 titles, abstracts, authors, dates, and available metadata
- **Clearly relevant results:** `Ask or Assume?` evaluates clarification-seeking on an underspecified SWE-bench Verified variant; `Dialogue SWE-Bench` evaluates dialogue-driven coding agents with a user simulator and dialogue quality; `ClarEval` evaluates clarification skills under injected ambiguity and defines Average Turns to Clarify and Key Question Coverage.
- **Clearly irrelevant patterns:** No unrelated record appeared in the complete three-record sample. The branch remains benchmark-centered and recent.
- **Terminology discovered:** `clarification-seeking`, `requirement elicitation`, `dialogue-driven coding agents`, `underspecified instructions`, `user simulator`, `dialogue quality`, `Average Turns to Clarify`, `Key Question Coverage`.
- **Known-source checks:** SWE-agent `Not applicable`; SWE-bench `Retrieved as the basis or lineage for clarification variants, not as a clarification study`; Agentless `Not applicable as a non-interactive comparator`; AIDev `Not applicable`; Understanding Software Engineering Agents `Not applicable`; Ask or Assume? `Retrieved`; Dialogue SWE-Bench `Retrieved`; ClarEval `Retrieved`; SWE-RPG `Missed` under these exact terms.
- **Candidate seed sources:** No new seed promoted. The P9 clarification seeds remain the relevant candidates; the focused query confirms their direct terminology.
- **Query adjustment:** None. The query was sufficiently focused to validate clarification as a searchable branch.
- **Rationale:** Direct question-asking/elicitation terminology retrieves a coherent coding-agent neighborhood, while its benchmark design must be recorded as part of screening.
- **Notes:** This branch does not imply that clarification is required or beneficial. Older non-interactive benchmarks may omit the behavior because their task protocol does not permit it.

### P10-F6C2: Broader Interaction, Feedback, And Specification Alignment

#### P10-F6C2-01

- **Search ID:** `P10-F6C2-01`
- **Date:** `2026-08-20`
- **Evidence stream:** Coding-agent-specific scientific discovery
- **Database / source:** arXiv API
- **Query:** `all:"coding agent" AND (all:"task alignment" OR all:"dialogue quality" OR all:underspecification OR all:"specification refinement")`
- **Fields searched:** arXiv `all` fields
- **Filters:** None; first 10 sorted by relevance
- **Result count:** `5` reported by arXiv
- **Results inspected:** All 5 titles, abstracts, authors, dates, and available metadata
- **Clearly relevant results:** `Dialogue SWE-Bench` uses dialogue quality; `Humans are Missing from AI Coding Agent Research` uses task alignment, steerability, and adaptability; `ICAE-Bench` evaluates interactive project building from fuzzy requirements; `UnderSpecBench` separates clarification, refusal, and deferment under underspecified DevOps instructions.
- **Clearly irrelevant patterns:** `Software Delegation Contracts` is adjacent reviewability/authority research rather than direct dialogue; broader interaction terms can retrieve position papers and safety settings with different units of analysis.
- **Terminology discovered:** `task alignment`, `dialogue quality`, `specification refinement`, `underspecification`, `steerability`, `adaptability`, `deferment`, `interaction quality`, `bounded authority`.
- **Known-source checks:** SWE-agent `Missed`; SWE-bench `Retrieved as benchmark lineage/boundary`; Agentless `Retrieved as a non-interactive comparator`; AIDev `Not applicable`; Understanding Software Engineering Agents `Not applicable`; Dialogue SWE-Bench `Retrieved`; ICAE-Bench `Retrieved`; ClarEval `Missed`; Humans are Missing from AI Coding Agent Research `Retrieved`; UnderSpecBench `Retrieved`.
- **Candidate seed sources:** Zhongyuan Peng et al., `ICAE-Bench: Evaluating Coding Agents as Interactive Project Builders`, 2026, arXiv preprint, [arXiv:2607.21217](https://arxiv.org/abs/2607.21217); Zimo Ji et al., `Coding Agents Are Guessing: Measuring Action-Boundary Violations in Underspecified DevOps Instructions`, 2026, arXiv preprint, [arXiv:2607.02294](https://arxiv.org/abs/2607.02294). They extend the interaction branch into user simulation, fuzzy requirements, safety boundaries, refusal, and deferment; they should not be merged with clarification effectiveness without screening.
- **Query adjustment:** None. The query was sufficient to test whether P9's broader interaction terms formed a branch related to, but distinct from, question asking.
- **Rationale:** Interaction/feedback is searchable, but it is broader and more heterogeneous than clarification-seeking. It should be a supplementary branch or a screening layer around clarification, not silently substituted for it.
- **Notes:** The branch includes conversational assistants, repository-level agents, and DevOps agents; population and interaction protocol must be extracted separately.

### P10-F6D1: Tool Use, Interfaces, And Agent-Environment Interaction

#### P10-F6D1-01

- **Search ID:** `P10-F6D1-01`
- **Date:** `2026-08-20`
- **Evidence stream:** Coding-agent-specific scientific discovery
- **Database / source:** arXiv API
- **Query:** `all:"software engineering agent" AND (all:"agent-computer interface" OR all:"agent-environment interaction" OR all:"tool-mediated")`
- **Fields searched:** arXiv `all` fields
- **Filters:** None; first 10 sorted by relevance
- **Result count:** `2` reported by arXiv
- **Results inspected:** Both titles, abstracts, authors, dates, and available metadata
- **Clearly relevant results:** `SWE-World` studies a software-agent environment loop and execution feedback using a Docker-free surrogate; `Projecting the Emerging Mindset of SWE Agent by Launching a Wild Code Understanding Journey` studies bounded tool interfaces, tool-mediated trajectories, repository exploration, evidence selection, and stopping across 408 trajectories.
- **Clearly irrelevant patterns:** No unrelated record appeared in the complete sample, but ACI, environment simulation, and tool-mediated observation are different architectural objects.
- **Terminology discovered:** `agent-environment interaction`, `tool-mediated trajectories`, `bounded tool interface`, `execution feedback`, `environment interface`, `action space`, `self-directed stopping`, `repository exploration`.
- **Known-source checks:** SWE-agent `Missed`; SWE-bench `Not applicable`; Agentless `Not applicable`; AIDev `Not applicable`; Understanding Software Engineering Agents `Not applicable`; SWE-World `Retrieved`; Projecting the Emerging Mindset of SWE Agent `Retrieved`; SWE-agent ACI paper `Missed` under this combined query; OpenHands SDK `Not verified`.
- **Candidate seed sources:** Shuang Sun et al., `SWE-World: Building Software Engineering Agents in Docker-Free Environments`, 2026, arXiv preprint, [arXiv:2602.03419](https://arxiv.org/abs/2602.03419); Zhengyi Zhuo and Yan Liu, `Projecting the Emerging Mindset of SWE Agent by Launching a Wild Code Understanding Journey`, 2026, arXiv preprint, [arXiv:2606.08500](https://arxiv.org/abs/2606.08500). These are new environment/interface seeds; the latter is an observational methodology source and not a general tool-use benchmark.
- **Query adjustment:** None. The focused operational terms produced a compact environment/interface neighborhood.
- **Rationale:** Tool/environment interaction is meaningfully distinct from autonomy: an interface or environment can be studied without treating autonomy as the manipulated variable.
- **Notes:** This branch includes repository-level tool-using agents and environment/training infrastructure. It is not a measure of desirable autonomy.

### P10-F6D2: Agent Trajectories And Process-Level Execution Analysis

#### P10-F6D2-01

- **Search ID:** `P10-F6D2-01`
- **Date:** `2026-08-20`
- **Evidence stream:** Coding-agent-specific scientific discovery
- **Database / source:** arXiv API
- **Query:** `all:"software engineering agent" AND (all:"thought-action-result trajectory" OR all:"process-level trajectory" OR all:"trajectory evaluation")`
- **Fields searched:** arXiv `all` fields
- **Filters:** None; first 10 sorted by relevance
- **Result count:** `2` reported by arXiv
- **Results inspected:** Both titles, abstracts, authors, dates, and available metadata
- **Clearly relevant results:** `Process-Level Trajectory Evaluation for Environment Configuration in Software Engineering Agents` introduces process-level trajectory assessment; `Understanding Software Engineering Agents` studies thought-action-result trajectories from RepairAgent, AutoCodeRover, and OpenHands and combines structural, quantitative, and qualitative trajectory analysis.
- **Clearly irrelevant patterns:** No unrelated record appeared in the complete sample. The two sources address different tasks, but both treat trajectories as recorded execution sequences and analysis units.
- **Terminology discovered:** `thought-action-result trajectory`, `process-level trajectory evaluation`, `trajectory assessment`, `interaction logs`, `action patterns`, `feedback integration`, `anti-pattern detection`, `execution record`.
- **Known-source checks:** SWE-agent `Not applicable as a system source for this exact trajectory query`; SWE-bench `Not applicable as a benchmark source`; Agentless `Not applicable`; AIDev `Not applicable`; Understanding Software Engineering Agents `Retrieved`; Process-Level Trajectory Evaluation `Retrieved`; SeaView `Missed`; Same Signal, Different Semantics `Missed`.
- **Candidate seed sources:** No new seed promoted. Understanding Software Engineering Agents and Enconda-bench remain the P9 trajectory seeds; P10 confirms direct trajectory terminology.
- **Query adjustment:** None. The query isolated a small, coherent process-analysis neighborhood.
- **Rationale:** Trajectory analysis is sufficiently recognizable to remain a primary search branch for execution-process studies, while its interpretation must remain separate from reasoning quality, autonomy, or outcome causality.
- **Notes:** A trajectory is an observable execution record. This branch does not infer hidden reasoning or establish that any trajectory pattern is generally desirable.

### P10-F6E: Autonomy As A Boundary Concept

#### P10-F6E-01

- **Search ID:** `P10-F6E-01`
- **Date:** `2026-08-20`
- **Evidence stream:** Coding-agent-specific scientific discovery
- **Database / source:** arXiv API
- **Query:** `all:"software engineering agent" AND all:autonomy`
- **Fields searched:** arXiv `all` fields
- **Filters:** None; first 10 sorted by relevance
- **Result count:** `1` reported by arXiv
- **Results inspected:** The single title, abstract, author, date, and available metadata
- **Clearly relevant results:** `From Code-Centric to Intent-Centric Software Engineering` uses autonomy/bounded autonomy in a mixed literature and public-discourse analysis, alongside tools, context, tests, governance, and accountability.
- **Clearly irrelevant patterns:** The result is not a focused empirical study of autonomy as a coding-agent variable; it combines peer-reviewed literature, benchmarks, public talks, essays, product announcements, and social-media discourse.
- **Terminology discovered:** `bounded autonomy`, `autonomous software engineering`, `human-agent supervision`, `agent governance`, `accountability`.
- **Known-source checks:** SWE-agent `Missed`; SWE-bench `Not applicable`; Agentless `Missed`; AIDev `Not applicable`; Understanding Software Engineering Agents `Missed`; From Code-Centric to Intent-Centric Software Engineering `Retrieved`.
- **Candidate seed sources:** None promoted. The single result was retained as a boundary/context source, not as a primary autonomy seed.
- **Query adjustment:** None. The zero/one-record boundary result was sufficient to classify the standalone term for this round.
- **Rationale:** P9's autonomy concern is not supported as a coherent primary search branch by this focused check. Operational terms from P10-F6D1 and P10-F6D2 are more specific to observable agent execution.
- **Notes:** This downgrade is a search-method decision only. It is not a conclusion about autonomy's desirability, safety, or importance.

## P10 Query Evolution Records

P10 intentionally used one focused query per candidate branch and did not repeat P9's broad discovery queries. No P10 query required a revision: each focused query produced either a coherent small neighborhood or a deliberate boundary result. The material P9-to-P10 restructuring is recorded below.

- **P9 organization:** `F6-A context and repository understanding` → **P10 split:** `F6-A1 context quantity/long-context/memory` and `F6-A2 repository retrieval/selection/exploration/navigation`.
- **P9 organization:** `F6-B planning and task decomposition` → **P10 split:** `F6-B1 planning process/architecture` and `F6-B2 functional decomposition/subtasks/delegation`.
- **P9 organization:** `F6-C clarification, ambiguity resolution, and interactive assistance` → **P10 split:** `F6-C1 clarification-seeking/requirement elicitation` and `F6-C2 broader interaction/feedback/specification alignment`.
- **P9 organization:** `F6-D autonomy, tool use, and agent-environment interaction` → **P10 split:** `F6-D1 tool/interface/environment interaction`, `F6-D2 trajectory/process analysis`, and `F6-E autonomy boundary concept`.

The P10 search entries themselves document the focused original query, result count, inspection sample, and known-source status. There were no silent replacements, failed revisions, or zero-result revised searches in this round.

## P10 Terminology Registry Recalibration

P10 materially validates or narrows existing P9 rows without creating duplicate canonical terms. Existing rows are updated in place where P10 adds provenance: `context compression`, `memory management`, `repository exploration`, `structural code retrieval`, `explicit planning`, `implicit planning`, `functional decomposition`, `dependency-aware task plans`, `clarification-seeking`, `dialogue-driven coding agents`, `agent-environment interaction`, `process-level trajectory evaluation`, `agent trajectory / tool-mediated trajectory`, and `agent-computer interface (ACI)`. `autonomy` is not promoted to a new primary row; P10 records it as a boundary concept and retains `bounded autonomy` only as contextual terminology.

New canonical P10 terms are limited to terms materially distinct from the existing registry:

| Term | Related concept | Source / Search ID | Context | Action | Notes |
|---|---|---|---|---|---|
| context budget | context quantity/retention | P10-F6A1-01 | Long-horizon SWE agents | retain as contextual term | Distinguish from context relevance and repository selection. |
| persistent notes | context memory | P10-F6A1-01 | Production SWE-agent scaffolding | retain as contextual term | Source wording in Confucius/OpenHands-style architectures; not equivalent to repository understanding. |
| repository exploration decision point | repository retrieval/navigation | P10-F6A2-01 | SWE-agent trajectory analysis | investigate separately | Operational trajectory term; not a general context-quantity term. |
| planning-aware trajectories | planning/process analysis | P10-F6B1-01 | Cross-scaffold SWE-agent evaluation | investigate separately | Connects planning with trajectory collection but does not make trajectories a reasoning measure. |
| dialogue quality | interactive coding | P10-F6C1-01, P10-F6C2-01 | Dialogue SWE-Bench | test provisionally | Keep separate from clarification-question quality and task success. |
| interaction quality | human-agent interaction | P10-F6C2-01 | Interactive coding benchmarks | test provisionally | Broader than clarification and dialogue; screen benchmark design. |
| execution feedback | agent-environment interaction | P10-F6D1-01 | SWE-world/environment studies | retain as contextual term | Environment signal/setting term, not a planning or autonomy synonym. |
| self-directed stopping | agent-environment interaction | P10-F6D1-01 | Repository code-understanding trajectories | investigate separately | Observable stopping behavior; not equivalent to autonomy level. |
| feedback integration | trajectory/process analysis | P10-F6D2-01 | SWE-agent trajectory analysis | retain as contextual term | Trajectory annotation/analysis concept. |
| execution record | trajectory/process analysis | P10-F6D2-01 | Agent trajectory studies | retain as contextual term | Makes the observational status of trajectory data explicit. |

## P10 Candidate Seed Sources

New candidate seeds were added only where P10 exposed a materially distinct source or terminology. They are discovery candidates, not included evidence.

| Source | Year and status | DOI or stable URL | Search ID | F6 relevance |
|---|---:|---|---|---|
| Wang et al., `The OpenHands Software Agent SDK: A Composable and Extensible Foundation for Production Agents` | 2025, arXiv preprint; record states MLSys 2026 acceptance | [arXiv:2511.03690](https://arxiv.org/abs/2511.03690) | `P10-F6A1-01` | Agent architecture with memory management, tools, execution, and human interfaces; not a pure context-quantity study. |
| Ding and Zhang, `SWE-Replay: Efficient Test-Time Scaling for Software Engineering Agents` | 2026, arXiv preprint | [arXiv:2601.22129](https://arxiv.org/abs/2601.22129) | `P10-F6A2-01` | Repository exploration as an agent decision/process term across SWE-bench variants. |
| Sun et al., `SWE-World: Building Software Engineering Agents in Docker-Free Environments` | 2026, arXiv preprint | [arXiv:2602.03419](https://arxiv.org/abs/2602.03419) | `P10-F6D1-01` | Agent-environment interaction and execution-feedback infrastructure. |
| Zhuo and Liu, `Projecting the Emerging Mindset of SWE Agent by Launching a Wild Code Understanding Journey` | 2026, arXiv preprint | [arXiv:2606.08500](https://arxiv.org/abs/2606.08500) | `P10-F6D1-01` | Bounded tool interface, repository exploration, evidence selection, stopping, and observational trajectories. |
| Peng et al., `ICAE-Bench: Evaluating Coding Agents as Interactive Project Builders` | 2026, arXiv preprint | [arXiv:2607.21217](https://arxiv.org/abs/2607.21217) | `P10-F6C2-01` | Interactive project-building benchmark with fuzzy requirements and user simulation. |
| Ji et al., `Coding Agents Are Guessing: Measuring Action-Boundary Violations in Underspecified DevOps Instructions` | 2026, arXiv preprint | [arXiv:2607.02294](https://arxiv.org/abs/2607.02294) | `P10-F6C2-01` | Underspecification, clarification/refusal/deferment, and action-boundary evaluation in DevOps agents. |

## P10 Calibrated F6 Structure

| Branch | Purpose | Provisional terminology | Major exclusions/noise | Agent population | Benchmark dependence | F3/F4/F5 overlap | Status |
|---|---|---|---|---|---|---|---|
| F6-A1 Context quantity, long-context behavior, and memory management | Context-window/retention/compression and agent memory mechanisms | long-context; context compression; context budget; memory management; persistent memory; interaction history | Generic context, user-state-only context, unrelated long-context NLP, repository retrieval | Tool-using repository-level SWE agents and production agent scaffolds; some multi-turn training systems | SWE-bench Verified, SWE-bench Pro, SWE-rebench, custom production evaluations | F4 context/information needs and program comprehension; F5 coding-agent labels; limited F3 trajectory/planning overlap | `Primary` |
| F6-A2 Repository retrieval, selection, exploration, and navigation | How agents locate and select repository/code information | repository exploration; structural code retrieval; repository navigation; knowledge map; multi-hop dependencies | Generic repository understanding without operational mechanism; context-window quantity; general code search unrelated to agents | Repository-level tool-using SWE agents | Strong SWE-bench Verified/Pro and issue-resolution dependence | F4 information seeking/program comprehension; F3 repository/task context; F5 SWE-agent/ACI terminology | `Primary` |
| F6-B1 Planning process and architecture | Explicit plans, implicit scaffold planning, and planning interventions | explicit planning; implicit planning; planning structure; plan-source intervention; planning-aware trajectories | Planner presence treated as effectiveness; generic project planning; F3 human decomposition | Repository-level agents and CLI scaffolds; some multi-agent systems | Mostly SWE-bench-family or custom cross-scaffold settings | F3 coding plans/decomposition; F5 scaffold/trajectory terms | `Requires further calibration` |
| F6-B2 Functional decomposition, subtasks, and delegation | Agent-side subtask formation, dependency-aware plans, and multi-agent delegation | functional decomposition; subtask-level; dependency-aware task plans; centralized task delegation; isolated workspaces | Human/project decomposition, crowdsourcing decomposition, generic task decomposition, planning without subtask object | Multi-agent SWE systems plus single-agent memory/indexing agents | PaperBench, Commit0, SWE-bench Verified, custom multi-agent environments | F3 decomposition/allocation/interdependence; F5 agent architecture; F4 indirect context/memory overlap | `Requires further calibration` |
| F6-C1 Clarification-seeking and requirement elicitation | Agents asking questions or eliciting missing requirements | clarification-seeking; requirement elicitation; underspecified instructions; dialogue-driven coding agents; user simulator | Generic clarification outside software; non-interactive task results interpreted as clarification evidence; domain-specific CAD | Conversational coding assistants and repository-level agents with explicit interaction protocols | Modified SWE-bench Verified, Dialogue SWE-Bench, ClarEval, custom ambiguous tasks | F4 ambiguity/completeness/missing information; F3 task descriptions; F5 coding-agent populations | `Primary` |
| F6-C2 Interaction, feedback, and specification alignment | Broader dialogue, feedback, alignment, steerability, and specification-refinement settings | dialogue quality; interaction quality; task alignment; specification refinement; underspecification; steerability; deferment | Clarification-only metrics, generic human-AI interaction, unrelated safety/interactive agents | Conversational assistants, repository-level agents, and DevOps agents; populations must be separated | Dialogue SWE-Bench, ICAE-Bench, UnderSpecBench, custom interaction settings | F4 ambiguity/requirements; F3 descriptions; F5 human-agent/coding-agent terminology | `Supplementary` |
| F6-D1 Tool use, interfaces, and agent-environment interaction | Interfaces, tools, environment feedback, sandboxing, and observable execution loops | agent-computer interface; agent-environment interaction; tool-mediated; bounded tool interface; execution feedback; action space | Autonomy as a rhetorical label; generic computer-use/healthcare interfaces; trajectory analysis without interface focus | Tool-using repository-level SWE agents and environment/training infrastructures | SWE-bench Verified, HumanEvalFix, custom Docker/surrogate environments | F4 context/feedback; F3 execution/dependencies; F5 ACI/SWE-agent/tool terminology | `Primary` |
| F6-D2 Agent trajectories and process-level execution analysis | Recorded action/observation sequences and process-level evaluation | thought-action-result trajectory; process-level trajectory evaluation; trajectory assessment; feedback integration; execution record | Hidden reasoning claims, scalar autonomy claims, outcome causal claims without process design | Repository-level SWE agents such as RepairAgent, AutoCodeRover, OpenHands, plus environment agents | SWE-bench-related repair/issue settings and Enconda-bench/custom environments | F3 planning/execution; F4 information seeking/context; F5 trajectory terminology | `Primary` |
| F6-E Autonomy | Standalone autonomy terminology and operational definitions | autonomy; autonomous software engineering; bounded autonomy | Broad governance/position discourse and architecture papers without an autonomy variable | Mixed and not consistently identifiable | No stable benchmark dependence in the focused query | F5 general agent labels; F4 human-agent interaction; F3 execution | `Exclude from F6 systematic search` |

### Difference From P9 Organization

P9's four branches were useful discovery containers but combined distinct retrieval neighborhoods. P10 validates the following restructuring:

- P9 F6-A splits into F6-A1 context quantity/memory and F6-A2 repository retrieval/navigation. The P10 counts were `5` versus `2`, with different terminology and source objects.
- P9 F6-B splits into F6-B1 planning and F6-B2 functional decomposition/delegation. The focused terms produced `1` explicit-planning record versus `2` decomposition/delegation records, and the abstracts describe different units of analysis.
- P9 F6-C splits into F6-C1 direct clarification/elicitation and F6-C2 broader interaction/alignment. Both are searchable, but C2 is more heterogeneous and benchmark-dependent.
- P9 F6-D splits into F6-D1 tool/interface/environment interaction and F6-D2 trajectory/process analysis. P10's two-record neighborhoods share execution settings but study different objects. P9's standalone autonomy label is downgraded to F6-E and excluded as a primary search branch.

## P10 Special Decisions

1. **Context retrieval/selection versus context quantity:** They do not belong in one primary branch. P10-F6A1 retrieved long-context, compression, budget, and memory records; P10-F6A2 retrieved repository exploration and structural code retrieval records. They should be cross-linked because memory and retrieval can interact, but searched separately.
2. **Repository understanding/navigation as its own branch:** Yes, operationally. `Repository understanding` was sparse, but `repository exploration`, `structural code retrieval`, and `repository navigation` formed a distinct narrow neighborhood. The branch should use those operational terms rather than rely on the umbrella phrase alone.
3. **Planning versus decomposition:** Separate branches are justified. Explicit/implicit planning concerns a plan artifact or scaffold behavior; functional decomposition/subtask/delegation concerns the formation and coordination of subtasks. Some sources bridge them, so cross-screening is required.
4. **Planning maturity and status:** Planning is not sufficiently mature as one homogeneous primary branch in this pilot. It remains `Requires further calibration` because the focused explicit-planning query returned one record and P9 showed substantial architecture-description content. The broader planning neighborhood remains relevant but must distinguish architecture from empirical intervention/effectiveness.
5. **Clarification/question asking as a searchable branch:** Yes. P10-F6C1 returned three directly relevant records with consistent clarification/elicitation terminology and explicit benchmark designs.
6. **Clarification versus interaction/feedback terminology:** Clarification should remain the primary narrow branch; interaction/feedback/specification alignment should be supplementary. The P10-C2 sample was coherent enough to retain but materially broader, including steerability, safety boundaries, and user simulation.
7. **Autonomy as a primary concept:** No. P10-F6E returned one mixed discourse/analysis source and no focused autonomy variable. `Autonomy` should not be a primary systematic-search term for F6, though it can remain a contextual descriptor and be operationalized through more specific execution concepts.
8. **Tool/environment interaction independent from autonomy:** Yes. P10-F6D1 retrieved a compact environment/interface neighborhood without requiring autonomy as the study object. Tool access, interface design, environment feedback, and authority/autonomy must not be silently equated.
9. **Trajectory analysis status:** Primary for process/execution-analysis searching, not as a proxy for reasoning quality or autonomy. P10-F6D2 returned two directly relevant trajectory studies and P9 supplied additional trajectory seeds.
10. **Benchmark constraints on clarification retrieval:** Material. Standard issue-to-patch SWE-bench-style protocols generally do not provide ordinary question/answer interaction, while P10 clarification sources explicitly add underspecification, user simulators, dialogue, or clarification metrics. Sparse clarification retrieval from older benchmark studies cannot be interpreted without this protocol boundary.

## P10 Remaining Uncertainty

- The context quantity/memory branch is small and may combine compression, history management, and long-context training that later screening will need to separate further.
- Repository retrieval/navigation terminology is operationally clear but exact phrase retrieval is sparse; fielded searches and component-term variants may recover a larger neighborhood.
- Planning has direct recent intervention terminology but insufficient evidence in this pilot to classify the overall branch as mature; architecture descriptions and effectiveness studies remain mixed.
- Functional decomposition and delegation are distinguishable from planning but may still need separate single-agent and multi-agent screening strata.
- Clarification is searchable, but its current literature is recent, benchmark-heavy, and mostly preprint-based; interaction protocol is a major moderator of retrieval and interpretation.
- Tool/environment research includes both repository agents and general agent infrastructure. Coding-agent population boundaries must be applied at screening.
- Trajectory studies provide observable execution records, but their relationship to hidden reasoning, quality, or autonomy remains construct-sensitive and framework-dependent.
- The standalone autonomy query was too sparse to establish a coherent research tradition, but a database-limited pilot cannot prove that no such tradition exists elsewhere.
- P10 used only arXiv. IEEE Xplore, ACM Digital Library, Scopus, Web of Science, ScienceDirect, SpringerLink, Google Scholar, and publisher full-text platforms were not searched. Crossref was not used for broad counts.
- Full-text methods, datasets, later peer-reviewed versions, duplicate records, and benchmark interaction details remain to be verified during later screening.

## F6 Exit Decision

**F6 subfamily structure sufficiently calibrated for systematic-search design**

The methodological reason is that P10 validated distinct retrieval neighborhoods derived from P9 rather than preserving the original four-way structure by convention: context quantity/memory, repository retrieval/navigation, planning, functional decomposition/delegation, clarification-seeking, broader interaction/alignment, tool/environment interaction, and trajectory/process analysis. It also tested autonomy as a boundary term and found insufficient focused retrieval to retain it as a primary branch. The final structure records overlaps, benchmark interaction constraints, agent populations, and different evidence maturity without merging unlike units of analysis.

**F6 pilot exploration can close.**

No Work Item characteristics or research conclusions were derived. P10 did not determine an optimal context size, claim any effect direction, claim planning/decomposition/clarification/autonomy is beneficial or required, or generalize benchmark findings beyond studied settings. Family 7 was not executed. No final systematic search strings were frozen. No commit was made.

## Pilot Round 11 Family 7 Calibration

Pilot Round 11 was conducted on 2026-08-20 using focused arXiv API discovery searches, OpenAlex metadata discovery, and direct arXiv source-page retrieval. The round was limited to Family 7: verification, validation, review, acceptance, completion, rework, correction, and task-success evaluation. Counts are source-reported discovery diagnostics, not estimates of prevalence, precision, recall, or evidence strength. Source-page abstracts and metadata were inspected for terminology, outcome definitions, authority, publication status, and benchmark boundaries. No Work Item characteristic, lifecycle, acceptance rule, or substantive research conclusion was derived.

### F7-A: Verification And Validation Of Software Changes

#### P11-F7A-01

- **Search ID:** `P11-F7A-01`
- **Date:** `2026-08-20`
- **Evidence stream:** Traditional software-engineering scientific discovery
- **Database / source:** arXiv API
- **Query:** `all:"patch correctness" OR all:"software patch" AND all:validation`
- **Fields searched:** arXiv `all` fields
- **Filters:** None; first 10 sorted by relevance
- **Result count:** `42` reported by arXiv after API Boolean normalization
- **Results inspected:** First 10 records and abstracts; selected source pages for patch-correctness papers
- **Clearly relevant results:** `Predicting Patch Correctness Based on the Similarity of Failing Test Cases`, `On Reliability of Patch Correctness Assessment`, `Evaluating Representation Learning of Code Changes for Predicting Patch Correctness in Program Repair`, `Is this Change the Answer to that Problem?`, and `Identifying Patch Correctness in Test-Based Program Repair`.
- **Clearly irrelevant patterns:** Generic software-patch validation and unrelated validation uses occurred outside the patch-correctness cluster.
- **Terminology discovered:** `patch correctness`, `plausible patch`, `patch overfitting`, `automated patch correctness assessment (APCA)`, `independent test suite`, `author annotation`, `gold correctness labels`, `behavioral discrepancy`, `semantic correlation`, `patch validation`.
- **Candidate seed sources:** Le et al., `On Reliability of Patch Correctness Assessment`, 2018, arXiv record; the abstract describes automated test-suite labels, author labels, and a 35-professional-developer gold set. Tian et al., `Predicting Patch Correctness Based on the Similarity of Failing Test Cases`, 2022, arXiv record; source status requires later venue verification. Xiong et al., `Identifying Patch Correctness in Test-Based Program Repair`, 2018, ICSE record with DOI `10.1145/3180155.3180182`. Tian et al., `Is this Change the Answer to that Problem?`, 2022, DOI `10.1145/3551349.3556914`.
- **Known-source checks:** SWE-bench `Not applicable to this traditional patch-correctness query`; SWE-agent `Not applicable`; Agentless `Not applicable`; AIDev `Not applicable`; Understanding Software Engineering Agents `Not applicable`.
- **Query adjustment:** `all:"patch correctness" OR all:"software patch" AND all:validation` -> patch-correctness cluster was recognizable but Boolean scope and validation language remained mixed -> test exact `all:"patch correctness"`.
- **Rationale:** The exact phrase isolates an established automated-program-repair terminology neighborhood and avoids treating generic verification or validation as one construct.
- **Notes:** The inspected abstracts explicitly distinguish a patch that passes an available test oracle from a patch judged correct or generalizable. This is repository/change-level artifact evaluation, not a general measure of task completion. arXiv records identify some conference/journal status, but later screening must verify versions and venues.

#### P11-F7A-02

- **Search ID:** `P11-F7A-02`
- **Date:** `2026-08-20`
- **Evidence stream:** Traditional software-engineering scientific discovery
- **Database / source:** arXiv API
- **Query:** `all:"patch correctness"`
- **Fields searched:** arXiv `all` fields
- **Filters:** None; first 10 sorted by relevance
- **Result count:** `37` reported by arXiv
- **Results inspected:** First 10 records and abstracts
- **Clearly relevant results:** The first records consistently concerned automated patch correctness assessment, test-suite weakness, patch overfitting, learned correctness prediction, and human correctness annotation. `On Reliability of Patch Correctness Assessment` was especially useful for separating automated labels, author labels, and professional-developer labels.
- **Clearly irrelevant patterns:** Recent APCA model papers may evaluate a classifier's accuracy rather than the correctness of the underlying software patch; these are outcome-prediction studies and require separate screening.
- **Terminology discovered:** `plausible but incorrect`, `test oracle`, `generalizable patch`, `patch correctness prediction`, `automated annotation`, `author annotation`, `manual annotation`, `overfitting patch`.
- **Candidate seed sources:** The same patch-correctness sources remain candidate seeds. `PatchZero: Zero-Shot Automatic Patch Correctness Assessment`, 2023/2024 arXiv record, was also inspected as an APCA terminology source.
- **Known-source checks:** SWE-bench `Not applicable to this exact traditional query`; SWE-agent `Not applicable`; Agentless `Not applicable`; AIDev `Not applicable`; Understanding Software Engineering Agents `Not applicable`.
- **Query adjustment:** None beyond the exact-phrase revision above.
- **Rationale:** The revised query produced a coherent APCA neighborhood and confirmed that `patch correctness` is more precise than unqualified `software verification` for repository-level change evaluation.
- **Notes:** The branch remains adjacent to program repair and testing, but it has a distinct construct: whether a generated or repaired patch is correct beyond merely passing the available oracle. It does not establish that patch correctness equals end-to-end task success.

### F7-B: Review, Acceptance, And Completion

#### P11-F7B-01

- **Search ID:** `P11-F7B-01`
- **Date:** `2026-08-20`
- **Evidence stream:** Traditional software-engineering scientific discovery
- **Database / source:** arXiv API
- **Query:** `all:"code review" AND all:"task completion" OR all:"software task completion"`
- **Fields searched:** arXiv `all` fields
- **Filters:** None; first 10 sorted by relevance
- **Result count:** `3` reported by arXiv after API Boolean normalization
- **Results inspected:** All three records and abstracts
- **Clearly relevant results:** One study measured code-review burden and verification effort alongside perceived task completion; the remaining records were adjacent agent/education material. The direct phrase `task completion` did not yield a mature code-review acceptance neighborhood.
- **Clearly irrelevant patterns:** Generic productivity, educational role-play, and agent workflow records used completion without studying acceptance of a software change.
- **Terminology discovered:** `code review burden`, `output verification`, `pull request acceptance`, `merge decision`, `review iteration cycles`, `review comments`, `resolution time`, `review findings`, `modern code review`.
- **Candidate seed sources:** Afroz et al., `The Fast and Spurious: Developer Productivity with GenAI`, 2025, arXiv preprint; useful only for the distinction between perceived task completion and review/verification burden. No direct code-review completion seed was promoted from this exact query.
- **Known-source checks:** SWE-bench `Not applicable to this traditional code-review query`; SWE-agent `Not applicable`; Agentless `Not applicable`; AIDev `Not applicable`; Understanding Software Engineering Agents `Not applicable`.
- **Query adjustment:** `code review AND task completion` -> only three mixed records and no focused acceptance neighborhood -> test `modern code review` / `pull request acceptance` terminology.
- **Rationale:** The observed literature does not support treating `task completion` as the principal code-review term. Acceptance and merge outcomes are more operationally visible in repository mining.
- **Notes:** Code-review literature commonly studies defect detection, review quality, collaboration, review effort, comments, and merge outcomes. These outcomes should not be normalized to completion without source-level extraction.

#### P11-F7B-02

- **Search ID:** `P11-F7B-02`
- **Date:** `2026-08-20`
- **Evidence stream:** Traditional software-engineering scientific discovery, with a coding-agent boundary sample
- **Database / source:** arXiv API
- **Query:** `all:"pull request acceptance" OR all:"merge-ready"`
- **Fields searched:** arXiv `all` fields
- **Filters:** None; first 10 sorted by relevance
- **Result count:** `13` reported by arXiv
- **Results inspected:** First 10 records and abstracts; `Does Code Quality Affect Pull Request Acceptance?`, `Which Pull Requests Get Accepted and Why?`, `Replication Can Improve Prior Results`, and `MathlibPR` source pages/abstracts were inspected.
- **Clearly relevant results:** Pull-request acceptance is a recognizable empirical outcome in GitHub mining. Studies operationalize it as accepted/merged versus rejected/ignored, often using maintainer decisions and repository history. `MathlibPR` explicitly separates merge-ready PRs from build-passing PRs that were revised or never merged.
- **Clearly irrelevant patterns:** `merge-ready` also retrieved unrelated machine-learning model-merging papers; title-level screening is necessary.
- **Terminology discovered:** `pull request acceptance`, `accepted and merged`, `merge decision`, `merge-ready`, `review iteration cycles`, `review resolution`, `maintainer decision`, `revised PR`, `rejected PR`.
- **Candidate seed sources:** Lenarduzzi et al., `Does Code Quality Affect Pull Request Acceptance? An empirical study`, 2019, arXiv record; Dey and Mockus, `Which Pull Requests Get Accepted and Why?`, 2020, arXiv record; Chen, Stolee, and Menzies, `Replication Can Improve Prior Results`, 2019, CEUR/arXiv record; Xie et al., `MathlibPR: Pull Request Merge-Readiness Benchmark for Formal Mathematical Libraries`, 2026, arXiv preprint.
- **Known-source checks:** SWE-bench `Not applicable to traditional pull-request acceptance, but relevant as a coding-agent benchmark boundary`; SWE-agent `Not applicable`; Agentless `Not applicable`; AIDev `Retrieved indirectly through the agent-authored-PR acceptance sample exposed by the revised query`; Understanding Software Engineering Agents `Not applicable`.
- **Query adjustment:** None beyond the recorded revision.
- **Rationale:** Acceptance/merge and merge-readiness are stronger search terms for repository decisions than generic `completion` or `definition of done`. They still represent maintainer/repository outcomes, not necessarily semantic correctness or production quality.
- **Notes:** `MathlibPR` is coding-agent-relevant but not a general coding-agent success paper: it uses historical PR status to distinguish build passing from merge readiness and reports difficulty for agents/models in that classification task. Publication status is an arXiv preprint in this pilot.

### F7-C: Rework, Failure, Retry, And Correction

#### P11-F7C-01

- **Search ID:** `P11-F7C-01`
- **Date:** `2026-08-20`
- **Evidence stream:** Traditional software-engineering scientific discovery
- **Database / source:** arXiv API and OpenAlex Works API
- **Query:** arXiv `all:"software rework" OR all:"issue reopening" OR all:"pull request" AND all:revision`; OpenAlex full-text `"software rework"`
- **Fields searched:** arXiv `all`; OpenAlex full-text search
- **Filters:** arXiv first 10 sorted by relevance; OpenAlex `per-page=10`
- **Result count:** `11` arXiv records; OpenAlex reported `83` full-text matches
- **Results inspected:** arXiv first 10 records and abstracts; OpenAlex first-page metadata/abstracts and DOI/venue fields
- **Clearly relevant results:** The arXiv sample included pull-request revisions and post-initial-commit refactoring. OpenAlex exposed established published terminology including Morozoff, `Using a Line of Code Metric to Understand Software Rework`, 2009, *IEEE Software*, DOI `10.1109/MS.2009.160`; Damm, Lundberg, and Wohlin, `A model for software rework reduction through a combination of anomaly metrics`, 2008, *Journal of Systems and Software*, DOI `10.1016/j.jss.2008.01.017`; and Gopal, Mukhopadhyay, and Krishnan, `The role of software processes and communication in offshore software development`, 2002, *Communications of the ACM*, DOI `10.1145/505248.506008`.
- **Clearly irrelevant patterns:** `revision` retrieved generic document/code revision and unrelated pull-request applications. OpenAlex `software rework` matched older risk/process sources where rework was one project-performance or cost measure rather than a first-pass correction event.
- **Terminology discovered:** `software rework`, `reworked code`, `corrective maintenance`, `revision history`, `post-initial-commit edits`, `review-induced refactoring`, `pull request revision`, `issue reopening`, `rejected change`, `failure recovery`.
- **Candidate seed sources:** Morozoff, 2009, published *IEEE Software*; Damm et al., 2008, published *Journal of Systems and Software*; Coelho et al., `An Empirical Study on Refactoring-Inducing Pull Requests`, 2021, ESEM 2021 record; Khoshnoud et al., `Which bugs are missed in code reviews`, 2022, MSR 2022 record.
- **Known-source checks:** SWE-bench `Not applicable to the traditional rework query`; SWE-agent `Not applicable`; Agentless `Not applicable`; AIDev `Not applicable to traditional rework, although agent-authored PR revision is an adjacent observable`; Understanding Software Engineering Agents `Not applicable`.
- **Query adjustment:** `software rework / issue reopening / pull request revision` -> arXiv returned a small mixed revision neighborhood while OpenAlex returned established but broad project-rework literature -> test exact arXiv `all:"software rework"` and retain OpenAlex only for DOI/venue discovery.
- **Rationale:** Exact arXiv `software rework` returned zero, while OpenAlex exposed a coherent but historically process-oriented rework tradition. Review-induced edits and corrective maintenance are more retrievable observable branches than `issue reopening` alone.
- **Notes:** Rework is established as a software-process/cost/maintenance term, but its unit of analysis varies: code volume not retained in final builds, effort/cost, defect correction, review-induced edit, or later corrective maintenance. These must not be pooled as one failure measure.

#### P11-F7C-02

- **Search ID:** `P11-F7C-02`
- **Date:** `2026-08-20`
- **Evidence stream:** Coding-agent-specific scientific discovery with repository-mining comparison
- **Database / source:** arXiv API
- **Query:** `all:"review rework" OR all:"pull request" AND all:"review comments"`
- **Fields searched:** arXiv `all` fields
- **Filters:** None; first 10 sorted by relevance
- **Result count:** `16` reported by arXiv
- **Results inspected:** First 10 records and abstracts
- **Clearly relevant results:** `An Empirical Study on Refactoring-Inducing Pull Requests` operationalizes edits after initial commits as review-induced or spontaneous refactoring; `SWE-Review: Closing the Loop on Issue Resolution with Agentic Code Review` explicitly uses generate-review-revise and measures review correctness and downstream revision usefulness; `Does AI Code Review Lead to Code Changes?` measures whether review comments lead to code changes; agentic-review studies distinguish accepted, rejected, unresolved, and acted-on comments.
- **Clearly irrelevant patterns:** Vulnerability communication, general review-comment classification, and review-style/quality models appeared beside revision and correction studies.
- **Terminology discovered:** `generate-review-revise loop`, `review correctness`, `downstream revision usefulness`, `comment resolution`, `accepted review comment`, `rejected review comment`, `unresolved comment`, `code change after review`, `review-induced refactoring`, `corrective maintenance`.
- **Candidate seed sources:** Wang et al., `SWE-Review: Closing the Loop on Issue Resolution with Agentic Code Review`, 2026, arXiv preprint; Coelho et al., 2021, ESEM record; Bouraffa et al., `How Do Developers Use Code Suggestions in Pull Request Reviews?`, 2025, CHASE record; Watanabe et al., `On the Use of Agentic Coding: An Empirical Study of Pull Requests on GitHub`, 2025, arXiv preprint; Xia and Miller, `Do These Violent Delights Have Violent Ends? Measuring the Post-Merge Fate of Agentic Code`, 2026, arXiv preprint.
- **Known-source checks:** SWE-bench `Retrieved as the issue-resolution benchmark boundary in SWE-Review-related results, not as a rework study`; SWE-agent `Not applicable to this review-rework query`; Agentless `Not applicable`; AIDev `Retrieved indirectly through agent-authored PR/review studies`; Understanding Software Engineering Agents `Not applicable`.
- **Query adjustment:** None beyond the recorded revision.
- **Rationale:** Review-specific observable outcomes, especially comment resolution and post-review code change, provide more discriminating search vocabulary than generic retry or repair. They remain proxies for further work, not direct proof of unsuccessful first-pass completion.
- **Notes:** The agentic-review records are recent arXiv preprints unless a venue is stated in the record. Human acceptance/rejection and agent-generated review outcomes are separate authorities and should be extracted separately.

### F7-D: Coding-Agent Task Success And Benchmark Evaluation

#### P11-F7D-01

- **Search ID:** `P11-F7D-01`
- **Date:** `2026-08-20`
- **Evidence stream:** Coding-agent-specific scientific discovery
- **Database / source:** arXiv API
- **Query:** `all:"SWE-bench" AND (all:evaluation OR all:correctness OR all:resolution)`
- **Fields searched:** arXiv `all` fields
- **Filters:** None; first 10 sorted by relevance
- **Result count:** `362` reported by arXiv
- **Results inspected:** First 10 records and abstracts; direct source pages for SWE-bench, SWE-agent, Agentless, AIDev, and Understanding Software Engineering Agents
- **Clearly relevant results:** SWE-bench defines issue resolution as generating a patch for a real GitHub issue in a repository environment. SWE-agent reports `pass@1` on SWE-bench. Agentless reports `correct fixes` and a test-based benchmark score. UTBoost, SWE-Bench+, and `Are "Solved Issues" in SWE-bench Really Solved Correctly?` explicitly distinguish passed tests/resolution labels from insufficient tests, plausible-but-incorrect patches, or human/differential correctness checks.
- **Clearly irrelevant patterns:** The large result set included benchmark variants, training methods, multimodal extensions, contamination studies, and general LLM evaluation. `SWE-bench` identifies a benchmark lineage, not a single outcome construct.
- **Terminology discovered:** `issue resolution`, `resolved issue`, `pass@1`, `resolve rate`, `correct fix`, `plausible patch`, `test-passing patch`, `hidden tests`, `patch validation`, `differential patch testing`, `behavioral discrepancy`, `resolution rate`, `benchmark instance`.
- **Candidate seed sources:** Jimenez et al., `SWE-bench: Can Language Models Resolve Real-World GitHub Issues?`, ICLR 2024, arXiv record and OpenReview link inspected; Yang et al., `SWE-agent`, 2024 arXiv record; Xia et al., `Agentless`, 2024 arXiv record; Yu et al., `UTBoost: Rigorous Evaluation of Coding Agents on SWE-Bench`, ACL 2025 record; Wang and Pradel, `Are "Solved Issues" in SWE-bench Really Solved Correctly?`, 2025 arXiv record with DOI `10.1145/3744916.3764576`; Aleithan et al., `SWE-Bench+`, 2024 arXiv record.
- **Known-source checks:** SWE-bench `Retrieved`; SWE-agent `Retrieved`; Agentless `Retrieved`; AIDev `Not applicable to this exact SWE-bench evaluation query`; Understanding Software Engineering Agents `Retrieved indirectly as a trajectory-analysis source using issue-resolution agents, not as a benchmark-definition paper`.
- **Query adjustment:** `SWE-bench AND evaluation/correctness/resolution` -> `362` broad benchmark-lineage records with direct correctness-audit and evaluation terminology -> test broader `coding agent AND evaluation` to capture non-SWE-bench outcome terminology.
- **Rationale:** SWE-bench is high-yield for issue-resolution evaluation but benchmark-dependent. A broader coding-agent evaluation query is needed to avoid equating one benchmark's resolver with coding-agent success generally.
- **Notes:** The SWE-bench source page states 2,294 GitHub issues and corresponding pull requests across 12 Python repositories and reports evaluation as issue resolution. It does not make benchmark resolution equivalent to production acceptance, semantic correctness, or long-term maintainability.

#### P11-F7D-02

- **Search ID:** `P11-F7D-02`
- **Date:** `2026-08-20`
- **Evidence stream:** Coding-agent-specific scientific discovery
- **Database / source:** arXiv API
- **Query:** `all:"coding agent" AND all:evaluation`
- **Fields searched:** arXiv `all` fields
- **Filters:** None; first 10 sorted by relevance
- **Result count:** `577` reported by arXiv
- **Results inspected:** First 10 records and abstracts
- **Clearly relevant results:** `AgentLens` separates formal verification from trajectory review; `LoopsBench` reports resolved tasks and visible regression events; `Change2Task` distinguishes verified task construction from later agent evaluation; `Failure as a Process` studies failure onset, evolution, and recovery rather than only final outcomes; `SWE-PolyBench` uses execution-based evaluation across languages and task types.
- **Clearly irrelevant patterns:** Coding-agent evaluation also includes safety, general agent tasks, harness engineering, training, and non-software benchmarks. The broad phrase requires repository/task and outcome screening.
- **Terminology discovered:** `task success`, `task completion`, `execution-based evaluation`, `formal verification`, `trajectory review`, `production-assessed evaluation`, `resolved task`, `regression event`, `verified task construction`, `failure recovery`, `process-level evaluation`, `pass@1`.
- **Candidate seed sources:** Podivilov et al., `AgentLens: Production-Assessed Trajectory Reviews for Coding Agent Evaluation`, 2026, arXiv preprint; Li et al., `LoopsBench: From Harness Engineering to Loop Engineering in Coding Agent Evaluation`, 2026, arXiv preprint; Qi et al., `Change2Task`, 2026, arXiv preprint; Zhao et al., `Failure as a Process`, 2026, arXiv preprint; Rashid et al., `SWE-PolyBench`, 2025, arXiv preprint.
- **Known-source checks:** SWE-bench `Retrieved as a benchmark lineage in the broader evaluation neighborhood`; SWE-agent `Not verified in the inspected first-page sample`; Agentless `Not verified in the inspected first-page sample`; AIDev `Not verified in the inspected first-page sample`; Understanding Software Engineering Agents `Not verified in the inspected first-page sample`.
- **Query adjustment:** None beyond the recorded broadening from SWE-bench-specific evaluation.
- **Rationale:** The broader query confirms that coding-agent evaluation includes outcome, process, environment, and human/LLM review measures. These are related evaluation traditions, not interchangeable success definitions.
- **Notes:** The inspected sample is mostly recent preprints and benchmark/system papers. Human semantic review was visible in AgentLens-style trajectory review and in SWE-bench correctness audits, but it was not the default authority in the first-page benchmark sample.

## P11 Query Evolution Records

- **Date:** `2026-08-20`
- **Search family:** F7-A verification and patch correctness
- **Original query:** `all:"patch correctness" OR all:"software patch" AND all:validation`; observation: `42` mixed records but a strong patch-correctness cluster; revised query: `all:"patch correctness"`; rationale: isolate the established APCA/patch-overfitting vocabulary and avoid generic validation noise; database: arXiv; Search IDs: `P11-F7A-01`, `P11-F7A-02`.

- **Date:** `2026-08-20`
- **Search family:** F7-B review, acceptance, and completion
- **Original query:** `all:"code review" AND all:"task completion" OR all:"software task completion"`; observation: `3` mixed records and no focused acceptance neighborhood; revised query: `all:"pull request acceptance" OR all:"merge-ready"`; rationale: test repository-mining terminology for maintainer decisions and distinguish merge readiness from generic completion; database: arXiv; Search IDs: `P11-F7B-01`, `P11-F7B-02`.

- **Date:** `2026-08-20`
- **Search family:** F7-C rework, failure, retry, and correction
- **Original query:** `all:"software rework" OR all:"issue reopening" OR all:"pull request" AND all:revision`; observation: `11` arXiv records and `83` OpenAlex full-text matches, with mixed revision/rework meanings; revised query: `all:"review rework" OR all:"pull request" AND all:"review comments"`; rationale: test review-specific revision and comment-resolution vocabulary as observable correction pathways; database: arXiv; Search IDs: `P11-F7C-01`, `P11-F7C-02`.

- **Date:** `2026-08-20`
- **Search family:** F7-D coding-agent task success and benchmark evaluation
- **Original query:** `all:"SWE-bench" AND (all:evaluation OR all:correctness OR all:resolution)`; observation: `362` records centered on a high-yield but benchmark-specific issue-resolution lineage; revised query: `all:"coding agent" AND all:evaluation`; rationale: test whether non-SWE-bench agent evaluation uses distinct outcome/process terminology; database: arXiv; Search IDs: `P11-F7D-01`, `P11-F7D-02`.

No P11 query was silently replaced. No final systematic search string was frozen. The paired searches were sufficient for calibration, but the traditional-SE and coding-agent branches must remain separate during later systematic design.

## P11 Terminology Registry Recalibration

P11 adds only terms materially discovered in the inspected F7 sources. Existing canonical rows such as `SWE-bench`, `agent trajectory / tool-mediated trajectory`, `patch validation`, and coding-agent vocabulary remain single rows and are not duplicated.

| Term | Related concept | Source / Search ID | Context | Action | Notes |
|---|---|---|---|---|---|
| patch correctness | software-change correctness | P11-F7A-01, P11-F7A-02 | Automated program repair | retain as primary F7-A term | Coherent repository/change-level terminology; distinguish from test-passing or plausible patches. |
| plausible patch | software-change verification | P11-F7A-01, P11-F7A-02 | Automated program repair and benchmark evaluation | retain as outcome term | Candidate output that may pass an oracle without being semantically correct. |
| patch overfitting | software-change correctness | P11-F7A-01, P11-F7A-02 | Automated program repair | test provisionally | Established failure/evaluation term for weak-test behavior; not equivalent to all incorrect patches. |
| automated patch correctness assessment (APCA) | correctness evaluation | P11-F7A-01, P11-F7A-02 | Automated program repair | investigate separately | Method family for predicting or labeling patch correctness; classifier accuracy is not patch correctness itself. |
| independent test suite | correctness authority | P11-F7A-01 | Automated program repair | retain as contextual term | An automated oracle used to label patches; may be incomplete. |
| gold correctness labels | correctness authority | P11-F7A-01 | Human-annotated patch datasets | retain as contextual term | Human annotation/gold-set wording; preserve annotator population and agreement. |
| pull request acceptance | review/acceptance outcome | P11-F7B-02 | GitHub mining | retain as primary F7-B term | Operationally visible maintainer/repository outcome; not a synonym for semantic correctness. |
| merge-ready | acceptance/readiness outcome | P11-F7B-02 | Pull-request review and benchmark data | test provisionally | Explicitly separated from build-passing in MathlibPR; may be domain-specific. |
| review iteration cycles | review/rework process | P11-F7B-02, P11-F7C-02 | Pull-request mining | retain as outcome/process term | Counts review rounds or cycles; not a direct completion measure. |
| maintainer decision | acceptance authority | P11-F7B-02 | Open-source pull requests | retain as contextual term | Human/project authority behind accepted, rejected, or ignored PR labels. |
| software rework | rework/correction process | P11-F7C-01 | Traditional software process | retain as primary F7-C term | Established but heterogeneous across cost, code volume, process, and corrective-maintenance studies. |
| review-induced refactoring | review/rework process | P11-F7C-01, P11-F7C-02 | Modern code review | test provisionally | Observable post-initial-commit change associated with review; distinguish spontaneous edits. |
| corrective maintenance | rework/correction outcome | P11-F7C-02 | Software evolution and agent post-merge studies | retain as contextual term | Later correction after integration; not identical to first-pass review rework. |
| comment resolution | review/rework outcome | P11-F7C-02 | Human and agentic code review | retain as primary contextual term | Comment acted on, resolved, rejected, or unresolved; resolution authority varies. |
| generate-review-revise loop | iterative correction | P11-F7C-02 | Coding-agent review | investigate separately | Recent agentic-review process term; benchmark/system specific until broader retrieval. |
| issue resolution | coding-agent benchmark outcome | P11-F7D-01 | SWE-bench and repository-level agents | retain as primary F7-D term | Usually means generated patch passes the benchmark evaluator; extract exact harness definition. |
| pass@1 | coding-agent benchmark outcome | P11-F7D-01 | SWE-agent and benchmark evaluation | retain as benchmark outcome term | Single-attempt score, not a general task-success synonym. |
| resolve rate | coding-agent benchmark outcome | P11-F7D-01, P11-F7D-02 | Repository-level benchmarks | retain as outcome term | Benchmark-specific denominator and evaluator must be recorded. |
| execution-based evaluation | coding-agent evaluation | P11-F7D-02 | Coding-agent benchmarks | retain as primary contextual term | Automated execution/test harness outcome; does not by itself establish semantic or production correctness. |
| formal verification | verification authority | P11-F7D-02 | Coding-agent evaluation and formal software | retain as contextual term | Stronger/different authority when a formal property is checked; not interchangeable with tests. |
| trajectory review | coding-agent process evaluation | P11-F7D-02 | Production-assessed agent evaluation | investigate separately | Human/LLM-readable review of the run in addition to end-state scoring. |
| verified task construction | benchmark/data validation | P11-F7D-02 | Coding-agent benchmark construction | retain as contextual term | Validates task/environment construction, not agent task success. |
| failure recovery | coding-agent rework/process | P11-F7D-02 | Agent trajectories | test provisionally | Process-level recovery terminology; distinguish retry, revision, and final success. |

Terms downgraded or separated in P11:

- `software verification`: downgrade as a primary unqualified F7 term. It spans formal verification, test/oracle checking, requirements verification, and generic quality assurance. Retain only with an object and authority qualifier.
- `validation`: downgrade as an unqualified synonym. Use `patch validation`, `test validation`, `requirements validation`, or an explicitly named verification authority.
- `task completion`: retain as a contextual/outcome phrase, not a stable umbrella for acceptance. The focused code-review query was sparse and mixed; coding-agent papers use it variably for execution, benchmark pass, or user-perceived completion.
- `definition of done`: retain as practitioner/process terminology for a separate Agile/process search, not as a primary F7 academic synonym based on this round.
- `issue reopening`: retain as a possible repository proxy to investigate separately; P11 did not establish a coherent direct retrieval neighborhood.
- `retry`: exclude as a primary F7 term for now. It describes an agent/control action and can occur without an unsuccessful completed task.
- `repair`: separate from rework. Automated program repair is a distinct technical tradition and should not be pooled with human review rework or agent retry.
- `human acceptance`: separate from maintainer merge, reviewer comment acceptance, end-user acceptance, and production approval; P11 found no single common authority.
- `benchmark success`: retain only as a benchmark-qualified outcome label, never as a synonym for semantic correctness or production completion.

## P11 Candidate Seed Sources

The following sources were retrieved or inspected sufficiently for terminology and boundary calibration. They are candidate seeds for later screening, not included evidence or synthesized findings.

| Source | Year and status | DOI or stable URL | Search ID | F7 relevance |
|---|---:|---|---|---|
| Le et al., `On Reliability of Patch Correctness Assessment` | 2018, arXiv record; venue/status requires later verification | [arXiv:1805.05983](https://arxiv.org/abs/1805.05983) | `P11-F7A-01`, `P11-F7A-02` | Automated versus author versus professional-developer correctness labels. |
| Xiong et al., `Identifying Patch Correctness in Test-Based Program Repair` | 2018, ICSE record | [DOI:10.1145/3180155.3180182](https://doi.org/10.1145/3180155.3180182) | `P11-F7A-01` | Test strengthening and patch-correctness assessment. |
| Tian et al., `Is this Change the Answer to that Problem?` | 2022, published DOI record | [DOI:10.1145/3551349.3556914](https://doi.org/10.1145/3551349.3556914) | `P11-F7A-01`, `P11-F7A-02` | Semantic bug/patch correlation as correctness assessment. |
| Morozoff, `Using a Line of Code Metric to Understand Software Rework` | 2009, published *IEEE Software* | [DOI:10.1109/MS.2009.160](https://doi.org/10.1109/MS.2009.160) | `P11-F7C-01` | Software rework as code-volume/process measure. |
| Damm, Lundberg, and Wohlin, `A model for software rework reduction through a combination of anomaly metrics` | 2008, published *Journal of Systems and Software* | [DOI:10.1016/j.jss.2008.01.017](https://doi.org/10.1016/j.jss.2008.01.017) | `P11-F7C-01` | Rework reduction and anomaly/process metrics. |
| Lenarduzzi et al., `Does Code Quality Affect Pull Request Acceptance?` | 2019, arXiv record; later publication requires verification | [arXiv:1908.09321](https://arxiv.org/abs/1908.09321) | `P11-F7B-02` | Maintainer acceptance as repository outcome; quality and acceptance are not assumed equivalent. |
| Chen, Stolee, and Menzies, `Replication Can Improve Prior Results` | 2019, CEUR/arXiv record | [arXiv:1902.04060](https://arxiv.org/abs/1902.04060) | `P11-F7B-02` | Human opinions and merge prediction in pull-request acceptance. |
| Coelho et al., `An Empirical Study on Refactoring-Inducing Pull Requests` | 2021, ESEM record | [arXiv:2108.10994](https://arxiv.org/abs/2108.10994) | `P11-F7C-01`, `P11-F7C-02` | Post-initial-commit review-induced edits and review rework. |
| Jimenez et al., `SWE-bench: Can Language Models Resolve Real-World GitHub Issues?` | 2024, ICLR 2024 record | [arXiv:2310.06770](https://arxiv.org/abs/2310.06770) | `P11-F7D-01` | Benchmark issue-resolution definition and test harness lineage. |
| Yang et al., `SWE-agent: Agent-Computer Interfaces Enable Automated Software Engineering` | 2024, arXiv record | [arXiv:2405.15793](https://arxiv.org/abs/2405.15793) | `P11-F7D-01` | Agent-generated patch, repository execution, test execution, and pass@1. |
| Xia et al., `Agentless: Demystifying LLM-based Software Engineering Agents` | 2024, arXiv preprint | [arXiv:2407.01489](https://arxiv.org/abs/2407.01489) | `P11-F7D-01` | Localization/repair/patch-validation pipeline and benchmark boundary. |
| Yu et al., `UTBoost: Rigorous Evaluation of Coding Agents on SWE-Bench` | 2025, ACL 2025 | [ACL record](https://aclanthology.org/2025.acl-long.189/) | `P11-F7D-01` | Test insufficiency and erroneous passed patches in benchmark scoring. |
| Wang and Pradel, `Are "Solved Issues" in SWE-bench Really Solved Correctly?` | 2025, arXiv record with DOI | [arXiv:2503.15223](https://arxiv.org/abs/2503.15223) | `P11-F7D-01` | Differential testing, human inspection, and benchmark-resolution correctness gap. |
| Li, Zhang, and Hassan, `AIDev: Studying AI Coding Agents on GitHub` | 2026, arXiv record with related DOI | [arXiv:2602.09185](https://arxiv.org/abs/2602.09185) | `P11-F7B-02`, `P11-F7C-02` | Agent-authored PRs, reviews, comments, and merge outcomes; not a direct benchmark-success study. |
| Bouzenia and Pradel, `Understanding Software Engineering Agents` | 2025, arXiv record stating ASE 2025 acceptance | [arXiv:2506.18824](https://arxiv.org/abs/2506.18824) | `P11-F7D-01` | Successful/failed execution trajectories and process outcomes; not a completion-authority paper. |
| Wang et al., `SWE-Review: Closing the Loop on Issue Resolution with Agentic Code Review` | 2026, arXiv preprint | [arXiv:2607.06065](https://arxiv.org/abs/2607.06065) | `P11-F7C-02`, `P11-F7D-02` | Review decision, revision usefulness, and post-review resolve rate. |
| Podivilov et al., `AgentLens: Production-Assessed Trajectory Reviews for Coding Agent Evaluation` | 2026, arXiv preprint | [arXiv:2607.06624](https://arxiv.org/abs/2607.06624) | `P11-F7D-02` | Formal checks paired with trajectory reviews and production assessment. |
| Xia and Miller, `Do These Violent Delights Have Violent Ends?` | 2026, arXiv preprint | [arXiv:2607.09902](https://arxiv.org/abs/2607.09902) | `P11-F7C-02` | Post-merge corrective maintenance and longer-term contribution outcomes. |

## P11 Outcome Definitions And Evaluation Authorities

The inspected sources used materially different outcome definitions:

- **Agent-generated output:** A patch, pull request, code edit, or trajectory was produced. This is an output event, not evidence of correctness or acceptance.
- **Automated test success:** The patch passes the repository or benchmark test suite, sometimes including hidden tests or an independent test suite. This is an automated oracle outcome and may be incomplete.
- **Benchmark instance resolution:** SWE-bench-style studies generally count an instance as resolved when the generated patch satisfies the benchmark evaluator. The denominator, test harness, patch applicability, and execution environment are benchmark-specific.
- **Patch correctness:** APR literature uses human labels, independent test suites, behavioral/differential testing, semantic correlation, or combinations. The sources explicitly distinguish plausible/test-passing patches from correct/generalizable patches.
- **Review/acceptance:** A maintainer accepts, merges, rejects, ignores, or requests changes on a pull request; review comments may be accepted, rejected, resolved, or left unresolved. These are repository/social decisions, not automatically semantic correctness judgments.
- **Rework/correction:** Additional code after an initial commit, review-induced refactoring, corrective maintenance, post-merge bug fixing, or measured reworked code. These are different temporal and causal operationalizations.
- **Process success/failure:** Trajectory studies classify successful/failed execution, recovery, failure onset, feedback integration, or regression events. They assess process records in addition to or instead of final status.
- **Production quality/completion:** The pilot retrieved post-merge maintenance and production-assessed trajectory studies, but this is not the default coding-agent benchmark outcome and has limited direct evidence in this sample.

Evaluation authorities observed:

- automated repository tests, hidden tests, independent test suites, build/compile checks, and formal verifiers;
- benchmark harnesses that construct the environment, apply/extract the patch, and assign resolved/pass labels;
- static or learned patch-correctness predictors, which predict an authority's label rather than becoming the authority themselves;
- human professional developers or researchers annotating patch correctness and inter-rater agreement;
- project maintainers deciding PR acceptance/merge/rejection;
- users/developers resolving review comments or accepting suggested changes;
- mixed authorities combining tests, differential behavior, human inspection, maintainer history, and trajectory review.

No authority was treated as interchangeable with another. The pilot did not establish a universal hierarchy among them.

## Traditional Software Versus Coding-Agent Distinctions

- Traditional software-engineering literature is split across formal verification, software testing, automated program repair, requirements validation, modern code review, GitHub mining, software-process rework, and maintenance. Its units of analysis range from formal properties and test cases to patches, review comments, PR histories, effort, and post-release changes.
- Coding-agent literature is newer and dominated by benchmark evaluations, agent-system papers, trajectory studies, and GitHub mining of agent-authored PRs. It often operationalizes success as a generated patch passing a benchmark evaluator or as a PR being accepted/merged, with less frequent human semantic review.
- F5/F6 terminology such as `coding agent`, `software engineering agent`, `SWE-agent`, `agentless`, `agent trajectory`, `agent-environment interaction`, and `ACI` identifies populations, architectures, or execution records. It does not identify one success construct.
- Traditional patch-correctness and review literature can provide terminology and measurement alternatives, but transfer to coding agents requires explicit comparison of executor, issue/task setting, available context, authority, and outcome definition.
- `Task completion` in human productivity studies, `issue resolution` in benchmark studies, `PR acceptance` in repository mining, and `patch correctness` in APR should remain separate rows and search branches.

## Benchmark Dependencies And Limitations

- SWE-bench and related benchmarks depend on issue statements, repository snapshots, patch application/extraction, execution environments, repository tests, and often hidden tests. The benchmark result is conditional on that protocol.
- The inspected audits report weak or insufficient tests, plausible-but-incorrect patches, solution leakage, contamination concerns, and differences between generated and developer patches. These are calibration observations from the retrieved sources, not a final benchmark-validity judgment.
- Hidden tests and repository tests can detect behavior not covered by visible tests, but passing either remains an oracle result rather than a complete semantic or production-quality judgment.
- Patch applicability, environment setup, dependency versions, flaky/brittle tests, and benchmark instance construction can affect measured resolution independently of the agent's underlying software-engineering capability.
- Human review is meaningfully present in patch-correctness gold sets, correctness audits, PR acceptance histories, MathlibPR merge-readiness, and production-assessed trajectory studies. It is not the default authority in the ordinary first-page SWE-bench evaluation sample.
- Standard issue-to-patch benchmarks generally do not provide a normal user-approval or clarification loop. Interactive and review benchmarks add different authorities and should not be pooled with standard scores.
- Agent-authored PR acceptance and post-merge maintenance provide real-repository observables, but they measure social/project acceptance and later maintenance outcomes, not the same construct as benchmark resolution.

## P11 Calibration Assessment

### Conceptual coherence

- **F7-A:** Moderate to high after separating formal verification, testing/oracle validation, patch correctness, and generic quality assurance. `Patch correctness` is a coherent repository-level/APR neighborhood, but it remains adjacent to testing and program repair.
- **F7-B:** Moderate. Pull-request acceptance, merge readiness, review findings, review quality, collaboration, and task completion are connected but have different units of analysis and authorities. `Definition of done` was not validated as a primary academic term.
- **F7-C:** Moderate. Software rework is established, but its measures span cost, code volume, review revisions, corrective maintenance, and post-merge changes. Review-induced edits and comment resolution are useful narrower branches; issue reopening was not established as a standalone neighborhood.
- **F7-D:** High as a coding-agent evaluation family only after separating benchmark resolution, automated test success, patch correctness, human/maintainer acceptance, process/trajectory evaluation, and production/post-merge outcomes.

### Retrieval coherence

- **F7-A:** Exact `patch correctness` retrieval was recognizable and lower-noise than unqualified verification/validation. APR and patch-overfitting terms should be searched separately from formal verification and requirements validation.
- **F7-B:** `task completion` was sparse and noisy with code review. `pull request acceptance`, `merge decision`, and `merge-ready` produced a clearer repository-mining neighborhood but still mixed social acceptance and quality questions.
- **F7-C:** `software rework` was absent in the exact arXiv query but visible in OpenAlex historical metadata; review/revision terms retrieved a more actionable but heterogeneous modern-code-review neighborhood. Generic `retry` and `repair` are too broad or technically different.
- **F7-D:** SWE-bench is high-yield but benchmark-specific. `coding agent AND evaluation` broadens coverage to process, formal verification, trajectory review, environment, regression, and failure-recovery terms, requiring strong screening.

### Empirical maturity

- F7-A includes established traditional APR and testing research with empirical datasets, human labeling, and learned assessment methods.
- F7-B and F7-C include mature mining-software-repository and modern-code-review traditions, alongside recent agentic-review preprints.
- F7-D is rapidly developing and benchmark-heavy. SWE-bench has an established benchmark lineage; newer process and human-review evaluations are recent and often preprint-based.

### Relationship to previous families

- **F1:** Issues, tickets, issue descriptions, pull requests, and repository changes are the objects whose resolution or acceptance is evaluated; F7 must not duplicate work-unit representation searches.
- **F2:** Requirements, acceptance criteria, and requirements validation define or test expected behavior; F7 searches outcomes/authorities and should cross-screen without treating acceptance criteria as proof of completion.
- **F3:** Task type, decomposition, plans, and subtask structure may moderate success and rework; F7 measures outcomes/processes rather than task representation or decomposition.
- **F5:** Coding-agent population terms are required for F7-D and for recent F7-B/C agentic-review studies.
- **F6:** Planning, context, repository exploration, tool use, trajectories, clarification, and feedback describe execution conditions/processes. F7 adds outcome and correction labels; trajectory success/failure is not equivalent to final correctness.

## Answers To P11 Special Questions

1. **Is `software verification` too broad to serve as a primary F7 term?** Yes, for primary unqualified retrieval. The inspected material spans formal properties, tests/oracles, requirements validation, patch validation, and quality assurance. Use object-qualified branches such as `patch correctness`, `formal verification`, `regression testing`, or `requirements validation`.
2. **Is `patch correctness` a coherent repository-level research concept?** Yes, provisionally. APR studies repeatedly use it for whether generated patches are correct/generalizable beyond an available test oracle. It remains a patch/artifact construct, not a complete task-success construct.
3. **Is `task completion` established software-engineering terminology?** It is used, including in software-task productivity and coding-agent papers, but P11 did not establish it as a stable cross-tradition term for acceptance or correctness. Its meaning must be extracted per study.
4. **Does code review literature meaningfully represent acceptance/completion, or mainly defect detection and collaboration?** Both exist, but the focused query and inspected sources show substantial emphasis on defect detection, review comments, quality, collaboration, effort, and repository decisions. Acceptance/merge is a distinct mining outcome; review is not a synonym for completion.
5. **Is `software rework` a coherent research branch?** It is coherent enough as a traditional software-process/rework branch, but not as one uniform operational measure. Cost, code volume, review edits, corrective maintenance, and post-merge changes require separate extraction or sub-branches.
6. **Are issue reopening or pull-request revision useful observable proxies for rework?** Pull-request revision and post-initial-commit edits are useful observables for further work, with known attribution limits. Issue reopening was not sufficiently retrieved to validate as a primary proxy in this pilot.
7. **How do coding-agent papers operationalize task success?** Most inspected benchmark papers use resolved instances, pass@1, resolve rate, correct fixes, or execution/test outcomes. Other studies use PR acceptance/merge, trajectory success/failure, formal checks, review correctness, downstream revision usefulness, or post-merge maintenance.
8. **How dependent are coding-agent success definitions on automated tests?** Highly dependent in repository-level benchmark literature, especially SWE-bench-derived work. The retrieved audits explicitly show why test passing can diverge from semantic correctness. Human review and post-merge outcomes occur, but less often in ordinary benchmark scoring.
9. **Does SWE-bench resolution represent correctness, benchmark completion, or both according to the literature?** The benchmark papers use resolution as benchmark completion under an evaluator, commonly test-based. The retrieved correctness audits show that this label can include plausible or behaviorally divergent patches, so it should not be treated automatically as semantic correctness or production completion.
10. **Is human semantic review meaningfully represented in coding-agent evaluations?** Yes, but unevenly. It appears in correctness gold sets/audits, differential-patch inspection, maintainer PR history, MathlibPR merge-readiness, and production-assessed trajectory review. It is not the default authority across the inspected benchmark sample.
11. **Does F7 need separate traditional-software and coding-agent success branches?** Yes. Traditional branches include APR patch correctness, testing/verification, code-review mining, acceptance, rework, and maintenance. Coding-agent branches add benchmark harnesses, agent trajectories, tool/environment conditions, agent-authored PRs, and recent mixed human/automated evaluation. Transfer is not automatic.
12. **Does F7 require further subdivision before systematic-search design?** Yes. The four provisional labels are useful containers, but systematic design should separate at least F7-A patch correctness/testing/formal verification, F7-B review/merge acceptance from generic completion, F7-C process rework from review-induced revision and post-merge correction, and F7-D benchmark resolution from human acceptance, semantic correctness, process evaluation, and production/post-merge quality.

## Recommended F7 Search Status

| Branch | Status | Methodological reason |
|---|---|---|
| F7-A Verification and validation of software changes | `Requires further calibration` | Patch correctness is coherent, but formal verification, test/oracle validation, requirements validation, regression, and generic QA must be separated before systematic searching. |
| F7-B Review, acceptance, and completion | `Requires further calibration` | Pull-request acceptance and merge readiness are searchable, while generic task completion, review quality, collaboration, and definition-of-done terminology are not one outcome neighborhood. |
| F7-C Rework, failure, retry, and correction | `Requires further calibration` | Software rework is established but operationally heterogeneous; review revision, comment resolution, corrective maintenance, issue reopening, and retry need distinct treatment. |
| F7-D Coding-agent task success and benchmark evaluation | `Requires further calibration` | Benchmark resolution is recognizable but heavily test- and environment-dependent; semantic correctness, human acceptance, trajectory/process success, and production quality require separate evaluation branches. |

## F7 Remaining Uncertainty

- The pilot used arXiv and OpenAlex discovery rather than the protocol's full systematic databases; venue coverage and publication completeness remain untested.
- Several recent coding-agent records are preprints or future-dated relative to older rounds; later screening must verify publication status, versions, and duplicate records.
- Abstract-level retrieval cannot establish the exact hidden-test design, patch applicability rules, test brittleness, environment configuration, or human-review procedure of every benchmark.
- `Software verification`, `validation`, `acceptance`, `completion`, and `quality` may have stronger standards-based terminology that was not searched in this round.
- The relation between review acceptance and semantic correctness remains context-dependent; maintainer decisions may reflect project, social, timing, or scope factors.
- Rework proxies may be affected by repository conventions, issue-tracking completeness, review policy, contributor behavior, and post-merge observation windows.
- Human semantic review in coding-agent evaluation is visible but not yet quantifiable from this pilot; the sample does not support a frequency claim.
- Agent trajectories provide process records, but success/failure labels and trajectory quality may be framework-, model-, environment-, and benchmark-dependent.
- No substantive conclusion was drawn about whether tests, review, acceptance criteria, verification, or any other mechanism is necessary or sufficient.

## F7 Exit Decision

**F7 should be split into distinct search subfamilies before systematic-search design**

The methodological reason is that P11 retrieved distinct neighborhoods for patch correctness and oracle limitations, pull-request review and maintainer acceptance, software-process/review rework and correction, and coding-agent benchmark/process evaluation. Within those neighborhoods, automated test success, benchmark instance resolution, patch semantic correctness, human/maintainer acceptance, trajectory success, and production/post-merge quality are different outcomes with different evaluation authorities. A systematic search should therefore preserve traditional-software and coding-agent streams and subdivide each by object, authority, and outcome rather than use one F7 query.

F7 pilot exploration cannot close; another focused pilot may be needed after the split is specified. All seven search families have not completed pilot calibration because F7 requires this methodological subdivision before systematic-search design. This is a search-method decision only and does not interpret the literature as defining Work Item requirements.

No Work Item characteristics, acceptance criteria, lifecycle, hypotheses, or research conclusions were derived. Review was not concluded to be required, automated tests were not concluded to be sufficient, benchmark success was not equated with semantic correctness, and rework was not attributed to any Work Item property. No commit was made.

## Pilot Round 12 Family 7 Subfamily Calibration

Pilot Round 12 was conducted on 2026-08-20 to test whether the four P11 containers should be split into retrieval- and outcome-coherent subfamilies before systematic-search design. Searches used focused arXiv API discovery and an OpenAlex full-text discovery query. Counts are source-reported diagnostics, not estimates of prevalence, precision, recall, or evidence strength. The round remained a terminology and method calibration exercise; it did not derive Work Item characteristics or decide which evaluation authority is universally valid.

### P12-F7A: Change Correctness And Validation

#### P12-F7A-01

- **Search ID:** `P12-F7A-01`
- **Date:** `2026-08-20`
- **Evidence stream:** Traditional software-engineering scientific discovery
- **Database / source:** arXiv API
- **Query:** Focused combinations of `patch correctness`, `patch validation`, `regression`, `test suite`, and `correct patch` terms
- **Fields searched:** arXiv `all` fields
- **Filters:** None; relevance-ranked discovery sample
- **Result count:** `11` reported by arXiv
- **Results inspected:** Returned records and abstracts, including `On Reliability of Patch Correctness Assessment`
- **Clearly relevant results:** The sample formed a recognizable patch-correctness and validation neighborhood. It included automated test-suite assessment, independent-test assessment, human/author labels, plausible-versus-correct patches, and regression-oriented validation.
- **Clearly irrelevant patterns:** Generic testing, validation outside software changes, and classifier-performance papers appeared beside studies whose actual object was patch correctness.
- **Terminology discovered:** `patch correctness`, `plausible patch`, `patch overfitting`, `independent test suite`, `behavioral discrepancy`, `semantic correctness`, `regression test`, `patch validation`.
- **Candidate seed sources:** Le et al., `On Reliability of Patch Correctness Assessment`, 2018, arXiv record; the abstract distinguishes test-suite, author, and professional-developer labels. The P11 patch-correctness seeds remain applicable.
- **Known-source checks:** SWE-bench `Not applicable to this traditional change-correctness query`; SWE-agent `Not applicable`; Agentless `Not applicable`; AIDev `Not applicable`; Understanding Software Engineering Agents `Not applicable`.
- **Query adjustment:** Broad correctness/validation combinations -> focused patch-correctness and validation combinations -> retain object-qualified terms and avoid unqualified `verification` as a single branch.
- **Rationale:** The search supports a coherent change-level outcome neighborhood, but automated test passing, semantic correctness, and evaluation-model accuracy are different outcomes and authorities.
- **Notes:** This branch covers the correctness of a software change or patch. It does not establish end-to-end task completion, maintainer acceptance, or production quality.

### P12-F7B: Review And Acceptance

#### P12-F7B-01

- **Search ID:** `P12-F7B-01`
- **Date:** `2026-08-20`
- **Evidence stream:** Traditional software-engineering scientific discovery
- **Database / source:** arXiv API
- **Query:** Focused combinations of `code review`, `acceptance`, `merge`, `pull request`, `review findings`, and `maintainer decision`
- **Fields searched:** arXiv `all` fields
- **Filters:** None; relevance-ranked discovery sample
- **Result count:** `80` reported by arXiv
- **Results inspected:** Returned records and abstracts, including `Mining Code Review Data to Understand Waiting Times Between Acceptance and Merging`
- **Clearly relevant results:** Review decisions, acceptance, merge timing, review findings, and maintainer/repository decisions formed a retrievable neighborhood distinct from generic task completion.
- **Clearly irrelevant patterns:** Some records concerned review automation, review quality prediction, or collaboration without an acceptance/merge outcome; title and abstract screening remains necessary.
- **Terminology discovered:** `code review acceptance`, `pull request acceptance`, `merge decision`, `accepted and merged`, `maintainer decision`, `review findings`, `review outcome`, `review iteration`.
- **Candidate seed sources:** Existing P11 pull-request acceptance sources; `Mining Code Review Data to Understand Waiting Times Between Acceptance and Merging`, publication status and venue to be verified during later screening.
- **Known-source checks:** SWE-bench `Not applicable as a traditional review-acceptance study`; SWE-agent `Not applicable`; Agentless `Not applicable`; AIDev `Not verified in this focused traditional sample`; Understanding Software Engineering Agents `Not applicable`.
- **Query adjustment:** P11 `task completion` terminology -> acceptance/merge and maintainer-decision terminology -> retain review and acceptance as separate from semantic correctness and benchmark resolution.
- **Rationale:** Repository acceptance is operationally observable, but it is a social/project outcome whose authority is a maintainer or repository history, not automatically a correctness oracle.
- **Notes:** Acceptance, review-comment resolution, merge readiness, and semantic correctness must be extracted separately when co-occurring.

### P12-F7C: Rework And Revision

#### P12-F7C-01

- **Search ID:** `P12-F7C-01`
- **Date:** `2026-08-20`
- **Evidence stream:** Traditional software-engineering scientific discovery
- **Database / source:** arXiv API
- **Query:** Focused combinations of `pull request`, `revision`, `review iteration`, `rework`, and `issue reopening`
- **Fields searched:** arXiv `all` fields
- **Filters:** None; relevance-ranked discovery sample
- **Result count:** `6` reported by arXiv
- **Results inspected:** Returned records and abstracts
- **Clearly relevant results:** Pull-request revision and review-iteration records provided an observable neighborhood for additional work after an initial change. Issue reopening was much less consistently represented.
- **Clearly irrelevant patterns:** Generic document revision, unrelated pull-request applications, and broad software-maintenance uses of `rework` occurred in the sample.
- **Terminology discovered:** `pull request revision`, `review iteration`, `post-initial-commit edit`, `issue reopening`, `review-induced change`, `corrective change`, `revision cycle`.
- **Candidate seed sources:** Existing P11 sources on review-induced refactoring, review rework, and software rework remain candidates; no new source was promoted solely from this sparse sample.
- **Known-source checks:** SWE-bench `Not applicable to traditional rework`; SWE-agent `Not applicable`; Agentless `Not applicable`; AIDev `Not verified in this focused traditional sample`; Understanding Software Engineering Agents `Not applicable`.
- **Query adjustment:** P11 mixed rework/revision query -> narrower revision and iteration terms -> retain review-induced revision as an observable branch and treat issue reopening as an unvalidated proxy.
- **Rationale:** Further work is observable, but the causal meaning varies: reviewer request, spontaneous refactoring, defect correction, maintenance, or process policy.
- **Notes:** Rework is not a single failure label. The unit, trigger, timing, and authority must be recorded for each study.

### P12-F7D: Coding-Agent Benchmark Success

#### P12-F7D-01

- **Search ID:** `P12-F7D-01`
- **Date:** `2026-08-20`
- **Evidence stream:** Coding-agent-specific scientific discovery
- **Database / source:** arXiv API
- **Query:** Focused combinations of `coding agent`, `SWE-bench`, `resolved issue`, `correct fix`, `benchmark`, and `evaluation`
- **Fields searched:** arXiv `all` fields
- **Filters:** None; relevance-ranked discovery sample
- **Result count:** `21` reported by arXiv
- **Results inspected:** Returned records and abstracts, including `SWE-Bench+: Enhanced Coding Benchmark for LLMs`
- **Clearly relevant results:** Coding-agent benchmark papers used `resolved issue`, `resolve rate`, `pass@1`, `correct fix`, test execution, and benchmark-specific evaluators. The sample also contained audits showing that test-passing or solved labels can diverge from semantic correctness.
- **Clearly irrelevant patterns:** Benchmark construction, contamination, training, harness engineering, and non-software agent evaluation appeared beside task-success studies.
- **Terminology discovered:** `resolved issue`, `resolve rate`, `pass@1`, `correct fix`, `benchmark instance`, `hidden tests`, `test-passing patch`, `differential testing`, `benchmark evaluator`.
- **Candidate seed sources:** Jimenez et al., `SWE-bench`; Yang et al., `SWE-agent`; Agentless; Yu et al., `UTBoost`; Wang and Pradel, `Are "Solved Issues" in SWE-bench Really Solved Correctly?`; Aleithan et al., `SWE-Bench+`. Publication statuses remain as recorded in P11 and require later screening verification.
- **Known-source checks:** SWE-bench `Retrieved`; SWE-agent `Retrieved`; Agentless `Retrieved`; AIDev `Not applicable to this benchmark-focused sample`; Understanding Software Engineering Agents `Not verified in this focused benchmark sample`.
- **Query adjustment:** P11 broad coding-agent evaluation -> benchmark- and resolution-qualified terms -> preserve benchmark success as a coding-agent branch, but do not pool it with semantic correctness or repository acceptance.
- **Rationale:** This is the highest-yield coding-agent outcome neighborhood, but its definition depends on issue construction, patch application, environment, tests, and benchmark scoring.
- **Notes:** A benchmark result is conditional on its evaluator and denominator. It is not a universal task-success or production-quality measure.

### P12-F7E: Human And Semantic Evaluation

#### P12-F7E-01

- **Search ID:** `P12-F7E-01`
- **Date:** `2026-08-20`
- **Evidence stream:** Coding-agent-specific scientific discovery
- **Database / source:** arXiv API
- **Query:** Focused combinations of `human evaluation`, `coding agent`, `software engineering agent`, `semantic`, `correctness`, and `quality`
- **Fields searched:** arXiv `all` fields
- **Filters:** None; relevance-ranked discovery sample
- **Result count:** `4` reported by arXiv
- **Results inspected:** Returned records and abstracts, including `SEAlign: Alignment Training for Software Engineering Agent`
- **Clearly relevant results:** Human evaluation was visible in application/task-performance and user-experience assessment, and in adjacent coding-agent evaluation records. It was sparse compared with automated benchmark evaluation and was not standardized across the sample.
- **Clearly irrelevant patterns:** General human evaluation, preference optimization, and non-software user studies appeared beside coding-agent records.
- **Terminology discovered:** `human evaluation`, `user experience`, `semantic correctness`, `production-assessed evaluation`, `trajectory review`, `professional-developer annotation`, `human inspection`.
- **Candidate seed sources:** Zhang et al., `SEAlign: Alignment Training for Software Engineering Agent`, 2025, arXiv record; P11 correctness-audit, MathlibPR, and AgentLens sources remain relevant adjacent seeds.
- **Known-source checks:** SWE-bench `Retrieved indirectly through human/differential correctness audits, not as a human-evaluation paper`; SWE-agent `Not verified in this focused human-evaluation sample`; Agentless `Not verified`; AIDev `Not verified`; Understanding Software Engineering Agents `Not verified`.
- **Query adjustment:** Broad human/semantic evaluation query -> exact `"human evaluation" AND "software engineering agent"` revision -> one result, confirming retrievability but low yield.
- **Rationale:** Human/semantic evaluation is methodologically distinct because the authority and rubric differ from tests and benchmark harnesses, but P12 does not support treating it as a mature standalone primary branch without broader databases and citation chasing.
- **Notes:** Record this as a supplementary evaluation-authority branch for systematic design, with possible expansion if later database coverage produces a coherent corpus. Do not infer frequency from the four-result sample.

## P12 Query Evolution Records

- **Date:** `2026-08-20`; **Search family:** F7-A; **Search ID:** `P12-F7A-01`; **evolution:** P11 exact `patch correctness` -> patch correctness plus validation, regression, test-suite, and correctness qualifiers; **decision:** retain `patch correctness` and object-qualified validation terms, while separating test/oracle outcomes from semantic correctness.
- **Date:** `2026-08-20`; **Search family:** F7-B; **Search ID:** `P12-F7B-01`; **evolution:** P11 acceptance/merge vocabulary -> review, acceptance, merge, findings, and maintainer-decision qualifiers; **decision:** retain review/acceptance as a distinct repository-outcome branch.
- **Date:** `2026-08-20`; **Search family:** F7-C; **Search ID:** `P12-F7C-01`; **evolution:** P11 mixed rework/review query -> revision, review iteration, post-initial-commit, and issue-reopening qualifiers; **decision:** retain rework/revision, but do not promote issue reopening to a primary branch.
- **Date:** `2026-08-20`; **Search family:** F7-D; **Search ID:** `P12-F7D-01`; **evolution:** P11 broad coding-agent evaluation -> benchmark, resolution, correct-fix, and evaluator qualifiers; **decision:** retain coding-agent benchmark success as a separate branch with explicit benchmark dependence.
- **Date:** `2026-08-20`; **Search family:** F7-E; **Search ID:** `P12-F7E-01`; **evolution:** broad human/semantic evaluation -> exact `"human evaluation" AND "software engineering agent"`; **decision:** retain as a supplementary authority branch pending broader retrieval and screening.

No P12 query was silently replaced. Each query was retained as a calibration record. No systematic search string was frozen.

## P12 Calibrated F7 Structure

P12 supports replacing the four P11 containers with the following provisional structure:

| Provisional subfamily | Object / outcome | Typical authority | Retrieval status | Calibration status |
|---|---|---|---|---|
| **F7-A Change correctness and validation** | Patch/change correctness, test/oracle validation, regression behavior, formal or semantic checks | Tests, independent suites, formal verifiers, human annotators, differential behavior | Coherent when object-qualified | `Calibrated for systematic-search design` |
| **F7-B Review and acceptance** | Review findings, comment outcomes, pull-request acceptance, merge readiness, maintainer decisions | Reviewers, maintainers, repository history | Coherent but socially heterogeneous | `Calibrated for systematic-search design` |
| **F7-C Rework and revision** | Review-induced edits, revision cycles, corrective maintenance, post-initial-commit or post-merge change | Review process, repository history, maintenance records | Retrievable but operationally heterogeneous | `Calibrated with explicit sub-branches` |
| **F7-D Coding-agent benchmark success** | Resolved benchmark instance, resolve rate, pass@1, correct-fix label | Benchmark harness, tests, hidden tests, evaluator protocol | High yield but benchmark-dependent | `Calibrated for systematic-search design` |
| **F7-E Human and semantic evaluation** | Human correctness, semantic quality, user experience, production or trajectory assessment | Professional developers, maintainers, users, expert reviewers, mixed protocols | Sparse in focused arXiv discovery | `Supplementary; expand during systematic design if coverage supports it` |

The structure is coherent at the level of outcome neighborhood and evaluation authority, not because the outcomes are equivalent. Automated test success remains a cross-cutting authority/context dimension in F7-A and F7-D; P12 did not establish it as a sixth independent outcome family. Review acceptance remains distinct from correctness. Rework/revision remains distinct from failure because additional work may be deliberate or beneficial. Human/semantic evaluation remains distinct from both automated outcomes and social acceptance, despite its sparse retrieval.

## P12 Terminology Registry Recalibration

| Term | Related concept | Source / Search ID | Context | Action | Notes |
|---|---|---|---|---|---|
| patch validation | change correctness | P12-F7A-01 | Program repair and software changes | retain with object qualifier | Do not merge with generic validation. |
| semantic correctness | change/task correctness | P12-F7A-01, P12-F7E-01 | Patch audits and human evaluation | retain as outcome term | Extract rubric and authority; not equivalent to test passing. |
| regression test | change validation | P12-F7A-01 | Software testing | retain as contextual term | A test artifact/outcome, not a universal correctness definition. |
| maintainer decision | acceptance authority | P12-F7B-01 | Pull-request mining | retain as primary contextual term | Accepted, rejected, ignored, or revision-requested states must remain distinct. |
| review finding | review outcome/process | P12-F7B-01 | Code review | retain as outcome/process term | A finding is not necessarily a defect or an unsuccessful task. |
| review iteration | revision process | P12-F7C-01 | Pull-request review | retain as primary F7-C term | Count and causal interpretation vary by study. |
| post-initial-commit edit | rework/revision | P12-F7C-01 | Repository history | test provisionally | Observable additional work with uncertain trigger. |
| benchmark evaluator | coding-agent authority | P12-F7D-01 | Repository-level benchmarks | retain as contextual term | Record harness, tests, denominator, and patch applicability. |
| correct fix | coding-agent outcome | P12-F7D-01 | Benchmark evaluation | retain with benchmark qualifier | Do not assume semantic or production correctness. |
| human evaluation | human/semantic authority | P12-F7E-01 | Coding-agent and application evaluation | retain as supplementary branch term | Sparse focused retrieval; rubric and evaluator population are essential. |
| user experience | human evaluation outcome | P12-F7E-01 | Agent-created applications | test provisionally | User experience is not identical to code correctness or acceptance. |

Terms retained as separate or downgraded after P12:

- `automated test success`: retain as an authority-qualified outcome, not a universal F7 branch.
- `semantic correctness`: retain separately from `patch correctness` when the study's object or rubric differs.
- `acceptance`: qualify as pull-request, review-comment, user, maintainer, or production acceptance.
- `rework`: qualify by trigger and temporal unit, such as review-induced revision or post-merge corrective maintenance.
- `human evaluation`: retain as a supplementary branch until broader retrieval establishes its corpus size and operational diversity.
- `task completion`, `verification`, and `validation`: do not use unqualified as umbrella search terms.

## P12 Outcome Definitions And Evaluation Authorities

P12 did not collapse the following outcomes:

- **Change correctness:** Whether a patch or code change satisfies intended behavior under the study's correctness protocol.
- **Automated validation:** Whether tests, an independent suite, a build, or a formal checker accepts the change. This is an authority result and may be incomplete.
- **Review/acceptance:** Whether reviewers or maintainers accept, merge, reject, ignore, or request changes. This is a repository/social outcome.
- **Rework/revision:** Additional work after an initial change, with trigger and timing extracted separately.
- **Benchmark success:** Whether a benchmark instance receives a passing/resolved/correct-fix label under its evaluator.
- **Human/semantic evaluation:** Expert, maintainer, user, or production assessment under an explicit rubric or review process.

Observed authorities were automated tests and hidden tests; independent test suites; formal verifiers; benchmark harnesses; human professional developers; reviewers and maintainers; users; repository history; and mixed differential/trajectory protocols. No authority was treated as universally superior or interchangeable with another.

## Traditional Software Versus Coding-Agent Boundaries

- Traditional-SE retrieval remains necessary for automated program repair, testing, formal verification, code review, pull-request mining, software rework, and maintenance. Its units of analysis include patches, tests, comments, PRs, repositories, effort, and post-release changes.
- Coding-agent retrieval requires population and execution qualifiers such as `coding agent`, `software engineering agent`, benchmark, trajectory, repository environment, or agent-authored PR. It adds benchmark harnesses, tool-mediated trajectories, agent-environment interaction, and agent-authored repository outcomes.
- Traditional patch correctness, review acceptance, and rework findings may inform coding-agent measurement, but executor, task setting, context, authority, and outcome definition must be compared explicitly.
- Human evaluation in a traditional review or APR study must not be assumed equivalent to human evaluation of an autonomous coding-agent trajectory or generated application.

## Benchmark Dependencies And Limitations

- Coding-agent benchmark outcomes depend on issue construction, repository snapshot, patch application, environment, dependencies, visible/hidden tests, and scoring protocol.
- A passed test or resolved label can differ from semantic correctness; correctness audits and independent evaluation are therefore relevant cross-checks rather than interchangeable labels.
- Pull-request acceptance can reflect maintainer policy, project fit, timing, scope, or social factors in addition to technical quality.
- Revision and rework can indicate correction, requested improvement, refactoring, or maintenance and cannot be interpreted without temporal and causal context.
- The human/semantic branch is under-retrieved in this focused arXiv sample. The result supports a methodological distinction, not a prevalence or maturity claim.
- arXiv/OpenAlex discovery does not establish complete venue coverage, publication status, or systematic-search recall. Later screening must verify versions, venues, duplicates, and full-text operational definitions.

## Answers To P12 Special Questions

1. **Does P11's patch-correctness branch remain coherent?** Yes, provisionally, when restricted to a software-change object and separated from generic test, formal-verification, and classifier-evaluation terms.
2. **Should automated test success be its own primary F7 subfamily?** Not on P12 evidence. It is a cross-cutting authority/outcome dimension that requires explicit extraction in change-correctness and benchmark studies.
3. **Is review/acceptance distinct from completion?** Yes. Review findings, maintainer decisions, merge readiness, and generic completion have different objects and authorities.
4. **Is rework distinct from revision?** They overlap but should not be synonyms. Revision is an observable additional-change event; rework may additionally encode cost, code volume, maintenance, or corrective purpose.
5. **Is issue reopening validated as a primary proxy?** No. It remains a possible repository proxy requiring separate validation and should not define F7-C.
6. **Is coding-agent benchmark success a distinct branch?** Yes. It has high retrieval yield and a recognizable outcome vocabulary, but it is conditional on benchmark protocol.
7. **Does `resolved issue` mean semantic correctness?** Not necessarily. It means resolution under the named benchmark evaluator; semantic correctness requires the study's separate audit or authority.
8. **Should traditional-SE and coding-agent streams remain separate?** Yes. Their objects, executors, environments, and evaluation authorities differ, even where terminology overlaps.
9. **Is human/semantic evaluation retrievable?** Yes, but sparsely in this focused arXiv pilot. The exact revision retrieved `SEAlign` with human application/task and user-experience evaluation.
10. **Does sparse human retrieval justify dropping the branch?** No. It justifies treating it as supplementary and testing broader databases, citation chasing, and adjacent terms before making it primary.
11. **What terminology should be excluded as an umbrella?** Unqualified `verification`, `validation`, `completion`, `acceptance`, `quality`, and `retry`; each requires an object, authority, or outcome qualifier.
12. **Is F7 calibrated for systematic-search design?** Yes, with the five provisional subfamilies and explicit authority/outcome extraction. F7-E remains a supplementary branch subject to coverage validation.

## P12 Calibration Assessment

### Conceptual coherence

- **F7-A:** High enough for systematic design after separating change correctness, automated validation, formal checks, and generic quality.
- **F7-B:** Moderate to high for review and acceptance when maintainer/repository outcomes are kept separate from semantic correctness and completion.
- **F7-C:** Moderate with explicit temporal and causal sub-branches for revision, rework, corrective maintenance, and issue reopening.
- **F7-D:** High as a benchmark-qualified coding-agent outcome family, not as a universal task-success construct.
- **F7-E:** Conceptually distinct and methodologically important, but empirically sparse in this focused pilot.

### Retrieval coherence

- P12-A and P12-B produced the clearest neighborhoods when the object and authority were named.
- P12-C retrieved a small but useful revision neighborhood; broad rework terminology remains heterogeneous.
- P12-D was productive but benchmark-dominated and requires strong screening for evaluator dependence.
- P12-E confirmed a human-evaluation record but did not demonstrate a large or stable arXiv neighborhood.

### Relationship to previous families

- **F1/F2/F3:** Define work units, requirements, acceptance criteria, task descriptions, and decomposition. F7 evaluates outcomes or process events and must not duplicate those representation searches.
- **F5/F6:** Define coding-agent populations and execution conditions. F7-D/E adds outcome and evaluation-authority terms; trajectory/process records are not automatically final correctness.
- **Traditional-SE boundary:** F7-A/B/C can use traditional software-engineering evidence, while F7-D/E requires explicit coding-agent qualifiers when making agent-specific claims.

## P12 Recommended Search Status

| Branch | Status | Methodological reason |
|---|---|---|
| F7-A Change correctness and validation | `Calibrated for systematic-search design` | Object-qualified patch correctness and validation terms form a usable neighborhood, with authority extraction required. |
| F7-B Review and acceptance | `Calibrated for systematic-search design` | Review and maintainer/repository acceptance are retrievable and distinct from completion. |
| F7-C Rework and revision | `Calibrated with explicit sub-branches` | Revision is searchable, but rework measures and triggers remain heterogeneous. |
| F7-D Coding-agent benchmark success | `Calibrated for systematic-search design` | Benchmark outcome vocabulary is high-yield but evaluator- and environment-dependent. |
| F7-E Human and semantic evaluation | `Supplementary; coverage validation required` | Conceptually distinct but sparse in focused arXiv retrieval; broader database testing is required. |

## P12 Remaining Uncertainty

- The pilot still used discovery APIs rather than the protocol's full systematic databases; coverage, recall, and publication completeness remain untested.
- Human/semantic evaluation may expand substantially in standards, HCI, practitioner, or venue-specific literature not visible in this arXiv sample.
- The boundaries among patch correctness, semantic correctness, user experience, maintainer acceptance, and production quality remain context-dependent.
- Rework and revision proxies remain sensitive to repository policy, observation window, contributor behavior, and review conventions.
- Benchmark outcomes remain sensitive to test sufficiency, patch applicability, environment setup, hidden tests, leakage, and denominator choice.
- No substantive conclusion was drawn about whether tests, review, human approval, acceptance criteria, or any other mechanism is necessary or sufficient for successful work.

## P12 Exit Decision

**F7 subfamily structure sufficiently calibrated for systematic-search design**

P12 established a defensible provisional split by object, outcome, evaluation authority, and traditional-SE/coding-agent boundary: change correctness and validation; review and acceptance; rework and revision; coding-agent benchmark success; and human/semantic evaluation. The fifth branch remains supplementary because retrieval was sparse, not because the construct was treated as irrelevant. Systematic design may now specify separate strings and screening rules for these subfamilies, while preserving explicit extraction of authority, unit of analysis, temporal relation, benchmark dependence, publication status, and semantic-versus-social outcome distinctions.

No Work Item characteristics, acceptance criteria, lifecycle, hypotheses, or research conclusions were derived. No systematic search has begun. No commit was made.
