# Outcomist

**AI drives activity, not outcomes. Outcomist helps you figure out what you actually want before taking action.**

People frame decisions wrong. They ask AI to execute before they've clarified the real question. Outcomist surfaces what's actually being decided — then helps you act on it.

---

## What it actually does

Three real examples:

**"Should I take $6K/month client work or focus on my $2K MRR product?"**
Outcomist revealed: $60K savings (12-14 months runway), product grew 4X in 6 months, 97% retention rate. The "stable client" was $40/hour when broken down. *"The scarcity is in your head, not your bank account."* Recommendation: say no, go all in on the product.

**"10 customers want Feature X, 2 customers want Feature Y. Which should I build?"**
Outcomist revealed a product identity crisis — Feature X serves employers pushing RTO, Feature Y serves employee safety. They can't coexist. Recommendation: build Feature Y, clarify who you're actually building for.

**"I want to redesign my office to make it more inspiring"**
Outcomist revealed the real need was a personal sanctuary — games, memorabilia, a retreat space — not work optimization. Two completely different rooms.

---

## How it works

```
/explore [your decision or question]
```

1. **Pattern recognition** (30 sec) — identifies what's really being decided and reframes it
2. **Targeted questions** (5–10 min) — builds context one question at a time, adapts based on your answers
3. **Clear recommendation** — specific to your situation with concrete next actions

No hedging. No "here are 7 options." A clear stance.

---

## Quick start

### CLI (Claude Code)

```
/explore Should I hire a contractor or build this myself?
```

### Python library (v2.0)

```python
from outcomist_core import DiscoveryFlow
from outcomist_core.llm import AnthropicProvider

flow = DiscoveryFlow(llm_provider=AnthropicProvider(api_key="your-key"))
session, response = flow.start_session("Should I take this client work or focus on my product?")
print(response.content)
```

See [outcomist_core/README.md](./outcomist_core/README.md) for full library docs.

---

## Status

- **Epic 1: Deep Discovery** — ✅ shipped (v4.8). 100% pass rate on 10 regression tests.
- **Epic 2: Proposal Review** — 🔄 in design. Tangible, high-quality proposals for user validation.
- **Epic 3: Build & Track** — ⏳ planned. Execution support for validated proposals.

---

## Principles

1. **Progressive disclosure** — 30 seconds first, deeper only if needed
2. **Honest evidence** — pattern recognition yes, invented statistics no
3. **Adaptive questioning** — questions evolve based on your answers
4. **Clear stance** — one recommendation, not a list of options
5. **One question at a time** — never interrogate

---

## Built by

**Chris Park** — Senior PM, Microsoft Office of the CTO, AI Incubation group.
Engineering degree from Waterloo. 17 years shipping product.

[LinkedIn](https://www.linkedin.com/in/chrispark1/) · [GitHub](https://github.com/cpark4x)
