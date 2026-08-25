# GitHub Evidence

This document records the initial GitHub pilot for the Practitioner Evidence
stream. The records are paraphrases, not quotations, and remain uncoded.

## Evidence Records

### P-GH-AIDER-001

- **Platform/source:** GitHub, Aider repository
- **Source type:** Issue / user-reported problem
- **Original public URL:** https://github.com/Aider-AI/aider/issues/4113
- **Publication date:** 2025-05-27
- **Capture date:** 2026-08-24
- **Tool/ecosystem context:** Aider with Claude 3.7 hosted in AWS, as reported
  by the author
- **Software-development context:** A long or particularly complicated coding
  task continued without breaking it into chunks
- **Relevant RQ/domain:** Q1, Q2, Q4, Q6; context management and task
  decomposition
- **Neutral observation:** The author reports that after extended interaction
  or a complex unchunked task, the model began producing unusable responses;
  restarting and manually restoring a relevant portion of chat history was
  reported as a workaround.
- **Source-context note:** First-person self-report and feature suggestion;
  no independent reproduction in the record.
- **Directness:** direct
- **Uncertainty:** Model behavior, task details, and the proposed cause are not
  independently verified.
- **Coding/extraction status:** pilot captured — not coded

### P-GH-AIDER-002

- **Platform/source:** GitHub, Aider repository
- **Source type:** Feature request / practitioner report
- **Original public URL:** https://github.com/Aider-AI/aider/issues/5071
- **Publication date:** 2026-04-25
- **Capture date:** 2026-08-24
- **Tool/ecosystem context:** Aider; author describes a local proof of concept
  for context lifecycle management
- **Software-development context:** Multi-task sessions in which explicitly
  loaded files remain active after their immediate task relevance has ended
- **Relevant RQ/domain:** Q2, Q4, Q6; context management and information load
- **Neutral observation:** The report describes manually added files persisting
  across tasks and proposes compression or eviction of stale files; it also
  reports benchmark figures for a proof of concept.
- **Source-context note:** The figures and majority-of-users claim are
  author-reported and not independently verified here.
- **Directness:** direct
- **Uncertainty:** The report is both a feature proposal and a self-described
  implementation; causal effects and generality are unresolved.
- **Coding/extraction status:** pilot captured — not coded

### P-GH-AIDER-003

- **Platform/source:** GitHub, Aider repository
- **Source type:** Issue / benchmark harness report
- **Original public URL:** https://github.com/Aider-AI/aider/issues/5492
- **Publication date:** 2026-07-25
- **Capture date:** 2026-08-24
- **Tool/ecosystem context:** Aider's Polyglot benchmark and Exercism exercise
  configuration
- **Software-development context:** A benchmark task where read-only editor
  files define interfaces needed by a solution but were reportedly omitted from
  model context
- **Relevant RQ/domain:** Q1, Q2, Q3, Q8; repository context and information
  sufficiency
- **Neutral observation:** The report states that excluding declared editor
  files can leave the model to infer compile-time interfaces, while exposing
  solution files remains restricted to editable content.
- **Source-context note:** Concrete file examples and a proposed regression
  test are included in the public issue.
- **Directness:** direct
- **Uncertainty:** This is a report about a benchmark harness and its stated
  configuration; broader task generalization is unresolved.
- **Coding/extraction status:** pilot captured — not coded

### P-GH-CLAUDE-001

- **Platform/source:** GitHub, Claude Code repository
- **Source type:** Bug report / user-reported problem
- **Original public URL:** https://github.com/anthropics/claude-code/issues/85610
- **Publication date:** 2026-08-10
- **Capture date:** 2026-08-24
- **Tool/ecosystem context:** Claude Code CLI, version 2.1.220, with a stated
  plan-then-implementation workflow
- **Software-development context:** Implementation and PR-review requests in
  which the author reports repeated file searching despite a stated plan or
  clear review request
- **Relevant RQ/domain:** Q1, Q4, Q5; planning, context use, and executor
  behavior
- **Neutral observation:** The author reports canceling runs after unexpected
  file searches and reports token expenditure before cancellation.
- **Source-context note:** The source records a specific version and platform
  but provides no independent trace of the searches.
- **Directness:** direct
- **Uncertainty:** Self-report; the author's assessment that the searches were
  unnecessary is contextual and not independently evaluated.
- **Coding/extraction status:** pilot captured — not coded

### P-GH-CLAUDE-002

- **Platform/source:** GitHub, Claude Code repository
- **Source type:** Feature request / documented workflow report
- **Original public URL:** https://github.com/anthropics/claude-code/issues/18027
- **Publication date:** 2026-01-13
- **Capture date:** 2026-08-24
- **Tool/ecosystem context:** Claude Code with plan mode, subagents, context
  monitoring, and a user-created continuation workflow
- **Software-development context:** A reported implementation of 19 API
  handlers using a main orchestration context and isolated agent work
- **Relevant RQ/domain:** Q3, Q4, Q5, Q6, Q8; context boundaries, planning, and
  handoff
- **Neutral observation:** The author describes keeping plans and summaries in
  the main context while delegating implementation and reports completing the
  example work without the proposed context handoff being needed.
- **Source-context note:** This is a self-authored feature proposal and
  workflow report; reported quality and context figures are not independently
  verified.
- **Directness:** direct
- **Uncertainty:** One workflow report cannot establish reliability or compare
  the approach with alternatives.
- **Coding/extraction status:** pilot captured — not coded

### P-GH-CLAUDE-003

- **Platform/source:** GitHub, Claude Code repository
- **Source type:** Feature request / practitioner report
- **Original public URL:** https://github.com/anthropics/claude-code/issues/80751
- **Publication date:** 2026-07-24
- **Capture date:** 2026-08-24
- **Tool/ecosystem context:** Claude Code long-running development sessions
- **Software-development context:** Accumulated conversation history, loaded
  source code, and project context across a multi-day project
- **Relevant RQ/domain:** Q1, Q2, Q4, Q6, Q8; context management and continuity
- **Neutral observation:** The author reports that manually starting a new
  session or summarizing and copying selected context reduces accumulated
  context but interrupts the workflow and can lose project context.
- **Source-context note:** Feature proposal based on a first-person workflow;
  no usage measurements are supplied.
- **Directness:** direct
- **Uncertainty:** The report does not establish how often the problem occurs or
  whether retrieval would preserve the relevant details.
- **Coding/extraction status:** pilot captured — not coded

### P-GH-CODEX-001

- **Platform/source:** GitHub, OpenAI Codex repository
- **Source type:** Bug report / user-reported problem
- **Original public URL:** https://github.com/openai/codex/issues/36712
- **Publication date:** 2026-08-03
- **Capture date:** 2026-08-24
- **Tool/ecosystem context:** Codex CLI version 0.146.0
- **Software-development context:** A large multi-step coding task after
  automatic context compaction
- **Relevant RQ/domain:** Q1, Q2, Q6, Q8; continuity and context management
- **Neutral observation:** The author reports that compaction sometimes left the
  agent unable to continue the task, requiring a new conversation and
  reconstruction of prior work.
- **Source-context note:** The issue includes environment diagnostics and a
  reproduction outline, but not an independently captured session trace.
- **Directness:** direct
- **Uncertainty:** Frequency and mechanism are unresolved; the report is one
  account from one version and setting.
- **Coding/extraction status:** pilot captured — not coded

### P-GH-CODEX-002

- **Platform/source:** GitHub, OpenAI Codex repository
- **Source type:** Bug report / user-reported problem
- **Original public URL:** https://github.com/openai/codex/issues/40326
- **Publication date:** 2026-08-24
- **Capture date:** 2026-08-24
- **Tool/ecosystem context:** Codex desktop application, version 26.818.41509
- **Software-development context:** A long iterative coding workflow with
  screenshots, repository context, and step-by-step implementation guidance
- **Relevant RQ/domain:** Q1, Q2, Q6, Q8; context continuity and task state
- **Neutral observation:** The author reports repeated context compaction or
  reconnection that disrupted continuity and required reconstruction of the
  active task and completed work.
- **Source-context note:** Newly published issue with a concise first-person
  account and reproduction steps.
- **Directness:** direct
- **Uncertainty:** No independent reproduction or outcome trace is available.
- **Coding/extraction status:** pilot captured — not coded

## Pilot Boundary

The eight records above are a controlled pilot, not a thematic sample. No
recurrence count, cross-tool comparison, or favorable/unfavorable synthesis is
reported. Reddit, Cursor, OpenCode, Aider outside the captured repository
issues, OpenSpec, and Spec Kit remain eligible but were not forced into this
pilot.
