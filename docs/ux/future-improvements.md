# Future UX Improvements

**Created**: 2025-01-11
**Status**: Planned - Not Yet Implemented

---

## Overview

This document captures UX improvements identified from the Manus comparison that require backend/CLI changes and will be implemented in a future iteration.

---

## 1. Research Transparency

**Goal**: Show users what the AI is researching in real-time

### Current Behavior
- User sees generic "thinking" indicator
- No visibility into what research is happening
- Feels like a black box

### Desired Behavior (Manus Pattern)
- Show WebSearch queries as they happen
- Display: "Searching for: [query text]"
- Gives user confidence that AI is actively researching
- Makes the process feel transparent and trustworthy

### Implementation Requirements

**Backend Changes** (Primary):
- CLI must emit search events as they occur
- Either streaming updates or event-based system
- Send query text and status to frontend

**Frontend Changes** (Secondary):
- Create SearchActivity component to display queries
- Update ThinkingIndicator to show search queries
- Handle streaming updates from backend

### Example from Manus
```
[Thinking indicator shows]:
"Searching for: best practices for career transitions"
"Searching for: average time to find new job in tech"
```

### Priority
**Medium** - Nice-to-have for transparency, not critical for core functionality

---

## 2. Progressive Disclosure with Continue Buttons

**Goal**: Break up multi-question responses into digestible stages

### Current Behavior
- AI asks 3-4 questions all at once
- Can feel overwhelming
- User must address everything in one response

### Desired Behavior (Manus Pattern)
- AI asks 1-2 questions
- Shows "Continue" button
- User can respond or click Continue for next stage
- Breaks discovery into natural conversation flow

### Implementation Requirements

**Backend Changes** (Primary):
- Restructure `/explore` CLI prompt to break into stages
- Support multi-stage conversation flow
- Wait for user signal before continuing to next stage
- Track conversation state across stages

**Frontend Changes** (Secondary):
- Create ContinueButton component
- Handle multi-stage response state
- Distinguish between regular responses and stage-end responses

### Example Flow
```
Assistant: "Let's start with the basics. What's driving this decision right now?"
[User responds]