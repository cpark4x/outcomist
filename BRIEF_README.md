# Project Brief Tool - `/brief` (v2.0 - Problem-First)

The `/brief` command helps you discover what problem you're actually solving before committing to a solution. It's designed for the insight that **most people arrive with solutions ("I need X") when they should start with problems ("I can't do Y")**.

## The Core Problem

Most AI tools (and teams) jump straight into building based on vague requests:
- User: "I need a CRM"
- AI: "Great! Let me help you build that..."

This often leads to:
- Building the wrong thing
- Solving symptoms, not root causes
- Missing simpler alternatives
- Wasted resources on solutions that don't move the needle

## What Makes `/brief` Different

**Traditional approach**: "What are you building?" → Elaborate the solution

**`/brief` v2 approach**: "What can't you do today?" → Discover the problem → Explore alternatives → Choose optimal solution

### Key Innovation: Problem-First Discovery

The tool conducts a **two-phase conversation**:

**Phase 0-0.5: Problem Discovery** (NEW in v2)
- Surfaces the real problem before accepting any solution
- Challenges assumed solutions gently
- Explores 2+ alternatives
- Tests if problem is real via "constraint removal"

**Phase 1-4: Solution Planning**
- Once problem validated, plan the implementation
- Document context, users, success criteria, constraints

## What It Creates

The tool generates a **two-part brief** in `/brief/Brief.md`:

### Part 1: Problem Definition
- **What We Can't Do Today** - Problem in outcome terms (not solution terms)
- **Why It Matters** - Quantified impact (time/money/people affected)
- **Current Situation** - How it's handled today, why insufficient
- **Cost of Inaction** - What happens if we do nothing
- **Validation Evidence** - Checkpoints to confirm problem is real

### Part 2: Solution Approach
- **Alternatives Considered** - Minimum 2+ options explored
- **Why This Approach Wins** - Reasoning for chosen solution
- **Simplest Test** - How to validate direction quickly
- **Implementation Details** - Vision, users, success criteria, constraints

**Quality Gate**: Part 2 cannot be written until Part 1 shows validated problem.

## How To Use

### 1. Start the conversation

```bash
/brief
```

The AI will begin with:
> "Let's discover what problem you're solving. Start anywhere - tell me what's on your mind."

### 2. Answer naturally - but expect challenges

If you start with a solution ("I want to build X"):

**Old approach**: "Great! Let me help you plan that..."

**New approach**: "Before we dive into how to build that, help me understand: **what can't you do today?**"

The AI will:
- Probe for the real problem beneath your stated solution
- Ask "constraint removal" questions ("If you couldn't build software, how would you solve this?")
- Surface simpler alternatives
- Test if the problem is real

### 3. Explore alternatives together

Before committing to your solution, the AI will ask:
- "What's the simplest thing that could possibly work?"
- "Could you just use [spreadsheet/existing tool] for now?"
- "What's a $200 version before committing to the $20k version?"

**This isn't confrontational** - it's helping you find the right-sized solution.

### 4. Review the two-part brief

The AI generates Brief.md with:
- **Problem validation status** (Strong/Moderate/Weak)
- **Alternatives you considered** (so you know why you chose this path)
- **Recommended next step** (Proceed OR Test simpler approach first)
- **Flagged assumptions** (areas of uncertainty)

## Example Use Cases

### Example 1: Solution-Locked → Discovered Better Path

**User**: "I need to build a custom CRM for my 20 customers"

**AI**: "Before we plan that, what can't you do today?"

**User**: "Track customer conversations - keep forgetting what we discussed"

**AI**: "How often is this a problem?"

**User**: "Few times a week"

**AI**: "If you couldn't build software, how would you solve this?"

**User**: "I guess... Notion? Or a spreadsheet?"

**AI**: "Why not try that for 2 weeks before building custom?"

**User**: "That's way simpler. Let's test that first."

✅ **Outcome**: Avoided 3 months of building, tested problem with $0 investment

### Example 2: Problem Real, Solution Optimized

**User**: "Renovating kitchen with open floor plan - $60k project"

**AI**: "What can't you do in your current kitchen?"

**User**: "Can't host big family dinners - island only seats 4"

**AI**: "How often is that a problem?"

**User**: "3-4 times a year for holidays"

**AI**: "Rest of the year when it's just you two?"

**User**: "Actually fine, maybe even cozy"

**AI**: "So 3-4 events per year feel cramped. Before $60k renovation - could you extend the island for $2k? Or use workflow changes like buffet in dining room?"

**User**: "Wait... let me test the cheap stuff first"

✅ **Outcome**: Preserved solution direction, found right-sized approach

### Example 3: Problem Validated, Solution Confirmed

**User**: "Building analytics dashboard for product team"

**AI**: "What can't you do today?"

**User**: "Can't tell which features customers actually use - building blind"

**AI**: "Walk me through last time that cost you"

**User**: "Built entire reporting module - 6 weeks - zero usage. $50k wasted."

**AI**: "How often does this happen?"

**User**: "Every quarter we build unused features"

**AI**: "Could you just add logging + use existing BI tool?"

**User**: "Tried - our events are too custom, BI tools can't handle it"

**AI**: "Okay, so you need custom analytics. Why build vs buy?"

**User**: "Evaluated 5 tools - none fit our event schema"

✅ **Outcome**: Problem real, alternatives exhausted, solution validated

## Understanding Solution-Lock

### What is Solution-Lock?

**Solution-lock** is when someone jumps to a specific solution without validating the underlying problem or considering alternatives.

**Signs you're solution-locked:**
- ❌ You describe features, not pain: "It should have X, Y, Z"
- ❌ You use vague benefits: "Streamline our process"
- ❌ You copied someone: "Competitor has this, we need it too"
- ❌ Success = implementation: "Success is when it's deployed"
- ❌ Can't quantify impact: "It will save time" (how much?)
- ❌ Can't explain "why now": "We should probably do this"

### How `/brief` Helps

The tool uses **constraint removal tests** to surface real problems:

**Question**: "If you couldn't use software, how would you solve this?"

**Why this works**: Forces you to articulate the problem independent of your assumed solution. If you can't answer, the problem might not be real.

**Question**: "What's the dumbest, fastest way to test if this matters?"

**Why this works**: Reveals if you need the expensive solution or if a simple test would validate the problem first.

## The Two-Part Structure

### Why Two Parts?

**Part 1 must be complete** before Part 2 can be written. This enforces:
- Problem clarity before solution commitment
- Impact quantification before resource allocation
- Alternative exploration before building

**Quality Gates**:

Before moving to Part 2, you must have:
- [ ] Problem stated independently of any solution
- [ ] Impact quantified (numbers, not "it will be better")
- [ ] Concrete example of problem occurring
- [ ] Considered 2+ alternatives including "do nothing"

### What If Problem Validation Is Weak?

If the AI can't validate your problem strongly, the brief will:
- Flag it in `problem_validated: false` front-matter
- Document assumptions and risks explicitly
- Recommend testing simpler approach first
- Proceed with caution, not confidence

**This is a feature, not a bug** - it's better to know your foundation is shaky than to build confidently on sand.

## Tips for Best Results

### Start With Problem-Talk, Not Solution-Talk

❌ **Solution-talk**: "I need a CRM"
✅ **Problem-talk**: "I keep losing track of customer conversations"

❌ **Solution-talk**: "Need to renovate kitchen"
✅ **Problem-talk**: "Can't host family dinners comfortably"

### Quantify Everything

❌ "Wastes time"
✅ "Wastes 5 hours per week"

❌ "Costs money"
✅ "Costs $800/month in restaurants"

❌ "Happens often"
✅ "Happens daily with 20 customers"

### Be Open to Alternatives

The AI will ask "What if you just [simpler thing]?"

**Don't get defensive** - this is helping you find the right solution.

If your solution is best, you'll be able to explain why it beats alternatives. If you can't, that's valuable information.

### Use "Constraint Removal" Tests

When stuck, ask yourself:
- "If I couldn't build anything, how would I solve this?"
- "What's the cheapest way to test if this matters?"
- "If this magically worked tomorrow, what would I do differently?"

These questions reveal if you're attached to a solution or actually solving a problem.

## Advanced: When to Skip Problem Discovery

Some users have already done deep problem validation. You can say:

**"Skip to solution - I've validated the problem elsewhere"**

The AI will note this and proceed directly to implementation planning.

## Troubleshooting

### "The AI keeps challenging my solution"

**Why**: You might be solution-locked. The AI is helping you discover if there's a simpler path.

**Try**: Answer the "what can't you do today?" question without mentioning your solution.

### "I don't know how to quantify the impact"

**Why**: Problem might not be concrete enough yet.

**Try**: Think of the last time this problem hit you. What did it cost in time/money/stress?

### "The brief says 'Weak validation'"

**Why**: AI couldn't verify the problem is real with quantified impact.

**Action**: Either do more research to validate, or test a simpler approach first.

### "This is taking longer than 15 minutes"

**Why**: Deep problem discovery takes time if you started solution-locked.

**Options**:
1. Keep going - this time investment saves months later
2. Say "Skip to solution" if you've done this validation elsewhere

## Philosophy

### Outcomes Over Activities

**Activity-thinking**: "Renovate kitchen" (what you'll do)
**Outcome-thinking**: "Reduce family meal stress" (what will change)

`/brief` forces outcome-thinking by asking "what can't you do?" before "what will you build?"

### Test, Don't Guess

**Guessing**: "I think users need X"
**Testing**: "Let me try Y for 2 weeks and see if it solves the problem"

`/brief` pushes for simple tests before expensive solutions.

### Right-Sized Solutions

**Over-engineering**: "$60k full renovation"
**Right-sizing**: "$2k island extension - test first, then decide"

`/brief` surfaces the $200 version before committing to the $20k version.

## Integration with Development

### Before Planning
Run `/brief` to ensure you're solving a real problem

### During Planning
Reference Part 1 (Problem Definition) to keep focused on outcomes

### During Implementation
Check: Does this feature tie back to the validated problem?

### After Launch
Measure against Part 2 (Success Criteria) - did solving the problem create the expected outcome?

## Technical Details

### File Locations
```
outcomist/
└── brief/
    └── Brief.md  (two-part structure)
```

### Front-Matter
```yaml
---
created: 2025-10-31
updated: 2025-10-31
status: draft
owner: your@email.com
problem_validated: true/false
alternatives_explored: true/false
---
```

### Command Location
```
outcomist/
└── .claude/
    └── commands/
        └── brief.md  (v2.0 - problem-first)
```

## Version History

### v2.0 (Current) - Problem-First Discovery
- Added Phase 0: Problem Discovery (before solution acceptance)
- Added Phase 0.5: Solution Exploration (alternatives required)
- Two-part brief structure with quality gates
- Solution-lock detection and gentle challenges
- Constraint removal tests
- "What if you couldn't build anything?" questions

### v1.0 - Solution Elaboration
- Single-phase conversation
- Anchored on "What are you building?"
- Single Brief.md output
- No alternative exploration

## Success Metrics

Track these to measure `/brief` effectiveness:

1. **Problem Pivot Rate**: % of briefs where user changed their solution after problem discovery
2. **Alternative Exploration**: % of briefs documenting 2+ alternatives
3. **Validation Strength**: % of briefs with "Strong" problem validation
4. **Cost Avoidance**: Instances where simpler solution was tested first

**Target**: 30-40% of users should reconsider or optimize their solution after problem discovery

## Contributing

If you improve the `/brief` command:
1. Test on real projects first
2. Update this README with learnings
3. Share examples of good problem discovery
4. Track if changes increase problem pivot rate

---

**Ready to discover your real problem?** Run `/brief` and let's find out what you're actually trying to solve! 🎯
