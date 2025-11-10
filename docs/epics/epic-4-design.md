# Epic 4: Design & Specification

**Status**: ⏳ Proposed (not yet implemented)
**Duration**: Variable (depends on solution complexity)
**Target Version**: TBD

---

## Overview

Epic 4 helps users design solutions before building them. "Wireframes, specs, prototypes before code" prevents "building the wrong thing efficiently." Users walk away with validated designs ready for implementation.

## User Story

**As a decision-maker who has chosen a direction**, I design the solution (wireframes, specs, prototypes) before building, **so I** prevent "building the wrong thing efficiently."

## Outcome

Users walk away with:
- **Visual wireframes** of the solution
- **Written specifications** and requirements
- **Testable prototype** (if applicable)
- **Validation feedback** incorporated
- **Clear success criteria** for implementation

## Design Principles

### Design Before Build (Prevent costly mistakes)
Invest time in design to save time in rework. Catch problems before implementation.

### Iterate Quickly (Refine before committing)
Design iterations are cheap. Implementation iterations are expensive. Iterate on design.

### Validate Early (Feedback on design, not code)
Get stakeholder feedback on wireframes, not working code. Validate direction early.

### Specify Clearly (Reduce ambiguity)
Clear specs reduce implementation confusion. Make implicit explicit.

---

## Proposed Flow

### 1. Solution Vision Articulation

**System helps user describe desired solution**:
- What does success look like?
- Who will use this?
- What's the core value?
- What are must-haves vs. nice-to-haves?

**Output**: Clear vision statement

### 2. Wireframe Generation

**System generates initial wireframes/sketches**:

**For software decisions**:
- UI mockups (key screens)
- User flows (how users navigate)
- Data models (what gets stored)

**For process decisions**:
- Flowcharts (how process flows)
- Procedures (step-by-step)
- Checklists (what to verify)

**For strategy decisions**:
- Roadmaps (timeline and milestones)
- Frameworks (how to think about it)
- Dashboards (how to measure)

### 3. User Refinement

**User refines generated wireframes**:
- Add missing elements
- Remove unnecessary complexity
- Adjust flows
- Clarify ambiguities

**System adapts** based on feedback

### 4. Specification Creation

**System creates written specifications**:
- Functional requirements (what it must do)
- Non-functional requirements (performance, scale, constraints)
- Success criteria (how to know it's working)
- Edge cases (what happens when...)

**Format**: Clear, actionable, testable

### 5. Prototype Creation (Optional)

**For testable solutions, create prototype**:
- Interactive mockup (clickable)
- Simplified version (core flow only)
- Demo-ready artifact (can show stakeholders)

**Purpose**: Test assumptions before full build

### 6. Validation & Feedback

**System facilitates validation**:
- What works well?
- What's confusing?
- What's missing?
- What would you change?

**Stakeholder review**: Get feedback from users, team, sponsors

### 7. Refinement & Finalization

**Incorporate feedback**:
- Update wireframes
- Revise specs
- Adjust success criteria

**Output**: Final design package ready for Epic 5 (Build)

---

## Features (Proposed)

### Feature 4.1: Solution Wireframing
- Visual representation adapted to decision type
- AI-generated initial drafts
- User refinement and iteration

### Feature 4.2: Specification Generation
- Functional and non-functional requirements
- Success criteria and edge cases
- Clear, actionable, testable format

### Feature 4.3: Prototype Creation
- Interactive mockups for software
- Simplified demos for processes
- Shareable artifacts for validation

### Feature 4.4: Validation & Feedback
- Structured feedback collection
- Stakeholder review facilitation
- Identify gaps and improvements

### Feature 4.5: Refinement Iteration
- Incorporate feedback efficiently
- Update all artifacts consistently
- Finalize design package

---

## When to Use Epic 4

**Use when**:
- Solution is complex (many moving parts)
- Cost of building wrong thing is high
- Multiple stakeholders need alignment
- User wants to validate before building
- Design clarity valuable for team

**Skip when**:
- Solution is simple and well-understood
- Can build quickly (low cost to try)
- No stakeholders to align
- User confident in direction
- Ready to build and iterate

---

## Design Adaptation by Decision Type

### Software Decisions
**Wireframes**: UI mockups, user flows, data models
**Specs**: API contracts, data schemas, acceptance criteria
**Prototypes**: Clickable mockups, simplified demos

### Process Decisions
**Wireframes**: Flowcharts, procedures, decision trees
**Specs**: Step-by-step instructions, roles and responsibilities
**Prototypes**: Walkthrough with stakeholders, pilot test

### Strategy Decisions
**Wireframes**: Roadmaps, frameworks, visual models
**Specs**: Initiatives, milestones, success metrics
**Prototypes**: Pilot programs, proof of concepts

### Product Decisions
**Wireframes**: Feature mockups, user journeys
**Specs**: User stories, acceptance criteria, technical requirements
**Prototypes**: MVPs, beta versions

---

## Implementation Approach (Future)

### Architecture
**Engine**: `DesignEngine` (similar to `ExplorationEngine` pattern)

**Methods**:
- `articulate_vision()`: Clarify solution vision
- `generate_wireframes()`: Create initial design
- `refine_design()`: Incorporate user feedback
- `create_specifications()`: Generate written specs
- `create_prototype()`: Build testable artifact
- `collect_feedback()`: Facilitate validation
- `finalize_design()`: Produce final package

### Integration with Epic 3
**Input**: Chosen option from Epic 3, decision criteria
**Output**: Design package (wireframes + specs + prototype + success criteria)

### Integration with Epic 5
**Output becomes input**: Design package guides Epic 5 implementation

---

## Open Questions

**To resolve during implementation**:

1. **Wireframing**: How to adapt visual representation across decision types?
2. **Prototype depth**: When is prototype valuable vs. unnecessary?
3. **Validation process**: Structured questionnaire vs. open feedback?
4. **Iteration limit**: How many refinement rounds before finalizing?
5. **Success criteria**: How specific should criteria be?

---

## Success Criteria (When Implemented)

**Clarity**: Team/stakeholders understand what's being built
**Alignment**: All parties agree on direction before building
**Reduced rework**: Fewer surprises during implementation
**Faster building**: Clear specs accelerate development
**Better outcomes**: Build the right thing, not just build quickly

---

## Related Documentation

- **Epic 3 (Deep Analysis)**: [epic-3-deep-analysis.md](./epic-3-deep-analysis.md) - Epic 4 builds on chosen option
- **Epic 5 (Build & Track)**: [epic-5-build.md](./epic-5-build.md) - Implementation of design
- **Epic Transitions**: [../principles/epic-transitions.md](../principles/epic-transitions.md) - When to use Epic 4
- **End-to-End Flow**: [../vision/end-to-end-flow.md](../vision/end-to-end-flow.md) - Complete journey

---

## Document Status

**Last Updated**: 2025-01-10
**Status**: Proposed (visionary, high-level)
**Implementation**: TBD after Epic 3 validated
**Next Review**: When Epic 4 planning begins
