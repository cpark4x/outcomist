---
created: 2025-10-31
updated: 2025-10-31
status: draft
owner: Chris Park
problem_validated: true
alternatives_explored: true
---

# Outcomist

## PART 1: PROBLEM DEFINITION

### What We Can't Do Today
**Core Problem**: AI users state activities ("build X", "renovate Y") instead of outcomes ("achieve Z"). AI tools accept these activity-statements at face value and help execute them efficiently, but users end up building the wrong things because the activity doesn't map to their real problem.

**Specific Gap**: There's no systematic way for AI to discover what problem a user is actually solving before helping them build a solution. Every AI conversation starts with "what are you building?" instead of "what can't you do today?"

### Why It Matters

**Impact**:
- **Resource Waste**: Users spend time/money building things that don't solve their problems (Example: 3 months building unused features = $50k wasted; $60k renovation that might not be needed)
- **Frustrated Users**: AI helps them be efficient at the wrong thing
- **Unfulfilled Promise**: "AI helps you achieve more" becomes "AI helps you build more stuff that doesn't matter"
- **Frequency**: Every AI interaction for project planning (software, home projects, business initiatives, personal goals)

**Affected**:
- Anyone using AI for project planning/execution
- AI developers trying to help users achieve real outcomes
- Teams building on top of AI tools

### Current Situation

**How we handle it today**:
- AI accepts solution-statements immediately: "I need a CRM" → "Let me help you build a CRM"
- Rare deep conversations might uncover problems (like kitchen renovation example)
- Some users have learned to ask themselves better questions, but it's not systematic
- Consultants/advisors do this well, but not scalable for every AI interaction

**Why that's insufficient**:
- Unsystematic: Depends on user discipline or AI spontaneously probing deeper
- Not scalable: Can't hire consultant for every AI conversation
- Reactive: Problem only discovered after wasted effort
- Pattern unrecognized: Most users don't realize they're stating activities not outcomes

**Last occurrence**:
- Kitchen renovation: User stated "renovate kitchen" (activity), real problem was "reduce cooking stress + $9,600/year restaurant spending" (outcome)
- Past project: Built "analytics dashboard" because team said they needed it, but real problem was "can't make product decisions" (different solution needed)
- Common pattern: "Need CRM" when problem is "lose track of 20 customer conversations"

### Cost of Inaction

**If nothing changes**:
- AI becomes really good at helping people waste resources efficiently
- Users continue building wrong solutions to real problems
- Gap between AI promise and AI reality widens
- Resource drain: Organizations waste millions on well-executed wrong solutions
- Reputation risk: "AI helps you build faster" without "AI helps you build right"

**Personal cost**: Continue seeing projects waste time/money on solutions that don't achieve desired outcomes

### Validation Evidence

- [x] Problem stated independent of solution (activity-outcome mismatch in AI interactions)
- [x] Impact quantified (Historical: $50k in 3-month wasted features; Potential: $60k unnecessary renovation; Systemic: Every project planning AI interaction)
- [x] Concrete examples (Kitchen renovation, CRM vs customer tracking, analytics dashboard)
- [x] Root cause identified (People think in activities, AI takes them literally, outcomes not achieved)
- [x] Considered doing nothing (Perpetuates the problem, unacceptable)

---

## PART 2: SOLUTION APPROACH

### Alternatives Considered

**1. Do Nothing / Accept Current State**
- Let AI keep accepting activity-statements at face value
- **Why not**: Perpetuates resource waste, doesn't fulfill AI's potential to help achieve outcomes

**2. Pure Prompt Engineering**
- Change AI system prompts to ask "what can't you do?" before "what are you building?"
- **Cost**: $0 (just prompt updates)
- **Why this could work**: Might shift some conversations to problem-first
- **Why not sufficient**: Users can override prompts, no systematic structure, no artifact created

**3. Static Checklist/Template**
- Create document: "Fill this out before AI planning"
- **Cost**: 1 day to create template
- **Why this could work**: Forces problem thinking if users use it
- **Why not sufficient**: People skip checklists, no AI guidance through discovery, no learning/adaptation

**4. Manual Process**
- Train myself to always do problem-first questioning before any AI planning
- **Cost**: Just discipline
- **Status**: TESTED via kitchen renovation conversation
- **Result**: WORKS (saved $60k potential waste) but requires discipline to remember every time
- **Why not sufficient**: Not scalable, not shareable, depends on memory

**5. Interactive Brief Tool (CHOSEN)**
- Conversational AI tool that conducts problem discovery before accepting solutions
- Implemented as Claude Code slash command (`/brief`)
- **Cost**: 2-4 weeks to build and refine (v1.0 already built, v2.0 completed)
- **Why this wins**: Systematic, guided, creates artifact, shareable, hard to skip, proven effective
- **Status**: MVP EXISTS (v2.0 completed Oct 31, 2025)

**6. Platform-Level Integration**
- Embed problem discovery into all AI interactions (not just a tool)
- **Why this wins in theory**: Automatic, no separate step
- **Why not now**: Don't control AI platforms, need to prove approach first

### Why This Approach Wins

**CHOSEN: Interactive Brief Tool (`/brief` v2.0)**

**Reasoning**:
1. **Proven effective**: Kitchen renovation test saved $60k in potential waste by discovering real problem
2. **Systematic**: Users can't skip or forget - running `/brief` enforces the process
3. **Guided**: AI asks the right questions in right order (problem discovery → solution exploration → validation)
4. **Creates artifact**: Generates two-part brief (Problem Definition + Solution Approach) as canonical source of truth
5. **Shareable**: Tool can be used by anyone, approach is documented and repeatable
6. **Evolves**: Can refine questions based on usage, improve problem-discovery patterns
7. **Right-sized**: Started as minimal slash command (not over-engineered), can expand if needed

**Trade-offs acknowledged**:
- Adds ~15-20 min before project planning (but saves weeks/months of building wrong things)
- Requires user to engage with questions (can't be passive)
- Currently Claude Code-specific (but proven approach can expand to other platforms)

**Why this beats alternatives**:
- vs Do Nothing: Actively solves the problem vs accepting waste
- vs Prompt Engineering: Systematic structure, not just suggestion
- vs Checklist: AI-guided, adaptive, hard to skip
- vs Manual: Scalable, shareable, doesn't require discipline
- vs Platform Integration: Can build now, proves approach before seeking platform adoption

### Simplest Test

**Test Already Completed**: Kitchen renovation conversation (Oct 31, 2025)

**Results**:
- User stated activity: "Renovate kitchen with open floor plan" ($60k)
- `/brief` v2.0 discovered: "Daily cooking friction → $9,600/yr restaurants" (real problem)
- Alternative found: "Test $200 workflow changes before $60k renovation"
- **Outcome**: Potentially saved $59,800 by discovering right-sized solution

**Validation**: Problem-first discovery approach works ✅

**Next Test**: Use `/brief` on 5 real projects (software, home, business, personal) and track:
- How often problem discovery changes the solution
- How often simpler alternatives are found
- User feedback on conversation quality
- Time investment (15-20 min) vs resource savings

**Success Criteria for Next Test**:
- 3+ out of 5 projects discover simpler/better solution than originally stated
- Users report "this saved me time/money"
- Clear patterns emerge for improving question flow

---

## IMPLEMENTATION DETAILS

### Vision

**What We're Building**: Outcomist is a project housing outcome-focused AI tools that help users achieve real outcomes instead of just executing activities efficiently.

**Current State**: Contains `/brief` v2.0 - a conversational AI tool that discovers problems before accepting solutions

**Why It Exists**: To close the gap between AI's promise ("achieve more") and AI's current behavior ("build more stuff"). To ensure AI helps users solve the right problems, not just execute stated solutions efficiently.

**Success Looks Like**:
- Users routinely use `/brief` before starting projects
- Measurable reduction in "built but unused" features/solutions
- AI develops reputation for helping achieve outcomes, not just execute activities
- Approach proven enough that AI platforms adopt problem-first discovery

### Primary User

**Name/Role**: Chris Park, AI user and builder
**Context**: Uses AI for project planning (software, home projects, business); has experienced wasted effort from solution-first thinking; values efficiency but more values effectiveness
**Current Behavior**: Uses Claude Code for development; starting to manually do problem-first questioning but needs systematic approach
**Needs**:
- Systematic way to discover problems before committing to solutions
- Shareable tool that others can use
- Artifact (brief) that serves as source of truth for projects
- Validation that AI is helping achieve outcomes, not just build things

**Frustrations**:
- Seeing projects waste resources on wrong solutions
- AI jumping to "how to build" before "what to solve"
- Gap between promise and reality of AI assistance
- Difficulty remembering to do problem discovery every time

### Success Criteria

**Primary Success Metric**: Problem pivot rate - % of `/brief` sessions where user changes or optimizes their solution after problem discovery

**Baseline → Target**:
- **v1.0 baseline**: 0% (accepted all solutions at face value)
- **v2.0 target**: 30-40% of users reconsider/optimize solution
- **Current proof**: 100% in kitchen test (changed from $60k to $200 approach)

**Secondary Metrics**:
- Cost avoidance: Dollar value of unnecessary solutions not built (e.g., $59,800 in kitchen example)
- Alternative exploration: % of briefs documenting 2+ alternatives (target: 100%)
- Validation strength: % of briefs with "Strong" problem validation (target: 70%+)
- User satisfaction: Qualitative feedback on value received

**Done Looks Like**:
- `/brief` consistently surfaces simpler/better solutions than originally stated
- Users report saved time/money from problem discovery
- Clear patterns for when problem discovery is most valuable
- Tool is refined enough to share widely
- Decision made on whether Outcomist needs companion tools or if `/brief` is sufficient

**Failure Looks Like**:
- Users find `/brief` tedious without sufficient payoff
- Problem discovery doesn't consistently find better solutions
- Tool is too rigid/doesn't adapt to different project types
- 15-20 min investment not justified by outcomes

### Principles & Constraints

**Non-Negotiables**:
1. **Problem discovery first**: Must surface and validate problems before accepting solutions (enforced via two-part brief structure)
2. **Outcome-focused**: Must shift users from activity-thinking to outcome-thinking (core purpose)
3. **Conversational, not confrontational**: Must feel like helpful advisor, not interrogation (tone critical for adoption)
4. **Evidence-based**: Must prove approach works before expanding (test, measure, iterate)

**Acceptable Trade-offs**:
- **Time investment for value**: Willing to take 15-20 min upfront to save weeks/months later
- **Single-platform start**: Starting Claude Code-only, can expand to other platforms if proven
- **Minimal MVP**: Built as slash command not full application - can evolve based on usage
- **Manual refinement**: Willing to manually improve questions vs building ML/automation early

**Constraints**:
- **Time**: Limited time to build (favor simple, fast iterations)
- **Scope**: Start with `/brief`, expand only if proven necessary
- **Platform**: Currently constrained to Claude Code ecosystem
- **Solo development**: Just me building/refining initially

**Out of Scope** (for now):
- Companion tools (epic breakdown, outcome tracking) until `/brief` proven
- Multi-platform support until approach validated
- Automated learning/improvement (manual refinement is fine)
- Enterprise features (team collaboration, permissions, etc.)
- Integration with project management tools

### Open Questions

**About `/brief` effectiveness**:
- [ ] What types of projects benefit most from problem discovery? (software vs home vs business vs personal)
- [ ] What question patterns work best for different domains?
- [ ] How do we measure "value created" beyond anecdotal evidence?
- [ ] What % of users should we expect to pivot their solution? (30-40% target realistic?)

**About Outcomist scope**:
- [ ] After `/brief` is refined, what's the next highest-value tool?
- [ ] Is brief sufficient or do users need outcome-tracking companion tools?
- [ ] Should this remain personal project or evolve to shareable product?
- [ ] Is Claude Code the right platform long-term or need broader distribution?

**About user adoption**:
- [ ] Will users resist 15-20 min investment before planning?
- [ ] How do we communicate value proposition clearly?
- [ ] What's the right moment to suggest `/brief` to users?

---

## ASSUMPTIONS & RISKS

**Assumptions Made**:
<!-- VALIDATED: Problem-first discovery works (kitchen renovation test) -->
<!-- ASSUMED: Approach generalizes across project types (software, home, business, personal) - needs testing -->
<!-- ASSUMED: 15-20 min investment acceptable if it saves significant resources - needs validation -->
<!-- INFERRED: Claude Code slash command is sufficient for MVP - seems right-sized -->
<!-- ASSUMED: Users can articulate their problems if asked right questions - mostly true but varies -->

**Red Flags Detected**:
<!-- NONE: This brief itself used problem-first discovery, so meta-validation occurred -->
<!-- RISK: Small sample size (1 kitchen test) - need more diverse examples -->
<!-- RISK: Founder doing own testing - may be biased, need external users -->

**Recommendation**:
**PROCEED with user testing (5 diverse projects)**

Problem is real and well-articulated (activity-outcome mismatch in AI). Solution is proven to work (kitchen test) and exists in minimal form (`/brief` v2.0). Right next step is to validate across diverse project types and users.

**Validation Status**: STRONG
- Problem clearly stated (users confuse activities with outcomes)
- Root cause identified (AI accepts activity-statements at face value)
- Solution tested and working (kitchen example)
- Right-sized approach (minimal slash command, not over-engineered)
- Clear path forward (5-project test, then decide next steps)

**Next Step**:
1. Use `/brief` on 5 diverse real projects (mix of software, home, business, personal)
2. Track problem pivot rate, cost avoidance, user feedback
3. Refine questions based on learnings
4. Decide: Is `/brief` sufficient or does Outcomist need companion tools?
