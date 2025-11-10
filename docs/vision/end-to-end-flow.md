# Outcomist: Decision to Action Journey

**Complete end-to-end user flow across three epics**

**Last Updated**: 2025-01-10
**Status**: Aligned with Product Vision v2

---

## The Big Picture

Outcomist guides users through a complete decision-to-action journey structured as three epics:

1. **Epic 1: Deep Discovery** (✅ Validated) - 30 sec to 30 min (adaptive)
2. **Epic 2: Proposal Review** (⏳ Proposed) - Variable
3. **Epic 3: Build & Track** (⏳ Proposed - Optional) - Ongoing

### Core Principles

**Get to Proposal Quickly**: Users want to reach Epic 2 (proposal review) as fast as possible. Epic 1 exists solely to make Epic 2 proposals high-quality and executable.

**Quality Over Speed**: Proposals must be tangible, polished, and gap-free enough for users to confidently evaluate.

**No "Floating Countertops"**: AI only proposes solutions it can actually execute within user's constraints.

**User Agency**: Users choose depth at each transition. The system never forces unnecessary exploration.

**Evidence-Based**: Recommendations grounded in facts, constraints, and validated executability.

**Transparent Reasoning**: Users see why recommendations are made and what's required to execute.

---

## Epic 1: Deep Discovery

**Status**: ✅ Validated and shipped (v4.8)

**Note**: This epic combines what was previously "Pattern Recognition", "Discovery", and "Deep Analysis" into ONE continuous discovery process. The depth adapts to the decision's complexity.

### User Story

"As a decision-maker, I need AI to deeply understand my problem AND validate it can execute a solution, so I get a high-quality, executable proposal to review."

### Outcome

Users walk away with:
- Deep understanding of the real problem (not just stated problem)
- Validated that AI can execute within their constraints
- Executable proposal: "Here's what I'll build for you"
- Ready to transition to Epic 2 (proposal review)

### Principles

- **Adaptive Depth**: Quick (pattern + questions) OR thorough (includes alternatives comparison)
- **Executability First**: AI only proposes what it can actually deliver
- **Constraint Awareness**: Technical, resource, skill, access constraints captured
- **One Continuous Process**: Not separate stages, but one discovery flow

### Flow

1. User inputs decision statement
2. System detects pattern (9 documented patterns in [pattern library](../patterns/pattern-library.md))
3. System reframes question to reveal deeper issue
4. System previews what Epic 2 exploration would uncover
5. User chooses: Continue to Epic 2 or stop here

### Features

- **1.1: Decision Input** - Natural language decision statement
- **1.2: Pattern Detection** - Identifies which of 9 patterns applies
- **1.3: Reframing & Preview** - Shows real issue + exploration preview
- **1.4: Intent Checking** - User indicates validation vs execution intent

### Implementation

**Current**: Web interface (`outcomist_web/`) with streaming pattern recognition via Claude API.

**Key components**:
- `ExplorationEngine.generate_tier_1()` - Pattern recognition
- 9 documented patterns with signals, questions, and real problems
- Streaming Server-Sent Events for natural feel

See [Epic 1 detailed documentation](../epics/epic-1-pattern-recognition.md)

---

## Epic 2: Discovery & Understanding

**Status**: ✅ Validated and shipped

### User Story

"As a decision-maker, I explore my decision through adaptive questions that uncover constraints, priorities, and evidence, so I get a personalized recommendation grounded in my actual situation."

### Outcome

Users walk away with:
- Discovered constraints they hadn't articulated
- Clear priorities revealed through trade-offs
- Evidence gathered and facts verified
- Specific recommendation tailored to their situation

### Principles

- **Adaptive**: Questions based on previous answers
- **Evidence-Based**: "Show me" questions verify facts
- **Progressive**: Start broad, then targeted
- **Transparent**: Show reasoning for recommendations

### Flow

1. System asks 2-3 high-level questions (Round 1)
2. User answers, system gathers evidence
3. System synthesizes patterns and shows analysis
4. System asks targeted follow-up (Round 2)
5. User answers
6. System generates summary, user confirms
7. System delivers personalized recommendation

### Features

- **2.1: Adaptive Questioning (Round 1)** - Context-aware high-level questions
- **2.2: Evidence Gathering** - "Show me" questions verify facts
- **2.3: Pattern Synthesis** - Analysis showing what system detected
- **2.4: Targeted Follow-up (Round 2)** - Focused question based on Round 1
- **2.5: Summary & Confirmation** - User validates understanding
- **2.6: Personalized Recommendation** - Specific advice grounded in evidence

### Implementation

**Current**: Web interface with multi-turn conversation and streaming responses.

**Key components**:
- `ExplorationEngine.start_tier_2()` - Begins discovery
- `ExplorationEngine.handle_answer()` - Processes responses adaptively
- Question framework maps patterns to relevant questions
- Session persistence tracks conversation and insights

See [Epic 2 detailed documentation](../epics/epic-2-discovery.md)

---

## Epic 3: Deep Analysis & Alternatives

**Status**: ⏳ Proposed (not yet implemented)

### User Story

"As a decision-maker facing a complex choice, I systematically explore alternatives, assess risks, and plan scenarios, so I choose confidently even with uncertainty."

### Outcome

Users walk away with:
- Multiple options clearly compared
- Risks identified and assessed for each option
- Scenarios planned (best case, worst case, likely case)
- Decision criteria refined and explicit
- Clear recommendation with full rationale

### Principles

- **Systematic**: Structured option comparison across criteria
- **Risk-Aware**: Surface and assess uncertainties
- **Scenario-Based**: Plan for multiple futures
- **Criteria-Driven**: Help user define what matters most

### Flow (Proposed)

1. System generates 3-5 viable options from Epic 2 insights
2. User reviews options, adds or removes as needed
3. System facilitates option comparison across criteria
4. System identifies risks for each option
5. System facilitates scenario planning (best/worst/likely)
6. User clarifies decision criteria (what matters most)
7. System recommends option with full rationale

### Features (Proposed)

- **3.1: Option Generation & Comparison** - Create and compare alternatives
- **3.2: Risk Assessment** - Identify and evaluate risks per option
- **3.3: Scenario Planning** - Plan for best/worst/likely futures
- **3.4: Trade-off Analysis** - Explicit trade-off evaluation
- **3.5: Decision Criteria Refinement** - Clarify what matters most

### Future Implementation

Will follow same pattern as Epic 1-2:
- `AnalysisEngine` module for orchestration
- Streaming interactions
- Session-based state management
- Prompts in `outcomist_shared/prompts.py`

See [Epic 3 proposed documentation](../epics/epic-3-deep-analysis.md)

---

## Epic 4: Design & Specification

**Status**: ⏳ Proposed (not yet implemented)

### User Story

"As a decision-maker who has chosen a direction, I design the solution (wireframes, specs, prototypes) before building, so I prevent 'building the wrong thing efficiently.'"

### Outcome

Users walk away with:
- Visual wireframes of the solution
- Written specifications
- Testable prototype (if applicable)
- Validation feedback incorporated
- Clear success criteria

### Principles

- **Design Before Build**: Prevent costly implementation mistakes
- **Iterate Quickly**: Refine design before committing resources
- **Validate Early**: Get feedback on design, not implementation
- **Specify Clearly**: Reduce implementation ambiguity

### Flow (Proposed)

1. System helps user articulate solution vision
2. System generates initial wireframes or sketches
3. User refines, system adapts
4. System creates specifications
5. System generates prototype (if applicable)
6. User validates design
7. System incorporates feedback
8. Finalize design with success criteria

### Features (Proposed)

- **4.1: Solution Wireframing** - Visual representation of solution
- **4.2: Specification Generation** - Written specs and requirements
- **4.3: Prototype Creation** - Testable prototype when applicable
- **4.4: Validation & Feedback** - Structured design feedback
- **4.5: Refinement Iteration** - Incorporate feedback and refine

### Future Implementation

Design stage adapts to decision type:
- Software: Wireframes, API specs, data models
- Process: Flowcharts, procedures, checklists
- Strategy: Plans, roadmaps, frameworks
- Product: Mockups, feature specs, user flows

See [Epic 4 proposed documentation](../epics/epic-4-design.md)

---

## Epic 5: Build & Track

**Status**: ⏳ Proposed (not yet implemented)

### User Story

"As a decision-maker executing a solution, I track implementation, handle blockers, and measure outcomes, so I close the loop and learn from the entire decision-to-action journey."

### Outcome

Users walk away with:
- Clear task breakdown from design
- Visible execution progress
- Blockers identified and addressed
- Outcomes measured against success criteria
- Lessons captured for future decisions

### Principles

- **Track Progress**: Visibility into execution state
- **Handle Blockers**: Unblock when stuck
- **Measure Outcomes**: Did it work as expected?
- **Capture Learning**: Close the loop, improve future decisions

### Flow (Proposed)

1. System breaks design into actionable tasks
2. User executes and updates progress
3. System tracks completion
4. When blocked, system helps troubleshoot
5. System measures outcomes against success criteria
6. System captures lessons learned
7. Learning feeds back into pattern library

### Features (Proposed)

- **5.1: Task Breakdown** - Convert design into actionable tasks
- **5.2: Execution Tracking** - Track progress and completion
- **5.3: Blocker Handling** - Identify and resolve blockers
- **5.4: Outcome Measurement** - Measure against success criteria
- **5.5: Learning Capture** - Document lessons for future

### Future Implementation

Build & track adapts to execution context:
- Software: Development tasks, deployment, monitoring
- Process: Implementation steps, adoption tracking
- Strategy: Initiative tracking, KPI measurement
- Product: Feature rollout, user feedback, metrics

See [Epic 5 proposed documentation](../epics/epic-5-build.md)

---

## Epic Transitions: User Agency & Information Flow

### Transition Philosophy

Outcomist respects user agency at every stage. Users choose depth based on:
- Decision complexity
- Stakes involved
- Time available
- Confidence level
- Information needs

**The system never forces unnecessary depth.** Most decisions resolve at Epic 2.

### Transition Points

#### After Epic 1 (Pattern Recognition)

**Decision**: Continue to Epic 2 or stop?

**Why stop**:
- Pattern recognition alone provides sufficient clarity
- User sees the real issue and knows what to do
- Decision is simple enough without deeper exploration

**Why continue**:
- Want to explore the reframed question deeper
- Need specific recommendations
- Unclear about best path forward

**What flows forward**:
- Original decision statement
- Identified pattern
- Reframed question

---

#### After Epic 2 (Discovery)

**Decision**: Act on recommendation, continue to Epic 3, or stop?

**Why stop**:
- Recommendation is clear and actionable
- Have sufficient information to decide
- Decision isn't complex enough for deeper analysis

**Why continue to Epic 3**:
- Decision is complex with multiple viable options
- Need systematic comparison of alternatives
- Want risk assessment and scenario planning
- Stakes are high enough to warrant deeper analysis

**What flows forward**:
- Discovery insights (answers to all questions)
- Identified constraints and priorities
- Gathered evidence
- Initial recommendation

---

#### After Epic 3 (Deep Analysis)

**Decision**: Choose option and act, continue to Epic 4, or stop?

**Why stop**:
- Have chosen an option confidently
- Clear on next steps, can execute independently
- Decision doesn't require design phase

**Why continue to Epic 4**:
- Want to design solution before building
- Risk of "building the wrong thing" is high
- Solution is complex enough to benefit from wireframes/specs
- Need validation before committing resources

**What flows forward**:
- All options analyzed
- Chosen direction
- Refined decision criteria
- Risk assessments
- Scenario plans

---

#### After Epic 4 (Design)

**Decision**: Build on your own or continue to Epic 5?

**Why stop**:
- Have design and specifications
- Confident executing independently
- Don't need tracking support

**Why continue to Epic 5**:
- Want help tracking execution
- Benefit from blocker identification
- Need outcome measurement support
- Want to capture learning

**What flows forward**:
- Wireframes and visual designs
- Specifications and requirements
- Prototypes (if created)
- Success criteria

---

#### After Epic 5 (Build)

**Completion**: Decision fully executed, outcomes measured

**What flows back**:
- Learning captured from execution
- Patterns identified during implementation
- Blocker patterns documented
- Outcome data feeds future recommendations

---

### Information Architecture

```
Epic 1 Output: Pattern + Reframe
    ↓
Epic 2 Output: Insights + Recommendation
    ↓
Epic 3 Output: Options + Risks + Scenarios
    ↓
Epic 4 Output: Design + Specs + Success Criteria
    ↓
Epic 5 Output: Outcomes + Learning
    ↓
Pattern Library (feeds future Epic 1)
```

### Key Principle: Progressive Disclosure

The entire architecture embodies progressive disclosure:

- **Epic 1**: 30 seconds - Quick pattern insight
- **Epic 2**: 5-10 minutes - Structured discovery
- **Epic 3**: 20-30 minutes - Deep analysis
- **Epic 4**: Variable - Solution design
- **Epic 5**: Ongoing - Execution tracking

Most users stop at Epic 2. Epic 3-5 serve complex, high-stakes decisions.

See [Epic Transitions detailed documentation](../principles/epic-transitions.md)

---

## Implementation Roadmap

### Completed (✅)

**Epic 1: Pattern Recognition**
- Pattern detection with 9 documented patterns
- Streaming reframing
- Intent checking
- Web implementation

**Epic 2: Discovery**
- Adaptive questioning (2 rounds)
- Evidence gathering
- Pattern synthesis
- Personalized recommendations
- Web implementation

### In Progress

**Documentation Phase** (Current)
- End-to-end flow documentation
- Individual epic documentation
- Epic transitions documentation
- Updated vision and principles docs

### Planned (⏳)

**Epic 3: Deep Analysis**
- Prerequisites: Epic 1-2 documentation complete, pattern library mature
- Key decisions: Option generation approach, risk framework, scenario planning structure
- Implementation: AnalysisEngine following ExplorationEngine pattern

**Epic 4: Design**
- Prerequisites: Epic 3 complete and validated
- Key decisions: Design representation across decision types, validation approach
- Implementation: DesignEngine with wireframing/spec generation

**Epic 5: Build & Track**
- Prerequisites: Epic 4 complete and validated
- Key decisions: Task breakdown approach, blocker handling, outcome measurement
- Implementation: BuildEngine with execution tracking

---

## Architecture Principles

### Modular Design

Each epic is a self-contained module ("brick") with clear interfaces ("studs"):

**Modules**:
- Epic 1-2: `ExplorationEngine`
- Epic 3: `AnalysisEngine` (future)
- Epic 4: `DesignEngine` (future)
- Epic 5: `BuildEngine` (future)

**Interfaces** (Session state):
```python
{
  "id": "session_id",
  "decision_statement": str,
  "current_epic": 1-5,
  "pattern": Pattern | None,
  "insights": Insights | None,
  "analysis": Analysis | None,
  "design": Design | None,
  "plan": Plan | None,
  "completed_epics": [1, 2, ...]
}
```

**Shared Infrastructure**:
- Web stack: FastAPI + vanilla JS + Server-Sent Events
- Storage: JSON session persistence
- Prompts: Single source of truth (`outcomist_shared/prompts.py`)

### Ruthless Simplicity

- **Start minimal**: Epic 1-2 detailed (validated), Epic 3-5 high-level (proposed)
- **Avoid future-proofing**: Refine epics as we build and learn
- **Clear over clever**: Plain epic/feature terminology, not abstract stage/tier

### Progressive Disclosure

Progressive disclosure is not just a feature—it's the core product philosophy:
- Match complexity to decision needs
- User chooses depth
- Most decisions resolve at Epic 2
- Epic 3-5 for complex, high-stakes decisions only

---

## Open Questions (To Resolve During Implementation)

### Epic 3 Questions
- How to generate alternatives systematically?
- What makes a good risk assessment?
- How detailed should scenario planning be?
- When is Epic 3 overkill vs. necessary?

### Epic 4 Questions
- What does "design" mean for non-software decisions?
- How to make wireframing useful across decision types?
- When is prototyping valuable vs. wasteful?
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
- How to prevent "epic fatigue" (going too deep unnecessarily)?

---

## Success Criteria

### For This Documentation

**Primary goal**: AI understands complete vision and builds each piece correctly toward the big picture.

**Verification**:
- AI can explain all 5 epics and the user journey
- AI can articulate what's validated vs. proposed
- AI can identify which epic a feature request belongs to
- AI can build Epic 1-2 features without breaking the bigger picture
- AI can propose Epic 3-5 features consistent with the vision

### For Future Implementation

**Epic 3**: Users explore alternatives systematically, make more confident complex decisions

**Epic 4**: Users design solutions before building, prevent "building wrong thing efficiently"

**Epic 5**: Users track execution effectively, measure outcomes, learn from the journey

---

## Related Documentation

- **Individual Epics**: See [docs/epics/](../epics/) for detailed documentation per epic
- **Epic Transitions**: See [Epic Transitions](../principles/epic-transitions.md) for flow details
- **Pattern Library**: See [Pattern Library](../patterns/pattern-library.md) for 9 documented patterns
- **Question Framework**: See [Question Framework](../patterns/question-framework.md) for question design
- **Product Vision**: See [Product Vision](product-vision.md) for strategic context
- **Progressive Disclosure**: See [Progressive Disclosure](../principles/progressive-disclosure.md) for architecture principles

---

## Document Status

**Created**: 2025-01-10
**Epic 1-2**: Validated and documented based on shipped implementation
**Epic 3-5**: Proposed and documented as directional vision
**Audience**: AI assistant (primary) and product team (secondary)
**Maintenance**: Living document, will evolve as epics are implemented and validated
