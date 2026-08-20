# Research Protocol v1

This protocol defines the theoretical research phase described in [`research-plan.md`](../research-plan.md). It is intended to make evidence collection and synthesis systematic, reproducible, transparent, and resistant to confirmation bias; no evidence has been collected under this protocol yet.

## Research Objective

The objective is to discover what characteristics a unit of software work may need to be optimized for coding agents, the conditions under which those characteristics are useful, and the contexts in which a unit of work is insufficient without additional specification or artifacts.

The provisional Work Item definition is a starting point, not a conclusion. This phase must allow evidence to support, qualify, contradict, or reject candidate characteristics rather than assuming them in advance.

The methodological principle is:

> The research is not designed to prove that Work Items work. It is designed to discover what characteristics a unit of software work needs to be optimized for coding agents, under what conditions those characteristics are useful, and where they stop being sufficient.

## Methodological Orientation

This protocol applies Evidence-Based Software Engineering principles by making the question, search, appraisal, extraction, synthesis, and limitations explicit. Systematic literature review and systematic mapping practices provide the structure for identifying and describing the academic evidence; the mapping function is especially useful while the relevant concepts and evidence types are still being established.

PRISMA principles will guide transparent reporting of identification, screening, eligibility, and inclusion where applicable. They are used as reporting and traceability guidance, not as a claim that every PRISMA requirement fits every stream, especially standards and practitioner evidence.

The theoretical phase uses a mixed-method orientation consistent with quantitative, qualitative, and mixed research distinctions described by Hernández Sampieri and related methodological practice. Descriptive counts and coverage summaries characterize the evidence base, while qualitative thematic analysis explains meanings, mechanisms, contradictions, and context. This project does not assume that a statistical meta-analysis is appropriate; heterogeneity, indirect transfer, and different evidence types will be assessed before any aggregation is considered.

## Research Questions

The primary and secondary research questions are maintained in [`research-questions.md`](./research-questions.md), which mirrors the current questions in the research plan. This protocol does not add research questions.

The questions may be refined during the theoretical review only when the need is documented, the effect on the protocol is assessed, and the change is recorded before applying it to new evidence. Existing collected evidence must not be silently reinterpreted as if it had been gathered under a different question.

## Scope

### In Scope

- Evidence relevant to defining, delimiting, describing, executing, and evaluating units of software work for coding agents.
- Requirements Engineering and Agile Requirements Engineering.
- User Stories, acceptance criteria, specifications, tasks, and task or work decomposition.
- Software verification, validation, completion, rework, and review quality.
- Cognitive load, information overload, context management, and information sufficiency.
- Software engineering productivity, developer experience, and Human-AI collaboration.
- Coding agents, agent planning, repository understanding, context management, clarification, autonomy, and task execution.
- Existing software work-unit models, studied for the need they address and their limitations rather than to establish a preferred framework.

These domains are avenues for finding relevant evidence, not a claim that they contribute equally or that every source must address coding agents directly.

### Out Of Scope

- Product implementation of Work Items or a new work-structuring framework.
- Treating Nerv, OpenSpec, SDD, or another framework as the default theoretical construct or baseline.
- General AI-agent research with no meaningful connection to software work definition or execution.
- The public-alpha empirical study, its data collection, and final hypothesis testing; those are later phases.
- A final Work Item definition or a predetermined list of required characteristics.

## Evidence Streams

Evidence streams are kept distinct during extraction and synthesis. Agreement across streams may increase confidence, but evidence is not pooled as if all streams had the same epistemic status.

### Scientific Evidence

This stream includes peer-reviewed empirical studies, systematic reviews, systematic mapping studies, conference papers, and relevant academic research. Relevant preprints and non-peer-reviewed academic research, including work published through arXiv or comparable repositories, may also be included when their methods, data, and limitations are sufficiently assessable. They must be explicitly labeled as non-peer-reviewed and must not be presented as equivalent to peer-reviewed scientific evidence.

Preprints are useful for rapidly evolving coding-agent research, but a peer-reviewed or later published version should be preferred when one exists. Publication venue or peer-review status is recorded as evidence context, not treated by itself as proof of evidence quality.

### Standards And Authoritative Sources

This stream includes relevant ISO, IEC, IEEE, SWEBOK, ACM, and equivalent standards or authoritative technical sources. It is used to identify recognized requirements, quality attributes, practices, and evaluation concerns. It is not treated as empirical proof that a Work Item characteristic improves coding-agent outcomes.

### Practitioner Evidence

This stream includes GitHub Issues and Discussions, Reddit, Hacker News, developer communities, tool discussions, and documented practitioner experiences. It is used as qualitative complementary evidence for recurring practices, friction, needs, and edge cases. It is not treated as equivalent to peer-reviewed empirical evidence.

### Coding-Agent-Specific Evidence

This stream includes recent empirical work, benchmarks, experiments, evaluations, and studies specifically involving coding agents or autonomous software-engineering agents. It receives separate identification because agent behavior, model capabilities, interfaces, and evaluation conditions may differ from human software development.

Evidence from traditional software engineering may inform concepts, mechanisms, and questions for coding agents, but transfer is not assumed. Transfer requires explicit analysis of the executor, task environment, context available, outcome measure, and relevant limitations.

## Search Sources

The initial academic sources are IEEE Xplore, ACM Digital Library, Scopus, Web of Science, ScienceDirect, and SpringerLink. Their coverage, indexing behavior, access constraints, and search dates will be recorded when searches begin.

Google Scholar is primarily a discovery, citation-tracing, and snowballing tool. It must not be the sole systematic database for claims about the literature.

Standards repositories, official organizational publications, and technical documentation may be searched separately for the authoritative-source stream. Practitioner sources will be sampled through the communities listed in the research plan and recorded with their source context.

## Search Strategy

### Concept Groups

Search strings will be built from concept groups rather than one premature giant query. Initial groups are:

- Software work units: task, work unit, work item, issue, ticket, user story, change request, job to be done.
- Requirements and specifications: requirements engineering, requirement, specification, acceptance criteria, task description, documentation.
- Work definition and execution: task decomposition, work decomposition, planning, software development task, task execution.
- Information and ambiguity: ambiguity, clarity, completeness, information sufficiency, missing context, information overload, cognitive load, documentation overhead.
- Coding agents: coding agent, software engineering agent, autonomous software engineering, AI programming assistant, code agent.
- Context and planning: context management, repository understanding, long context, agent planning, clarification seeking, autonomy.
- Verification and completion: software verification, validation, completion, acceptance, rework, review findings, task success.

These are search concepts only. They are not candidate Work Item characteristics.

### Query Construction

- Combine concept groups with Boolean `AND` where a source must connect the concepts, and combine synonyms within a group with `OR`.
- Expand terminology from seed sources, database thesauri, known indexing terms, and pilot-search results.
- Keep separate query families when a single query would obscure important literature, especially for traditional software engineering and coding-agent-specific research.
- Adapt field names, phrase syntax, wildcards, controlled vocabulary, and result limits to each database while preserving the conceptual intent.
- Record each final query, database, date, fields searched, filters, and result count.

Exact final search strings remain `TBD — to be established through research` until pilot searches establish useful terminology and manageable retrieval. Pilot changes must be recorded rather than applied silently.

### Snowballing

For included and high-relevance seed sources, perform backward snowballing through cited references and forward snowballing through citing works when the indexing source supports it. Record the seed source, direction, date, and reason for screening each candidate. Snowballing supplements database searches; it does not replace them.

### Evolving Terminology

Coding-agent terminology changes rapidly. Search logs must record aliases, older terms, product-neutral terms, and newly discovered terminology. A later terminology update may add a search iteration, but it must identify the date, rationale, affected stream, and whether earlier searches need to be rerun.

## Time Coverage

Traditional software-engineering evidence should use broad historical coverage when older work is necessary to understand requirements, work decomposition, information, productivity, verification, or completion. The starting period must be justified by the concept being searched rather than selected as an arbitrary cutoff.

Coding-agent-specific evidence should prioritize recent work because models, tools, interfaces, and capabilities change quickly. Older relevant work may still be included when it establishes terminology, methods, benchmarks, or a directly applicable finding. Every date restriction must record its rationale and the technological context it is intended to represent.

The final coverage periods and any stream-specific cutoffs are `TBD — to be established through research` after pilot searches.

## Inclusion Criteria

A source may enter screening and final inclusion only when the applicable criteria are recorded:

- It addresses at least one research question or a clearly documented subtopic in scope.
- It contributes empirical evidence, a systematic synthesis, a relevant theoretical analysis, a standard, or an authoritative description of practice.
- It has meaningful relevance to software work definition, software work execution, software verification/completion, or coding-agent execution where applicable.
- Its methods, reasoning, source context, or evidentiary basis are sufficiently accessible for assessment.
- Its population, dataset, task setting, or organizational context is identifiable enough to judge relevance and transferability.
- For preprints and other non-peer-reviewed academic research, its publication status is identifiable and its methods, data, and limitations are assessable enough to support cautious use.
- For practitioner evidence, the source has identifiable context and contains an experience, observation, or discussion relevant to the questions; popularity alone is not sufficient.

Relevance is assessed relative to the evidence stream. Direct coding-agent evidence is not required for a traditional software-engineering source, but claims about coding agents must identify when they depend on indirect transfer.

## Exclusion Criteria

Exclude a candidate from the final evidence set when it:

- Concerns an unrelated AI-agent domain without meaningful relevance to software work or coding-agent execution.
- Is pure marketing or promotional content presented as scientific evidence without an independently assessable basis.
- Duplicates another publication or report; retain the most complete version and record the relationship.
- Lacks enough methodological or source information to assess what was done and what supports the claim.
- Is an opinion piece, editorial, or anecdote being used as scientific evidence without being classified in the appropriate practitioner or commentary stream.
- Does not address software work definition, execution, context, verification, completion, or a clearly relevant mechanism.

Contradictory findings are never excluded because they conflict with an emerging interpretation. They may be excluded only for a documented scope, relevance, or source-quality reason that would also apply to supporting evidence.

## Screening Process

Screening will follow a documented sequence:

1. Collect records and assign a provisional Source ID.
2. Deduplicate records and link duplicate publications, preprints, technical reports, and later versions.
3. Screen titles and available metadata for obvious scope mismatch.
4. Screen abstracts, summaries, or source descriptions against the inclusion and exclusion criteria.
5. Retrieve and screen the full text or complete source where available.
6. Record the final inclusion decision, evidence stream, research-question relevance, and exclusion reason.

Exclusion reasons must use a small documented vocabulary such as `out of scope`, `duplicate`, `insufficient method`, `insufficient source information`, `not evidence for the claimed use`, or `other documented reason`. A source that is useful context but not eligible evidence may be recorded as contextual material without being used to support a conclusion.

The screening log, search details, and decisions will be stored in Git in the smallest practical research artifact. A PRISMA-style flow summary may be used to report identification, screening, eligibility, and inclusion counts; it is a reporting aid, not a claim that every PRISMA review requirement applies unchanged.

This project may be conducted by a single researcher and therefore may not have two independent human screeners or extractors. That limitation must be reported; the protocol does not claim independent dual screening or inter-rater reliability when those activities are not performed. Mitigations are a second-pass review of exclusions, periodic audits of a sample of inclusion and exclusion decisions, explicit recording of uncertainty, and human resolution of ambiguous or consequential decisions. If a coding agent assists with screening, extraction, or classification, record that assistance and preserve the source passages, metadata, and reasoning used to support its recommendation; the human researcher remains responsible for the decision.

## Quality Assessment

Quality assessment is multidimensional and descriptive. It must not collapse unlike evidence streams into an unexplained single score.

Assess, where applicable:

- Source type and publication status.
- For academic sources, whether the work is peer-reviewed, a preprint, a technical report, or another non-peer-reviewed publication, and whether a later peer-reviewed or published version exists.
- Transparency of the methods, data, analysis, and reasoning.
- Suitability of the study design for the claim.
- Relevance of the sample, population, dataset, task, or setting.
- Reproducibility of the procedure, materials, data, or analysis.
- Identified threats to internal, construct, external, and conclusion validity.
- Directness to the research question and to coding-agent execution.
- Recency when model capabilities, tools, or practices are technologically material.
- For practitioner evidence, provenance, context detail, independence, and evidence of recurrence.

Each source receives a short narrative assessment and a confidence/evidence-strength judgment supported by these dimensions. A weakness in one dimension must be preserved rather than hidden by an arithmetic average. Quality describes how much weight a source can carry for a particular claim; it does not decide the claim by itself. Peer-review status informs the assessment but does not substitute for assessing methods, relevance, directness, and validity.

## Data Extraction

Each included source receives a stable Source ID and an extraction record. The minimum record contains:

- Source ID.
- Citation, year, source type, and URL/DOI where available.
- Publication status, including peer-reviewed, preprint, technical report, or other non-peer-reviewed status, and a linked later version where applicable.
- Evidence stream and research-question relevance.
- Research context, population or dataset, and task setting.
- Study design or source method.
- Main findings and relevant observations about software work.
- Limitations and threats to validity.
- Supporting implications and contradictory implications, kept in separate fields.
- Applicability to coding agents, including directness and transfer assumptions.
- Confidence/evidence strength and notes.

Bibliographic registration remains aligned with [`evidence/sources.md`](../evidence/sources.md). Claim-level supporting and contradictory material is synthesized in [`evidence/evidence-matrix.md`](../evidence/evidence-matrix.md), while material that directly challenges an emerging interpretation is also recorded in [`evidence/contradictory-evidence.md`](../evidence/contradictory-evidence.md). No source is represented as supporting or contradicting a claim without preserving the relevant context and limitations.

## Contradictory Evidence Policy

The search, screening, extraction, and synthesis steps must actively look for evidence that weakens, qualifies, or contradicts emerging interpretations. Search terms, snowballing, and source selection must not stop when a plausible supporting pattern appears.

Contradictory evidence must:

- Be retained when it meets the same eligibility rules as supporting evidence.
- Be extracted separately from supporting implications.
- Be recorded in `evidence/contradictory-evidence.md` when it challenges an emerging Work Item interpretation.
- Be compared by context, population, task complexity, executor, intervention, outcome, and study quality before judging whether findings truly conflict.
- Remain visible in synthesis summaries, even when the final interpretation favors one explanation.

The absence of supporting evidence is not automatically contradictory evidence, and a difference in context is not automatically a contradiction. Both cases must be labeled accurately.

## Practitioner Evidence Methodology

Practitioner evidence is a qualitative complementary stream intended to identify lived friction, recurring patterns, needs, and edge cases. It does not establish prevalence or causal effect by itself.

### Source Selection And Sampling

Sample GitHub Issues and Discussions, Reddit, Hacker News, developer communities, tool discussions, and documented practitioner experiences when they have identifiable context and relevance to the research questions. Use purposive sampling for relevance and variation across tools, task types, and reported outcomes; use snowballing only when the source trail is documented. The sampling frame, search terms, dates, inclusion decisions, and source availability must be recorded.

### Analysis

Extract the situation, task, executor, context supplied, observed outcome, reported friction, and author interpretation where available. Apply thematic coding using categories that emerge from the data. Initial labels from the research plan may guide discovery, but they must not be treated as final categories or conclusions.

Distinguish a single anecdote, multiple independent reports, repeated discussion of the same unverified claim, and a pattern supported by varied sources. Popularity metrics such as upvotes, reactions, comments, or reposts describe visibility or engagement, not validity, prevalence, or causal strength.

Record selection, self-reporting, platform, moderation, survivorship, and confirmation biases. Practitioner evidence may suggest mechanisms or candidate characteristics for comparison with other streams, but cannot by itself establish that a characteristic improves coding-agent outcomes.

### Ethical Handling

Use only publicly accessible practitioner material unless separate consent or authorization exists. Store no unnecessary personal information; focus analysis on the reported experience rather than the author's identity, and prefer paraphrasing when a direct quotation or identity adds no analytical value. Source IDs and URLs may be retained when needed for research traceability, subject to source availability and platform terms. Do not infer sensitive personal characteristics from posts. Respect platform terms, reasonable research ethics, and the practical possibility that a source may later become unavailable.

## Synthesis Method

The theoretical phase uses a staged, mixed-method synthesis. Quantitative summaries such as source counts, coverage, and study characteristics describe the evidence base; they do not substitute for assessing the quality, context, or meaning of findings. Qualitative thematic synthesis compares concepts, mechanisms, outcomes, limitations, and contexts across sources.

Synthesis proceeds as follows:

1. Build a structured evidence map by research question, domain, evidence stream, context, and study type.
2. Code recurring concepts and reported relationships without converting them into Work Item requirements.
3. Compare supporting, contradictory, and null or inconclusive findings.
4. Examine contextual moderators such as task complexity, size, risk, scope, executor, autonomy, available context, and verification setting.
5. Compare direct coding-agent evidence with traditional software-engineering evidence, explicitly recording transfer assumptions and gaps.
6. Identify candidate characteristics, trade-offs, and applicability boundaries only when they emerge from the combined evidence.
7. Record the interpretation, evidence strength, remaining uncertainty, and plausible alternative explanations in the evidence artifacts.

The synthesis must distinguish observations supported by sources from interpretations, open questions, and later hypotheses. It must not treat the intuitive appeal of a property as evidence.

## Evidence Classification

The following categories are mutually distinct labels for the current state of support for a specific claim in a defined context. They are not a ranking that combines different categories, and no slash-combined label may be used.

- **Established**: Normally requires multiple independent and methodologically credible sources, meaningful convergence across the evidence, sufficient directness to the claim, and reasonably understood applicability boundaries, with no unresolved high-quality contradiction that materially changes the claim. Source count alone is never sufficient. For a young or rapidly evolving area such as coding agents, use `Strongly supported` when the evidence is compelling but not mature enough for this category.
- **Strongly supported**: The available evidence supports the claim consistently and directly, but the evidence base is narrower, less independent, or less mature than required for `Established`.
- **Moderately supported**: Evidence supports the claim, but important limitations, indirectness, heterogeneity, or contextual dependence remain.
- **Preliminary**: The claim has some relevant support, but the evidence is sparse, early, indirect, or insufficiently replicated.
- **Mixed evidence**: Relevant evidence includes meaningful support and meaningful contradiction or materially different results that have not been resolved by context or quality differences.
- **Unsupported**: The reviewed evidence does not provide adequate support for the claim, without providing evidence strong enough to affirmatively contradict it.
- **Contradicted**: Relevant evidence consistently challenges the claim, or credible contradictory evidence outweighs the available support within the defined context.
- **Unknown**: The claim has not been adequately investigated, or the available sources cannot support a reliable interpretation.

Each label must be accompanied by its context, evidence stream(s), main limitations, and reasons for the classification. The classification is claim-specific and may differ across task types, populations, or coding-agent settings.

## Bias And Validity Controls

The protocol applies the following controls:

- **Confirmation bias:** Predefine questions, search concepts, eligibility rules, extraction fields, contradictory-evidence handling, and classification vocabulary. Search for disconfirming evidence and preserve alternative interpretations.
- **Publication bias:** Include systematic reviews, negative or null findings, replication attempts, technical reports where methodologically assessable, and relevant authoritative or practitioner evidence with its source type clearly labeled. Treat the absence of publication as unknown, not as support.
- **Selection bias:** Record database coverage, query changes, snowballing, access limitations, and exclusion reasons. Use more than one academic source and do not rely on popularity or convenience alone.
- **Recency bias:** Use broad historical coverage for stable software-engineering questions and justify recent-focused coverage for rapidly changing coding-agent evidence. Do not treat newer as inherently better.
- **Survivorship bias in practitioner communities:** Seek failed, abandoned, negative, and ordinary experiences as well as successful reports; record which populations and platforms are missing.
- **Transferability from human teams to coding agents:** Keep executor and context explicit, classify indirect evidence separately, and require an argument rather than an assumption for transfer.
- **Changing model capabilities:** Record agent, model, interface, tool access, date, benchmark/task conditions, and relevant version information when available. Avoid generalizing a time-specific result beyond its observed setting.
- **Researcher interpretation bias:** Maintain extraction notes separate from synthesis interpretations, preserve revisions in Git, and record reasons for changes.

These controls reduce but cannot eliminate bias. Residual uncertainty and threats to validity remain part of every synthesis.

## Reproducibility And Traceability

Research decisions must be recorded in Git in small, reviewable changes. At minimum, record search dates, databases, exact queries, filters, result counts, terminology changes, snowballing paths, screening decisions, exclusion reasons, extraction changes, quality assessments, and synthesis revisions.

Every synthesis claim must be traceable to Source IDs and the relevant extracted observations. Evidence artifacts should distinguish source registration, claim-level synthesis, contradictory evidence, and derived interpretation. Do not add duplicate bureaucratic artifacts when an existing repository file can record the decision clearly.

If access to a source is incomplete, record the limitation and do not represent an unverified abstract, summary, or citation as full-text evidence.

## Protocol Evolution

This is Protocol v1 and may be revised when a genuine methodological gap, reproducibility problem, terminology change, database limitation, or scope clarification is discovered. Changes must be made in a separate Git change with a dated rationale, affected sections, expected effect on coverage or comparability, and whether previously screened or extracted sources must be revisited.

After evidence collection begins, changes require explicit justification and must preserve the original protocol for comparison. A correction that restores the stated intent of the protocol must be distinguished from a change made because observed results are inconvenient or because it improves the apparent support for an interpretation. If both occur, record them separately.

## Exit Criteria For The Theoretical Phase

The theoretical phase may proceed to the next research artifacts only when:

- The search scope, sources, terminology, coverage, screening, and extraction decisions are documented well enough to reproduce the review process.
- Relevant evidence streams have been searched or their gaps and access limitations are explicitly recorded.
- Supporting, contradictory, null, and inconclusive evidence has been considered symmetrically.
- The evidence matrix contains traceable source-level observations organized by research question and context.
- Candidate characteristics, trade-offs, and applicability boundaries are clearly distinguished from established findings, interpretations, and unknowns.
- Transfer from traditional software engineering to coding agents has been assessed rather than assumed.
- Remaining disagreements, gaps, and limitations are documented.

Only after these conditions are met should the project construct the derived Work Item theoretical model. Operationalization should follow the model and its contextual boundaries; falsifiable hypotheses should follow operationalization; and the public-alpha study design should be finalized before empirical data collection begins. This protocol does not define the model, characteristics, hypotheses, or alpha instruments.
