# Discovery Session: AI Knowledge Manager for Daily Journals

**Date**: 2025-11-03
**Session Type**: Outcomist /brief - Tier 2 Discovery
**Decision**: How to build an AI knowledge manager that integrates with daily journaling

---

## Problem Statement

User wants an AI system that:
1. **Makes reading compound over time** - Can recall articles when needed (not just save-and-forget)
2. **Enables cross-domain pattern recognition** - Connects tech articles, work experiences, and life lessons automatically
3. **Integrates with daily journal** - The journal is the integration layer where everything comes together

### Key Insight
This is NOT about:
- Storing more articles efficiently
- Building a comprehensive knowledge base
- Organizing bookmarks better

This IS about:
- **Learning integration across entire life** (tech + work + personal)
- **Active synthesis during journaling** - System suggests connections as user writes
- **Making past reading inform current thinking** - Surface relevant articles at the right moment

---

## Discovery Findings

### Current Workflow
- **Journaling**: Daily entries with mix of work + personal thoughts (structured format)
- **Article consumption**: Saves to read-later app (Pocket/Instapaper-like), rarely revisits
- **Recall problem**: Hits hardest when designing systems or having tech conversations - can't remember that perfect article from 2 weeks ago

### Desired System Behavior

**Example scenario**: User is journaling about RAG implementation challenges

System should:
1. **Auto-suggest**: "This connects to those 2 RAG articles from 2 weeks ago"
2. **Generate synthesis**: Brief summary showing how the articles relate to current thinking
3. **Bi-directional linking**: Link journal entry back to articles for future retrieval

### Friction Tolerance
- **Seamless required**: Won't use if clunky
- **Automatic linking preferred**: System auto-suggests, no manual tagging
- **Willing to accept some friction**: Can handle manual linking if necessary, but prefers automation

### Cross-Domain Example
User wants system to surface connections like:
- Philosophy article → Team management challenge
- RAG technical article → Current system design problem
- Business leadership piece → Personal reflection

**Pattern recognition across domains** is the key value proposition.

---

## Recommendation: AI-Powered Learning Integration Layer

### Core Architecture

```
Daily Journal (Integration Layer)
    ↕️ (AI-powered connections)
Saved Articles (Tech blogs, essays, papers)
```

### Key Features

1. **Retrieval During Journaling** (Primary Use Case)
   - As user writes journal entry, system surfaces relevant saved articles
   - Shows key excerpts + brief synthesis
   - Suggests connections user wouldn't consciously make

2. **Two-Way Linking**
   - Journal entry → Articles (what influenced this thinking)
   - Articles → Journal entries (when did I engage with this idea)

3. **Cross-Domain Pattern Detection**
   - AI finds non-obvious connections between tech, work, and life
   - "That philosophy piece from last month relates to your API design challenge today"

### Implementation Strategy

**Phase 1: MVP - Focus on Core Loop**
- Journal + article ingestion only (not full knowledge manager yet)
- Single primary use case: "retrieval when journaling"
- Test if auto-suggestions actually help before building more

**Phase 2: Validate Value**
- Does automatic surfacing of connections improve journaling?
- Are cross-domain patterns actually useful?
- What friction points emerge?

**Phase 3: Expand (Only If Phase 1/2 Succeed)**
- Add more content types (books, videos, conversations)
- Improve synthesis quality
- Build explicit graph visualization

### What NOT to Build (Yet)

- ❌ Complex tagging systems
- ❌ Manual knowledge graph construction
- ❌ Comprehensive search interface
- ❌ Multiple export formats
- ❌ Collaboration features

Start minimal. Test core hypothesis: **Does AI-powered article surfacing during journaling make reading compound over time?**

---

## Technical Considerations for Engineer

### Key Requirements

1. **Real-time suggestion engine**
   - As user types journal entry, system processes and surfaces relevant articles
   - Latency target: < 2 seconds for suggestions

2. **Semantic similarity matching**
   - Embeddings-based retrieval (not keyword matching)
   - Need to handle cross-domain connections (tech article → personal reflection)

3. **Context window management**
   - Journal entry (current writing) + article excerpts + synthesis
   - Balance between relevance and context length

4. **Storage & Retrieval**
   - Article content storage (full text or excerpts?)
   - Journal entry history
   - Connection metadata (which articles surfaced for which entries)

### Open Questions

1. **What triggers article surfacing?**
   - Every N words typed?
   - On-demand button click?
   - Paragraph completion?

2. **How many articles to surface at once?**
   - Top 3? Top 5?
   - Threshold for relevance score?

3. **Synthesis format**
   - Single paragraph summary?
   - Bullet points showing connections?
   - Just article titles + excerpts?

4. **Where does this live?**
   - Obsidian plugin?
   - VS Code extension?
   - Standalone web app?
   - Cursor/Claude Code integration?

---

## Success Metrics

**Primary**: Does user feel like reading is compounding?
- "I'm making connections I wouldn't have made manually"
- "Articles surface at the right moment"
- "My journal entries are richer because of article integration"

**Secondary**:
- How often do surfaced articles get acknowledged/engaged with?
- Do cross-domain connections feel valuable or noisy?
- Is friction low enough that user journals regularly?

---

## Next Steps for Engineering

1. **Review this document** - Validate understanding of the problem
2. **Prototype retrieval mechanism** - Test semantic similarity approach
3. **Define integration point** - Where does this live? (Obsidian? VS Code? Web?)
4. **Build Phase 1 MVP** - Journal + articles + basic surfacing
5. **User testing** - Does it actually help?

---

## Notes

- This discovery used Outcomist v3.4 (Tier 2 - 5-10 min structured inquiry)
- User's friction tolerance is key constraint: **seamless or bust**
- Start with journal as primary interface, not separate knowledge base app
- Test hypothesis before building elaborate features
