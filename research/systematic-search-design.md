# Systematic Search Design

## 1. Pilot-Phase Closure

Pilot Rounds P1-P12 completed calibration of terminology, field behavior, major noise, known-item candidates, and branch boundaries. Families F1-F7 are ready for systematic-search design, although several families require multiple subfamilies. The pilot used discovery-oriented sources, principally arXiv, OpenAlex, and Crossref; systematic coverage of the protocol databases has not been executed or validated. No Work Item characteristics, research findings, or conclusions were derived during the pilot.

The durable execution record is [`systematic-search-log.md`](./systematic-search-log.md). The historical pilot record remains [`search-log.md`](./search-log.md). This document specifies retrieval only. It does not perform research-record deduplication, screening, quality assessment, extraction, synthesis, or hypothesis formation.

## 2. Research-Question Map

The current questions are identified as follows. The wording and authority remain in [`research/research-questions.md`](./research-questions.md).

| ID | Current question |
|---|---|
| Q0 | ¿Qué características debe tener una unidad de trabajo de software para estar optimizada para coding agents? |
| Q1 | ¿Qué información necesita un coding agent para ejecutar correctamente una unidad de trabajo? |
| Q2 | ¿Qué efectos producen la ambigüedad, la información insuficiente y el exceso de información? |
| Q3 | ¿Qué papel cumplen el objetivo, el alcance, los criterios de aceptación, las restricciones y las tareas? |
| Q4 | ¿Cuánto detalle es útil antes de empezar a generar overhead o reducir flexibilidad? |
| Q5 | ¿Qué debería definir la unidad de trabajo y qué debería quedar bajo decisión del coding agent? |
| Q6 | ¿Cómo cambian estas necesidades según complejidad, tamaño, riesgo o alcance del trabajo? |
| Q7 | ¿Qué diferencias existen entre las unidades de trabajo diseñadas para humanos y las diseñadas para coding agents? |
| Q8 | ¿En qué contextos un Work Item deja de ser suficiente y necesita complementarse con una Spec u otros artifacts? |

The mapping is intentionally many-to-many. A branch may inform several questions, and a question may require direct and indirect evidence from several branches. A mapping does not imply that a retrieved source answers a question; eligibility and relevance remain screening decisions.

## 3. Calibrated Branch Inventory

The inventory below uses the latest structure in P6, P8, P10, and P12. Terminology is search terminology, not a list of Work Item characteristics.

| Branch ID | Branch name | Purpose | Status | Primary terminology | Supplementary/contextual terminology | Major noise or boundary |
|---|---|---|---|---|---|---|
| F1 | Software work units and work definition | Retrieve studies about software tasks and work-unit representations as objects of study. | Primary | `software task`; `software development task`; `work unit`; `work item`; `issue`; `ticket`; `user story`; `change request`; `issue description` | `task type`; `task completion performance`; `issue comments`; `task management` | Generic `task`, `issue`, `ticket`, project management, and governance without software-work focus. |
| F2A | Requirements and specifications | Retrieve requirements-engineering and specification artifacts. | Primary | `software requirements`; `requirements engineering`; `requirements specification`; `software requirements specification`; `functional requirements`; `non-functional requirements`; `natural-language requirements` | `requirements artifact`; `requirements validation`; `SRS` | Non-software requirements, security or domain specifications without software-work relevance, generic specification generation. |
| F2B | User stories and acceptance criteria | Retrieve user-story, acceptance-criteria, BDD, and requirement-coverage traditions. | Primary | `user story`; `user stories`; `user-story quality`; `acceptance criteria`; `acceptance testing criteria`; `Gherkin`; `Behavior-Driven Development`; `requirement coverage` | `story readability`; `user-story set`; `acceptance-criteria generation`; `INVEST` | General user acceptance, education, ethical stories, domain-specific stories, and cost-model acceptance. |
| F2C | Requirements quality and validation | Retrieve quality, assurance, assessment, and validation studies about requirements. | Primary | `requirements quality`; `requirements quality assurance`; `requirements validation`; `requirements quality assessment`; `requirements quality control`; `natural-language requirements quality` | `requirements metrics`; `requirements completeness`; `requirements traceability` | Generic software quality, package descriptions, and quality claims not attached to requirements. |
| F3A | Software-project decomposition and planning | Retrieve traditional software-work decomposition plus planning terminology, while labeling coding-agent planning separately during screening. | Primary | `task decomposition`; `work decomposition`; `task breakdown`; `software project decomposition`; `requirement-driven task decomposition`; `coding plans` | `software development task`; `task planning`; `preparing tasks`; `task decomposition and collaboration` | General AI/robotics decomposition, generic project planning, and agent architecture unless the software-work object is explicit. |
| F3B | Task descriptions and issue representations | Retrieve textual representations of software work in issue trackers and projects. | Primary | `issue description`; `issue descriptions`; `issue comments`; `issue success`; `software project`; `issue-tracking system` | `textual descriptions of issues`; `task description`; `software task description` | Generic descriptions, API documentation, prompt/code-task descriptions, and issue classification without work representation. |
| F3C | Allocation, interdependence, and crowdsourced software work | Target allocation/interdependence and crowdsourced software-work contexts for comparison and gap coverage. | Supplementary | `task allocation`; `work allocation`; `task interdependence`; `crowdsourcing software development`; `parallel tasks` | `task scheduling`; `task life cycle`; `project description length`; `distributed software development` | Robotics and computing allocation, marketplace/worker effects, scheduling, and external-worker conditions. |
| F4A | Information-quality properties | Retrieve ambiguity, completeness, coverage, traceability, and information-quality measurement in software artifacts. | Primary | `requirements ambiguity`; `ambiguity detection`; `requirements completeness`; `completeness metrics`; `requirements coverage`; `traceability completeness` | `ambiguity explanation`; `ambiguity measurement`; `requirements quality` | Generic linguistic ambiguity, legal/regulatory requirements, source-code ambiguity, and unqualified quality. |
| F4B | Developer information needs and context | Retrieve what human developers seek, need, use, and comprehend during software work. | Primary | `developer information needs`; `software developers' information needs`; `information seeking`; `information foraging`; `program comprehension`; `relevant information` | `software evolution`; `maintenance tasks`; `task context`; `information sources`; `missing context` | Generic information behavior, health/social-media studies, scientific-package papers, and unqualified `information sufficiency`. |
| F4C1 | Mental workload and cognitive burden | Retrieve professional-programmer workload and comprehension studies. | Primary | `mental workload`; `cognitive workload`; `programmers' cognitive load`; `program comprehension`; `subjective workload` | `NASA-TLX`; `EEG`; `fNIRS`; `BCI`; `mental effort` | Educational-only studies, generic neuroscience/HCI, runtime load, model context load, and coding-agent context load. |
| F4C2 | Information overload | Target adjacent overload, communication, and awareness literature for contextual comparison. | Supplementary | `information overload`; `communication breakdowns`; `awareness`; `developer coordination` | `information volume`; `communication systems`; `productivity paradox` | Broad information systems, networking, psychology, package, and general productivity noise. |
| F4D | Documentation information and burden | Retrieve software-documentation relevance, quality, usefulness, navigation, maintenance, effort, cost, and amount questions. | Primary | `software documentation`; `documentation relevance`; `documentation quality`; `documentation usefulness`; `documentation maintenance`; `task navigation` | `documentation effort`; `documentation cost`; `how much is enough`; `source-code comments`; `traceability` | Do not use `documentation overhead` as an umbrella; exclude package descriptions and unrelated maintenance/testing. |
| F5A | Coding-agent population | Retrieve recent literature using the broad coding-agent labels. | Primary | `coding agent`; `coding agents`; `AI coding agent`; `agentic coding`; `agentic software engineering` | `AI programming assistant`; `coding-agent workload`; `software delegation contract` | Autocomplete, generic AI agents, compiler/system papers, and conversational assistants without software-work execution. |
| F5B | Software-engineering-agent population | Retrieve the software-engineering-agent terminology lineage. | Primary | `software engineering agent`; `software-engineering agents`; `SWE agent`; `AI software engineer`; `autonomous software engineering` | `LLM-based software engineering agents`; `repository-level software engineering tasks` | Embodied agents, general agent infrastructure, and papers naming an agent without repository/software-work scope. |
| F5C | SWE-agent lineage and population boundaries | Retrieve the named SWE-agent/SWE-bench lineage without treating it as the whole population. | Primary | `SWE-agent`; `SWE agents`; `mini-SWE-agent`; `SWE-bench`; `agent-computer interface` | `SWE-bench Verified`; `SWE-bench Pro`; `issue resolution`; `repository navigation` | Named-system studies may concern training, infrastructure, or evaluation rather than the relevant phenomenon. |
| F6A1 | Context quantity, long-context behavior, and memory | Retrieve context-window, retention, compression, history, and memory mechanisms in coding agents. | Primary | `long-context`; `context compression`; `context budget`; `memory management`; `persistent memory`; `interaction history` | `context length limitations`; `persistent notes`; `long-horizon`; `multi-turn SWE agent` | Generic long-context NLP, user-state-only memory, and repository retrieval mechanisms. |
| F6A2 | Repository retrieval, selection, exploration, and navigation | Retrieve how coding agents locate and select repository/code information. | Primary | `repository exploration`; `structural code retrieval`; `repository navigation`; `repository-level understanding` | `knowledge map`; `multi-hop dependencies`; `structural queries`; `retrieval` | Generic code search, repository mining without agents, context quantity, and memory management. |
| F6B1 | Planning process and architecture | Retrieve explicit/implicit plans and planning interventions in coding-agent workflows. | Requires further calibration | `explicit planning`; `implicit planning`; `planning structure`; `plan-source intervention`; `agent planning` | `planner`; `multi-stage workflow`; `planning-aware trajectories`; `task plans` | Planner presence treated as effectiveness, generic project planning, and F3 human decomposition. |
| F6B2 | Functional decomposition, subtasks, and delegation | Retrieve agent-side subtask formation, dependency-aware plans, and delegation. | Requires further calibration | `functional decomposition`; `subtask-level`; `dependency-aware task plans`; `task delegation`; `centralized task delegation` | `isolated workspaces`; `subtask execution`; `multi-agent coordination`; `branch-and-merge` | Human/project decomposition, crowdsourcing, generic task decomposition, and planning without a subtask object. |
| F6C1 | Clarification-seeking and requirement elicitation | Retrieve agents asking questions or eliciting missing requirements under explicit interaction protocols. | Primary | `clarification-seeking`; `requirement elicitation`; `underspecified instructions`; `dialogue-driven coding agents`; `user simulator` | `uncertainty-aware clarification`; `implicit requirement recovery`; `Average Turns to Clarify`; `Key Question Coverage` | Generic clarification, non-interactive results, CAD, and ambiguity without coding-agent interaction. |
| F6C2 | Interaction, feedback, and specification alignment | Retrieve broader interaction, alignment, steerability, and refinement settings. | Supplementary | `dialogue quality`; `interaction quality`; `task alignment`; `specification refinement`; `underspecification` | `steerability`; `adaptability`; `deferment`; `bounded authority` | Generic human-AI interaction, safety agents, and clarification-only metrics. |
| F6D1 | Tool use, interfaces, and agent-environment interaction | Retrieve tools, interfaces, sandboxes, environment feedback, and execution loops. | Primary | `agent-computer interface`; `agent-environment interaction`; `tool-mediated`; `bounded tool interface`; `execution feedback` | `action space`; `environment interface`; `self-directed stopping`; `tool use` | Generic computer-use/healthcare interfaces and autonomy rhetoric. |
| F6D2 | Agent trajectories and process-level execution analysis | Retrieve recorded action/observation sequences and process evaluation. | Primary | `thought-action-result trajectory`; `process-level trajectory evaluation`; `trajectory assessment`; `execution record` | `feedback integration`; `interaction logs`; `action patterns`; `anti-pattern detection` | Hidden-reasoning claims, scalar autonomy claims, and outcome causality without process design. |
| F7A | Change correctness and validation | Retrieve patch/change correctness, test/oracle validation, regression, formal, and semantic checks. | Primary | `patch correctness`; `patch validation`; `plausible patch`; `patch overfitting`; `semantic correctness` | `independent test suite`; `behavioral discrepancy`; `regression test`; `gold correctness labels` | Unqualified verification/validation, requirements validation, classifier accuracy, and generic testing. |
| F7B | Review and acceptance | Retrieve review findings, pull-request acceptance, merge readiness, and maintainer decisions. | Primary | `code review acceptance`; `pull request acceptance`; `merge decision`; `accepted and merged`; `maintainer decision` | `merge-ready`; `review findings`; `review outcome`; `review iteration` | Generic completion, review automation without outcome, and semantic correctness. |
| F7C | Rework and revision | Retrieve additional work after an initial change, with trigger and timing preserved. | Primary, explicit sub-branches | `software rework`; `pull request revision`; `review iteration`; `post-initial-commit edit`; `review-induced change` | `corrective maintenance`; `revision cycle`; `issue reopening`; `failure recovery` | Rework cost, code volume, review edits, maintenance, and agent retry are not interchangeable. |
| F7D | Coding-agent benchmark success | Retrieve benchmark-qualified resolution and evaluation outcomes. | Primary | `resolved issue`; `resolve rate`; `pass@1`; `correct fix`; `benchmark evaluator` | `SWE-bench`; `test-passing patch`; `hidden tests`; `differential testing`; `execution-based evaluation` | Benchmark construction, contamination, harness engineering, and treating resolution as semantic or production correctness. |
| F7E | Human and semantic evaluation | Target human, expert, semantic, user, production, and trajectory evaluation authority. | Supplementary | `human evaluation`; `semantic correctness`; `human inspection`; `professional-developer annotation` | `user experience`; `production-assessed evaluation`; `trajectory review` | General human evaluation and preference studies; sparse coding-agent-specific retrieval. |

Standalone autonomy (`F6E`) is not an execution branch. P10 classified it as a boundary concept; operational terms such as interfaces, environment interaction, and trajectories are searched instead.

## 4. Research-Question Mapping

| Search family / subfamily | Research question(s) | Search purpose |
|---|---|---|
| F1 | Q0, Q3, Q6, Q7, Q8 | Identify software work-unit objects, boundaries, types, and human-oriented representations. |
| F2A | Q0, Q3, Q5, Q7, Q8 | Identify requirements/specification artifacts and their roles in defining software work. |
| F2B | Q0, Q3, Q4, Q5, Q7, Q8 | Identify user-story and acceptance-criteria representations and their scope/detail relations. |
| F2C | Q1, Q2, Q3, Q4, Q6, Q8 | Retrieve requirements-quality, validation, completeness, and assurance concepts without treating them as conclusions. |
| F3A | Q3, Q4, Q5, Q6, Q7, Q8 | Retrieve decomposition and planning traditions, including task boundaries and work structure. |
| F3B | Q1, Q2, Q3, Q5, Q7, Q8 | Retrieve issue/task-description representations and information carried by them. |
| F3C | Q4, Q6, Q7 | Provide targeted comparison with allocation, interdependence, and externally distributed software work. |
| F4A | Q1, Q2, Q3, Q4, Q6, Q8 | Retrieve ambiguity, completeness, coverage, traceability, and information-quality measures. |
| F4B | Q1, Q2, Q4, Q5, Q6, Q7 | Retrieve developer information needs, seeking, foraging, and comprehension. |
| F4C1 | Q2, Q4, Q6, Q7 | Retrieve human workload and comprehension research with explicit population boundaries. |
| F4C2 | Q2, Q4, Q6, Q7 | Target contextual overload and communication literature without promoting it to direct evidence. |
| F4D | Q1, Q2, Q4, Q5, Q7, Q8 | Retrieve documentation usefulness, navigation, maintenance, effort, cost, and information-volume work. |
| F5A-F5C | Q0, Q1, Q2, Q3, Q5, Q6, Q7, Q8 | Identify coding-agent populations and terminology; these branches do not by themselves answer outcome questions. |
| F6A1 | Q1, Q2, Q4, Q5, Q6, Q8 | Retrieve context quantity, retention, compression, and memory-management settings. |
| F6A2 | Q1, Q2, Q5, Q6, Q8 | Retrieve repository information selection, retrieval, and navigation. |
| F6B1 | Q3, Q4, Q5, Q6, Q8 | Retrieve explicit and implicit planning as agent process or architecture. |
| F6B2 | Q3, Q5, Q6, Q7, Q8 | Retrieve agent-side subtasks, delegation, and multi-agent coordination. |
| F6C1 | Q1, Q2, Q3, Q5, Q6, Q8 | Retrieve question asking, requirement elicitation, and interaction under underspecification. |
| F6C2 | Q2, Q3, Q5, Q7, Q8 | Provide supplementary coverage of alignment, feedback, steerability, and refinement. |
| F6D1 | Q1, Q5, Q6, Q7, Q8 | Retrieve tools, interfaces, environments, and feedback conditions. |
| F6D2 | Q1, Q2, Q5, Q6, Q7, Q8 | Retrieve observable execution trajectories and process-level evaluation. |
| F7A | Q0, Q1, Q3, Q5, Q6, Q8 | Retrieve change correctness and validation authorities. |
| F7B | Q3, Q5, Q6, Q7, Q8 | Retrieve review findings, maintainer acceptance, merge decisions, and readiness. |
| F7C | Q2, Q4, Q6, Q7, Q8 | Retrieve revision, review-induced change, corrective maintenance, and rework proxies. |
| F7D | Q0, Q1, Q2, Q3, Q5, Q6, Q7, Q8 | Retrieve coding-agent benchmark outcomes while preserving evaluator dependence. |
| F7E | Q0, Q1, Q2, Q5, Q6, Q7, Q8 | Target human and semantic authorities as a supplementary counterweight to automated scores. |

## 5. Concept Blocks and Canonical Queries

Canonical queries are conceptual expressions, not database strings. They preserve separate traditions rather than creating one giant Boolean query. A block is included only when it makes the branch conceptually precise; execution may use separate sensitivity and precision variants.

### F1-F4: Traditional Software-Engineering Branches

| Branch | Population/domain block | Phenomenon block | Outcome/context block | Canonical conceptual query |
|---|---|---|---|---|
| F1 | `software development` OR `software engineering` OR `programming` | `software task` OR `software development task` OR `work unit` OR `work item` OR `issue description` OR `ticket` OR `user story` OR `change request` | `work definition` OR `task type` OR `task management` OR `issue tracking` | (`software development` OR `software engineering`) AND (`software task` OR `software development task` OR `work unit` OR `work item` OR `issue description` OR `ticket` OR `user story` OR `change request`) |
| F2A | `software` OR `software engineering` | `software requirements` OR `requirements engineering` OR `requirements specification` OR `software requirements specification` OR `functional requirements` OR `non-functional requirements` | `requirements artifact` OR `requirements validation` OR `natural-language requirements` | (`software` OR `software engineering`) AND (`software requirements` OR `requirements engineering` OR `requirements specification` OR `software requirements specification` OR `functional requirements` OR `non-functional requirements`) |
| F2B | `software engineering` OR `agile software development` | `user story` OR `user-story quality` OR `acceptance criteria` OR `acceptance testing criteria` OR `Gherkin` OR `Behavior-Driven Development` | `requirement coverage` OR `story readability` OR `acceptance-criteria generation` | (`software engineering` OR `agile software development`) AND (`user story` OR `acceptance criteria` OR `Gherkin` OR `Behavior-Driven Development`) |
| F2C | `software requirements` OR `requirements engineering` | `requirements quality` OR `requirements quality assurance` OR `requirements quality assessment` OR `requirements quality control` OR `requirements validation` | `requirements metrics` OR `requirements completeness` OR `requirements traceability` | (`requirements engineering` OR `software requirements`) AND (`requirements quality` OR `requirements quality assurance` OR `requirements quality assessment` OR `requirements validation`) |
| F3A | `software development` OR `software project` OR `software engineering` | `task decomposition` OR `work decomposition` OR `task breakdown` OR `software project decomposition` OR `requirement-driven task decomposition` | `planning` OR `coding plans` OR `task collaboration` | (`software development` OR `software project`) AND (`task decomposition` OR `work decomposition` OR `task breakdown` OR `software project decomposition`) |
| F3B | `software project` OR `software development` OR `issue-tracking system` | `issue description` OR `issue comments` OR `textual descriptions of issues` OR `software task description` | `issue success` OR `issue management` | (`software project` OR `issue-tracking system`) AND (`issue description` OR `issue comments` OR `textual descriptions of issues`) |
| F3C | `software development` OR `global software development` OR `crowdsourcing software development` | `task allocation` OR `work allocation` OR `task interdependence` OR `parallel tasks` OR `crowdsourcing software development` | `task scheduling` OR `task life cycle` OR `project description length` | (`software development` OR `crowdsourcing software development`) AND (`task allocation` OR `task interdependence` OR `parallel tasks`) |
| F4A | `software requirements` OR `requirements engineering` OR `software development` | `requirements ambiguity` OR `ambiguity detection` OR `requirements completeness` OR `requirements coverage` OR `traceability completeness` | `ambiguity measurement` OR `requirements quality` OR `validation` | (`software requirements` OR `requirements engineering`) AND (`requirements ambiguity` OR `requirements completeness` OR `requirements coverage` OR `traceability completeness`) |
| F4B | `software developer` OR `software engineer` OR `software maintenance` | `developer information needs` OR `information seeking` OR `information foraging` OR `program comprehension` | `software evolution` OR `maintenance task` OR `relevant information` OR `task context` | (`software developer` OR `software engineer`) AND (`developer information needs` OR `information seeking` OR `information foraging` OR `program comprehension`) |
| F4C1 | `programmer` OR `software developer` OR `software engineer` | `mental workload` OR `cognitive workload` OR `programmers' cognitive load` OR `program comprehension` | `subjective workload` OR `NASA-TLX` OR `code review` OR `programming` | (`programmer` OR `software developer`) AND (`mental workload` OR `cognitive workload` OR `program comprehension`) |
| F4C2 | `software developer` OR `software team` OR `communication system` | `information overload` OR `communication breakdowns` OR `awareness` OR `developer coordination` | `information volume` OR `productivity` | (`software developer` OR `software team`) AND (`information overload` OR `communication breakdowns` OR `awareness`) |
| F4D | `software development` OR `software maintenance` OR `software engineering` | `software documentation` OR `documentation relevance` OR `documentation quality` OR `documentation usefulness` OR `task navigation` | `documentation maintenance` OR `documentation effort` OR `documentation cost` OR `how much is enough` | (`software development` OR `software maintenance`) AND (`software documentation` OR `documentation relevance` OR `documentation quality` OR `documentation usefulness`) |

F3C and F4C2 are supplementary targeted searches. F4D is primary, but its effort/cost, maintenance, and usefulness meanings should remain separate query variants. F2 and F4 overlap intentionally at screening; F3B and F1 also overlap on issue representations.

### F5-F7: Coding-Agent and Evaluation Branches

| Branch | Population/domain block | Phenomenon block | Outcome/context block | Canonical conceptual query |
|---|---|---|---|---|
| F5A | `coding agent` OR `AI coding agent` OR `agentic coding` | The population label itself | `software development` OR `coding-agent workload` OR `repository-level task` when needed | (`coding agent` OR `AI coding agent` OR `agentic coding`) AND (`software development` OR `software engineering` OR `repository-level task`) |
| F5B | `software engineering agent` OR `AI software engineer` OR `SWE agent` | The population label itself | `repository-level software engineering task` OR `agent trajectory` OR `software engineering` | (`software engineering agent` OR `AI software engineer` OR `SWE agent`) AND (`software engineering` OR `repository-level task`) |
| F5C | `SWE-agent` OR `SWE agents` OR `mini-SWE-agent` | Named lineage, system, or benchmark | `SWE-bench` OR `issue resolution` OR `repository navigation` OR `agent-computer interface` | (`SWE-agent` OR `SWE agents` OR `mini-SWE-agent`) OR (`SWE-bench` AND (`coding agent` OR `software engineering agent`)) |
| F6A1 | `coding agent` OR `software engineering agent` OR `SWE agent` | `long-context` OR `context compression` OR `context budget` OR `memory management` | `persistent memory` OR `interaction history` OR `long-horizon` OR `multi-turn` | (`coding agent` OR `software engineering agent` OR `SWE agent`) AND (`long-context` OR `context compression` OR `context budget` OR `memory management`) |
| F6A2 | `coding agent` OR `software engineering agent` OR `SWE agent` | `repository exploration` OR `structural code retrieval` OR `repository navigation` OR `repository-level understanding` | `knowledge map` OR `multi-hop dependencies` OR `structural queries` | (`coding agent` OR `software engineering agent` OR `SWE agent`) AND (`repository exploration` OR `structural code retrieval` OR `repository navigation`) |
| F6B1 | `coding agent` OR `software engineering agent` OR `SWE agent` | `explicit planning` OR `implicit planning` OR `planning structure` OR `plan-source intervention` | `planner` OR `scaffold` OR `planning-aware trajectory` OR `task plan` | (`coding agent` OR `software engineering agent` OR `SWE agent`) AND (`explicit planning` OR `implicit planning` OR `planning structure` OR `plan-source intervention`) |
| F6B2 | `coding agent` OR `software engineering agent` OR `multi-agent software development` | `functional decomposition` OR `subtask-level` OR `task delegation` OR `dependency-aware task plan` | `isolated workspace` OR `multi-agent coordination` OR `branch-and-merge` | (`coding agent` OR `software engineering agent`) AND (`functional decomposition` OR `subtask-level` OR `task delegation`) |
| F6C1 | `coding agent` OR `software engineering agent` OR `interactive coding agent` | `clarification-seeking` OR `requirement elicitation` OR `underspecified instructions` OR `dialogue-driven coding agent` | `user simulator` OR `ambiguous instruction` OR `clarification metric` | (`coding agent` OR `software engineering agent`) AND (`clarification-seeking` OR `requirement elicitation` OR `underspecified instructions`) |
| F6C2 | `coding agent` OR `software engineering agent` OR `DevOps agent` | `dialogue quality` OR `interaction quality` OR `task alignment` OR `specification refinement` OR `underspecification` | `steerability` OR `adaptability` OR `deferment` OR `bounded authority` | (`coding agent` OR `software engineering agent`) AND (`dialogue quality` OR `interaction quality` OR `task alignment` OR `specification refinement`) |
| F6D1 | `coding agent` OR `software engineering agent` OR `SWE agent` | `agent-computer interface` OR `agent-environment interaction` OR `tool-mediated` OR `bounded tool interface` | `execution feedback` OR `action space` OR `environment interface` | (`coding agent` OR `software engineering agent` OR `SWE agent`) AND (`agent-computer interface` OR `agent-environment interaction` OR `tool-mediated`) |
| F6D2 | `coding agent` OR `software engineering agent` OR `SWE agent` | `thought-action-result trajectory` OR `process-level trajectory evaluation` OR `trajectory assessment` OR `execution record` | `feedback integration` OR `interaction logs` OR `action patterns` | (`coding agent` OR `software engineering agent` OR `SWE agent`) AND (`thought-action-result trajectory` OR `process-level trajectory evaluation` OR `trajectory assessment`) |
| F7A | `software change` OR `patch` OR `automated program repair` OR `coding agent` | `patch correctness` OR `patch validation` OR `plausible patch` OR `patch overfitting` OR `semantic correctness` | `independent test suite` OR `behavioral discrepancy` OR `regression test` OR `gold correctness labels` | (`patch` OR `software change`) AND (`patch correctness` OR `patch validation` OR `plausible patch` OR `patch overfitting`) |
| F7B | `software repository` OR `GitHub` OR `software engineering` | `code review acceptance` OR `pull request acceptance` OR `merge decision` OR `maintainer decision` | `merge-ready` OR `review findings` OR `review outcome` OR `review iteration` | (`software repository` OR `GitHub`) AND (`pull request acceptance` OR `merge decision` OR `maintainer decision`) |
| F7C | `software development` OR `software repository` OR `pull request` | `software rework` OR `pull request revision` OR `review iteration` OR `post-initial-commit edit` OR `review-induced change` | `corrective maintenance` OR `revision cycle` OR `issue reopening` | (`software development` OR `pull request`) AND (`software rework` OR `pull request revision` OR `review iteration` OR `review-induced change`) |
| F7D | `coding agent` OR `software engineering agent` OR `SWE-agent` | `resolved issue` OR `resolve rate` OR `pass@1` OR `correct fix` OR `benchmark evaluator` | `SWE-bench` OR `hidden tests` OR `execution-based evaluation` OR `differential testing` | (`coding agent` OR `software engineering agent` OR `SWE-agent`) AND (`resolved issue` OR `resolve rate` OR `pass@1` OR `correct fix` OR `SWE-bench`) |
| F7E | `coding agent` OR `software engineering agent` OR `software engineering` | `human evaluation` OR `semantic correctness` OR `human inspection` OR `professional-developer annotation` | `user experience` OR `production-assessed evaluation` OR `trajectory review` | (`coding agent` OR `software engineering agent`) AND (`human evaluation` OR `semantic correctness` OR `human inspection` OR `production-assessed evaluation`) |

F5 branches identify populations and should be used both as standalone population searches and as population blocks for F6/F7. F6C2 and F7E remain supplementary. F7C requires distinct variants for review-induced revision, software-process rework, corrective maintenance, and post-merge change. F7A must not use unqualified `verification` or `validation` as the phenomenon block.

## 6. Tiered Execution Architecture

Protocol v1.1 uses the following prospective architecture:

1. Scopus systematic core: all 22 Primary branches remain planned for Scopus.
2. Additional-database API/capture feasibility validation.
3. Seven-branch cross-database calibration: `F2A`, `F4B`, `F5A`, `F6A1`, `F6C1`, `F7A`, and `F7D`.
4. Calibration-corpus deduplication.
5. Calibration title/abstract screening.
6. Marginal-contribution and research-question coverage analysis.
7. Freeze an empirical stopping/expansion rule.
8. Conditional branch/database expansion.
9. Complete systematic screening after retrieval expansion closes.

Feasibility validation is operational validation and is not a systematic corpus execution. Additional databases enter the seven-branch calibration only after a feasible, complete, and auditable route is demonstrated. Existing valid historical executions may satisfy calibration cells; the execution log remains the source of truth for their status and provenance.

Calibration screening is limited to methodological coverage analysis. It must not become evidence extraction, evidence synthesis, Work Item-characteristic derivation, or hypothesis formation.

The six Supplementary branches (`F3C`, `F4C2`, `F6B1`, `F6B2`, `F6C2`, and `F7E`) are conditionally activated by documented evidence gaps, unresolved research-question coverage, contradiction or boundary evidence, contextual comparison needs, snowballing, or database-specific unique contribution. They are not automatically required in any database.

## 7. Branch-Sensitive Database Roles

The six-database source set remains unchanged, but roles are earned by branch family or evidence domain rather than assigned universally:

| Database | Protocol v1.1 role policy |
|---|---|
| Scopus | Systematic core for all 22 Primary branches, using the validated API where complete retrieval fits its service limits and the validated Web route otherwise. |
| IEEE Xplore | Candidate domain, validation, or targeted source by branch family after feasibility and calibration. |
| ACM Digital Library | Separate feasibility-gated domain, validation, or targeted source; Basic capture must satisfy its reconciliation controls. |
| Web of Science | Cross-database validation or targeted source by branch family after feasibility and calibration. |
| ScienceDirect | Publisher-specific validation or targeted source by branch family after feasibility and calibration. |
| SpringerLink | Publisher-specific validation or targeted source by branch family after feasibility and calibration. |

Google Scholar is for discovery, citation tracing, and backward/forward snowballing, not the sole systematic database. arXiv, OpenAlex, and Crossref remain pilot/discovery or metadata-support sources; they do not replace protocol databases. Access feasibility, authentication, quotas, export limits, and indexing coverage must be verified before an additional database enters calibration. Any unavailable database must be recorded as an operational limitation, not silently replaced.

### Feasibility Gate

For IEEE Xplore, ScienceDirect, Springer Nature Link, and Web of Science, the feasibility gate uses one or more representative frozen queries and records Web/API counts where available, stable-identifier comparison, field semantics, complete pagination, export/capture reconciliation, raw provenance, and entitlement limitations. The allowed outcomes are `equivalent enough for systematic retrieval`, `usable with documented differences`, and `unsuitable as a systematic API route`.

ACM Digital Library is assessed separately. Its route must first demonstrate complete capture using the approved manual Basic workflow or an independently authorized Premium export. Undocumented APIs, scraping, browser automation intended to bypass restrictions, and access circumvention are prohibited.

The gate is not a systematic corpus execution. A database that passes the gate enters the seven-branch calibration; it does not thereby receive all 22 Primary branches. Expansion remains branch- and evidence-domain-sensitive.

### Calibration And Expansion

The seven calibration branches are `F2A`, `F4B`, `F5A`, `F6A1`, `F6C1`, `F7A`, and `F7D`. After calibration retrievals are complete, records are deduplicated and titles/abstracts are screened under the unchanged protocol. The analysis measures unique contribution after deduplication and screening, research-question coverage, contradictory/boundary coverage, coding-agent-specific contribution, and branch-sensitive database contribution.

Only after those observations exist may the stopping/expansion rule be frozen. No universal numerical threshold is defined in v1.1. Conditional expansion may execute any active frozen query, including queries not selected for automatic execution, and must record its trigger before execution.

## 8. Database-Specific Adaptation

The conceptual queries above are database-independent. The following adaptation rules apply to every branch. Exact syntax not verified in the repository is explicitly left for execution-time validation.

| Database | Preferred fields and translation | Phrase/wildcard/proximity status | Filters and operational notes |
|---|---|---|---|
| IEEE Xplore | Prefer metadata search over title, abstract, and author keywords; use title-only sensitivity checks for high-noise branches. Exact field names and advanced-query syntax: `TBD — verify against database search interface before execution`. | Quoted phrases should be tested. Wildcard and proximity syntax: `TBD — verify against database search interface before execution`. | Filter by publication year and document type only after confirming available controls. Record conference, journal, review, and preprint status separately. |
| ACM Digital Library | Prefer title, abstract, and author-supplied keywords where the interface exposes them; use title-only variants for exact artifact/lineage checks. Field syntax: `TBD — verify against database search interface before execution`. | Quoted phrases are expected but exact phrase behavior, wildcard, and proximity syntax: `TBD — verify against database search interface before execution`. | Record journal, proceedings, workshop, survey/review, and preprint records separately. Do not assume ACM indexing of an arXiv version. |
| Scopus | Use `TITLE-ABS-KEY(...)` for the default title+abstract+keyword search; use `TITLE(...)` for precision checks. Exact wildcard, proximity, and document-type syntax: `TBD — verify against database search interface before execution`. | Phrase quoting is expected; wildcard/proximity behavior must be verified before execution. | Use publication-year and `DOCTYPE` filters only after interface verification. Avoid limiting subject area unless documented as a sensitivity variant. |
| Web of Science | Use the Topic field (`TS`) where it searches title, abstract, author keywords, and Keywords Plus; use title-only (`TI`) sensitivity checks where appropriate. Exact query parser and proximity syntax: `TBD — verify against database search interface before execution`. | Phrase and wildcard behavior: `TBD — verify against database search interface before execution`; do not assume Scopus syntax transfers. | Record database edition/indexes, years, document types, and any language filter. Do not silently treat Topic as unrestricted full text. |
| ScienceDirect | Prefer title, abstract, and keywords through the advanced search interface; exact field syntax and API behavior: `TBD — verify against database search interface before execution`. | Phrase, wildcard, and proximity syntax: `TBD — verify against database search interface before execution`. | Record article type, year, journal/conference context, and whether the result is full text or metadata-only. Avoid unrestricted full text for high-noise branches. |
| SpringerLink | Prefer title, abstract, and keyword fields when available; exact advanced-search field syntax: `TBD — verify against database search interface before execution`. | Phrase, wildcard, and proximity syntax: `TBD — verify against database search interface before execution`. | Record content type, year, journal/book chapter/conference proceedings, and preprint or accepted-manuscript status. Search interface limits and access: `TBD — verify before execution`. |

For each branch, execution should create at least one default title+abstract+keyword/topic variant and, where justified below, a title-only precision or broader sensitivity variant. Boolean parentheses must be checked in the live interface. Database syntax correction is not a conceptual query change, but it must still be logged as a query-version event.

### Field Strategy

| Branch group | Default field strategy | Reason from P1-P12 |
|---|---|---|
| F1-F3 traditional work/requirements branches | Title+abstract+keywords/topic, with separate title-only checks for exact phrases and known items. | Broad all-field searches made `task`, `issue`, `description`, decomposition, and allocation noisy; title-only searches improved precision but missed known items. |
| F4A/F4B/F4C1/F4D | Title+abstract+keywords/topic for the systematic default; exact title branches for ambiguity, completeness, developer information needs, and software documentation; broader variants only as sensitivity searches. | P8 showed low-noise title neighborhoods but incomplete recall; broad full-text searches produced linguistic, package, education, and general information noise. |
| F4C2 | Targeted title+abstract+keywords/topic only; do not use unrestricted full text as the default. | Information-overload retrieval remained extremely noisy and is supplementary. |
| F5 | Title+abstract+keywords/topic, preserving F5A/F5B/F5C separately; title-only lineage checks for `SWE-agent` and exact coding-agent labels. | Title restriction reduced breadth while abstract inclusion recovered recent terminology; no single field is recall-complete. |
| F6 | Title+abstract+keywords/topic with separate exact-phrase variants; broader context/planning/interaction variants are sensitivity searches. | P10 found operational terms more useful than umbrella terms, but exact wording is sparse and rapidly changing. |
| F7 | Object- and authority-qualified title+abstract+keywords/topic. Use title-only checks for `patch correctness`, `pull request acceptance`, and named benchmarks. | P11-P12 showed that unqualified verification, validation, completion, acceptance, and quality collapse unlike outcomes and create noise. |

No branch defaults to unrestricted full text. A broader field variant is justified only when title+abstract+keyword retrieval misses a validated known item or when the branch is demonstrably sparse; the reason and expected recall/noise effect must be logged.

## 9. Time Coverage and Publication Types

Time restrictions follow [`research/protocol.md`](./protocol.md), not result-set convenience.

| Branches | Coverage design |
|---|---|
| F1-F4 and traditional portions of F3/F7 | Broad historical coverage. Do not impose a single cutoff. If a database requires a start date, select and document a concept-specific rationale, or use no date restriction initially. Older requirements, decomposition, information, documentation, review, rework, and verification work may be necessary. |
| F5 | Recent-focused, technology-sensitive coverage with no silent cutoff. Include older agent labels or directly relevant precursor studies when they establish terminology, methods, or benchmarks. Exact start date: `TBD — execution-time decision requiring documented rationale`. |
| F6 | Recent coding-agent-focused coverage because models, tools, interfaces, and environments change quickly. Retain older directly applicable agent/software-engineering-agent studies and benchmark lineage sources. Exact cutoff: `TBD — execution-time decision requiring documented rationale`. |
| F7D/F7E and agentic F7B/F7C | Recent coding-agent-focused coverage, with benchmark lineage and older traditional comparison branches retained separately. Exact cutoff: `TBD — execution-time decision requiring documented rationale`. |

Retrieval should include peer-reviewed journal papers, conference papers, systematic reviews, systematic mapping studies, relevant preprints, and technically assessable reports. Relevant technical reports may be included in retrieval when methods and provenance are assessable. Preprints must be identifiable as preprints and must not be treated as equivalent to peer-reviewed work. Recent coding-agent work must not be excluded solely for lack of peer review. Publication type, peer-review status, later version, and evidence stream are recorded before screening; they are not screening decisions by themselves.

## 10. Known-Item Retrieval Validation

Known items are calibration seeds, not included evidence. Before freezing a database-specific query variant, execution must test representative items for that branch and record one of `Retrieved`, `Missed`, `Not indexed`, `Not applicable`, or `Not verified`. A miss triggers analysis of terminology, indexing, field restriction, database coverage, and publication/version differences. Queries must not be changed solely to force every seed to appear.

| Branch | Representative pilot seed(s) for execution checks |
|---|---|
| F1 | Licorish and MacDonell, *software development task type*; Ramírez-Mora et al., *Descriptions of issues and comments*. |
| F2A | Krishna et al., *Using LLMs in Software Requirements Specifications*; del Sagrado and del Águila, *Stability prediction of the software requirements specification*. |
| F2B | Raharjana et al., *User Stories and Natural Language Processing*; Schwedt and Ströder, *From Bugs to Benefits*. |
| F2C | Atoum et al., *Requirements Quality Assurance and Validation*; Wong and Lau, *Requirements quality control*. |
| F3A | Khanfor, *Tasks Decomposition Approaches in Crowdsourcing Software Development*; Zeng et al., *Benchmarking... End-to-End Software Development*. |
| F3B | Ramírez-Mora et al., *Descriptions of issues and comments for predicting issue success*. |
| F3C | Stol and Fitzgerald, *Two's company, three's a crowd*; Saremi and Yang, *Empirical Analysis on Parallel Tasks*. |
| F4A | Bano, *Addressing the challenges of requirements ambiguity*; Rempel and Mader, *Requirements Traceability Completeness*. |
| F4B | Liu et al., *API-Related Developer Information Needs*; Ko et al., *Information Needs in Collocated Software Development Teams*. |
| F4C1 | Nakagawa et al., *Quantifying programmers' mental workload*; Cao et al., *NASA TLX*. |
| F4C2 | Damian et al., *Awareness in the Wild*; *Structuring computer-mediated communication systems to avoid information overload*. |
| F4D | Forward and Lethbridge, *The relevance of software documentation*; Briand, *Software documentation: how much is enough?*. |
| F5A | *SWE-chat*; *Change2Task*; *AIDev*. |
| F5B | *Demystifying LLM-Based Software Engineering Agents*; *Unified Software Engineering Agent as AI Software Engineer*. |
| F5C | *SWE-agent*; *SWE-bench*; *Agentless*. |
| F6A1 | *On Problems of Implicit Context Compression*; *SWE-MeM*; *Confucius Code Agent*. |
| F6A2 | *OwlPath*; *SWE-Replay*; *SWE-agent*. |
| F6B1 | *DCAS*; *HyperAgent*; *PatchPilot*. |
| F6B2 | *Structurally Aligned Subtask-Level Memory*; *Effective Strategies for Asynchronous Software Engineering Agents*. |
| F6C1 | *Ask or Assume?*; *ClarEval*; *Dialogue SWE-Bench*. |
| F6C2 | *ICAE-Bench*; *Humans are Missing from AI Coding Agent Research*; *UnderSpecBench*. |
| F6D1 | *SWE-agent*; *SWE-World*. |
| F6D2 | *Understanding Software Engineering Agents*; *Process-Level Trajectory Evaluation*. |
| F7A | Le et al., *On Reliability of Patch Correctness Assessment*; Xiong et al., *Identifying Patch Correctness*. |
| F7B | Lenarduzzi et al., *Does Code Quality Affect Pull Request Acceptance?*; Dey and Mockus, *Which Pull Requests Get Accepted and Why?*. |
| F7C | Coelho et al., *An Empirical Study on Refactoring-Inducing Pull Requests*; Morozoff, *Using a Line of Code Metric to Understand Software Rework*. |
| F7D | *SWE-bench*; *SWE-agent*; *UTBoost*. |
| F7E | *SEAlign*; *AgentLens*; Wang and Pradel, *Are Solved Issues in SWE-bench Really Solved Correctly?*. |

## 11. Search Execution Unit and Logging

One systematic search execution is one branch, database, query version, field configuration, filter configuration, and execution date. The stable ID scheme is:

`S1-F6A2-SCOPUS-01`

`S1` identifies the systematic-search execution phase, `F6A2` identifies the branch, `SCOPUS` identifies the database, and `01` identifies the query iteration/version. Pilot IDs beginning with `P` must not be reused.

Systematic records must be appended to [`systematic-search-log.md`](./systematic-search-log.md) in a clearly marked section after the historical records. The log is the source of truth for completed, failed, superseded, and reused historical executions. Each record must contain:

| Required field | Recording rule |
|---|---|
| Search ID | Stable ID from the scheme above. |
| Date | Actual execution date, not design date. |
| Database | Exact database, edition/index, and access mode where relevant. |
| Exact query | Copy the executed database string, including parentheses and field operators. |
| Fields | Title, abstract, keywords, topic, or other live-interface field. |
| Filters | Year, language if used, subject/document type, and any result limits. |
| Time coverage | Start/end dates or no restriction, with rationale. |
| Publication filters | Journal, conference, review, mapping, preprint, report, or other selected types. |
| Result count | Database-reported count and whether it is before/after any export limit. |
| Known-item results | Item-by-item status using the five allowed labels. |
| Operational limitations | Access, authentication, rate limits, indexing, export, or syntax problems. |
| Query version | `v1`, `v2`, and so on, linked to the branch/database. |
| Notes | Duplicates, unexpected noise, field behavior, and planned follow-up. |

Query changes cannot be silent. `v1` is the initial systematic query. `v2` or later requires a log entry recording the reason, affected databases, expected effect on recall/precision, whether earlier executions need rerunning, and whether comparability is affected. The reason must be classified as syntax correction, database adaptation, terminology update, or methodological scope change. A methodological scope change may require protocol evolution and must not be hidden as a query edit.

## 12. Record Collection and Deduplication

Before screening, collect at least:

- provisional Source ID;
- title;
- authors;
- year;
- venue;
- DOI;
- stable URL;
- database;
- Search ID and branch provenance;
- publication status;
- abstract when legally and technically available.

Retrieval metadata is not evidence extraction. No finding, outcome, quality judgment, or Work Item implication is recorded at this stage.

Deduplicate in descending reliability:

1. Exact normalized DOI, after removing resolver prefixes, case differences, and harmless punctuation.
2. Normalized title plus author overlap and year tolerance.
3. Stable publication identifier, database record ID, or repository identifier.
4. Manual comparison of title, authors, venue, pages, abstract, and version history when ambiguity remains.

Preserve a relationship record between preprint, conference paper, journal extension, technical report, accepted manuscript, and duplicate database records. Do not simply discard an earlier version if it contains a materially different method, dataset, evaluation, or limitation. Screening will later select a preferred version for a claim while retaining linked versions and their differences. The preferred version should normally be the most complete and assessable peer-reviewed or published version, but a preprint may remain the relevant version for a recent coding-agent result or for material absent from the later version. Publication status must remain explicit.

## 13. Screening Handoff

After collection and deduplication, hand off a candidate corpus with provisional Source IDs and preserved database/Search ID provenance to the protocol sequence:

1. Deduplicated candidate corpus.
2. Title and metadata screening.
3. Abstract or source-description screening.
4. Full-text or complete-source screening.
5. Inclusion/exclusion decision, evidence stream, and research-question relevance.

This design performs none of those screening steps. Exclusion reasons must use the protocol vocabulary, including `out of scope`, `duplicate`, `insufficient method`, `insufficient source information`, `not evidence for the claimed use`, or another documented reason. A useful contextual source that is not eligible evidence may be retained as contextual material without supporting a conclusion.

## 14. Snowballing Design

Backward and forward snowballing supplements, and does not replace, the six protocol database searches.

- Seeds may be included sources, high-relevance full-text candidates, systematic reviews or mappings, standards/authoritative sources where citation tracing is meaningful, and pilot seed sources after they have been independently verified during execution.
- Snowballing begins after title/abstract screening has identified sufficiently relevant seeds and is repeated after full-text screening for included or high-relevance sources. The trigger, direction, date, seed Source ID, and reason must be recorded.
- Backward candidates receive a provenance Search ID such as `S1-F4A-SNOWBACK-01`; forward candidates use `S1-F4A-SNOWFWD-01`. The source seed and citation direction are mandatory fields.
- Snowballing candidates enter the same title, abstract, full-text, eligibility, and exclusion-reason sequence as database candidates.
- Repeated discovery is deduplicated using DOI, normalized title/authors, stable identifiers, and manual comparison while retaining every discovery path.
- Citation chasing must actively seek contradictory, null, and boundary evidence, not only sources cited as support by a seed.

Google Scholar may support discovery and citation tracing, but its result ranking and coverage must not replace systematic database retrieval.

## 15. Freeze Condition and Risks

A branch is sufficiently designed to execute only when all of the following are present:

- conceptual query and separate supplementary variants;
- branch purpose, population boundary, and known major noise;
- database adaptation plan for each primary database;
- field strategy and reason for any broad variant;
- coverage period and rationale;
- publication/source-type filters;
- representative known-item checks;
- branch-to-question mapping;
- stable execution ID and logging fields;
- collection, deduplication, and screening handoff rules.

Unresolved issues before execution are:

- Access to Scopus, Web of Science, IEEE Xplore, ACM Digital Library, ScienceDirect, and SpringerLink, including institutional authentication and export limits.
- Live syntax verification for field names, phrase handling, wildcards, proximity, Boolean precedence, document types, and year filters.
- Database overlap and the possibility that one publication appears as preprint, conference, journal, and repository records.
- Indexing of rapidly changing coding-agent terminology and recent preprints.
- Sparse human/semantic coding-agent evaluation and whether broader databases or snowballing expand it.
- Benchmark-heavy coding-agent evidence and the difference between benchmark resolution, test passing, semantic correctness, maintainer acceptance, and production outcomes.
- Publication-version deduplication where later versions change methods or results.
- Rapidly changing agent, benchmark, scaffold, and tool terminology.
- Transferability of traditional software-engineering evidence to coding-agent populations.
- Whether sparse terms such as repository understanding, planning intervention, and human evaluation require documented terminology updates after database validation.

## 16. Execution-Readiness Decision

**Systematic search design ready for Protocol v1.1 feasibility validation and tiered execution**

The conceptual branch structure, research-question mapping, field strategy, source roles, time rules, publication distinctions, known-item checks, logging, deduplication, screening handoff, snowballing, change control, and freeze condition are documented. Exact live database syntax and access have not been validated, so the systematic search is not declared ready to run.

No new database/API request, screening, evidence extraction, synthesis, Work Item-characteristic derivation, hypothesis formation, or research conclusion was performed while recording this amendment. Historical execution status remains in [`systematic-search-log.md`](./systematic-search-log.md).
