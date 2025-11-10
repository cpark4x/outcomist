# Epic 3: Build & Track

**Status**: ⏳ Proposed (not yet implemented, optional)
**Duration**: Ongoing (depends on project)
**Goal**: Execute validated proposal and track to completion

---

## Overview

Epic 3 is **optional**. Users choose to continue when they want execution support, progress tracking, blocker handling, and outcome measurement.

After Epic 2, users have a validated proposal they're confident in. Epic 3 is where that proposal gets executed, deployed to production, and tracked through completion.

**Note**: Production deployment happens in Epic 3, not Epic 2.

**Why separate deployment from proposal?**
- Epic 2 focus: Get user to "yes" without production concerns
- Allow refinement and iteration without deployment complexity
- User commits before deployment begins
- Can iterate proposal freely without production issues

---

## User Story

"As a decision-maker executing a solution, I track implementation, handle blockers, and measure outcomes, so I close the loop and learn from the entire decision-to-action journey."

---

## Core Principles

### Track Progress
Visibility into execution state:
- What's completed
- What's in progress
- What's blocked
- What's next

### Handle Blockers
Unblock when stuck:
- Identify issues preventing progress
- Troubleshoot problems
- Adjust plan as needed
- Escalate when necessary

### Measure Outcomes
Did it work as expected?
- Track against success criteria
- Gather performance data
- Collect user feedback
- Validate results

### Capture Learning
Close the loop, improve future decisions:
- Document what worked
- Document what didn't
- Extract lessons for future projects
- Feed learning back into pattern library (Epic 1)

---

## What Happens in Epic 3

### 1. Execute Validated Proposal

**Production deployment**:
- Deploy to production environment
- Handle real-world integration
- Configure services and tools
- Set up monitoring and alerts

**Integration**:
- Connect to existing systems
- Configure APIs and services
- Set up data flows
- Test end-to-end

**Launch preparation**:
- Final quality checks
- Performance validation
- Security review
- User acceptance testing

### 2. Track Progress

**Milestone tracking**:
- Break proposal into actionable tasks
- Track completion status
- Update timeline as work progresses
- Identify critical path items

**Task management**:
- Individual task status
- Dependencies between tasks
- Resource allocation
- Timeline adherence

**Visibility**:
- Dashboard showing progress
- Regular status updates
- Next actions clearly defined
- Blockers highlighted

### 3. Handle Blockers

**Blocker identification**:
- What's preventing progress?
- Is it technical, resource, or decision-based?
- How critical is it?
- What's the impact on timeline?

**Troubleshooting**:
- Diagnose root cause
- Propose solutions
- Test fixes
- Validate resolution

**Plan adjustment**:
- Adapt timeline if needed
- Reallocate resources
- Adjust scope if necessary
- Keep user informed

**Escalation**:
- When blocker can't be resolved
- When decisions needed from user
- When external dependencies delayed
- When scope needs revision

### 4. Measure Outcomes

**Against success criteria**:
- Were goals achieved?
- Did metrics hit targets?
- Is user satisfied with results?
- What worked better/worse than expected?

**Performance tracking**:
- System performance metrics
- User engagement data
- Business impact measurement
- Technical health indicators

**User feedback**:
- Direct user interviews
- Usage analytics
- Issue reports
- Feature requests

**Result validation**:
- Compare to original goals
- Assess overall success
- Identify areas for improvement
- Document unexpected outcomes

### 5. Capture Learning

**What worked**:
- Successful approaches
- Effective tools/techniques
- Good decisions made
- Patterns to reuse

**What didn't work**:
- Failed approaches
- Ineffective tools
- Bad decisions
- Patterns to avoid

**Lessons for future**:
- Insights for next projects
- Process improvements
- Tool recommendations
- Pattern updates

**Feed back to Epic 1**:
- Update pattern library with learnings
- Refine discovery questions based on outcomes
- Improve executability validation
- Enhance proposal quality over time

---

## Output of Epic 3

At completion, user has:

- ✅ **Working solution deployed to production**
  - Fully functional
  - Integrated with existing systems
  - Monitored and maintained

- ✅ **Outcomes measured against success criteria**
  - Goals achieved (or understood why not)
  - Metrics tracked and validated
  - User satisfaction confirmed

- ✅ **Learning documented**
  - What worked and why
  - What didn't and why
  - Lessons for future
  - Pattern library updated

- ✅ **User can maintain/operate independently**
  - Documentation complete
  - Training provided if needed
  - Handoff clean
  - Support transition plan

---

## Flow Diagram

```
Epic 2 Validated Proposal
    ↓
Deploy to Production
    ↓
Configure & Integrate
    ↓
Launch
    ↓
Track Progress
    ↓
[Blocker detected?]
    ↓ Yes
Troubleshoot & Resolve
    ↓
Adjust Plan if Needed
    ↓ No
Continue Execution
    ↓
Measure Outcomes
    ↓
Capture Learning
    ↓
Feed back to Epic 1 Pattern Library
    ↓
Project Complete
```

---

## Adaptation by Project Type

Epic 3 adapts to execution context:

### Software Projects
- **Deploy**: To production environment (Vercel, AWS, etc.)
- **Track**: Development tasks, deployment milestones
- **Monitor**: System performance, error rates, uptime
- **Measure**: User engagement, feature usage, performance metrics
- **Learn**: Technical patterns, deployment practices, architecture decisions

### Content Projects
- **Deploy**: Publish to CMS, social platforms, email service
- **Track**: Publication schedule, content calendar
- **Monitor**: Engagement metrics, SEO performance
- **Measure**: Views, shares, conversions, audience growth
- **Learn**: Content themes that resonate, optimal timing, format effectiveness

### Process Projects
- **Deploy**: Roll out to team, train users
- **Track**: Adoption rate, usage frequency
- **Monitor**: Process compliance, efficiency gains
- **Measure**: Time savings, quality improvements, team satisfaction
- **Learn**: Change management patterns, training effectiveness, process refinements

### Document/Artifact Projects
- **Deploy**: Distribute to stakeholders, integrate into workflow
- **Track**: Usage, iterations, feedback
- **Monitor**: Accuracy, updates needed, pain points
- **Measure**: Time savings, error reduction, user satisfaction
- **Learn**: Document structure effectiveness, maintenance requirements

### Strategy Projects
- **Deploy**: Communicate to team, initiate execution
- **Track**: Initiative completion, milestone achievement
- **Monitor**: KPI progress, resource utilization
- **Measure**: Business impact, goal achievement, ROI
- **Learn**: Strategy effectiveness, pivot points, execution patterns

---

## Quality Standards

### What Makes Good Execution Tracking

**✅ Good tracking**:
- Progress always visible
- Blockers identified early
- User knows what's next
- Timeline realistic and updated
- Clear completion criteria

**❌ Bad tracking**:
- User unsure of progress
- Blockers discovered late
- Timeline stale or inaccurate
- Completion criteria vague
- No regular updates

### What Makes Good Blocker Handling

**✅ Good blocker handling**:
- Identified proactively
- Root cause diagnosed quickly
- Solutions proposed with trade-offs
- User kept informed
- Timeline adjusted transparently

**❌ Bad blocker handling**:
- Discovered reactively (too late)
- Symptoms treated, not root cause
- Solutions without considering trade-offs
- User surprised by delays
- Timeline optimism without basis

### What Makes Good Outcome Measurement

**✅ Good measurement**:
- Based on original success criteria
- Data collected systematically
- Results interpreted honestly
- Unexpected outcomes explored
- Learning extracted and documented

**❌ Bad measurement**:
- Criteria changed post-hoc
- Cherry-picked positive data
- Negative results ignored
- Surprises not investigated
- Learning not captured

---

## Transition Points

### From Epic 2 to Epic 3

**User chooses Epic 3 when they want**:
- Execution support (not building alone)
- Progress tracking (visibility into status)
- Blocker handling (help when stuck)
- Outcome measurement (validate success)
- Learning capture (close the loop)

**User skips Epic 3 when they want to**:
- Execute independently (confident in their ability)
- Use own project management (have existing tools)
- Handle blockers themselves (technical capability)
- Measure outcomes themselves (have analytics)

**What flows from Epic 2**:
- Validated proposal (locked)
- Success criteria defined
- Timeline and milestones
- Resource requirements
- Technical specifications

### Completing Epic 3

**Project completion criteria**:
- All tasks completed (or consciously descoped)
- Success criteria met (or understood why not)
- Learning documented
- User can operate independently
- Clean handoff

**What happens after**:
- Learning feeds back to Epic 1 pattern library
- User has working solution in production
- Documentation enables independent maintenance
- Relationship can continue with new projects

---

## Open Questions

### For Future Implementation

**1. Task breakdown granularity**
- How detailed should tasks be?
- Who creates the task breakdown (AI or user)?
- How to balance detail with flexibility?

**2. Blocker handling approach**
- When to troubleshoot vs escalate?
- How to prevent blockers proactively?
- What level of autonomy for AI?

**3. Outcome measurement**
- What metrics for each project type?
- How to measure meaningfully without overhead?
- When is "good enough" actually good enough?

**4. Learning capture**
- What format for captured learning?
- How to make learning actionable for future users?
- When to update pattern library?

**5. User involvement level**
- How hands-on vs hands-off should Epic 3 be?
- What requires user decision vs AI autonomy?
- How to balance updates with notification fatigue?

---

## Success Metrics

### Qualitative
- ✅ Solution deployed to production successfully
- ✅ Outcomes measured against criteria transparently
- ✅ User can maintain/operate independently
- ✅ Learning captured for future use
- ✅ User satisfied with execution support

### Quantitative
- ✅ 90%+ of projects complete on adjusted timeline
- ✅ <10% of blockers require escalation
- ✅ 80%+ of success criteria met or exceeded
- ✅ Learning captured for 100% of projects
- ✅ User satisfaction score 8+/10

---

## Future Implementation

Will follow same pattern as Epic 1-2:
- **Module**: BuildEngine for orchestration
- **Tracking**: Dashboard showing progress
- **Session persistence**: Project state across time
- **Prompts**: In `outcomist_shared/prompts.py`
- **Integration**: With deployment platforms, analytics tools

**Prerequisites**:
- Epic 1-2 complete and validated
- At least one winning scenario proven end-to-end
- User feedback on what tracking/support is most valuable

**Implementation approach**:
1. Start with simplest tracking (manual updates, basic dashboard)
2. Add automated integration (GitHub, Vercel, analytics)
3. Build blocker detection and troubleshooting
4. Create outcome measurement framework
5. Develop learning capture and feedback system

---

## Related Documentation

- [Product Vision v2](../vision/product-vision-v2.md) - Strategic context
- [End-to-End Flow](../vision/end-to-end-flow.md) - Complete journey
- [Epic 1: Deep Discovery](./epic-1-deep-discovery.md) - Discovery process
- [Epic 2: Proposal Review](./epic-2-proposal-review.md) - Proposal validation

---

## Document History

**Created**: 2025-01-10
**Replaces**: epic-5-build.md (same content, renumbered)
**Status**: Aligned with Product Vision v2
**Audience**: Product team, AI assistants, future builders
