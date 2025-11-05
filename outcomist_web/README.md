# Outcomist Web

Beautiful, minimal web application for Outcomist decision exploration.

## Features

- **Apple-inspired UI** - Clean, spacious, elegant design
- **Real-time streaming** - AI responses stream in naturally
- **Local-first** - All data stored locally (JSON files)
- **Progressive disclosure** - Tier 1 pattern recognition (30 seconds)
- **Session persistence** - Conversations saved automatically

## Phase 1: Minimal Working Slice

This is Phase 1 implementation focusing on:
- Tier 1 pattern recognition only
- Beautiful streaming UI
- Session persistence
- End-to-end working flow

## Setup

1. **Install dependencies:**
   ```bash
   cd outcomist_web
   uv sync
   ```

2. **Set API key:**
   ```bash
   cp .env.example .env
   # Edit .env and add your ANTHROPIC_API_KEY
   ```

3. **Run the server:**
   ```bash
   ./run.sh
   ```

4. **Open in browser:**
   ```
   http://localhost:8000
   ```

## Architecture

**Backend:**
- FastAPI with SSE streaming
- JSON file storage for sessions
- Claude API integration (Anthropic SDK)

**Frontend:**
- Vanilla HTML/CSS/JavaScript
- No build tools or frameworks
- Server-Sent Events for streaming

**File Structure:**
```
outcomist_web/
├── backend/
│   ├── main.py              # FastAPI app
│   ├── routes.py            # API endpoints
│   ├── engine.py            # ExplorationEngine (Tier 1)
│   ├── storage.py           # JSON persistence
│   ├── prompts.py           # Tier 1 prompt template
│   └── models.py            # Pydantic models
├── frontend/
│   ├── index.html           # Main page
│   ├── styles.css           # Apple-inspired CSS
│   └── app.js               # Vanilla JS
└── data/
    └── sessions/            # JSON session files
```

## API Endpoints

- `POST /api/sessions/start` - Create new session
- `GET /api/sessions/{id}/stream` - SSE stream for Tier 1 response
- `GET /api/sessions/{id}` - Get session state

## Design Philosophy

- **Ruthless simplicity** - No unnecessary abstractions
- **Modular design** - Each component independently regenerable
- **Beautiful UX** - Users should feel delighted
- **Progressive disclosure** - Match Outcomist's philosophy

## Next Steps (Phase 2)

After Phase 1 is tested and working:
- Add Tier 2-4 logic
- Implement intent check handling
- Add conversation history UI
- Support multi-turn interactions

## Testing

1. Start server: `./run.sh`
2. Open browser: `http://localhost:8000`
3. Enter a decision (e.g., "Should I quit my job to work on my startup?")
4. Watch Tier 1 response stream in
5. Verify session saved to `data/sessions/`
6. Check console for errors

## Requirements

- Python 3.11+
- ANTHROPIC_API_KEY environment variable
