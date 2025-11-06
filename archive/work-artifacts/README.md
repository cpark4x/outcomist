# Work Artifacts Archive

This folder contains analysis documents, design explorations, and working documents from the development process. These files were used during development but are not part of the core product documentation.

---

## Nov 5, 2025 - Shared Prompts & Redesign

### `nov5-shared-prompts/`
**Context**: Created shared prompt library to eliminate drift between web app and CLI

**Files**:
- `CLI_PROMPT_EVALUATION.md` - Side-by-side scoring of old vs new prompts (71% improvement)
- `CLI_CHANGES_CRITIQUE.md` - Devil's advocate analysis of potential negatives
- `FINAL_SHARED_PROMPTS_VALIDATION.md` - Validation of architecture
- `SHARED_PROMPTS_TEST_REPORT.md` - Test results after implementation
- `KEN_FEEDBACK_INCORPORATION.md` - Analysis of which Test #9 feedback was incorporated

**Outcome**: Successfully created `outcomist_shared/prompts.py` as single source of truth

### `nov5-redesign/`
**Context**: Web app UI redesign and launch

**Files**:
- `REDESIGN_SUMMARY.md` - Summary of redesign decisions
- `.design/specs/outcomist-redesign-2025-11-05.md` - Design spec
- `frontend-explorations/` - Design option mockups and explorations
  - `demo.html` - Demo version
  - `design-options.html` - Design explorations
  - `mockup-comparison.html` - Comparison views
  - `option-b-refined.html` - Refined option B
  - `icons.js` - Icon explorations

**Outcome**: Beautiful minimal UI launched (Apple-inspired, SSE streaming)

---

## Purpose

These artifacts document **how decisions were made** and **what was explored**, which is valuable for:
- Understanding design rationale
- Avoiding repeating past explorations
- Learning from analysis approaches
- Documenting the development journey

They are **not** part of the core product but provide valuable context for anyone understanding the evolution of the system.
