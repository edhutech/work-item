# Agent Instructions

## Repository Scope

- This is a documentation-only research repository; there is currently no application code, package manager, test suite, formatter, linter, CI workflow, or build command.
- `README.md` gives the project context. `research-plan.md` is the detailed research process and is written in Spanish; preserve its methodological intent when editing related material.

## Research Constraints

- Keep the research in vanilla coding-agent workflows: do not introduce Nerv, OpenSpec, an SDD framework, persistent agent memory, or another work-structuring layer unless the research explicitly changes this constraint.
- Treat the Work Item definition and example characteristics in `research-plan.md` as provisional, not established conclusions.
- Seek evidence both supporting and contradicting candidate characteristics; do not write conclusions merely because a property seems intuitive.
- Keep claims tied to their evidence and distinguish scientific literature, standards, practitioner reports, and empirical alpha data rather than treating them as equivalent.

## Change Guidance

- There are no repository-local development or verification commands yet. For documentation-only changes, verify links and internal consistency manually.
- Keep additions focused on the research questions, evidence, operationalization, and validation described by `research-plan.md`; avoid adding product implementation assumptions before the research supports them.

## Git

* Keep commits small and limited to one logical research change.
* Use Conventional Commits: `type(scope): subject`.
* Prefer `research` for new findings, evidence synthesis, or research outputs; `docs` for documentation-only edits; and `chore` for repository maintenance.
* Write commit subjects in imperative, lowercase form and keep them concise.
* Do not combine unrelated research findings, structural changes, and documentation cleanup in the same commit.
* Before committing, review the diff to ensure claims, citations, and research artifacts changed only as intended.
