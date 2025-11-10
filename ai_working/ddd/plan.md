# DDD Plan: Outcomist End-to-End User Flow (Explore → Design → Build)

## Problem Statement

**What we're solving**: Outcomist has a powerful decision exploration capability (Epics 1-2 shipped, validated), but the complete journey from "I have a decision" → "I understand it deeply" → "I have a solution design" → "I've built and tracked it" isn't fully documented.

**Why it matters**:
- AI assistant (Claude) needs to understand the complete vision to build each piece correctly
- Current "Stage/Tier" terminology is confusing - need clear Epic/Feature structure
- Missing documentation prevents aligned, incremental building toward the right destination

**User value**:
- **For user**: Complete decision-to-action journey with clear outcomes at each step
- **For AI**: Context to build features that fit the bigger picture
- **For product**: Roadmap from validated capabilities to future vision

## Proposed Solution

Create comprehensive end-to-end flow documentation structured as **Epics** (major user capabilities) and **Features** (specific functionality), covering:

1. **Epic 1-2**: Pattern Recognition & Discovery (✅ **VALIDATED** - shipped and working)
2. **Epic 3**: Deep Analysis & Alternatives (⏳ **PROPOSED** - planned, not built)
3. **Epic 4**: Design & Specification (⏳ **PROPOSED** - visioned, not defined)
4. **Epic 5**: Build & Track (⏳ **PROPOSED** - visioned, not defined)

Each epic will document:
- **User story**: What user can accomplish
- **Outcome**: What they walk away with
- **Principles**: What makes it work well
- **Flow**: How it unfolds (high-level)
- **Features**: Specific capabilities

## Alternatives Considered

### Alternative 1: Just Finish Explore Stage (Epics 1-3 only)
**Approach**: Document only decision exploration epics, leave Design/Build for later

**Why not chosen**: User explicitly wants to see "the big picture" including Design and Build stages to ensure each smaller step is built correctly toward the complete vision.

### Alternative 2: Incremental Documentation (Phase by Phase)
**Approach**: Complete one epic fully before planning the next

**Why not chosen**: Doesn't give AI the complete context needed to build intermediate steps correctly. Misses connections between epics that inform earlier decisions.

### Alternative 3: Full Three-Stage Journey ✓ CHOSEN
**Approach**: Document complete Explore → Design → Build journey as Epics 1-5

**Why chosen**:
- Aligns with user's explicit request: "I want you to see the big picture"
- Provides AI with vision context for building each piece
- Epic 1-2 validated, Epic 3-5 high-level (directional not prescriptive)
- Matches product vision: "Three-stage decision journey"
- Enables roadmap planning

## Architecture & Design

### Epic Structure

```
OUTCOMIST: DECISION TO ACTION JOURNEY

Epic 1: Pattern Recognition & Quick Insight (✅ VALIDATED)
├─ Feature 1.1: Bring a decision
├─ Feature 1.2: Pattern detection (9 patterns)
├─ Feature 1.3: Reframing preview
└─ Feature 1.4: Intent checking (validate vs execute)

Epic 2: Discovery & Understanding (✅ VALIDATED)
├─ Feature 2.1: Adaptive questioning (Round 1)
├─ Feature 2.2: Evidence gathering ("Show me")
├─ Feature 2.3: Pattern synthesis & analysis
├─ Feature 2.4: Targeted follow-up (Round 2)
├─ Feature 2.5: Summary & confirmation
└─ Feature 2.6: Personalized recommendation

Epic 3: Deep Analysis & Alternatives (⏳ PROPOSED)
├─ Feature 3.1: Option generation & comparison
├─ Feature 3.2: Risk assessment
├─ Feature 3.3: Scenario planning
├─ Feature 3.4: Trade-off analysis
└─ Feature 3.5: Decision criteria refinement

Epic 4: Design & Specification (⏳ PROPOSED)
├─ Feature 4.1: Solution wireframing
├─ Feature 4.2: Specification generation
├─ Feature 4.3: Prototype creation
├─ Feature 4.4: Validation & feedback
└─ Feature 4.5: Refinement iteration

Epic 5: Build & Track (⏳ PROPOSED)
├─ Feature 5.1: Task breakdown
├─ Feature 5.2: Execution tracking
├─ Feature 5.3: Blocker handling
├─ Feature 5.4: Outcome measurement
└─ Feature 5.5: Learning capture
```

### Key Interfaces (The "Studs")

**Between Epics**:
1. **Epic 1 → Epic 2**: Decision statement + identified pattern + user intent
2. **Epic 2 → Epic 3**: Discovery insights + constraints + user priorities
3. **Epic 3 → Epic 4**: Chosen direction + criteria + trade-offs understood
4. **Epic 4 → Epic 5**: Solution design + specifications + success criteria
5. **Epic 5 → Learning**: Outcomes + blockers encountered + lessons learned

**Key data structures flowing through**:
- **Session**: Persists conversation, user answers, analysis, recommendations
- **Pattern**: Identified deeper issue, reframe, relevant questions
- **Insights**: Discoveries from questioning (constraints, priorities, evidence)
- **Options**: Alternatives analyzed with pros/cons/risks
- **Design**: Wireframes, specs, prototypes
- **Plan**: Tasks, milestones, success metrics

### Module Boundaries

**Current modules** (Epics 1-2):
- `ExplorationEngine`: Orchestrates Epics 1-2 (pattern recognition, discovery)
- `SessionStorage`: Persists session state across epics
- `Prompts`: System prompts for each epic feature (single source of truth)
- `Routes`: API endpoints for streaming interactions
- `Frontend`: Minimal UI for chat-based interaction

**Future modules** (Epics 3-5):
- `AnalysisEngine`: Orchestrates Epic 3 (deep analysis, alternatives)
- `DesignEngine`: Orchestrates Epic 4 (wireframing, specs, prototypes)
- `BuildEngine`: Orchestrates Epic 5 (execution tracking, blockers)
- Each engine follows same pattern: streaming, session-based, adaptive

**Shared infrastructure**:
- Same web stack (FastAPI + vanilla JS + SSE streaming)
- Same storage pattern (JSON session persistence)
- Same prompt library pattern (outcomist_shared/prompts.py)

### Data Models

**Session** (extends across all epics):
```python
{
  "id": "session_id",
  "decision_statement": "original user input",
  "current_epic": 1-5,
  "conversation": [Message],
  "pattern": Pattern | None,
  "insights": Insights | None,
  "analysis": Analysis | None,
  "design": Design | None,
  "plan": Plan | None,
  "completed_epics": [1, 2, ...]
}
```

**Pattern** (Epic 1 output):
```python
{
  "type": "Pattern name",
  "reframe": "Deeper question revealed",
  "preview": "What we'd explore in Epic 2"
}
```

**Insights** (Epic 2 output):
```python
{
  "answers": {"question": "answer", ...},
  "evidence": ["fact 1", "fact 2", ...],
  "constraints": ["constraint 1", ...],
  "priorities": ["priority 1", ...],
  "recommendation": "specific advice"
}
```

**Analysis** (Epic 3 output):
```python
{
  "options": [Option],
  "risks": [Risk],
  "scenarios": [Scenario],
  "trade_offs": [TradeOff]
}
```

**Design** (Epic 4 output):
```python
{
  "wireframes": [Image/Sketch],
  "specs": [Specification],
  "prototypes": [Prototype],
  "success_criteria": ["criterion 1", ...]
}
```

**Plan** (Epic 5 output):
```python
{
  "tasks": [Task],
  "milestones": [Milestone],
  "blockers": [Blocker],
  "outcomes": [Outcome]
}
```

## Files to Create/Update

### Non-Code Files (Phase 2: Documentation)

#### New Documentation Files

- [ ] **docs/vision/end-to-end-flow.md** - Complete Epic 1-5 flow documentation (PRIMARY DELIVERABLE)
  - Epic structure overview
  - User stories for each epic
  - Outcomes and principles
  - High-level flows
  - Feature breakdown

- [ ] **docs/epics/epic-1-pattern-recognition.md** - Epic 1 detailed documentation
  - User story: "Bring a decision, get immediate pattern recognition"
  - Features 1.1-1.4 detailed
  - Current implementation status (validated)

- [ ] **docs/epics/epic-2-discovery.md** - Epic 2 detailed documentation
  - User story: "Explore decision through guided questions"
  - Features 2.1-2.6 detailed
  - Current implementation status (validated)

- [ ] **docs/epics/epic-3-deep-analysis.md** - Epic 3 proposed documentation
  - User story: "Analyze options, risks, scenarios"
  - Features 3.1-3.5 proposed
  - Implementation roadmap

- [ ] **docs/epics/epic-4-design.md** - Epic 4 proposed documentation
  - User story: "Design solution before building"
  - Features 4.1-4.5 proposed
  - Integration with Epic 3

- [ ] **docs/epics/epic-5-build.md** - Epic 5 proposed documentation
  - User story: "Execute and track implementation"
  - Features 5.1-5.5 proposed
  - Integration with Epic 4

- [ ] **docs/principles/epic-transitions.md** - How users move between epics
  - Decision points (when to proceed vs stop)
  - Information flow (what carries forward)
  - User agency (choice at each stage)

#### Updated Documentation Files

- [ ] **docs/vision/product-vision.md** - Update to use Epic terminology
  - Replace "Stage/Tier" with "Epic/Feature"
  - Clarify validated vs proposed epics
  - Add roadmap section

- [ ] **docs/principles/progressive-disclosure.md** - Reframe with Epic structure
  - Map old Tier 1-4 to Epic 1-3
  - Explain Epic 1 (quick) → Epic 3 (comprehensive)
  - Update decision flow diagram

- [ ] **README.md** - Update with Epic structure
  - Epic 1-2: Available now
  - Epic 3-5: Coming soon
  - Clear roadmap

- [ ] **MUST_HAVES.md** - Verify against Epic structure
  - Ensure must-haves span all epics
  - Add any missing principles

### Code Files (Phase 4: Implementation)

**Note**: This plan focuses on *documentation*. Code changes for Epic 3-5 will be planned separately when we start implementing.

**Potential code structure** (for context):

- [ ] **outcomist_web/backend/analysis_engine.py** - NEW: Epic 3 orchestration
  - Option generation
  - Risk assessment
  - Scenario planning

- [ ] **outcomist_web/backend/design_engine.py** - NEW: Epic 4 orchestration
  - Wireframe generation
  - Spec creation
  - Prototype handling

- [ ] **outcomist_web/backend/build_engine.py** - NEW: Epic 5 orchestration
  - Task breakdown
  - Execution tracking
  - Outcome measurement

- [ ] **outcomist_shared/prompts.py** - UPDATE: Add Epic 3-5 prompts
  - Epic 3 system prompts
  - Epic 4 system prompts
  - Epic 5 system prompts

- [ ] **outcomist_web/backend/models.py** - UPDATE: Add Epic 3-5 data models
  - Analysis, Design, Plan models
  - Extend Session model

- [ ] **outcomist_web/backend/routes.py** - UPDATE: Add Epic 3-5 endpoints
  - /api/sessions/{id}/analyze
  - /api/sessions/{id}/design
  - /api/sessions/{id}/build

## Philosophy Alignment

### Ruthless Simplicity

**Start minimal**:
- Epic 1-2 exist and work → document what's validated
- Epic 3-5 proposed → high-level user stories, not detailed specs
- Don't over-plan what we haven't validated

**Avoid future-proofing**:
- Epic 3-5 documentation is *directional*, not *prescriptive*
- We'll refine as we build and learn
- Keep it flexible for discovery

**Clear over clever**:
- Use plain "Epic/Feature" instead of abstract "Stage/Tier"
- User stories focus on outcomes, not implementation
- Principles guide without constraining

**What we're NOT building yet**:
- Detailed Epic 3-5 implementations
- Complex workflows we haven't validated
- Features that assume too much

### Modular Design

**Bricks (self-contained modules)**:
- Each Epic is a module that can be built/improved independently
- Epic 1-2 already modular (ExplorationEngine, SessionStorage, Prompts)
- Epic 3-5 will follow same pattern (AnalysisEngine, DesignEngine, BuildEngine)

**Studs (clear interfaces)**:
- Session state persists across epics (clear data contract)
- Each epic outputs specific artifacts (Pattern, Insights, Analysis, Design, Plan)
- Epics can be enhanced without breaking others

**Regeneratable**:
- Each epic can be rebuilt from its spec
- Engines follow consistent pattern (streaming, adaptive, session-based)
- Prompts in single source of truth (outcomist_shared/prompts.py)

### Progressive Disclosure Architecture

This is core to Outcomist's design philosophy:

**Match complexity to decision needs**:
- Epic 1: 30 seconds - Quick pattern recognition
- Epic 2: 5-10 minutes - Structured discovery
- Epic 3: 20-30 minutes - Deep analysis (future)
- Epic 4: Variable - Solution design (future)
- Epic 5: Ongoing - Execution tracking (future)

**User chooses depth**:
- After Epic 1: Continue to Epic 2 or stop
- After Epic 2: Continue to Epic 3 or act on recommendation
- After Epic 3: Continue to Epic 4 or decide without design
- After Epic 4: Continue to Epic 5 or build on your own
- User agency at every transition

**Start simple, go deeper only if needed**:
- Don't force users through all 5 epics
- Most decisions resolved at Epic 2
- Epic 3-5 for complex, high-stakes decisions
- This is the entire product philosophy

## User Flow Documentation Structure

### Primary Documentation: docs/vision/end-to-end-flow.md

**Purpose**: Give AI (and team) complete vision so each piece is built correctly

**Structure**:
```markdown
# Outcomist: Decision to Action Journey

## The Big Picture
- Three phases: Explore (Epics 1-3) → Design (Epic 4) → Build (Epic 5)
- Progressive disclosure: match complexity to needs
- User agency: choose depth at each transition

## Epic 1: Pattern Recognition & Quick Insight (✅ VALIDATED)
### User Story
"As a decision-maker, I bring a decision statement and immediately see the deeper pattern I'm actually facing, so I understand what I'm really deciding."

### Outcome
- User sees their decision reframed
- Understands the underlying pattern
- Previews what deeper exploration would uncover
- Decides: validate the reframe or explore deeper

### Principles
- Speed: 30 seconds or less
- Insight: Reveal non-obvious patterns
- Agency: User chooses next step
- Transparency: Show reasoning

### Flow
1. User inputs decision statement
2. System detects pattern using 9 documented patterns
3. System reframes question to reveal real issue
4. System previews what Epic 2 would explore
5. User chooses: Continue to Epic 2 or stop

### Features
- 1.1: Decision input
- 1.2: Pattern detection (9 patterns)
- 1.3: Reframing & preview
- 1.4: Intent checking

### Current Status
✅ Shipped, validated across 13 test scenarios

---

## Epic 2: Discovery & Understanding (✅ VALIDATED)
### User Story
"As a decision-maker, I explore my decision through adaptive questions that uncover constraints, priorities, and evidence, so I get a personalized recommendation grounded in my actual situation."

### Outcome
- User discovers constraints they didn't articulate
- Priorities become clear through trade-offs
- Evidence gathered (facts verified)
- Specific recommendation tailored to their situation

### Principles
- Adaptive: Questions based on answers
- Evidence-based: "Show me" questions verify facts
- Progressive: Start broad, then targeted
- Transparent: Show reasoning for recommendation

### Flow
1. System asks 2-3 high-level questions (Round 1)
2. User answers, system gathers evidence
3. System synthesizes patterns, shows analysis
4. System asks targeted follow-up (Round 2)
5. User answers
6. System generates summary, user confirms
7. System delivers personalized recommendation

### Features
- 2.1: Adaptive questioning (Round 1)
- 2.2: Evidence gathering ("Show me")
- 2.3: Pattern synthesis & analysis
- 2.4: Targeted follow-up (Round 2)
- 2.5: Summary & confirmation
- 2.6: Personalized recommendation

### Current Status
✅ Shipped, validated across 13 test scenarios

---

## Epic 3: Deep Analysis & Alternatives (⏳ PROPOSED)
### User Story
"As a decision-maker facing a complex choice, I want to systematically explore alternatives, assess risks, and plan scenarios, so I can choose confidently even with uncertainty."

### Outcome
- Multiple options clearly compared
- Risks identified and assessed
- Scenarios planned (best/worst/likely)
- Decision criteria refined
- Clear recommendation with rationale

### Principles
- Systematic: Structured option comparison
- Risk-aware: Surface and assess uncertainties
- Scenario-based: Plan for multiple futures
- Criteria-driven: Help user define what matters

### Flow (HIGH-LEVEL)
1. System generates 3-5 viable options from Epic 2 insights
2. User reviews options, adds/removes as needed
3. System facilitates option comparison across criteria
4. System identifies risks for each option
5. System facilitates scenario planning
6. User clarifies decision criteria
7. System recommends option with full rationale

### Features (PROPOSED)
- 3.1: Option generation & comparison
- 3.2: Risk assessment
- 3.3: Scenario planning (best/worst/likely)
- 3.4: Trade-off analysis
- 3.5: Decision criteria refinement

### Current Status
⏳ Planned, not implemented. Will design when Epic 1-2 documentation complete.

---

## Epic 4: Design & Specification (⏳ PROPOSED)
### User Story
"As a decision-maker who's chosen a direction, I want to design the solution (wireframes, specs, prototypes) before building, so I prevent 'building the wrong thing efficiently.'"

### Outcome
- Visual wireframes of solution
- Written specifications
- Testable prototype (if applicable)
- Validation feedback incorporated
- Clear success criteria

### Principles
- Design before build: Prevent costly mistakes
- Iterate quickly: Refine before committing
- Validate early: Get feedback on design
- Specify clearly: Reduce implementation ambiguity

### Flow (HIGH-LEVEL)
1. System helps user articulate solution vision
2. System generates initial wireframes/sketches
3. User refines, system adapts
4. System creates specifications
5. System generates prototype (if applicable)
6. User validates design
7. System incorporates feedback
8. Finalize design with success criteria

### Features (PROPOSED)
- 4.1: Solution wireframing
- 4.2: Specification generation
- 4.3: Prototype creation
- 4.4: Validation & feedback
- 4.5: Refinement iteration

### Current Status
⏳ Visioned, not designed. High-level concept only.

---

## Epic 5: Build & Track (⏳ PROPOSED)
### User Story
"As a decision-maker executing a solution, I want to track implementation, handle blockers, and measure outcomes, so I close the loop and learn from the entire decision-to-action journey."

### Outcome
- Clear task breakdown
- Execution progress visible
- Blockers identified and addressed
- Outcomes measured against criteria
- Lessons captured for future decisions

### Principles
- Track progress: Visibility into execution
- Handle blockers: Don't get stuck
- Measure outcomes: Did it work?
- Capture learning: Close the loop

### Flow (HIGH-LEVEL)
1. System breaks design into actionable tasks
2. User executes, updates progress
3. System tracks completion
4. When blocked, system helps troubleshoot
5. System measures outcomes against success criteria
6. System captures lessons learned
7. Learning feeds back into pattern library

### Features (PROPOSED)
- 5.1: Task breakdown from design
- 5.2: Execution tracking
- 5.3: Blocker handling
- 5.4: Outcome measurement
- 5.5: Learning capture

### Current Status
⏳ Visioned, not designed. High-level concept only.

---

## Epic Transitions: User Agency & Information Flow

### Transition Points

**After Epic 1 (Pattern Recognition)**:
- **Decision**: Continue to Epic 2 or stop?
- **Why stop**: Pattern recognition alone gives clarity, no further exploration needed
- **Why continue**: Want to explore deeper, validate the reframe
- **What flows forward**: Decision statement, identified pattern, reframe

**After Epic 2 (Discovery)**:
- **Decision**: Act on recommendation, continue to Epic 3, or stop?
- **Why stop**: Recommendation is clear and actionable
- **Why continue to Epic 3**: Decision is complex, need deeper analysis
- **What flows forward**: Insights, constraints, priorities, recommendation

**After Epic 3 (Deep Analysis)**:
- **Decision**: Choose option and act, continue to Epic 4, or stop?
- **Why stop**: Option chosen, feel confident executing without design
- **Why continue to Epic 4**: Want to design solution before building
- **What flows forward**: Options analyzed, chosen direction, criteria, risks

**After Epic 4 (Design)**:
- **Decision**: Build on your own or continue to Epic 5?
- **Why stop**: Have design and specs, can execute independently
- **Why continue to Epic 5**: Want support tracking execution and measuring outcomes
- **What flows forward**: Wireframes, specs, prototypes, success criteria

**After Epic 5 (Build)**:
- **Completion**: Decision executed, outcomes measured, lessons captured
- **What flows forward**: Learning feeds back into pattern library for future users

### Key Principle: Progressive Disclosure

Most users resolve decisions at **Epic 2**.
Epic 3-5 are for complex, high-stakes decisions.

User chooses depth based on decision complexity and their needs.
System never forces unnecessary depth.

---

## Implementation Roadmap

### Completed (✅)
- Epic 1: Pattern Recognition (validated)
- Epic 2: Discovery (validated)
- Web implementation (FastAPI + SSE + vanilla JS)
- Session persistence
- Test scenarios and validation

### Next: Document Current State (Phase 2)
**Goal**: Complete Epic 1-2 documentation

**Deliverables**:
- docs/vision/end-to-end-flow.md (THIS STRUCTURE)
- docs/epics/epic-1-pattern-recognition.md
- docs/epics/epic-2-discovery.md
- Update docs/vision/product-vision.md (Epic terminology)
- Update docs/principles/progressive-disclosure.md (Epic structure)

**Timeline**: 1-2 sessions

### Future: Epic 3 (Deep Analysis)
**Goal**: Implement systematic alternatives exploration

**Prerequisites**:
- Epic 1-2 documentation complete
- Pattern library mature
- Test scenarios for complex decisions

**Key decisions to make**:
- How many options to generate?
- How to structure comparison?
- What risk assessment framework?
- How to facilitate scenario planning?

**Timeline**: TBD after Epic 1-2 docs complete

### Future: Epic 4 (Design)
**Goal**: Implement solution design before building

**Prerequisites**:
- Epic 3 complete and validated
- Understand types of decisions that need design phase
- Define what "design" means across decision types

**Key decisions to make**:
- What constitutes a "wireframe" for non-software decisions?
- How to generate specifications?
- What makes a good prototype?
- How to validate designs?

**Timeline**: TBD after Epic 3 shipped

### Future: Epic 5 (Build)
**Goal**: Implement execution tracking and outcome measurement

**Prerequisites**:
- Epic 4 complete and validated
- Understand execution patterns
- Define outcome measurement framework

**Key decisions to make**:
- How to break designs into tasks?
- What does "tracking" look like?
- How to help with blockers?
- How to measure success?

**Timeline**: TBD after Epic 4 shipped

---

## Open Questions (To Resolve As We Build)

### Epic 3 Questions
- How to generate alternatives systematically?
- What makes a good risk assessment?
- How detailed should scenario planning be?
- When is Epic 3 overkill vs necessary?

### Epic 4 Questions
- What does "design" mean for non-software decisions?
- How to make wireframing useful across decision types?
- When is prototyping valuable vs wasteful?
- How to validate designs effectively?

### Epic 5 Questions
- What granularity for task breakdown?
- How to handle blockers without becoming a PM tool?
- How to measure outcomes meaningfully?
- How to capture learning that helps future users?

### Cross-Epic Questions
- How to help users choose the right epic depth?
- What information should persist across epics?
- How to make transitions seamless?
- How to prevent "epic fatigue" (going too deep)?

---

## Success Criteria

### For This Documentation (Phase 2)

**Primary goal**: AI understands complete vision and can build each piece correctly

**Verification**:
- [ ] AI can explain all 5 epics
- [ ] AI can describe user journey end-to-end
- [ ] AI can articulate what's validated vs proposed
- [ ] AI can identify which epic a feature request belongs to
- [ ] AI can build Epic 1-2 features without breaking the bigger picture
- [ ] AI can propose Epic 3-5 features consistent with the vision

**Documentation quality**:
- [ ] User stories are clear and outcome-focused
- [ ] Principles are explicit and actionable
- [ ] Flows are understandable at high level
- [ ] Features are well-organized
- [ ] Transitions explain user agency
- [ ] Roadmap shows validated → proposed progression

### For Future Implementation (Phases Beyond This Plan)

**Epic 3 success**:
- Users can explore alternatives systematically
- Risk assessment adds value
- Scenario planning reduces uncertainty
- Users make more confident decisions

**Epic 4 success**:
- Users can design solutions before building
- Wireframes/specs reduce implementation errors
- Validation catches problems early
- Users feel confident in their design

**Epic 5 success**:
- Users can track execution effectively
- Blocker handling unblocks users
- Outcome measurement closes the loop
- Learning improves future decisions

---

## Next Steps

✅ **Phase 1 (Planning)** complete - this document

➡️ **Ready for Phase 2**: Update all non-code files (documentation)

**Run**: `/ddd:2-docs`

This plan will guide documentation updates to establish Epic 1-5 as the canonical structure for Outcomist's end-to-end flow.
```

This structure documents the complete Epic 1-5 flow at the right level of detail:
- Epic 1-2: Detailed (validated and working)
- Epic 3-5: High-level user stories (proposed, directional)
- Transitions: Clear user agency
- Roadmap: Validated → proposed progression

Each epic follows same template:
- User story (outcome-focused)
- Outcome (what user walks away with)
- Principles (what makes it work)
- Flow (high-level steps)
- Features (specific capabilities)
- Status (validated vs proposed)

### Individual Epic Files

Each epic will also have its own detailed markdown file in `docs/epics/`:

- `epic-1-pattern-recognition.md` - Deep dive on Epic 1
- `epic-2-discovery.md` - Deep dive on Epic 2
- `epic-3-deep-analysis.md` - Proposed Epic 3 design
- `epic-4-design.md` - Proposed Epic 4 vision
- `epic-5-build.md` - Proposed Epic 5 vision

These individual files provide additional detail, examples, and rationale for each epic.

### Other Supporting Documentation

- `docs/principles/epic-transitions.md` - Deep dive on how users move between epics
- Updated `docs/vision/product-vision.md` - Epic terminology throughout
- Updated `docs/principles/progressive-disclosure.md` - Mapped to Epic structure
- Updated `README.md` - Epic-based roadmap

This documentation gives you (and AI) the complete vision while clearly marking what's validated (Epic 1-2) vs proposed (Epic 3-5).

## Test Strategy

### Validation Strategy

**Epic 1-2 (Already Validated)**:
- 13 test scenarios already exist and pass
- Regression testing ensures new features don't break existing functionality
- Test coverage documented in `docs/testing/`

**Epic 3-5 (Future Validation)**:
- Will create test scenarios when implementing
- Follow same test capture protocol
- Validate each epic before moving to next

### Documentation Testing

**How to verify this documentation works**:

1. **AI Comprehension Test**:
   - Ask AI: "What is Outcomist?" → Should describe Epic 1-5 journey
   - Ask AI: "What's Epic 3?" → Should describe deep analysis with proposed status
   - Ask AI: "Where does X feature belong?" → Should correctly categorize

2. **User Story Clarity Test**:
   - Can a new team member read this and understand the vision?
   - Are outcomes clear enough to guide implementation?
   - Are principles actionable?

3. **Implementation Guidance Test**:
   - When building a new Epic 2 feature, does this doc help?
   - When planning Epic 3, does this provide direction?
   - When proposing a feature, can we map it to an epic?

### User Testing Approach

**For Epic 3-5 (When Implementing)**:
- Build minimal version
- Test with 5-10 real decision scenarios
- Capture what works / what doesn't
- Iterate based on feedback
- Document validated patterns

## Philosophy Alignment Check

### ✓ Ruthless Simplicity

**Evidence**:
- Epic 1-2 detailed because validated, Epic 3-5 high-level because proposed
- User stories focus on outcomes, not implementation details
- Progressive disclosure core principle: don't force unnecessary depth
- "What we're NOT building yet" section explicitly called out
- Open questions captured for future resolution, not over-planned now

**Passes**: Yes - we're documenting the vision without over-engineering unvalidated epics

### ✓ Modular Design

**Evidence**:
- Each epic is a self-contained "brick" (module)
- Clear interfaces between epics (Session data, outputs like Pattern/Insights/Analysis)
- Epic 1-2 already modular (ExplorationEngine follows pattern)
- Epic 3-5 will follow same engine pattern
- Epics can be enhanced independently
- Prompts in single source of truth (outcomist_shared/prompts.py)

**Passes**: Yes - epic structure is inherently modular with clear interfaces

### ✓ Progressive Disclosure

**Evidence**:
- Progressive disclosure is THE core product philosophy
- Match complexity to decision needs (30 seconds → ongoing tracking)
- User chooses depth at each transition
- Most decisions resolve at Epic 2
- Epic 3-5 for complex, high-stakes decisions only
- Epic transitions document explains user agency

**Passes**: Yes - progressive disclosure is fundamental to the architecture

### ✓ Clear Purpose

**Evidence**:
- Problem statement articulates why this matters
- User value explicitly called out (for user, for AI, for product)
- Each epic has clear outcome
- Success criteria focused on "AI understands vision"
- Documentation structured for AI comprehension

**Passes**: Yes - purpose is clear and serves the stated goal

## Additional Considerations

### Epic vs Feature Terminology

**Epic**: Major user capability (e.g., "Pattern Recognition & Quick Insight")
**Feature**: Specific functionality within an epic (e.g., "1.2: Pattern detection")

This aligns with standard product terminology and makes the structure more intuitive than "Stage/Tier."

### Documentation Audience

**Primary**: AI assistant (Claude) - needs to understand complete vision to build correctly
**Secondary**: Product team - needs roadmap and design context
**Future**: External users - may become part of public documentation

### Maintenance

**Living document**: This documentation will evolve as we:
- Validate Epic 3 and refine its definition
- Learn from building and update our understanding
- Add new epics or features as needs emerge
- Capture patterns and learnings

**Single source of truth**: `docs/vision/end-to-end-flow.md` is the canonical Epic 1-5 reference

**Update triggers**:
- When implementing a new epic (update status from proposed to in-progress)
- When validating an epic (update status to validated, add learnings)
- When discovering new patterns (add to relevant epic documentation)
- When user feedback changes our understanding (refine epic definition)

---

**This plan provides AI with the complete vision while maintaining ruthless simplicity, modular design, and progressive disclosure principles.**

**Ready for Phase 2: Documentation updates using this plan as the guide.**
