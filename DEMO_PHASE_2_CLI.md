# Outcomist Demo - Phase 2: The CLI Command (/explore)

**Duration**: 4-5 minutes
**Focus**: The core decision exploration engine implemented as a CLI command

---

## Opening (30 seconds)

"In Phase 1, we saw Amplifier - the framework that enables rapid quality development.

Now let's see what we actually built: the /explore CLI command.

This is the heart of Outcomist - an AI-guided decision exploration tool that helps you think through unclear decisions."

---

## The /explore Command (1 minute)

### Show: The Command File

```bash
cd ~/amplifier/outcomist
cat .claude/commands/explore.md | head -100
```

**Talk Through**:
- "This file IS the product"
- "It's a Claude Code slash command - type `/explore` and it runs"
- "300 lines of carefully crafted instructions"
- "Three-phase discovery process built in"

### Show: How to Use It

```bash
# In Claude Code terminal
/explore
```

**User will see**:
```
I'm Outcomist. I help you explore decisions through guided discovery.

What decision are you working through?
```

---

## Live Demo: Decision Exploration (2 minutes)

### Scenario: "Client Work vs Product Development"

**Type**:
```
Client wants ongoing work $6K/month (90% of time).
Means pausing product for 6+ months.
Product has traction (100 users, $2K MRR growing).
Stable money or bet on product?
```

### Phase 1: Deep Discovery (~45 seconds)

**Outcomist responds with**:
- Context-rich questions (not generic ones)
- Probing the actual trade-offs
- Understanding what matters to YOU

**Example questions**:
- "What's driving the product growth right now?"
- "Is the $6K/month covering your needs or just comfortable?"
- "What happens to those 100 users if you pause?"

**Talk Through**:
- "Notice it's not giving advice"
- "It's helping me think through what I know vs what I'm assuming"
- "Building a complete picture before proposing anything"

### Phase 2: Pattern Recognition (~30 seconds)

**Outcomist synthesizes**:
- "Here's what I'm hearing..."
- Reflects back the real tensions
- Identifies what's actually at stake

**Talk Through**:
- "This is where it gets valuable"
- "It's articulating tensions I feel but haven't named"
- "Not solving yet - just making the problem crystal clear"

### Phase 3: Building a Proposal (~45 seconds)

**Outcomist proposes**:
- Specific options with trade-offs
- What each path actually means
- What to consider next

**Example**:
```
Option 1: Hybrid (20% product time)
- Keep product alive, slow client work
- Risk: Half-commit to both

Option 2: Full client commitment
- Stable 6 months, negotiate part-time
- Risk: Product momentum lost

Option 3: Bet on product
- Turn down client, commit fully
- Risk: Income drop during growth phase
```

**Talk Through**:
- "These aren't generic options"
- "They're built from everything we discussed"
- "Each option acknowledges the real trade-offs"

---

## What Makes This Different (1 minute)

### Traditional AI Chat
```
User: "Should I take the client work?"
AI: "Here are pros and cons..." [generic list]
```

### Outcomist (/explore)
```
User: [Describes decision]
AI: [Asks probing questions]
User: [Answers]
AI: [Reflects patterns]
User: [Confirms/clarifies]
AI: [Builds grounded proposal]
```

### Show: The Three-Phase Structure

```bash
cat .claude/commands/explore.md | grep "## Phase" -A 5
```

**Talk Through**:
- "Phase 1: Discovery - 5-7 questions"
- "Phase 2: Review - Reflect what you heard"
- "Phase 3: Propose - Grounded options"
- "This structure is what makes it work"

---

## The Technical Implementation (45 seconds)

### Show: How It Connects to Claude

```bash
cat .claude/commands/explore.md | head -20
```

**Key Points**:
```markdown
You are Outcomist. I help you explore decisions...

# Conversation Management
- Track which phase we're in
- Remember what user said
- Build context progressively

# Quality Guidelines
- No generic advice
- Ground everything in user's specifics
- Acknowledge uncertainty
```

**Talk Through**:
- "This prompt engineering is the product"
- "It's not just 'be helpful' - it's structured guidance"
- "The three phases prevent premature solutions"

---

## Why This Works (30 seconds)

### The Problem It Solves
- "Most decisions aren't information problems"
- "They're framing problems"
- "We know the facts but can't see the pattern"

### How /explore Helps
- "Forces you to externalize what you're thinking"
- "Asks questions you didn't think to ask yourself"
- "Reflects back patterns so you can see clearly"
- "Then helps you build grounded options"

---

## Closing (30 seconds)

"So that's the /explore CLI command - the core of Outcomist.

It's a slash command in Claude Code that runs a structured decision exploration process.

Built in Amplifier's framework, following its principles of simplicity and quality.

In Phase 3, I'll show you the web app that wraps this CLI tool in a beautiful user interface - making it accessible to anyone, not just developers using Claude Code."

---

## Demo Tips

### Terminal Setup
- **Window 1**: Claude Code terminal (for running /explore)
- **Window 2**: File viewer (showing explore.md)
- **Window 3**: Git history (showing development)

### Have These Ready
1. `.claude/commands/explore.md` (the core spec)
2. A real decision to explore (make it personal for authenticity)
3. Answers to likely questions (prepared but natural)

### Timing Notes
- ⏱️ **Don't rush Phase 1** - Let viewers see 2-3 questions
- ⏱️ **Summarize Phase 2** - Don't read entire reflection
- ⏱️ **Highlight Phase 3** - Show how proposal is grounded

### Common Questions

**Q: "Can I use this?"**
A: "Yes! It's a Claude Code slash command. The .claude/commands/explore.md file is the entire implementation. Copy it to your project and it works immediately."

**Q: "Does it work for any decision?"**
A: "It's best for decisions where you have context but unclear framing. Not good for pure information gathering ('what laptop should I buy?') but excellent for trade-off decisions ('should I take this job?')."

**Q: "How accurate is it?"**
A: "It's not about accuracy - it's about clarity. It helps YOU think better. The value is in the process, not the AI's opinion."

**Q: "Why not just use ChatGPT?"**
A: "ChatGPT gives answers. This guides discovery. The three-phase structure prevents premature solutions and builds grounded proposals. Structure matters."

---

## Recording Tips

### Camera Angles
- **Wide**: Show full terminal during interaction
- **Close**: Zoom on key parts of explore.md
- **Switch**: Between live demo and code explanation

### Audio Callouts
- "Watch what question it asks next..."
- "Notice it's not solving - it's clarifying..."
- "Here comes the synthesis..."

### Visual Highlights
- Highlight the three phases in explore.md
- Circle key questions during demo
- Arrow to options in final proposal

---

## Success Metrics

Viewer should understand:
- ✅ What /explore does (guided decision exploration)
- ✅ How it works (three-phase structured process)
- ✅ Why it's different (discovery before solutions)
- ✅ The technical implementation (slash command + prompt)
- ✅ How to use it themselves (copy explore.md)

Next: Phase 3 will show the web app UI wrapping this CLI tool.
