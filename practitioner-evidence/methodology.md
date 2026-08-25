# Practitioner Evidence Methodology

## Protocol

This artifact establishes the initial **Practitioner Evidence** stream under
Research Protocol v1.1. Practitioner material is qualitative complementary
evidence. It can document experiences, observations, practices, friction,
workarounds, trade-offs, and contextual boundaries, but it does not establish
prevalence, causal effect, or equivalence with scientific evidence.

Practitioner records remain separate from scientific, authoritative, and
coding-agent-specific empirical evidence. They are not entered into the
Evidence Matrix as conclusions. The initial capture is a format and sampling
pilot; no themes, recurrence claims, hypotheses, or Work Item characteristics
are derived here.

## Eligible Sources

Eligible public sources include GitHub Issues and Discussions, Reddit, Hacker
News, public developer forums, official public tool discussions, public project
discussions, and documented developer-experience reports. Relevant tool
ecosystems may include Codex, Claude Code, Cursor, OpenCode, Aider, OpenSpec,
Spec Kit, and comparable tools when the record contains relevant experience.
Product mention alone is not an eligibility reason.

A record is eligible when its public source has identifiable context and
contains at least one experience, observation, behavior, friction, workaround,
failure mode, need, trade-off, or boundary relevant to a research question or
documented in-scope domain. Likes, stars, upvotes, reposts, and promotional
claims are not evidence of validity, recurrence, prevalence, or causation.

## Initial Sampling Strategy

The pilot uses purposive maximum-variation sampling rather than popularity
sampling. Search and selection are recorded by source context, date, tool or
ecosystem, software-development setting, and directness to coding-agent
execution. Selection seeks both favorable and unfavorable experiences and does
not require every named platform to be represented.

The initial frame is:

- one small set of high-relevance public GitHub records from Aider, Claude Code,
  and Codex repositories;
- one small set of high-relevance public Hacker News records;
- Reddit and other communities retained as eligible frames but not forced into
  the pilot when public access or context quality is insufficient;
- records spanning context management, task decomposition or planning,
  information supplied to the agent, continuity, and human review/workflow;
- both problem reports and reports describing a workflow that the author says
  worked, while retaining self-report and selection limitations.

The pilot does not target a quota. A candidate is deferred rather than included
when its context is too thin, its text is primarily promotional, or its public
availability cannot be preserved. Capture date for this pilot is `2026-08-24`.

## Source Record Model

Each record uses these fields:

- **Practitioner Source ID:** Stable ID prefixed `P-` and unique within this
  stream.
- **Platform/source:** Public platform and project or community context.
- **Source type:** Issue, discussion, self-report, experience report, or other
  descriptive type.
- **Original public URL:** Canonical source URL, not an API or search URL.
- **Publication date:** Date shown by the source, when available.
- **Capture date:** Date the record entered this repository.
- **Tool/ecosystem context:** Tool, repository, model, or workflow context
  stated by the source; unknown fields remain unknown.
- **Software-development context:** Task, repository, workflow, or failure
  setting described by the source.
- **Relevant RQ/domain:** Provisional mapping to the research questions or
  domains, not a coded finding.
- **Neutral observation:** Researcher-written paraphrase limited to what the
  source reports.
- **Source-context note:** Directness, self-report status, version information,
  and other context needed to interpret the observation.
- **Directness:** `direct`, `indirect`, or `unclear` relation to coding-agent
  execution.
- **Uncertainty:** Missing context, self-report limits, unverifiable metrics,
  possible duplication, or other limitations.
- **Coding/extraction status:** `pilot captured — not coded` until a later
  approved analysis phase.

Personal names, usernames, demographics, institutions, and other identifying
details are not recorded unless a later methodological need justifies them.
The pilot stores no screenshots, emails, account identifiers, or private data.

## Copyright And Quotation Boundary

The repository stores canonical public URLs and concise researcher-written
paraphrases. It does not reproduce posts, comments, threads, screenshots, or
long excerpts. No direct quotations are used in the pilot. The source remains
the place to consult the original context, subject to availability and
platform terms.

## Limitations And Deferred Work

This pilot is not a representative sample and cannot support claims about how
often an experience occurs. Public-community sampling is exposed to selection,
self-reporting, moderation, survivorship, platform, and visibility biases.
The pilot has not assessed independence among records, recurrence across
authors, or the accuracy of reported metrics. Those questions are deferred to
later extraction and appraisal.

No cross-stream synthesis, thematic category system, Work Item characteristic,
final Evidence Matrix entry, or hypothesis is created by this artifact.
