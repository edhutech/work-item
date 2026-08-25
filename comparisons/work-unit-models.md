# Work-Unit Model Comparisons

## Boundary And Method

This is a descriptive comparison of existing software-development work
representations. It is analytically distinct from the Practitioner Evidence
stream and from the Standards and Authoritative Sources evidence stream. It is
not a ranking, design proposal, evaluation of Work Items, or mapping of every
model into the provisional Work Item definition.

Models are studied on their own terms. Similar words can operate at different
levels or in different ecosystems. A model may be an artifact, a planning
container, a workflow record, a user-centered framing device, or a relationship
between artifacts rather than a bounded unit of execution.

The cells below summarize source-described scope and preserve variation. An
`Unresolved` cell means that the sources captured here do not justify a
generalized description. `Context-dependent` means that the source supports a
description only within a named method or platform. The later-analysis columns
are intentionally unresolved and make no inference about coding-agent
suitability.

## Comparison Dimensions

- **Problem addressed:** Need the model is intended to organize or communicate.
- **Unit and scope:** What one instance represents and its usual boundary.
- **Information:** Typical content or relationships, without assuming a fixed
  schema across ecosystems.
- **Executor:** Expected actor or audience in the source context.
- **Product/system context:** Relationship to a broader product, service, or
  system.
- **Completion/acceptance:** How completion, value, or acceptance is treated.
- **Lifetime and persistence:** Typical duration and state history.
- **Composition/dependencies:** Parent, child, sequencing, or blocking
  relationships.
- **Verification/validation:** Stated relationship to tests, review, or other
  validation.
- **Prescription and workflow role:** How much implementation detail is
  expected and where the model sits in a workflow.
- **Human interaction and limitations:** Expected collaboration and documented
  ambiguity or boundary.
- **Later analysis fields:** Coding-agent applicability, transfer limitations,
  possible structural friction, possible benefits, and contextual conditions;
  all remain `Unresolved` in this initial comparison.

## Matrix

| Model | Authoritative or primary basis | Problem addressed | Unit and scope | Typical information | Executor and broader context | Completion/acceptance | Lifetime, composition, dependencies | Verification, prescription, workflow, limitations |
|---|---|---|---|---|---|---|---|---|
| **Requirement** | [WU-ISO-29148] | Express and manage a needed capability, condition, or constraint in requirements engineering. Exact normative classification requires the standard text. | A statement or related requirements information item; not necessarily an executable change. Scope is system/software lifecycle context. | Need, capability, condition, constraint, or relationship; exact required fields are `Unresolved` from public metadata. | Requirements stakeholders, acquirers, developers, and other lifecycle participants; relates to the system or product being engineered. | Satisfaction, validation, and acceptance treatment are context-dependent; exact completion rule is `Unresolved`. | May be decomposed, traced, baselined, changed, and linked to other lifecycle artifacts; exact relationship model is `Unresolved`. | Supports verification/validation planning but does not itself prescribe implementation. Not necessarily a bounded execution unit; may persist across lifecycle changes. |
| **Specification** | [WU-ISO-29148]; [WU-ISO-25010] | Provide a structured description against which requirements, design, quality, or evaluation can be communicated. The precise meaning varies by document type and method. | Usually a document or set of information items, not inherently one implementation task. Boundary is defined by its subject and governing process. | Requirements, interfaces, constraints, quality properties, measures, or acceptance-related information depending on specification type. ISO/IEC 25010 explicitly describes use in requirements specification and evaluation. | Multiple stakeholders across the lifecycle; not limited to the eventual implementer. | Can provide evaluation or acceptance bases, but a specification is not itself proof of satisfaction. Completion of the specification and satisfaction of its contents are distinct and context-dependent. | Often durable and versioned; may contain or reference many requirements and implementation units. Dependencies and decomposition are method-specific. | Can be highly prescriptive or intentionally abstract. It may support verification and validation while remaining too broad to define one executable unit. Detailed document schema and overhead are `Unresolved`. |
| **User Story** | [WU-AGILE-USER-STORY] | Communicate a user-valued functional increment and support incremental planning and feedback. | A functional increment framed around value or a user goal; Agile Alliance warns it is not necessarily a document, use case, or technical component. | Brief reminder, user role/goal/value, discussion knowledge, examples, and acceptance criteria as the work approaches implementation. | Customer/product owner collaborates with a development team; the team decides technical how in the cited description. | Expected to yield a contribution to product value; acceptance criteria and ongoing feedback commonly support completion, but the source does not define one universal DoD. | Can be split, scheduled, prioritized, and related to epics; detail evolves with planning horizon. Usually persists through planning and delivery states. | Encourages incremental delivery and technical discretion, with acceptance criteria and automated acceptance testing often relevant. The source documents testing cost and the need for ongoing information; story quality is not guaranteed by the label. |
| **Task** | [WU-SCRUM-GUIDE]; [WU-GITHUB-ISSUES] | Represent an actionable piece of work within a planning or issue-tracking workflow. Meaning differs between Scrum usage, platform issue types, and local practice. | Usually a smaller action or implementation unit, but may be a top-level issue type in a platform. It is not universal. | Summary, description, assignee, status, estimates, links, and local fields vary by tool or method. | Often an implementer or team member; Scrum and repository contexts differ. It sits under a broader product backlog, issue, or sprint context when configured that way. | Status transition, review, or local Definition of Done may indicate completion; no universal acceptance rule. | Commonly decomposed from a larger item and linked to dependencies, but hierarchy is platform/method-specific. Lifetime follows the tracking system. | Often more action-oriented and implementation-prescriptive than a user story, but the degree is local. Verification and review may be linked rather than contained. Terminology is not standardized across all tools. |
| **Issue** | [WU-GITHUB-ISSUES] | Track ideas, feedback, bugs, tasks, or work to discuss and manage in a repository or project. | A flexible conversation/work record; GitHub explicitly supports multiple uses and sub-issues. It may be a container rather than a standardized execution unit. | Title, description, discussion, labels, assignees, milestones, issue types, links, sub-issues, and dependencies, depending on platform configuration. | Repository contributors, maintainers, and project participants; relates to a repository/project context. | Resolution, closure, linked pull request, or project workflow may signal completion; GitHub does not impose one acceptance schema. | Persistent record with comments and state history; can contain sub-issues and dependency links. | Templates and metadata can structure reports, but free-form use remains possible. Verification may occur through linked pull requests, checks, or discussion. The same word covers bugs, ideas, and tasks, so cross-platform equivalence is unsafe. |
| **Ticket** | [WU-ATLASSIAN-CHANGE]; [WU-GITHUB-ISSUES] | Route, queue, and maintain a request or incident record in service/support or work-management operations. The term is used differently across products. | Usually a record in a queue, not a universal software-development schema. It may represent a request, incident, change, or other service interaction. | Requester/context, description, priority, status, ownership, communication, approvals, and resolution fields vary by system. | Service desk, support, operations, development, or other assigned personnel; broader service/system context is typical. | Resolution, fulfillment, closure, or approval according to the service workflow; exact acceptance is context-dependent. | Often persists for audit/history and passes through workflow states; may link to changes, incidents, problems, or implementation tasks. | Workflow and routing are usually more central than implementation prescription. Verification may be an operational resolution check. “Ticket” is a colloquial cross-tool term, not a single model. |
| **Epic** | [WU-ATLASSIAN-EPICS]; [WU-AGILE-USER-STORY] | Organize and track a large body of work or outcome that cannot normally be delivered as one small increment. | An aggregate/container above stories or other child items in the cited Agile/Jira context; not normally one executable unit. | Outcome or theme, summary, priority, roadmap/release information, progress, and child-item links vary by tool. | Product/project stakeholders and delivery teams; relates to a product, initiative, or release context. | Completion depends on child work and the local outcome/acceptance definition; no universal epic-level acceptance rule. | Longer-lived than child stories/tasks; decomposes into stories or other items and may depend on multiple streams. | Low implementation prescription at the aggregate level. Verification is distributed across child items and product outcome checks. Its container nature is a central boundary, not a reason to treat it as synonymous with a task. |
| **Change Request** | [WU-ATLASSIAN-CHANGE] | Govern a proposed addition, modification, or removal that may affect an IT service, including assessment, authorization, scheduling, and implementation tracking. | A request/record for a change to a service or system; it can encompass multiple implementation activities. | Description, reason, risk/impact, affected service, approval, schedule, implementation, and rollback/review information vary by process. | Change requester, approver, service owner, implementer, and reviewer; assumes organizational/service governance context. | Authorization is not implementation completion. Completion may include implementation, validation, review, and closure under the local change process. | Often persistent for audit and governance; may link to incidents, tasks, releases, or implementation records. Dependencies and approvals are process-specific. | More governance-prescriptive than implementation-prescriptive. Verification and post-implementation review may be required by the process. It is not necessarily a bounded code change. |
| **Job To Be Done** | [WU-JTBD] | Frame the circumstances, forces, and progress a person or organization is trying to achieve when choosing or using a product/service. | A job is a goal-oriented lens or situation, not inherently a software implementation unit. It can span multiple product capabilities or work items. | Circumstances, functional/social/emotional forces, desired progress, and decision context. | Innovators/researchers and users/customers; broader life or organizational context is central. | Success is progress for the actor in the relevant circumstance, not code completion; operational acceptance is `Unresolved`. | May persist or change with circumstances; composition, dependencies, and decomposition into software work are not defined by the source. | Low implementation prescription and high contextual framing. It can inform discovery but does not specify tests, code scope, or an execution workflow. |
| **Pull Request** | [WU-GITHUB-PR] | Propose, review, discuss, and merge a set of repository changes. | A repository change proposal, typically a diff between branches/commits; it represents implementation/review work rather than the original need alone. | Title, description, commits, changed files, review comments, checks, approvals, links, and merge state. | Contributors, reviewers, and maintainers in a repository context. | Review approval, required checks, and merge/close state are platform/workflow signals; acceptance criteria may come from a linked issue. | Persists as an auditable conversation and change record; can link to issues and commits, but one PR may address several concerns. | Directly tied to code review and automated checks, but prescription depends on the linked request and repository norms. It is a work representation and delivery gate, not necessarily a requirements unit. |

## Later-Analysis Fields

These fields are intentionally not populated from human-oriented definitions:

| Model set | Coding-agent applicability | Transfer limitations | Possible structural friction | Possible benefits | Contextual conditions |
|---|---|---|---|---|---|
| All models above | Unresolved | Unresolved | Unresolved | Unresolved | Unresolved |

No practitioner record is used to define any model. No model definition is
used to claim a practitioner benefit, failure, or preference.

## Explicit Abstraction Boundaries

- A requirement can constrain or describe a need without being a task to
  execute.
- A specification can contain many requirements and artifacts without being a
  bounded implementation unit.
- A user story describes a valued increment but is not necessarily a document,
  technical component, or task list.
- A task is often action-oriented, but its meaning and hierarchy depend on the
  method or tracking platform.
- An issue can be a flexible conversation, report, or container rather than a
  standardized work-unit schema.
- A ticket is a workflow record whose meaning varies across service and
  development systems.
- An epic aggregates work and should not be treated as one executable unit.
- A change request governs a proposed change and may include several artifacts
  or implementation tasks.
- A Job To Be Done frames circumstances and progress rather than code scope.
- A pull request represents a code-change and review boundary, not necessarily
  the requirement or user outcome that motivated it.

## Deferred Models

- **SDD-style Change:** Deferred from the initial comparison. It is a
  framework-specific representation, and this research does not adopt SDD or
  OpenSpec as a default baseline. A later comparison requires a clearly
  identified primary framework source and must preserve ecosystem-specific
  meaning rather than treating “change” as a universal model.
- **Other variants:** Deferred unless a source establishes a materially distinct
  software-development representation rather than a synonym or tool-specific
  label.

## Sources And Provenance

- **[WU-ISO-29148]** ISO/IEC/IEEE 29148:2018, *Systems and software
  engineering — Life cycle processes — Requirements engineering*, ISO standard
  record: https://www.iso.org/standard/72089.html. Normative standard record;
  full text not reproduced.
- **[WU-ISO-25010]** ISO/IEC 25010:2023, *Systems and software engineering —
  Systems and software Quality Requirements and Evaluation (SQuaRE) — Product
  quality model*, ISO standard record: https://www.iso.org/standard/78176.html.
  Normative standard record; used for the specification/evaluation distinction;
  full text not reproduced.
- **[WU-AGILE-USER-STORY]** Agile Alliance, “User Stories,” official glossary:
  https://www.agilealliance.org/glossary/user-stories/. Professional
  methodology reference, not an empirical study.
- **[WU-GITHUB-ISSUES]** GitHub Docs, “About issues”:
  https://docs.github.com/en/issues/tracking-your-work-with-issues/about-issues.
  Official platform documentation; its description is GitHub-specific.
- **[WU-GITHUB-PR]** GitHub Docs, “About pull requests”:
  https://docs.github.com/en/pull-requests/get-started/about-pull-requests.
  Official platform documentation; the description is GitHub-specific.
- **[WU-ATLASSIAN-EPICS]** Atlassian, “Epics”:
  https://www.atlassian.com/agile/project-management/epics. Official product
  and methodology guidance; Jira/Agile context is explicit.
- **[WU-ATLASSIAN-CHANGE]** Atlassian, “IT Change Management”:
  https://www.atlassian.com/itsm/change-management. Official ITSM guidance;
  service-management context is explicit.
- **[WU-SCRUM-GUIDE]** Scrum Guides, *The 2020 Scrum Guide*:
  https://scrumguides.org/scrum-guide.html. Primary Scrum framework source;
  task language is not assumed to define a universal task schema.
- **[WU-JTBD]** Christensen Institute, “Jobs to Be Done Theory”:
  https://www.christenseninstitute.org/theory/jobs-to-be-done/. Official
  theory reference; it is not a software work-tracking model.

## Status

- Comparison type: descriptive preparation
- Ranking: none
- Work Item superiority claim: none
- Coding-agent suitability inference: none
- Cross-stream synthesis: none
- Unsupported dimensions marked `Unresolved`: yes
