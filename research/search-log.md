# Search Log

This document is the durable record of pilot searches and, later, systematic searches conducted under [`research/protocol.md`](./protocol.md). Pilot searches validate and refine terminology, query families, database coverage, precision, recall, and feasibility; they do not establish research findings or Work Item characteristics.

Pilot Round 1 was conducted on 2026-08-20 using arXiv search/API endpoints and OpenAlex discovery. Pilot Round 2 calibration was conducted on 2026-08-20 using arXiv, OpenAlex, and Crossref APIs. Pilot Round 3 database-field calibration was conducted on 2026-08-20 using arXiv, OpenAlex, and Crossref APIs. Pilot Round 4 terminology calibration for Families 2 and 3 was conducted on 2026-08-20 using arXiv, OpenAlex, and DOI/publisher metadata. Pilot Round 5 focused calibration for Family 3 was conducted on 2026-08-20 using subgroup-specific arXiv and OpenAlex searches plus Crossref metadata verification. No systematic literature review search has begun.

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
| agent-computer interface (ACI) | agent execution environment | P1-F5-04 | SWE-agent system paper | add as contextual term | Specific interface terminology associated with repository navigation, editing, and execution. |
| SWE-bench | coding-agent evaluation | P1-F5-04 | GitHub issue resolution benchmark | retain as contextual term | Benchmark name, not a general synonym for coding agents. |
| agent trajectory / tool-mediated trajectory | agent execution trace | P1-F5-03, P1-F5-04 | Agent evaluation and analysis | add as contextual term | Used to describe multi-step agent/environment interaction. |
| agentic coding | coding-agent vocabulary | P2-F5-01, P3-F5-01 | Recent coding-agent research | investigate separately | Appeared as a related term in AIDev and the Round 3 arXiv sample; not yet tested as a standalone search phrase. |
| agentic software engineering | coding-agent vocabulary | P2-F5-01, P3-F5-01 | Recent coding-agent research | investigate separately | Appeared as a related term in AIDev and the Round 3 arXiv sample; may overlap with software-engineering-agent terminology. |
| Agentic-PRs | coding-agent activity/data | P2-F5-01, P3-F5-01 | GitHub repository studies | investigate separately | Term used for agent-authored pull requests; source and population boundaries need later screening. |
| software delegation contract | coding-agent work framing | P2-F5-01, P3-F5-01 | Coding-agent task/review study | retain as contextual term | A source-specific term for a study's unit of analysis; not a Work Item characteristic or final vocabulary. |
| agentless software engineering | coding-agent comparison vocabulary | P2-F5-03, P3-F5-03 | Agentless versus agent-based systems | retain as contextual term | Useful for separating autonomous-agent claims from non-agent workflow baselines. |
| SWE-Gym | coding-agent training/evaluation | P2-F5-03, P3-F5-03 | Agent training/evaluation | retain as contextual term | Benchmark/framework name, not a general synonym for coding agents. |
| task decomposition approaches | software work decomposition | P4-F3-01, P4-F3-03, P4-F3-06, P5-F3-01 | Crowdsourcing software development | test provisionally with software context | Title-qualified search retrieved the direct Khanfor seed; retain separately from generic AI task decomposition. |
| crowdsourcing software development | software work decomposition and allocation | P4-F3-01, P4-F3-03, P4-F3-05, P5-F3-10, P5-F3-14 | Crowdsourcing/project decomposition | retain as a domain-qualified subfamily | Produced a relatively coherent but heterogeneous corpus covering decomposition, parallel tasks, allocation, scheduling, lifecycle, and marketplace studies. |
| task preparation | task description/decomposition | P4-F3-01, P5-F3-02, P5-F3-15 | Crowdsourcing software development | downgrade to source-specific wording | Exact phrase retrieved non-software task automation/neuroscience; Khanfor used `preparing tasks`, not the exact phrase. |
| manageable software tasks | task scope/decomposition | P4-F3-01 | Crowdsourcing software development | test provisionally | Context-bound phrase; do not generalize it beyond the inspected crowdsourcing literature. |
| preparing tasks | task description/decomposition | P5-F3-01 | Crowdsourcing software development | investigate separately | Natural wording in the Khanfor abstract; not tested as an independent broad search phrase. |
| software project decomposition | software work decomposition | P5-F3-01 | Crowdsourcing software development | test provisionally with domain qualifier | Phrase observed in the title/abstract context of the direct decomposition seed; keep separate from generic task decomposition. |
| coding plans | software development planning | P5-F3-03 | Coding-agent-specific software development | investigate separately | Retrieved in agent workflow literature; distinct from traditional decomposition and from project planning. |
| issue descriptions and comments | task description/work representation | P5-F3-04 | Issue-tracking research | test provisionally with software context | More specific and higher-yield than generic `task description` in the inspected sample. |
| textual descriptions of issues | task description/work representation | P5-F3-04 | Issue-tracking research | retain as contextual term | Representation phrase from a software-task study; not a decomposition synonym. |
| task decomposition and collaboration | software development planning | P4-F3-03 | Coding-agent-specific software development | investigate separately | Agent-architecture phrase; keep distinct from human/team task decomposition. |
| requirement-driven task decomposition | software development planning | P4-F3-03 | End-to-end software-development agents | investigate separately | Recent agent-specific wording; publication status and transferability require later screening. |
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
