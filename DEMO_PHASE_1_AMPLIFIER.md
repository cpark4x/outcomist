# Outcomist Demo - Phase 1: Building with Amplifier

**Duration**: 3-4 minutes
**Focus**: The framework and philosophy that enables rapid, quality product development

---

## Opening (30 seconds)

"I want to show you how I built Outcomist - a decision exploration tool - in just a few days. But more importantly, I want to show you *how* it was built, because the process is as interesting as the product.

This is Phase 1: Understanding Amplifier - the framework that made this possible."

---

## What is Amplifier? (1 minute)

### Show: Repository Structure

```bash
cd ~/amplifier
tree -L 1
```

**Talk Through**:
- "Amplifier is my personal framework for building products with AI assistance"
- "Each project lives as a subdirectory: outcomist, remember-twelve, ridecast..."
- "They all share common patterns, agents, and philosophy"

### Show: Key Files

```bash
cat AGENTS.md | head -30
```

**Talk Through**:
- "AGENTS.md defines how AI agents should work on my projects"
- "It embeds my development philosophy: ruthless simplicity, spec-driven development"
- "Every project inherits these principles automatically"

### Show: Shared Context

```bash
cat ai_context/IMPLEMENTATION_PHILOSOPHY.md | head -40
```

**Key Points**:
- "Wabi-sabi philosophy: simplicity and the essential"
- "Occam's Razor: as simple as possible, but no simpler"
- "Trust in emergence: complex systems from simple components"

---

## The Amplifier Advantage (1 minute)

### Traditional Development
```
Idea → Months of coding → Launch
- Start from scratch each time
- Reinvent patterns
- Inconsistent quality
```

### Amplifier Development
```
Idea → Spec → AI builds with shared context → Launch in days
- Shared patterns across projects
- Consistent philosophy
- Quality guardrails built-in
```

### Show: The Evidence

**Terminal 1 - Git History**:
```bash
cd ~/amplifier/outcomist
git log --oneline --graph | head -20
```

**Talk Through**:
- "Built in 5 days"
- "Each commit follows established patterns"
- "Claude Code as co-author on every commit"

**Terminal 2 - Code Quality**:
```bash
cat outcomist-demo/src/components/layout/Header.svelte
```

**Talk Through**:
- "Clean, readable code"
- "Consistent design tokens (--space-*, --blue-500)"
- "Accessibility built-in, not bolted on"
- "This quality comes from Amplifier's embedded standards"

---

## How It Works: Spec-Driven Development (1 minute)

### Show: Project Structure

```bash
tree -L 2 ~/amplifier/outcomist
```

**Talk Through**:
```
outcomist/
├── docs/               # Vision, epics, features
│   ├── vision/
│   ├── epics/
│   └── patterns/
├── .claude/            # AI agent commands
│   └── commands/
│       └── explore.md  # The core /explore logic
└── outcomist-demo/     # The web app
    ├── src/
    └── server.js
```

### Show: The /explore Specification

```bash
cat .claude/commands/explore.md | head -60
```

**Key Points**:
- "This 300-line file IS the product specification"
- "It defines the three-phase discovery process"
- "The AI builds code that implements this spec"
- "Spec-first means quality is defined before implementation"

---

## The Three Pillars (45 seconds)

### 1. Philosophy (AGENTS.md)
- "How we build: simply, accessibly, thoughtfully"

### 2. Patterns (ai_context/)
- "What we build: modular, regeneratable components"

### 3. Specs (docs/, .claude/)
- "What it should do: behavior defined before code"

**Together**:
- "This creates a 'recipe' for rapid, quality development"
- "Each project I build gets faster because patterns compound"

---

## Closing (30 seconds)

"So that's Amplifier: a framework that embeds quality, philosophy, and patterns into every project I build.

In Phase 2, I'll show you the actual Outcomist CLI tool that was built using this framework.

And in Phase 3, we'll see the web app that wraps it all up into a user-friendly interface.

But it all starts here - with Amplifier providing the foundation for rapid, quality product development."

---

## Demo Tips

### Terminal Setup
- **Window 1**: Repository navigation
- **Window 2**: File viewing (cat, less)
- **Window 3**: Git commands

### Key Files to Have Ready
1. `~/amplifier/AGENTS.md`
2. `~/amplifier/ai_context/IMPLEMENTATION_PHILOSOPHY.md`
3. `~/amplifier/outcomist/.claude/commands/explore.md`
4. `~/amplifier/outcomist/docs/vision/product-vision-v2.md`

### Common Questions

**Q: "Is this just a template?"**
A: "No, it's a living framework. Each project adds patterns that future projects benefit from. Remember Twelve taught me about profile learning. Outcomist teaches about decision exploration. The next project will leverage both."

**Q: "Can I use Amplifier?"**
A: "It's my personal framework, but the principles are universal: embed your philosophy in shared context, use specs to define behavior, let AI handle implementation within quality guardrails."

**Q: "How much is AI vs you?"**
A: "I define what and why. AI handles how. The Amplifier framework ensures 'how' follows my standards. It's collaborative: I'm the architect, AI is the builder, Amplifier is the quality inspector."

---

## Success Metrics

Viewer should understand:
- ✅ What Amplifier is (framework for AI-assisted development)
- ✅ Why it matters (speed + quality + consistency)
- ✅ How it works (philosophy + patterns + specs)
- ✅ The advantage (rapid development without sacrificing quality)

Next: Phase 2 will show the actual CLI tool built with this framework.
