# Project Brief Tool - `/brief` (v3.0 - Adaptive Decision Support)

**Version**: 3.0.0
**Philosophy**: Context-aware advisor that adapts to YOUR needs

The `/brief` command helps you make better decisions by understanding your situation first, then guiding you through the appropriate discovery process. Not all decisions need 20 minutes of interrogation - some need quick validation, others need deep exploration.

---

## What's New in v3.0

### The Critical Insight from v2.0 Testing

v2.0 worked brilliantly for its sweet spot (unclear problems, high-cost decisions) but had blind spots:
- Treated all users as if they needed full discovery
- No escape hatch for crises or validated work
- Didn't recognize domain expertise
- Forced process on team-validated decisions

**v3.0 fixes this with adaptive intelligence.**

### Four Modes, Not One Process

v3.0 starts with **context detection** (30-90 seconds) to understand:
- What's the urgency?
- What exploration has already happened?
- What's your expertise level?
- Are you solo or working with a team?

Then routes you to the right mode:

1. **QUICK EXIT** (< 2 min): Crisis, validated decisions, expert practitioners
2. **LIGHT DISCOVERY** (5-7 min): Experienced users, moderate complexity
3. **DEEP DISCOVERY** (15-20 min): Unclear problems, solution-first framing
4. **VALIDATED BUILDER** (5-10 min): Decision made, need execution planning

**You stay in control** - can switch modes anytime by saying "go deeper" or "speed up".

---

## How To Use v3.0

### 1. Start the conversation

```bash
/brief
```

The AI begins with context detection:

> "I'll help you think through this decision. First, let me understand your situation with a few quick questions:
>
> 1. What are you trying to decide?
> 2. Is this urgent, or can we take time to explore?
> 3. Have you or your team already done any exploration or validation?
> 4. What's your experience level in this domain?"

### 2. Get routed to the right mode

Based on your answers:

```
Based on your situation, I recommend LIGHT DISCOVERY:
- Estimated time: 5-7 minutes
- We'll focus on: validating problem and exploring alternatives
- You can switch modes anytime: say "go deeper", "speed up", or "just validate"

Sound good?
```

### 3. Work through your mode

Each mode is optimized for its use case:

**Quick Exit** → Sanity check, gotchas, done
**Light Discovery** → Problem essence, constraints, alternatives, decision factors
**Deep Discovery** → Full problem excavation like v2.0
**Validated Builder** → Validate foundation, plan execution

### 4. Get mode-appropriate output

- **Quick Exit**: Conversation summary (no file unless requested)
- **Light**: Streamlined two-part brief
- **Deep**: Full two-part brief with confidence levels
- **Validated Builder**: Execution plan with milestones and risks

---

## When To Use Each Mode

### Mode 1: QUICK EXIT (< 2 min)

**Perfect for**:
- Production outages: "API returning 500s, need logging"
- Validated requirements: "PM approved, just need to execute"
- Expert decisions: "I've done this 10 times, just want sanity check"
- Micro-decisions: "async/await or promises?"

**What you get**:
```
✅ Quick Validation Complete

**Decision**: Add error logging to login endpoint

**Key Considerations**:
- Watch for PII in logs
- Deploy with feature flag
- Monitor log volume

**Next Action**: Deploy logging update, check last 24hr errors

Need full brief? Say "write it up"
Otherwise, proceed!
```

---

### Mode 2: LIGHT DISCOVERY (5-7 min)

**Perfect for**:
- Experienced users: "I've thought about this some"
- Moderate complexity: "Adding caching to our API"
- Some validation done: "Talked to a few people"
- Clear domain: Software, home, business with known patterns

**Process**:
1. Problem essence (90 sec)
2. Constraint exploration (90 sec)
3. Alternatives sweep (90 sec)
4. Decision factors (60 sec)
5. Domain-specific questions (90 sec)
6. Streamlined brief (60 sec)

**What you get**: Focused two-part brief with problem validation, alternatives, and next actions

---

### Mode 3: DEEP DISCOVERY (15-20 min)

**Perfect for**:
- Unclear problems: "Something feels off..."
- Solution-first framing: "We need to migrate to X"
- High complexity: Many unknowns, vague requirements
- No prior exploration: "Just starting to think about this"

**Process** (preserved from v2.0 with improvements):
1. Problem excavation (4-5 min) + NEW: Team/org context
2. Alternatives exploration (4-5 min)
3. Context & details (3-4 min)
4. Synthesis & validation (2-3 min)
5. Full brief generation (2-3 min)

**What you get**: Complete two-part brief with:
- Confidence level (High/Medium/Low)
- Team/org context
- Reversibility assessment
- Comprehensive alternatives analysis

---

### Mode 4: VALIDATED BUILDER (5-10 min)

**Perfect for**:
- Decision already made: "We've decided to build notifications"
- Prior discovery complete: "PM validated with customer research"
- Need execution help: "Just need to plan implementation"
- Stakeholder-driven: "Leadership mandated this"

**Process**:
1. Validate the validation (90 sec) - sanity check without repeating work
2. Solution planning (4-5 min) - approach, risks, team, timeline
3. Execution brief (2-3 min)

**What you get**: Execution-focused brief with:
- Milestones and checkpoints
- Risks and mitigation plans
- Team and stakeholder map
- Success criteria

---

## Domain Adaptation

v3.0 automatically detects your domain and adapts questions:

### Software Projects
- "How does this fit existing architecture?"
- "What's team expertise with [technology]?"
- "What happens at 10x current scale?"
- "What's the maintenance burden long-term?"

### Home/Personal Projects
- "What's 5-year total cost including maintenance?"
- "Do you have time/skills for ongoing upkeep?"
- "Impact on home value or future flexibility?"
- "Have you vetted contractors/gotten quotes?"

### Business Initiatives
- "Who are key stakeholders and what do they care about?"
- "What organizational change is required?"
- "What's the cost of delay? Expected ROI timeline?"
- "Does team have bandwidth for this?"

### Career Decisions
- "What matters most in your career?"
- "Where do you want to be in 2-3 years?"
- "What are you willing to sacrifice? Not willing?"
- "How easy to change course if this doesn't work?"

---

## Examples Across Modes

### Example 1: Crisis → Quick Exit

**User**: "Production API is returning 500s on login endpoint. I need to add error logging."

**Context Detection**: Urgent crisis
**Mode**: Quick Exit (< 2 min)

**Process**:
- Validate framing: One-sentence summary
- Sanity check: "Watch out for PII in logs"
- Output: Verbal validation, no file

**Result**: User unblocked immediately, proceeds with confidence

---

### Example 2: Experienced → Light Discovery

**User**: "I want to add Redis caching to our API. I've thought about it some - endpoints are getting slow."

**Context Detection**: Moderate experience, some thought
**Mode**: Light Discovery (5-7 min)

**Process**:
- Problem: "What's actually slow? Have you profiled?"
- Constraint: "Is caching the bottleneck or unindexed queries?"
- Alternatives: Database indexing, query optimization, caching
- Domain: Software-specific scale questions

**Result**: User discovers unindexed queries are actual problem. Tries indexing before adding Redis complexity.

---

### Example 3: Solution-First → Deep Discovery

**User**: "We need to migrate from PostgreSQL to MongoDB. It's more modern."

**Context Detection**: Solution-first framing, borrowed thinking
**Mode**: Deep Discovery (15-20 min)

**Process**:
- Problem excavation: "What can't you do with Postgres?"
- Constraint removal: "If DB wasn't the constraint, what would you change?"
- Alternatives: Stay with Postgres, optimize queries, evaluate actual problem
- Validation: "Is 'modern' solving a real problem?"

**Result**: User realizes no actual problem with Postgres. MongoDB doesn't solve anything. Stays with Postgres, invests time elsewhere.

---

### Example 4: Validated → Validated Builder

**User**: "Our PM validated we need a notification system with customer research. We've decided to build it. Need help planning execution."

**Context Detection**: Decision made, prior validation complete
**Mode**: Validated Builder (5-10 min)

**Process**:
- Validate validation: Quick sanity check on foundation
- Execution planning: Milestones, risks, team, timeline
- Execution brief: Implementation-focused output

**Result**: Execution-focused brief with milestones, team plan. References PM's prior discovery.

---

## Switching Modes Mid-Conversation

You're always in control. Switch modes by saying:

- **"Go deeper"** → Move to more thorough mode
- **"Speed up"** → Move to lighter mode
- **"Just validate this"** → Jump to Quick Exit

The AI also watches for signals to suggest switching:

**Quick Exit → Light/Deep**:
- Sanity check reveals unclear problem
- Complexity emerges unexpectedly

**Light → Deep**:
- Problem definition still unclear after 3 minutes
- More unknowns than expected

**Deep → Light**:
- Problem becomes clearer fast
- User signals time pressure: "Can we speed this up?"

---

## Philosophy Improvements in v3.0

### Ruthlessly Simple
- Four clear modes, not complex decision trees
- Context detection is 3-5 questions max
- Each mode has single clear purpose
- No elaborate state machines

### Trusts Emergence
- Doesn't force discovery on validated work
- Adapts to what user reveals
- Allows mode switching organically
- Recognizes "enough" naturally

### Respects User Agency
- Transparent about time/process upfront
- User can switch modes or exit anytime
- **Validates user's expertise and prior work** (NEW)
- **Doesn't assume user is wrong** (NEW - Quick Exit mode)
- Shows progress and options throughout
- Always asks permission before proceeding

### Present-Moment Focus
- **Detects actual current context** (NEW)
- **Quick Exit serves real urgency** (NEW)
- Doesn't over-plan for hypotheticals
- Focuses on decision at hand

---

## What's Preserved from v2.0

v3.0 keeps all the strengths of v2.0 in Deep Discovery mode:

✅ Problem-first discovery
✅ Constraint removal tests
✅ Solution-lock detection
✅ Alternatives exploration required
✅ Two-part brief structure
✅ Quality gates
✅ Gentle, curious tone

**New**: v3.0 adds context awareness so these strengths apply when appropriate, not universally.

---

## Success Metrics (Updated for v3.0)

### Process Metrics
1. **Mode Distribution**: % of sessions in each mode
   - Target: Diverse distribution (not 90% in one mode)
2. **Mode Switches**: % of sessions that switch modes
   - Target: 10-20% (indicates good responsiveness)
3. **Completion Rate**: % of sessions completed vs abandoned
   - Target: 70%+ (v2.0 baseline: 50-60%)

### Outcome Metrics
4. **Problem Pivot Rate**: % where user changes solution after discovery
   - Target: 30-40% in Deep Discovery mode
   - Target: 10-20% in Light Discovery mode
5. **Time Efficiency**: User satisfaction with time invested
   - Target: 80%+ say "time was worth it"
6. **Cost Avoidance**: Documented cases of waste prevented
   - Target: 5+ significant examples per quarter

---

## Known Limitations & When NOT To Use

v3.0 is better but not perfect. Don't use `/brief` when:

### 1. Pure Execution Tasks
**Example**: "Format this code snippet"
**Why**: No decision to make, just do it

### 2. Pure Learning
**Example**: "Teach me React hooks"
**Why**: Learning is the outcome, not a decision

### 3. Already Deep In Implementation
**Example**: "Debug this error message"
**Why**: Discovery phase is past, you're in execution

### 4. Extremely Simple Choices
**Example**: "Tabs or spaces?"
**Why**: Just pick one and move on

### 5. Creative Exploration
**Example**: "Help me brainstorm ideas"
**Why**: Brainstorming needs divergent thinking, not convergent decision-making

---

## Tips for Best Results

### 1. Be Honest in Context Detection

The routing only works if you're honest:
- ✅ "I haven't really thought about this much" → Deep Discovery
- ❌ "I'm sure about this" (when you're not) → Wrong mode, poor results

### 2. Trust the Process

If routed to Deep Discovery when you wanted Quick Exit:
- The AI detected something in your framing
- Give it 3-4 minutes before requesting mode switch
- Often reveals blindspots you didn't see

### 3. Speak Up About Time

If time becomes a constraint mid-conversation:
- Say "Can we speed this up?"
- AI will offer to switch to lighter mode
- You stay in control

### 4. Use "Write It Up" Strategically

In Quick Exit mode, output is verbal by default.

Say "write it up" if:
- Need to reference later
- Want to share with team
- Building body of decision docs

### 5. Reference Prior Work

If your team did discovery:
- Say so in context detection
- Reference PM work, customer research, stakeholder decisions
- AI will route to Validated Builder and build on that foundation

---

## Troubleshooting

### "I got routed to Deep Discovery but don't have 20 minutes"

**Solution**: Say "I only have 5 minutes, can we do Light Discovery instead?"

The AI will switch modes and focus on essentials.

### "Quick Exit didn't give me enough detail"

**Solution**: Say "write it up" to get a full brief document, or "go deeper" to switch to Light Discovery.

### "I'm in Light Discovery but need more depth"

**Solution**: Say "go deeper" or "this is more complex than I thought."

AI will offer to switch to Deep Discovery mode.

### "The AI is challenging my solution and I'm getting defensive"

**Possible causes**:
1. You're solution-locked and the AI spotted it (this is helpful!)
2. You have domain expertise the AI doesn't recognize (say "I'm an expert in this")
3. You've already validated elsewhere (say "this is validated, just need execution help")

**Solution**: Be explicit about what you know and what you need.

---

## Version History

### v3.0 (Current) - Adaptive Decision Support
- **NEW**: Context detection phase (30-90 seconds)
- **NEW**: Four distinct modes (Quick Exit, Light, Deep, Validated Builder)
- **NEW**: Domain-specific question adaptation
- **NEW**: Team/organizational context awareness
- **NEW**: Mode switching during conversation
- **NEW**: Progress indicators throughout
- **Improved**: Respects user expertise and prior work
- **Improved**: Graceful exits for crises and validated work
- **Preserved**: All v2.0 strengths in Deep Discovery mode

### v2.0 - Problem-First Discovery
- Added Phase 0: Problem Discovery
- Added Phase 0.5: Solution Exploration
- Two-part brief structure with quality gates
- Solution-lock detection
- Constraint removal tests
- **Limitation**: One-size-fits-all approach

### v1.0 - Solution Elaboration
- Single-phase conversation
- Anchored on "What are you building?"
- No alternative exploration
- **Limitation**: Accepted solutions without problem validation

---

## Technical Details

### File Locations
```
outcomist/
└── brief/
    └── Brief.md  (format varies by mode)
```

### Front-Matter (Mode-Specific)
```yaml
# Deep Discovery Mode
---
created: 2025-10-31
mode: deep_discovery
problem_validated: true/false
alternatives_explored: true/false
confidence: high/medium/low
---

# Light Discovery Mode
---
created: 2025-10-31
mode: light_discovery
confidence: high/medium/low
---

# Validated Builder Mode
---
created: 2025-10-31
mode: validated_builder
decision_validated: [reference to prior work]
---
```

### Command Location
```
outcomist/
└── .claude/
    └── commands/
        └── brief.md  (v3.0 - adaptive)
```

---

## Contributing

If you improve `/brief`:
1. Test across all 4 modes
2. Validate mode detection logic works
3. Update this README with learnings
4. Track metrics for your domain
5. Share examples of good adaptations

---

## The Bottom Line

**v2.0 was a powerful tool for its sweet spot** (unclear problems, high-cost decisions).

**v3.0 is a flexible advisor** that meets you where you are:
- Crisis? Quick validation.
- Experienced? Light discovery.
- Unclear? Deep exploration.
- Validated? Execution planning.

**Same rigor, better fit.**

---

**Ready to make a better decision?** Run `/brief` and let's understand your situation first. 🎯
