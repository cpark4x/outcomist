# Project Brief Tool - `/brief` (v3.1 - Frictionless Adaptive Discovery)

**Version**: 3.1.0
**Philosophy**: Front-load value, minimize ceremony, offer recommendations over questions

The `/brief` command helps you make better decisions by **immediately delivering value**, then offering the right depth of exploration. Respects that people are busy, want recommendations not interrogation, and need to see value before committing time.

---

## What's New in v3.1

### The Critical Insight from v3.0 Testing

v3.0 was architecturally correct but practically tedious. Through simulated real-world testing, we discovered:
- Context detection felt like bureaucracy when user already stated their ask
- Open-ended questions created cognitive load
- Users wanted recommendations, not interrogation
- No preview of value before time commitment
- Problem-first broke for creation/learning projects
- Expert users had no fast-track escape hatch

**v3.1 fixes this with frictionless intelligence.**

### Five Key Improvements

1. **Intelligent Context Parsing** (NEW)
   - Parses your initial statement BEFORE asking questions
   - Detects urgency keywords → skips directly to Quick Exit
   - Detects validation signals → skips to Validated Builder
   - Detects expertise → minimal questioning
   - **Result**: 0-3 questions instead of 5

2. **Front-Load Immediate Value** (NEW)
   - Gives useful insight BEFORE asking for time
   - "Quick thought: Have you profiled to confirm caching is the bottleneck?"
   - Shows common traps related to your approach
   - **Result**: Value delivered in first 30 seconds

3. **Output Preview Before Commitment** (NEW)
   - Shows exactly what you'll get before asking for time
   - Clear deliverable format preview
   - Options: quick / light / deep / expert fast-track
   - **Result**: Informed choice, no surprises

4. **Recommendations Over Questions** (NEW)
   - AI generates alternatives FOR you, you react
   - "Here are 3 options I see..." instead of "What are your options?"
   - Offers typical constraints, you confirm/correct
   - **Result**: 50% less cognitive load

5. **Expert Fast-Track Mode** (NEW - Mode 0)
   - "I know what I'm doing, just document it"
   - You dictate, AI structures
   - No interrogation, just capture
   - **Result**: 2 minutes for expert documentation

### Five Modes, Not Four

v3.1 adds **Expert Fast-Track** to the four adaptive modes:

0. **EXPERT FAST-TRACK** (< 2 min): "I know what I'm doing, just document it"
1. **QUICK EXIT** (< 2 min): Crisis, validated decisions, sanity checks
2. **LIGHT DISCOVERY** (5-7 min): Experienced users, moderate complexity
3. **DEEP DISCOVERY** (15-20 min): Unclear problems, solution-first framing
4. **VALIDATED BUILDER** (5-10 min): Decision made, need execution planning

**You stay in control** - can switch modes anytime or fast-track if you're the expert.

---

## How To Use v3.1

### 1. Start the conversation

```bash
/brief
```

**New in v3.1**: AI parses your initial statement for context signals BEFORE asking questions.

**Rich statement example** (AI skips to value immediately):
```
User: "I want to add Redis caching to our API. Endpoints are slow."

AI: "Quick thought: Have you profiled to confirm caching is the bottleneck?
     Common trap: adding caching when actual issue is unindexed queries.

     Want me to help validate that?
     • Quick check (< 2 min)
     • Light discovery (5-7 min)
     • You're sure, just document it"
```

**Minimal statement example** (AI asks only missing context):
```
User: "Need help with a decision"

AI: "I'll help you think through this. Quick context:
     1. What's the urgency?
     2. What validation have you done?
     3. Your experience level?

     This helps me give you the right process - 2 to 20 minutes depending on needs."
```

### 2. See what you'll get (NEW)

Before committing time, AI shows output preview:

```
Based on your situation, I recommend LIGHT DISCOVERY (5-7 min):

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
📄 You'll get:
  • Problem validated in your words
  • 3+ alternatives with recommendations
  • Next 3 concrete actions
  • Brief document you can share with team
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

Worth the time?
• Yes, let's do it
• Show me quick version instead
• I'll dictate, you document (expert fast-track)
```

### 3. Work through your mode

Each mode is optimized and **recommendation-first** (NEW):

**Expert Fast-Track** → You dictate, AI documents (no questions)
**Quick Exit** → AI offers gotchas/recommendations, you react
**Light Discovery** → AI offers alternatives/constraints, you refine
**Deep Discovery** → AI hypothesizes problem, you validate
**Validated Builder** → AI proposes execution plan, you adjust

### 4. Get mode-appropriate output

- **Expert Fast-Track**: Brief based on your expert dictation (< 2 min)
- **Quick Exit**: Verbal validation with gotchas (no file unless requested)
- **Light**: Streamlined two-part brief
- **Deep**: Full two-part brief with confidence levels
- **Validated Builder**: Execution plan with milestones and risks

---

## When To Use Each Mode

### Mode 0: EXPERT FAST-TRACK (< 2 min) - NEW

**Perfect for**:
- Expert practitioners: "I've done this 5 times, know exactly what I'm doing"
- Completed thinking: "Already analyzed, just need documentation"
- Team documentation: "Want this structured for team review"
- No time for questions: "Just let me dictate what matters"

**What you get**:
```
✅ Expert Brief Complete

📁 File: /brief/Brief.md

_Note: This brief reflects the user's expert judgment and prior analysis._

# [Your Project]

## Problem & Context
[Your problem description, structured]

## Solution Approach
[Your alternatives, reasoning, chosen approach - as you dictated]

**Next Actions**: [Your next steps]
**Success Criteria**: [Your metrics]
```

**Example flow**:
```
User: "I need to add rate limiting to our API. I've done this 5 times before,
      know exactly what I'm doing. Just want it documented."

AI: "Got it - you're the expert here. Tell me what should go in the brief:
     - What problem are you solving?
     - What alternatives did you consider?
     - Why this approach wins?
     - Success criteria?"

User: [Dictates analysis]

AI: [Generates structured brief in 2 minutes]
```

---

### Mode 1: QUICK EXIT (< 2 min)

**Perfect for**:
- Production crises: "URGENT: API returning 500s, need logging NOW"
- Validated requirements: "PM approved, compliance requires this"
- Quick sanity check: "Just want to verify my thinking before proceeding"
- Micro-decisions: "Should I use async/await or promises?"

**What you get** (NEW - recommendation-first):
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

## Philosophy Improvements in v3.1

### What Changed From v3.0

**v3.0 was architecturally correct:**
- ✅ Adaptive modes based on context
- ✅ Problem-first discovery
- ✅ Quality gates
- ✅ Domain adaptation

**But practically tedious:**
- ❌ Context detection felt bureaucratic
- ❌ Open questions created cognitive load
- ❌ No immediate value before time commitment
- ❌ Didn't respect expert users
- ❌ Repeated information user provided

### v3.1 Core Principles

#### 1. Ruthlessly Simple (preserved)
- Five clear modes (not complex decision trees)
- Context detection is 0-3 questions (down from 5)
- Each mode has single clear purpose
- No elaborate state machines

#### 2. Front-Load Value (NEW)
- Give insight BEFORE asking for time
- Show what they'll get BEFORE commitment
- Recommendations BEFORE questions
- **Philosophy**: Earn the user's time, don't assume it

#### 3. Respects Laziness (NEW)
- People are busy - minimize ceremony
- Parse initial statement for signals
- Don't repeat information user provided
- Offer recommendations over open questions
- **Philosophy**: Cognitive load is a cost; minimize it

#### 4. Trusts Expertise (NEW)
- Expert Fast-Track for experienced users
- "I know what I'm doing" escape hatch
- Don't interrogate validated decisions
- Let experts dictate, AI documents
- **Philosophy**: Expertise should accelerate, not slow down

#### 5. Trusts Emergence (preserved)
- Doesn't force discovery on validated work
- Adapts to what user reveals
- Allows mode switching organically
- Recognizes "enough" naturally

#### 6. Present-Moment Focus (preserved)
- Detects actual urgency immediately
- Serves crises with <2 min validation
- Doesn't over-plan for hypotheticals
- Focuses on decision at hand

### The "People Are Lazy" Insight

Not "lazy" in a negative sense - **cognitively efficient**:
- Want recommendations they can react to, not blank-slate questions
- Want to see value immediately, not after 15 minutes
- Want their expertise recognized, not re-questioned
- Want brevity when urgent, depth when needed

**v3.1 respects this by default.**

---

## Known Limitations & When NOT To Use

v3.1 is significantly better but not perfect. Don't use `/brief` when:

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

### 1. Provide Rich Initial Statements (NEW)

The more context in your opening, the less ceremony:
- ✅ "Need Redis caching (API slow), not urgent, done this before" → Skips detection
- ❌ "Need help" → Full context detection required
- **v3.1 benefit**: Rich statements = immediate value, minimal questions

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
- Say so upfront: "PM validated this with 20 customers"
- AI will skip to Validated Builder immediately (v3.1 improvement)
- Reference PM work, customer research, stakeholder decisions
- AI builds on that foundation, doesn't repeat validation

### 6. Use Expert Fast-Track When Appropriate (NEW)

If you've done the thinking:
- Say "I know what I'm doing, just document it"
- Or choose "expert fast-track" when offered options
- You dictate, AI structures
- 2 minutes to documentation vs 15 minutes of interrogation

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

### v3.1 (Current) - Frictionless Adaptive Discovery
- **NEW**: Intelligent context parsing (parses initial statement before asking)
- **NEW**: Front-load immediate value (insight before questions)
- **NEW**: Output preview before time commitment
- **NEW**: Recommendation-first approach (AI offers, you react)
- **NEW**: Expert Fast-Track mode (Mode 0: dictation, no interrogation)
- **Improved**: 0-3 questions instead of 5 for context detection
- **Improved**: Respects "people are lazy" (cognitively efficient)
- **Improved**: Skips directly to mode when signals detected
- **Preserved**: All v3.0 adaptive intelligence and modes
- **Result**: Dramatically reduced friction, maintained rigor

### v3.0 - Adaptive Decision Support
- **NEW**: Context detection phase (30-90 seconds)
- **NEW**: Four distinct modes (Quick Exit, Light, Deep, Validated Builder)
- **NEW**: Domain-specific question adaptation
- **NEW**: Team/organizational context awareness
- **NEW**: Mode switching during conversation
- **NEW**: Progress indicators throughout
- **Improved**: Respects user expertise and prior work
- **Improved**: Graceful exits for crises and validated work
- **Preserved**: All v2.0 strengths in Deep Discovery mode
- **Limitation**: Context detection felt bureaucratic, open questions created cognitive load

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
# Expert Fast-Track Mode (NEW in v3.1)
---
created: 2025-10-31
mode: expert_dictation
source: user_expertise
---

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
1. Test across all 5 modes (including Expert Fast-Track)
2. Validate context parsing and signal detection works
3. Update this README with learnings
4. Track friction points and cognitive load
5. Share examples where v3.1 improvements shined

---

## The Bottom Line

**v2.0 was powerful** for its sweet spot (unclear problems, high-cost decisions).

**v3.0 was adaptive** but practically tedious (context detection ceremony, open questions).

**v3.1 is frictionless**:
- Front-loads value before asking for time
- Parses your statement before interrogating
- Offers recommendations, you react
- Expert fast-track when you know what you're doing
- Shows what you'll get before you commit

**Same rigor, zero friction.**

---

**Ready to make a better decision?** Run `/brief` and get immediate value. 🎯
