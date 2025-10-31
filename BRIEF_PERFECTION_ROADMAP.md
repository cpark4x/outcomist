# /brief Perfection Roadmap

**Created**: 2025-10-31
**Purpose**: Define what "perfect" means for `/brief` and create actionable path to achieve it

---

## Executive Summary

The `/brief` v2.0 tool already represents a major breakthrough in problem-first discovery. This document analyzes current state, identifies gaps to "perfection," and provides a roadmap for making `/brief` the definitive tool for outcome-focused AI interactions while ensuring it's reusable across all amplifier projects.

**Current State**: `/brief` v2.0 is **functional and validated** (kitchen test proved $59,800 savings potential)
**Target State**: `/brief` is **perfect** - consistently surfaces better solutions, trusted by users, reusable everywhere
**Gap**: Testing at scale, portability patterns, continuous improvement system

---

## Part 1: What "Perfect" Means for /brief

### 1.1 User Experience Excellence

**Perfect means users trust the process completely:**

✅ **Achieved in v2.0:**
- Conversational, not confrontational tone
- Gentle assumption challenges ("Have you considered...")
- Clear structure (Phases 0 → 0.5 → 1-4)
- Two-part brief with explicit quality gates
- Constraint removal tests that reveal real problems

🔄 **Needs Enhancement:**
- **Adaptability**: Some projects need 5 min, others need 20 min - tool should flex to project complexity
- **Momentum preservation**: Users get impatient if discovery takes too long without visible progress
- **Context awareness**: Tool should remember past briefs and avoid re-asking established patterns
- **Recovery from resistance**: When users push back strongly, tool needs graceful degradation paths

### 1.2 Problem Discovery Effectiveness

**Perfect means consistently finding simpler/better solutions:**

✅ **Achieved in v2.0:**
- Problem-first questioning ("What can't you do today?")
- Solution-lock detection (7 red flags defined)
- Alternative exploration required (minimum 2+)
- Cost of inaction questioning
- Quantified impact requirements

🔄 **Needs Enhancement:**
- **Domain-specific patterns**: Software projects need different questions than home projects
- **Depth calibration**: Some problems need 3 levels of "why," others need 5
- **Alternative quality**: Tool should generate alternatives if user can't think of any
- **Evidence strength**: Better detection of when problem validation is weak vs strong

### 1.3 Output Quality

**Perfect means briefs are immediately actionable:**

✅ **Achieved in v2.0:**
- Two-part structure enforces problem validation first
- YAML front-matter for machine readability
- Clear sections with specific purposes
- Validation evidence checkboxes
- Assumptions and risks explicitly flagged

🔄 **Needs Enhancement:**
- **Conciseness**: Some sections get verbose - need editing pass for clarity
- **Actionability**: "Next Steps" should be more specific (not just "test for 5 projects")
- **Measurability**: Success criteria should include specific metrics and baselines
- **Revisitability**: Briefs should be easy to update as projects evolve

### 1.4 Reusability and Portability

**Perfect means works identically across all amplifier projects:**

❌ **Not Yet Achieved:**
- Currently lives only in `outcomist/.claude/commands/`
- No mechanism to share improvements across projects
- README is project-specific, not general-purpose
- No versioning or update distribution system

**Requirements for Portability:**
1. `/brief` command available in any amplifier project
2. Updates to `/brief` propagate automatically
3. Project-specific customizations possible without breaking core
4. Documentation works for any project type

---

## Part 2: Amplifier Learnings for Reusability

### 2.1 How Amplifier Achieves Reusability

From examining amplifier structure and philosophy:

**Pattern 1: Centralized Commands with Project Symlinks**
```
~/amplifier/.claude/commands/commit.md        # Master copy
~/amplifier/outcomist/.claude/commands/ → symlink to ../../../.claude/commands/
~/amplifier/ridecast/.claude/commands/  → symlink to ../../../.claude/commands/
```

**Why this works:**
- Single source of truth for command definition
- All projects automatically get updates
- Projects can override by creating local file with same name
- Clear ownership (amplifier owns the canonical version)

**Pattern 2: Modular Design Philosophy**
- "Bricks and studs" - each command is self-contained
- Public contract (command interface) stays stable
- Internal implementation can be regenerated
- Commands reference shared context files via `@` syntax

**Pattern 3: YAML Front-matter for Metadata**
```yaml
---
description: Create well-formatted git commits
category: version-control-git
allowed-tools: Bash, Read, Glob
---
```

**Why this works:**
- Machine-readable metadata
- Tooling can query/filter commands
- Permissions and constraints defined upfront
- Self-documenting command capabilities

**Pattern 4: Separation of Concerns**
- Command logic (in `.claude/commands/`)
- Context/philosophy (in `ai_context/`)
- Project-specific data (in project subdirectories)
- Shared utilities (in `amplifier/` if needed)

### 2.2 Applying These Patterns to /brief

**Immediate Actions:**

1. **Move `/brief` to amplifier root**
   ```
   FROM: ~/amplifier/outcomist/.claude/commands/brief.md
   TO:   ~/amplifier/.claude/commands/brief.md
   ```

2. **Add YAML front-matter**
   ```yaml
   ---
   description: Problem-first project discovery and briefing
   category: planning-project-management
   allowed-tools: Read, Write, Glob
   version: 2.0.0
   last-updated: 2025-10-31
   ---
   ```

3. **Create portable README**
   ```
   FROM: ~/amplifier/outcomist/BRIEF_README.md (project-specific)
   TO:   ~/amplifier/ai_context/brief/README.md (general-purpose)
   ```

4. **Version the command explicitly**
   - Add version to front-matter
   - Track breaking changes in CHANGELOG
   - Allow projects to pin to specific version if needed

**Long-term Portability:**

1. **Template System for Domain-Specific Variants**
   - Core `/brief` for all projects
   - Optional plugins: `/brief-software`, `/brief-home-project`, `/brief-business`
   - Each plugin adds domain-specific questions on top of core

2. **Learning System**
   - Track problem pivot rate across projects
   - Identify which questions work best by domain
   - Feed learnings back into core `/brief` improvements
   - Create "greatest hits" question bank

3. **Update Distribution**
   - When amplifier `/brief` improves, all projects benefit
   - Projects can test new version before adopting
   - Rollback mechanism if new version doesn't work well

---

## Part 3: Current Gaps Analysis

### 3.1 Effectiveness Gaps

**Gap 1: No validation at scale**
- **Evidence**: Only 1 real test (kitchen renovation)
- **Risk**: Unknown how tool performs across diverse project types
- **Impact**: Can't confidently claim tool is "perfect" with sample size of 1

**Gap 2: Question patterns not optimized**
- **Evidence**: Some questions might be redundant, others missing
- **Risk**: Users get fatigued by unnecessary questions
- **Impact**: Lower adoption if tool feels tedious

**Gap 3: Domain-agnostic approach**
- **Evidence**: Same questions for software, home, business projects
- **Risk**: Generic questions miss domain-specific insights
- **Impact**: Problem discovery effectiveness varies by domain

**Gap 4: No continuous improvement loop**
- **Evidence**: No system to track what works/doesn't work
- **Risk**: Tool stagnates instead of improving
- **Impact**: Can't measure if changes make tool better or worse

### 3.2 Portability Gaps

**Gap 1: Not in amplifier root**
- **Evidence**: Currently in `outcomist/.claude/commands/`
- **Risk**: Other projects can't use it
- **Impact**: Tool improvements don't propagate

**Gap 2: Project-specific documentation**
- **Evidence**: BRIEF_README.md references outcomist specifically
- **Risk**: README doesn't transfer to other projects
- **Impact**: Users in other projects lack guidance

**Gap 3: No versioning system**
- **Evidence**: Tool evolved from v1.0 to v2.0 but no formal versioning
- **Risk**: Can't track which projects use which version
- **Impact**: Breaking changes affect all projects simultaneously

**Gap 4: No update mechanism**
- **Evidence**: Improvements require manual copying/updating
- **Risk**: Projects drift out of sync
- **Impact**: Learnings from one project don't benefit others

### 3.3 User Experience Gaps

**Gap 1: No progress visibility during discovery**
- **Evidence**: User doesn't know if they're in Phase 0 vs Phase 1
- **Risk**: Users feel lost in long conversations
- **Impact**: Abandonment before completion

**Gap 2: No escape hatch for time-constrained users**
- **Evidence**: Tool assumes users have 15-20 minutes
- **Risk**: Users skip `/brief` when pressed for time
- **Impact**: Miss opportunities to prevent resource waste

**Gap 3: No brief updating workflow**
- **Evidence**: Briefs are created once, never revisited
- **Risk**: Projects evolve but briefs don't
- **Impact**: Briefs become stale and ignored

**Gap 4: No validation that brief was useful**
- **Evidence**: No follow-up after brief completion
- **Risk**: Don't know if tool actually helped
- **Impact**: Can't measure real-world value creation

---

## Part 4: Roadmap to Perfection

### Phase 1: Validation and Learning (Weeks 1-2)

**Objective**: Prove `/brief` works across diverse projects

**Tasks:**

1. **Test on 5 diverse projects** (as outlined in outcomist brief)
   - 2 software projects (different types: API, UI, data pipeline)
   - 1 home project (renovation, decluttering, etc.)
   - 1 business initiative (process improvement, hiring, etc.)
   - 1 personal goal (health, learning, etc.)

2. **Track metrics for each test:**
   - Problem pivot rate (did user change solution after discovery?)
   - Cost avoidance (quantified resources not wasted)
   - Time investment vs perceived value
   - User satisfaction (qualitative feedback)
   - Question effectiveness (which questions led to insights?)

3. **Identify patterns:**
   - Which domains need specialized questions?
   - Which questions are universally valuable?
   - Where do users get impatient?
   - What makes "strong" vs "weak" problem validation?

4. **Document learnings in DISCOVERIES.md**
   - What worked well, what didn't
   - Patterns discovered
   - Improvements needed

**Success Criteria:**
- 3+ out of 5 projects discover simpler/better solution than stated
- Users report "this saved me time/money"
- Clear patterns emerge for improving question flow
- Data supports 30-40% problem pivot rate target

**Deliverables:**
- 5 completed briefs (in respective project `/brief/` directories)
- Analysis document comparing results
- Updated question patterns based on learnings

### Phase 2: Portability Implementation (Week 3)

**Objective**: Make `/brief` available and maintainable across all projects

**Tasks:**

1. **Move to amplifier root:**
   ```bash
   mv ~/amplifier/outcomist/.claude/commands/brief.md ~/amplifier/.claude/commands/
   ```

2. **Add YAML front-matter:**
   ```yaml
   ---
   description: Problem-first project discovery - surfaces real problems before accepting solutions
   category: planning-project-management
   allowed-tools: Read, Write, Glob
   version: 2.0.0
   last-updated: 2025-10-31
   changelog:
     - v2.0.0 (2025-10-31): Problem-first discovery with constraint removal tests
     - v1.0.0 (2025-10-30): Initial solution elaboration approach
   ---
   ```

3. **Create general-purpose README:**
   - Move from `outcomist/BRIEF_README.md`
   - To: `amplifier/ai_context/brief/README.md`
   - Remove outcomist-specific references
   - Add examples from multiple project types
   - Document versioning and update process

4. **Set up symlinks in existing projects:**
   ```bash
   # For each project in ~/amplifier/*:
   cd ~/amplifier/<project>/.claude/commands
   ln -s ../../../.claude/commands/brief.md brief.md
   ```

5. **Create update mechanism:**
   - Document in README how to adopt new versions
   - Create rollback instructions
   - Add testing guidelines before adopting updates

**Success Criteria:**
- `/brief` command works identically in all amplifier projects
- Updates to master copy propagate via symlinks
- Documentation is project-agnostic
- Projects can override with local customizations if needed

**Deliverables:**
- `/brief` in amplifier root with front-matter
- General-purpose README in `ai_context/brief/`
- Symlinks in all existing projects
- Update/rollback documentation

### Phase 3: Continuous Improvement System (Week 4)

**Objective**: Build mechanisms to measure and improve `/brief` over time

**Tasks:**

1. **Add instrumentation to brief generation:**
   - Log which questions were asked
   - Track which questions led to pivots
   - Record time spent in each phase
   - Capture user satisfaction ratings

2. **Create brief effectiveness tracking:**
   - Template: `ai_context/brief/effectiveness_log.jsonl`
   - Fields: project_type, pivot_occurred, cost_avoidance, validation_strength, user_feedback
   - Append entry after each brief completion

3. **Implement quarterly review process:**
   - Analyze effectiveness log every 3 months
   - Identify high-impact vs low-impact questions
   - Discover patterns by project type
   - Propose improvements to question flow

4. **Create A/B testing framework (optional):**
   - Allow testing question variants
   - Measure which variants work better
   - Roll winning variants into core

5. **Build learning feedback loop:**
   - Document insights in DISCOVERIES.md
   - Update `/brief` command with learnings
   - Increment version number
   - Notify projects about improvements

**Success Criteria:**
- Instrumentation captures useful data without friction
- Review process identifies 2-3 improvements per quarter
- Tool measurably improves over time (higher pivot rate, better user feedback)
- Learning loop is self-sustaining

**Deliverables:**
- Instrumentation in `/brief` command
- `effectiveness_log.jsonl` template and examples
- Quarterly review process documentation
- First review with recommendations

### Phase 4: Enhancement and Optimization (Week 5+)

**Objective**: Address gaps identified in Phase 1 testing

**Potential Enhancements** (prioritize based on Phase 1 findings):

1. **Domain-Specific Plugins:**
   - `/brief-software` - adds tech stack, architecture questions
   - `/brief-home` - adds budget, timeline, contractor questions
   - `/brief-business` - adds stakeholder, ROI, change management questions
   - Core `/brief` remains unchanged

2. **Progress Visibility:**
   - Show phase indicators: "Phase 0: Problem Discovery (5-7 min)"
   - Track % through conversation
   - Provide "skip to next phase" option if user is confident

3. **Quick Mode:**
   - `/brief --quick` for time-constrained users
   - 5-minute version with core questions only
   - Still enforces problem validation but faster

4. **Brief Updating:**
   - `/brief --update` to revisit existing brief
   - Show what changed since last version
   - Preserve history (appending, not replacing)

5. **Alternative Generation:**
   - If user can't think of alternatives, tool suggests 2-3
   - Based on problem type and common patterns
   - Helps users who are truly stuck

6. **Validation Strength Scoring:**
   - Automated scoring: Strong (4/4 criteria) vs Weak (1-2/4)
   - Flag specific gaps: "Need quantified impact"
   - Help tool know when to probe deeper

7. **Follow-Up System:**
   - Schedule check-in 2 weeks after brief
   - Ask: "Did the solution work? Did you pivot again?"
   - Feed results back into effectiveness log

**Success Criteria:**
- Enhancements address real pain points from Phase 1
- User satisfaction improves measurably
- Tool maintains simplicity (no feature bloat)
- Each enhancement pulls its weight

**Deliverables:**
- Prioritized enhancement list based on Phase 1
- Implementation of top 2-3 enhancements
- Documentation updates
- Testing with real users

---

## Part 5: Success Metrics

### Leading Indicators (Measure During Process)

1. **Adoption Rate**: % of projects that use `/brief` before planning
   - Target: 80% of projects within 6 months

2. **Completion Rate**: % of `/brief` sessions completed vs abandoned
   - Target: 70%+ completion rate

3. **Time Investment**: Average time spent in `/brief` session
   - Target: 10-15 minutes (down from 15-20)

4. **User Satisfaction**: Qualitative feedback post-session
   - Target: "This was valuable" in 80%+ of sessions

### Lagging Indicators (Measure Outcomes)

1. **Problem Pivot Rate**: % of sessions where user changes solution
   - Baseline: 100% (1/1 in kitchen test)
   - Target: 30-40% sustained across all projects

2. **Cost Avoidance**: Dollar value of unnecessary work prevented
   - Examples: $59,800 (kitchen), $50k (unused features)
   - Target: Document 5+ cases of significant cost avoidance

3. **Solution Right-Sizing**: % of sessions finding simpler approach
   - Example: $200 workflow test before $60k renovation
   - Target: 40%+ find simpler approach than originally stated

4. **Validation Strength**: % of briefs with "Strong" problem validation
   - Target: 70%+ achieve strong validation

### Learning Indicators (Measure Improvement)

1. **Question Effectiveness**: Which questions consistently lead to insights?
   - Measure: Track pivot occurrences by question
   - Target: Identify top 5 highest-impact questions

2. **Domain Patterns**: Do different domains need different approaches?
   - Measure: Compare effectiveness by project type
   - Target: Clear pattern identification within 5 tests

3. **Iteration Speed**: How fast does tool improve?
   - Measure: Improvements implemented per quarter
   - Target: 2-3 meaningful improvements per review cycle

---

## Part 6: Risk Mitigation

### Risk 1: Users Resist 15-20 Minute Investment

**Likelihood**: Medium
**Impact**: High (low adoption kills value)

**Mitigation:**
- Implement Quick Mode (5 minutes) for time-constrained users
- Show time investment vs cost avoidance stats upfront
- Make early phases show value fast (pivot in Phase 0 if possible)
- Allow "pause and resume" for long sessions

### Risk 2: Tool Doesn't Generalize Across Domains

**Likelihood**: Medium
**Impact**: Medium (reduces effectiveness in some domains)

**Mitigation:**
- Test 5 diverse projects immediately (Phase 1)
- Build domain-specific plugins if needed
- Keep core domain-agnostic
- Document which domains work best

### Risk 3: Improvements Don't Propagate to Projects

**Likelihood**: Low (symlinks solve this)
**Impact**: Medium (fragmentation)

**Mitigation:**
- Use symlink pattern from day 1
- Document update process clearly
- Make breaking changes extremely rare
- Version explicitly and communicate changes

### Risk 4: Measurement Overhead Reduces Adoption

**Likelihood**: Low
**Impact**: Low (can disable instrumentation)

**Mitigation:**
- Make instrumentation optional
- Keep data collection lightweight
- Show value of measurement (better tool)
- Allow opt-out per project

### Risk 5: Tool Becomes Too Complex

**Likelihood**: Medium
**Impact**: High (violates amplifier philosophy)

**Mitigation:**
- Every enhancement must justify complexity
- Regular "simplification passes"
- Ruthlessly cut features that don't pull weight
- Keep core focused, make enhancements optional

---

## Part 7: Immediate Next Steps

### This Week

1. **Move `/brief` to amplifier root** (30 min)
   - Add YAML front-matter
   - Update references in outcomist

2. **Create general-purpose README** (2 hours)
   - Remove project-specific references
   - Add examples from multiple domains
   - Document versioning approach

3. **Begin Phase 1 testing** (ongoing)
   - Identify 5 diverse projects to test
   - Schedule testing sessions
   - Set up effectiveness log

### Next 2 Weeks

1. **Complete Phase 1: Validation** (5 project tests)
2. **Analyze results and document learnings**
3. **Implement Phase 2: Portability** (symlinks, etc.)
4. **Begin Phase 3: Continuous improvement system**

### This Month

1. **Complete Phases 1-3** (validation, portability, improvement system)
2. **Prioritize Phase 4 enhancements** based on findings
3. **Implement top 2-3 enhancements**
4. **Document first quarterly review**

---

## Part 8: Measuring "Perfect"

**We'll know `/brief` is "perfect" when:**

✅ **Adoption**: 80%+ of amplifier projects use it before planning
✅ **Effectiveness**: 30-40% pivot rate sustained across diverse projects
✅ **Satisfaction**: 80%+ users say "this was valuable"
✅ **Portability**: Works identically in all projects via symlinks
✅ **Learning**: Tool measurably improves every quarter
✅ **Simplicity**: Core remains simple, enhancements are optional
✅ **Trust**: Users proactively suggest `/brief` to others

**Current Status (v2.0):**
- ✅ Core problem-first approach validated (kitchen test)
- ✅ Two-part brief structure working
- ❌ Not yet tested at scale (1 project only)
- ❌ Not portable (stuck in outcomist)
- ❌ No improvement system
- ❌ No measurement of real-world value

**Path Forward:**
Execute Phases 1-4 systematically, measuring progress against success criteria at each gate.

---

## Conclusion

**The `/brief` v2.0 tool is fundamentally sound** - the kitchen renovation test proved the problem-first approach works and creates significant value ($59,800 potential savings).

**The path to "perfect" is clear:**
1. **Validate at scale** (5 diverse projects)
2. **Make portable** (move to amplifier root, symlinks)
3. **Build improvement system** (measure, learn, iterate)
4. **Enhance strategically** (based on real findings)

**The amplifier learnings provide the blueprint:**
- Centralized commands with symlinks = automatic updates
- YAML front-matter = machine-readable metadata
- Modular design = regeneratable, improvable
- Documentation separation = portable guidance

**Next milestone:** Complete Phase 1 validation (5 projects) to prove approach generalizes.

**Ultimate vision:** `/brief` becomes the standard for AI-human alignment on problems before solutions, not just in amplifier but in any AI-assisted project planning context.
