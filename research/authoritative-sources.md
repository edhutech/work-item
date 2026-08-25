# Standards And Authoritative Sources

## Stream Protocol

This is the Protocol v1.1 **Standards and Authoritative Sources** evidence
stream. It is epistemically distinct from scientific, coding-agent-specific,
and practitioner evidence. Its purpose is to identify recognized terminology,
process concerns, quality concepts, and evaluation language. Inclusion does
not mean that a source supports a Work Item characteristic, improves coding-
agent performance, or establishes a causal effect.

This inventory is independent of academic-database calibration. It does not
deduplicate or screen academic records. Initial capture establishes source
identity, status, relevance, access boundary, and provenance only. Full source
extraction and any later transfer analysis remain pending.

## Eligible Classes

- **Normative standard:** Published standards containing requirements,
  provisions, or normative guidance issued through a recognized standards
  process.
- **Body of knowledge:** A recognized professional synthesis describing the
  scope and generally accepted knowledge of a discipline. It is not itself a
  normative standard or empirical study.
- **Official guidance:** Guidance or methodology published by a recognized
  standards or professional body, without assuming that all guidance is
  mandatory or universally applicable.
- **Terminology/reference source:** An official vocabulary, reference model, or
  classification whose primary role is shared terminology.
- **Contextual official documentation:** Official organizational documentation
  retained only when it directly informs a documented research domain; an
  official vendor or product page is not authoritative evidence merely because
  it is official.

## Source Interpretation

Classes are not a numerical quality ranking. A normative standard can define
requirements without showing that they improve an outcome. A body of knowledge
can summarize consensus-oriented knowledge without being a causal evaluation.
Guidance and reference sources can clarify concepts without establishing
universal practice. Each later use must state the source class, intended claim,
context, and limitations.

## Relevance Domains

The following are capture and mapping domains, not predetermined Work Item
characteristics:

- requirements and specification quality;
- completeness, ambiguity, and traceability;
- verification, validation, testing, and acceptance;
- task/work decomposition and software engineering process;
- information and software quality;
- change management and software maintenance;
- software engineering terminology and professional practice.

## Public Access And Copyright Boundary

The public repository stores only source metadata, official URLs, short
original-language relevance notes, provenance, and access/copyright decisions.
It does not store ISO or IEEE standards PDFs, licensed full text, copyrighted
tables, long definitions, or copied clauses. ISO's official copyright page
states that ISO online content and publications are copyright-protected and
that reproduction requires permission. The official SWEBOK terms state that
the guide may not be publicly posted, shared, or distributed; limited
reasonable passages may be quoted in scholarly or educational material with
citation. These terms control the repository boundary. Public metadata or a
public landing page is not treated as permission to redistribute the document.

## Record Model

Each inventory record contains:

- `source_id`, stable within this stream;
- title, issuing organization, class, identifier, and edition/version/year;
- official URL and provenance-capture date;
- access status and copyright/publication note;
- relevant research questions and domains;
- inclusion reason and evidence-use boundary;
- current/superseded status and predecessor/successor links;
- unresolved status/version questions.

Future extracted observations receive separate evidence IDs and retain the
source ID, official locator, normative/descriptive status, context, transfer
limitations, and extraction status. The inventory record is never overwritten
by later interpretation.

## Initial Inventory

### AUTH-ISO-IEC-IEEE-29148-2018

- **Source:** ISO/IEC/IEEE 29148:2018, *Systems and software engineering —
  Life cycle processes — Requirements engineering*
- **Issuing organization:** ISO, IEC, and IEEE
- **Source class:** Normative standard
- **Edition/version/year:** Edition 2, 2018-11
- **Current status:** ISO records the 2018 edition as published and last
  reviewed/confirmed in 2024, with the version remaining current. The same
  record marks it `90.92 — To be revised` and identifies a DIS 29148 successor
  under development. ISO/IEC/IEEE 29148:2011 is recorded as withdrawn.
- **Official provenance:** [ISO standard record](https://www.iso.org/standard/72089.html);
  [IEEE SA standard record](https://standards.ieee.org/standard/29148-2018.html)
- **Access status:** Public metadata, abstract, and preview information;
  complete standard is sold or subscription-accessed.
- **Research relevance:** Requirements engineering, requirements information
  items, requirements-related process, specification, requirements quality,
  and lifecycle context. Mapped provisionally to Q1, Q2, Q3, Q5, Q6, and Q8,
  and domains `requirements/specification`, `completeness/ambiguity`, and
  `traceability`.
- **Reason for inclusion:** Directly within the protocol's identified
  requirements-engineering authoritative-source scope.
- **Redistribution boundary:** Metadata and short original research notes only;
  no standard text, clauses, tables, or PDF.
- **Evidence-use boundary:** Normative reference for what the standard
  specifies or guides in its stated context; not empirical proof and not a
  coding-agent evaluation.
- **Version relationship:** Predecessor `ISO/IEC/IEEE 29148:2011` withdrawn;
  successor/revision status is under development and must be rechecked before
  later extraction.
- **Capture date:** 2026-08-24

### AUTH-SWEBOK-4.0A

- **Source:** *Guide to the Software Engineering Body of Knowledge (SWEBOK
  Guide), Version 4.0a*
- **Issuing organization:** IEEE Computer Society
- **Source class:** Body of knowledge
- **Edition/version/year:** V4.0 base citation identifies 2024; the official
  page reports a 2025-09-25 minor-revision update identified as V4.0a.
- **Current status:** Official IEEE Computer Society pages identify V4.0a as
  the newest edition. The public page also describes a future Version 5
  development/review activity; this is not treated as a current replacement.
- **Official provenance:** [SWEBOK official overview](https://www.computer.org/education/bodies-of-knowledge/software-engineering);
  [official V4 download page](https://www.computer.org/education/bodies-of-knowledge/software-engineering/v4)
- **Access status:** Public overview and download workflow; guide use is
  subject to the official individual non-commercial license.
- **Research relevance:** Software requirements, software quality, testing,
  maintenance, configuration management, software engineering process, and
  professional practice. Mapped provisionally to Q0, Q1, Q3, Q5, Q6, Q7, and
  Q8, and the corresponding relevance domains.
- **Reason for inclusion:** Recognized professional body of knowledge directly
  covering the software-engineering domains in the research plan.
- **Redistribution boundary:** No guide PDF or substantial text is stored.
  Official terms prohibit public posting/sharing/distribution; only minimal,
  legally reviewed quotations with citation could be considered later.
- **Evidence-use boundary:** Describes consensus-oriented professional
  knowledge and topical scope; it is not a normative standard, empirical proof,
  or coding-agent performance evaluation.
- **Version relationship:** V4.0a is the current minor-revision form of V4.0;
  V3 and earlier editions remain historical references only unless a later
  review establishes a specific reason to use them.
- **Capture date:** 2026-08-24

### AUTH-ISO-IEC-25010-2023

- **Source:** ISO/IEC 25010:2023, *Systems and software engineering — Systems
  and software Quality Requirements and Evaluation (SQuaRE) — Product quality
  model*
- **Issuing organization:** ISO and IEC
- **Source class:** Normative standard
- **Edition/version/year:** Edition 2, 2023-11
- **Current status:** ISO records the 2023 edition as published. ISO/IEC
  25010:2011 is withdrawn and the ISO record identifies the 2023 edition as a
  revised replacement within the related SQuaRE series.
- **Official provenance:** [ISO standard record](https://www.iso.org/standard/78176.html);
  [withdrawn 2011 record](https://www.iso.org/standard/35733.html)
- **Access status:** Public metadata, abstract, and preview information;
  complete standard is sold or subscription-accessed.
- **Research relevance:** Product quality model, quality requirements,
  specification, measurement, evaluation, testing objectives, acceptance
  criteria, and quality-control context. Mapped provisionally to Q1, Q2, Q3,
  Q4, Q6, and Q8, and domains `software quality`, `verification/validation`,
  and `acceptance`.
- **Reason for inclusion:** Directly addresses quality requirements and
  evaluation concepts listed in the research plan and protocol.
- **Redistribution boundary:** Metadata and short original research notes only;
  no standard text, clauses, tables, or PDF.
- **Evidence-use boundary:** Normative quality-model reference in its stated
  product-quality context; not empirical proof, a task prescription, or a
  coding-agent evaluation.
- **Version relationship:** `ISO/IEC 25010:2011` withdrawn; current record is
  the 2023 edition. Historical 2011 material is not treated as current.
- **Capture date:** 2026-08-24

## Initial Capture Outcome

- **Sources captured:** 3
- **Sources rejected:** None
- **Sources deferred:** No additional source was added merely to enlarge the
  inventory. Candidate standards on lifecycle management, maintenance,
  measurement, and testing remain deferred until a concrete research-domain
  need is documented.
- **Unresolved questions:** The future 29148 revision's final publication and
  replacement status require rechecking before relying on it as current. The
  precise V4.0a publication/update date beyond the official 2025-09-25 notice
  is not asserted here. No claim is made about transferability to coding-agent
  execution.

## Transfer Boundary

Traditional software-engineering authority does not automatically transfer to
coding agents. Any later transfer analysis must separately consider executor,
available context, interaction model, autonomy, repository/tool access, task
environment, evaluation criteria, and technological limitations. This initial
capture performs none of that analysis.

## Pending Extraction And Synthesis

No clause-level evidence extraction, quality assessment, cross-stream
synthesis, Evidence Matrix conclusion, Work Item characteristic, or hypothesis
was created by this inventory.
