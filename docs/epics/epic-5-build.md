# Epic 5: Build & Track

**Status**: ⏳ Proposed (not yet implemented)
**Duration**: Ongoing (depends on implementation timeline)
**Target Version**: TBD

---

## Overview

Epic 5 helps users execute solutions, track progress, handle blockers, and measure outcomes. "Close the loop" from decision to action to learning. Users walk away with completed implementations and captured lessons.

## User Story

**As a decision-maker executing a solution**, I track implementation, handle blockers, and measure outcomes, **so I** close the loop and learn from the entire decision-to-action journey.

## Outcome

Users walk away with:
- **Clear task breakdown** from design
- **Visible execution progress**
- **Blockers identified** and addressed
- **Outcomes measured** against success criteria
- **Lessons captured** for future decisions

## Design Principles

### Track Progress (Visibility into execution)
Users see what's done, what's in progress, what's next. No mystery about state.

### Handle Blockers (Unblock when stuck)
When stuck, system helps identify root cause and potential solutions. Don't stay blocked.

### Measure Outcomes (Did it work?)
Compare actual results to success criteria from Epic 4. Learn from outcomes.

### Capture Learning (Close the loop)
Document lessons learned. Feed back into pattern library for future users.

---

## Proposed Flow

### 1. Task Breakdown

**System breaks design into actionable tasks**:

**From Epic 4 specs**, generate:
- Implementation tasks (what to build)
- Milestones (progress checkpoints)
- Dependencies (what blocks what)
- Estimated effort (time/complexity)

**Format**: Clear, actionable, sequenced

**Example** (from software decision):
- Task 1: Set up database schema
- Task 2: Create API endpoints
- Task 3: Build frontend components
- Milestone 1: Core flow working end-to-end
- Milestone 2: Edge cases handled
- Milestone 3: Production-ready

### 2. Execution Tracking

**User executes tasks and updates progress**:
- Mark tasks as: Not started / In progress / Completed / Blocked
- Add notes on each task
- Track time spent (optional)

**System tracks**:
- Completion percentage
- Velocity (tasks per week)
- Blockers encountered
- Milestones reached

**Visibility**: Dashboard showing current state

### 3. Blocker Handling

**When user marks task as "Blocked"**:

**System asks**:
- What's preventing progress?
- Have you encountered this before?
- What have you tried?
- What would unblock you?

**System helps**:
- Identify root cause (scope? skill? resource? external dependency?)
- Suggest solutions (break task smaller, get help, use different approach)
- Connect to similar past blockers (pattern recognition)

**Purpose**: Don't stay stuck—troubleshoot systematically

### 4. Outcome Measurement

**When implementation complete, measure against success criteria**:

**From Epic 4**, success criteria were defined:
- "Users can complete core flow in <2 minutes"
- "System handles 100 concurrent users"
- "95% of users understand without help"

**System facilitates measurement**:
- Did we meet criteria?
- What worked better than expected?
- What didn't work as expected?
- What would we change?

**Output**: Outcomes report (actual vs. expected)

### 5. Learning Capture

**System captures lessons**:
- What we learned about the problem
- What we learned about the solution
- What blockers we hit (for future pattern recognition)
- What we'd do differently

**Feeds back into**:
- Pattern library (new patterns from execution experience)
- Question framework (new questions to ask)
- Blocker library (common blockers and solutions)

**Purpose**: Close the loop—learning improves future decisions

---

## Features (Proposed)

### Feature 5.1: Task Breakdown from Design
- Convert Epic 4 design into tasks
- Sequence tasks with dependencies
- Estimate effort and set milestones

### Feature 5.2: Execution Tracking
- Dashboard showing progress
- Task status updates (not started / in progress / completed / blocked)
- Velocity tracking

### Feature 5.3: Blocker Handling
- Blocker identification and root cause analysis
- Solution suggestions
- Pattern recognition (similar past blockers)

### Feature 5.4: Outcome Measurement
- Compare actual vs. expected results
- Measure against success criteria from Epic 4
- Generate outcomes report

### Feature 5.5: Learning Capture
- Document lessons learned
- Feed patterns back into library
- Improve future recommendations

---

## When to Use Epic 5

**Use when**:
- Implementation is complex (many tasks, long timeline)
- User wants progress visibility
- Blocker handling valuable (likely to get stuck)
- Outcome measurement important (learn from results)
- Capturing learning benefits future decisions

**Skip when**:
- Implementation is simple (few tasks, short timeline)
- User confident executing independently
- No need for tracking support
- Ready to act without system support

---

## Implementation Approach (Future)

### Architecture
**Engine**: `BuildEngine` (similar to `ExplorationEngine` pattern)

**Methods**:
- `break_down_tasks()`: Convert design to tasks
- `update_progress()`: Track task completion
- `identify_blocker()`: Diagnose blockers
- `suggest_solutions()`: Help unblock
- `measure_outcomes()`: Compare actual vs. expected
- `capture_learning()`: Document lessons

### Integration with Epic 4
**Input**: Design package (specs, success criteria)
**Output**: Task list, milestones, dependencies

### Session State
```python
{
  "plan": {
    "tasks": [Task],
    "milestones": [Milestone],
    "progress": {
      "completed": 15,
      "in_progress": 3,
      "blocked": 1,
      "not_started": 8
    },
    "blockers": [Blocker],
    "outcomes": {
      "criteria": [Criterion],
      "results": [Result],
      "lessons": [Lesson]
    }
  }
}
```

---

## Open Questions

**To resolve during implementation**:

1. **Task granularity**: How detailed should task breakdown be?
2. **Tracking overhead**: How to minimize administrative burden?
3. **Blocker patterns**: What common blockers exist? How to recognize them?
4. **Outcome metrics**: How to measure qualitative success criteria?
5. **Learning capture**: How to make lessons actionable for future users?
6. **PM tool overlap**: How to avoid becoming a generic project management tool?

---

## Success Criteria (When Implemented)

**Execution confidence**: Users feel supported during implementation
**Blocker resolution**: Users get unstuck faster
**Outcome awareness**: Users know whether solution worked
**Learning captured**: Patterns and lessons feed forward
**Not PM tool**: Stays focused on decision-to-action journey, not generic project management

---

## Related Documentation

- **Epic 4 (Design)**: [epic-4-design.md](./epic-4-design.md) - Epic 5 implements Epic 4 design
- **Epic Transitions**: [../principles/epic-transitions.md](../principles/epic-transitions.md) - When to use Epic 5
- **Pattern Library**: [../patterns/pattern-library.md](../patterns/pattern-library.md) - Epic 5 learning feeds patterns
- **End-to-End Flow**: [../vision/end-to-end-flow.md](../vision/end-to-end-flow.md) - Complete journey

---

## Document Status

**Last Updated**: 2025-01-10
**Status**: Proposed (visionary, high-level)
**Implementation**: TBD after Epic 4 validated
**Next Review**: When Epic 5 planning begins
