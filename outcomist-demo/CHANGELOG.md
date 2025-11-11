# Changelog

## 2025-01-10 - Voice Input & UI Polish

### Added
- **Voice Input Feature**: Speech-to-text using Web Speech API
  - Microphone button in chat input
  - Visual recording state with pulsing animation
  - Auto-submit after voice transcription
  - Browser compatibility detection (Chrome, Edge, Safari)
  - Accessible with ARIA labels

### Technical Details
- Created VoiceButton.svelte component with Web Speech API integration
- Added recording state management with visual feedback
- Graceful degradation for unsupported browsers
- Auto-submission workflow for voice input

## 2025-01-10 - Dynamic Project Titles

### Added
- **Dynamic Project Title System**: Header now displays context-aware project title extracted from first user message
  - Smart title generation removes common prefixes ("I want to", "Help me", etc.)
  - Topic shift detection updates title when conversation changes direction
  - Fallback to "Untitled Project" for empty conversations

- **Professional Header Component**: Added minimal header bar with branding
  - "Outcomist" logo on left
  - Dynamic project title on right
  - Only appears after conversation starts
  - Clean, professional layout following Gmail/Linear/Notion patterns

- **Adaptive Discovery Preview**: Made /explore CLI conversational
  - Short preview for straightforward questions (conversational tone)
  - Detailed preview for complex questions (structured with 2-round breakdown)
  - Smart detection based on question complexity, stakes, and clarity
  - Defaults to conversational (less scripted) approach

### Changed
- Improved discovery transition to feel more natural and less formal
- Updated explore.md prompt with adaptive preview system
- Enhanced conversation store with projectTitle state management

### Files Modified
- `.claude/commands/explore.md` - Added adaptive discovery preview
- `src/stores/conversation.ts` - Added projectTitle to state
- `src/containers/ChatContainer.svelte` - Added title generation logic
- `src/components/layout/Header.svelte` - New header component

### Technical Details
- Title generation uses regex patterns to clean user messages
- Topic shift detection looks for indicators like "actually", "what about", "different question"
- Reactive state management using Svelte 5 stores
- TypeScript interfaces for type safety

## 2025-01-09 - Option C: Precise Elegance Implementation

### Added
- Complete UI redesign with "Precise Elegance" design system
- Blue chat bubbles (#3B7FE8) for user messages
- Polished welcome screen with gradient accent line
- Refined typography and spacing throughout

### Changed
- Updated color palette for professional appearance
- Improved message styling with subtle shadows
- Enhanced input component with focus states
- Optimized layout for better visual hierarchy
