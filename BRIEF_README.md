# Project Brief Tool - `/brief`

The `/brief` command helps you create structured project specifications before starting any work. It's designed to extract clarity about what you're building, why, for whom, and how success will be measured.

## Purpose

Most AI tools (and teams) jump straight into building based on vague requests. This often leads to:
- Building the wrong thing
- Misaligned expectations
- Unclear success criteria
- Wasted effort

`/brief` solves this by conducting a focused interview that helps you think through your project systematically. Even if you don't know exactly what you want, the conversation helps you discover it.

## What It Creates

The tool generates a single comprehensive markdown file in a `/brief` folder:

**Brief.md** - A structured document containing:
- **Vision** - Why this project exists, what success looks like
- **Problem** - What you're solving, for whom, why now
- **Success Criteria** - Measurable outcomes and timeline
- **Users** - Who will use this, their needs and context
- **Principles & Constraints** - Core rules, trade-offs, boundaries
- **Open Questions** - Flagged assumptions to research

This becomes your **canonical source of truth** - all features, designs, and decisions reference back to this brief.

## How To Use

### 1. Start the conversation

```bash
/brief
```

The AI will begin interviewing you with questions like:
- "What are you building?"
- "Who's your primary user?"
- "What's broken right now that this fixes?"
- "What does success look like in 3 months?"

### 2. Answer naturally

Respond conversationally. The AI will:
- Ask follow-up questions based on your answers
- Probe for specifics when you're vague
- Challenge assumptions
- Extract trade-offs and constraints

**Duration**: As long as needed for clarity (typically 10-15 minutes)

### 3. Review and refine

The AI generates Brief.md with:
- Simple YAML front-matter (timestamps, status, owner)
- Clear sections with your synthesized answers
- Completeness validation (all critical elements present)
- Flagged gaps or open questions

### 4. Use as foundation

All subsequent work references the brief:
- Features must map to problems in Problem section
- Success tracked via metrics in Success Criteria section
- Users validated against Users section
- Decisions aligned with Principles & Constraints section

## Example Use Cases

- **App development**: "Build a mobile app for tracking workouts"
- **Home projects**: "Remodel my kitchen"
- **Personal goals**: "Lose 20 pounds"
- **Business initiatives**: "Launch a new product line"
- **Process improvements**: "Reduce deployment time"

The tool works for **any type of project** - software, physical, personal, business.

## Tips for Best Results

### Be Specific
❌ "I want better analytics"
✅ "I can't tell which features users actually use, so I waste time building the wrong things"

### Name Real People
❌ "For business users"
✅ "For Sarah, our sales manager who spends 2 hours/day in spreadsheets"

### Use Numbers
❌ "Make it faster"
✅ "Reduce processing time from 5 minutes to 30 seconds"

### State Trade-offs
❌ "I want it fast, cheap, and high-quality"
✅ "I'll accept rough UX if we can ship in 2 weeks"

### Describe Current State
❌ "We need a better solution"
✅ "Right now people email CSV files back and forth, which breaks when files get too large"

## Understanding the Output

### Front-matter (YAML)
The brief starts with simple metadata:
```yaml
---
created: 2025-10-30
updated: 2025-10-30
status: draft
owner: your@email.com
---
```

**Status values:**
- **draft**: Initial version, being refined
- **approved**: Ready to use, team aligned
- **archived**: Superseded or abandoned

Update the `updated` timestamp whenever you make changes.

### Quality Indicators
Look for:
- ✅ Specific users (not generic "users")
- ✅ Measurable outcomes (numbers, behaviors)
- ✅ Explicit trade-offs stated
- ✅ Real constraints identified
- ✅ Timeline with stakes

### Red Flags
Watch for:
- ⚠️ Generic terms ("better", "improved", "users")
- ⚠️ No metrics or success criteria
- ⚠️ No trade-offs (wants everything)
- ⚠️ Vague timeline ("ASAP", "soon")
- ⚠️ No constraints mentioned

## Iterating on Your Brief

Briefs evolve as you learn. That's expected and good!

### When to Update
- User research reveals new insights
- Technical constraints discovered
- Market conditions change
- Priorities shift

### How to Update
1. Edit Brief.md directly
2. Update `updated` timestamp in front-matter
3. Consider changing `status` if major shifts occur
4. Document what changed and why (add notes in the brief or commit message)

### Track Evolution
Use git to see how your thinking evolved:
```bash
git log brief/Brief.md
git diff HEAD~1 brief/Brief.md
```

## Integration with Development

### Planning Phase
- Features reference problems from Problem section
- User stories reference users from Users section
- Success criteria become KPIs

### Design Phase
- User journeys inform designs
- Principles guide decisions
- Trade-offs clarify what to optimize for

### Implementation Phase
- All features must trace back to brief
- Scope changes require brief updates
- Principles validate technical decisions

### Review Phase
- Success measured against Success Criteria
- User validation against Users section
- Anti-goals ensure boundaries

## Philosophy

The `/brief` tool embodies several key principles:

### Clarity Before Code
Building without clarity is expensive. 15 minutes of thinking saves weeks of building the wrong thing.

### Falsifiability
"We'll know it works when X happens" is more valuable than "make it better."

### Alignment
Everyone working on the project has the same source of truth. No hidden assumptions.

### Evolution Over Perfection
Briefs don't need to be perfect - they need to be clear enough to start. They'll evolve as you learn.

### User-Centric
The brief forces you to name specific people with real problems, not abstract "users."

## Troubleshooting

### "The AI keeps asking vague questions"
This usually means you're giving vague answers. Try:
- Give concrete examples
- Name specific people or situations
- Use numbers and timelines
- Describe current behavior

### "The brief feels incomplete"
Check if you have all critical elements:
- Specific user (not "users")
- Concrete problem (not "better")
- Measurable success (numbers/behaviors)
- Timeline with stakes
- Binding constraint identified
- Explicit trade-off stated

### "I don't know the answer to some questions"
That's fine! Say "I don't know yet" and the AI will help you think it through, or flag it as an open question to research.

### "The conversation is taking too long"
If you're past 15 minutes:
- You might be overthinking - aim for "clear enough to start"
- Consider stopping and resuming after you research unknowns
- Check if you're being specific enough (vague answers require more probing)

## Next Steps After Creating a Brief

1. **Review with stakeholders** - Ensure alignment
2. **Identify open questions** - Research gaps
3. **Create epics/features** - Break down the work (future tool)
4. **Start building** - With confidence and clarity
5. **Measure outcomes** - Track against metrics in `outcome.md`
6. **Update as you learn** - Version and evolve

## Technical Details

### File Locations
```
outcomist/
└── brief/
    └── Brief.md
```

### Command Location
```
outcomist/
└── .claude/
    └── commands/
        └── brief.md    # The slash command implementation
```

### Dependencies
- None! Pure conversational AI, no code execution needed
- Works in any Claude Code environment

## Contributing

If you improve the `/brief` command:
1. Test it on a real project first
2. Update this README with learnings
3. Consider if changes should be versioned (major/minor/patch)
4. Share insights on what questioning patterns work best

## License

Part of the outcomist project. See main project README for license details.

---

**Ready to create your first brief?** Run `/brief` and let's get started!
