# Changelog

All notable changes to Outcomist will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/).

## [Unreleased]

### Added v4.6 (2025-01-07)
- **Trade-off Discovery Mechanism**: Reveals actual priorities through concrete choices
  - Triggers after Tier 2 Round 1 when conflicting dimensions detected
  - Presents 2 concrete options with explicit Pro/Con/Impact structure
  - Uses revealed preference (choices) over stated preference (abstract questions)
  - Example conflicts: Timeline vs. quality, volume vs. revenue, vision vs. resources
- **Factual Validation Requirement**: Verify claims before presenting trade-off options
  - Don't assume facts (whale season dates, feature complexity, market data)
  - Research first, then present options with accurate information
  - Prevents undermining recommendations with incorrect data
- **Revealed Preference Guidance**: Use choice behavior to guide discovery
  - If Option A chosen: Focus remaining discovery on maximizing that dimension
  - If Option B chosen: Focus discovery on alternative path
  - Choice behavior > stated preferences when conflicts exist
- **Documentation**: Analysis confirmed trade-off presentation is systemic improvement (5 of 8 tests had conflicting preferences)

### Changed
- **Tier 2 Structure**: Added optional trade-off presentation between Round 1 and Round 2
- **Discovery Flow**: Round 1 → (Conflict check) → Trade-off presentation (if needed) → Round 2
- **Priority Detection**: Concrete choices reveal actual priorities more reliably than abstract questions

### Fixed
- Users' hidden trade-offs now surfaced explicitly (Test #12 failure - diving dates vs. whale season)
- Recommendations now based on revealed priorities, not assumed priorities
- Factual errors caught before presenting options (verify whale seasons, feature complexity, etc.)

### Added v4.5 (2025-01-07)
- **Collaborative Partnership Tone**: Replaced patronizing language with stress-testing framing
  - Changed "But the real question is" → "Let me offer another angle"
  - Added acknowledgment: "that's a solid starting point" before reframing
  - Framed recommendations as stress-tests, not prescriptions
  - Added explicit invitation to disagree: "Does this direction feel right?"
- **Dimension Preview (Not Questions)**: Prevents users from answering immediately
  - Shows dimension labels without question marks
  - Added "(Don't answer yet...)" instruction
  - Clarifies these are exploration dimensions, not prompts to respond to
- **Clear Call-to-Action**: Reduced confusion about what to type
  - Changed from bullets to bold commands: **yes**, **show me**, **clarify**
  - Prevents users typing "(1)" instead of command words
  - Explicit instruction: "Type one of these to continue:"
- **Value Proposition for All Users**: Discovery validates even good thinking
  - "Even if you're confident in your framing, structured discovery often reveals insights"
  - Positions discovery as validation + exploration, not just fixing confusion
- **Context Inference Guidelines**: Prevents bad assumptions
  - Ask explicitly about role/goal/stage before recommending, or caveat assumptions
  - Don't assume "founder building product" vs "engineer learning"
  - Don't assume project stage without evidence
  - Partnership language: "you know your context better than I do"
- **Competitive Analysis Depth**: HOW/WHY explanations, not just assertions
  - Explain HOW competitors work with examples
  - Show WHY their approaches fail specifically
  - Acknowledge Outcomist's tradeoffs honestly
- **Tier 2 Collaborative Tone**: Softer, partnership language
  - "Help me understand" instead of "Walk me through"
  - Reassurance that limited data is useful: "just share what you know"
  - "Let's explore together" framing
- **Documentation**: Created [test-session-summary-2025-01-06.md](docs/testing/test-session-summary-2025-01-06.md) with findings from Tests #10 and #11

### Changed
- **Tier 1 Format**: Updated dimension preview to show labels, not questions
- **Tier 1 Tone**: Partnership language throughout reframing and explanation
- **Tier 2 Questions**: Collaborative framing in all question guidance
- **Tier 3 Recommendations**: Stress-test framing with explicit invitation to disagree
- **Context Handling**: Added guidelines for inferring or asking about missing context

### Fixed
- Users no longer try to answer dimension preview questions immediately (removed question marks, added "Don't answer yet")
- Users no longer respond "(1)" to options (removed bullets, used bold commands)
- Inconsistent list formatting (standardized: bullets for info, bold for commands, numbers for dimensions)
- Missing role/goal context causing biased assumptions (added context inference guidelines)
- Missing project stage context causing misaligned recommendations (ask or caveat assumptions)
- Too prescriptive tone without confidence (stress-test framing, partnership language)
- Tier 3 lacks competitive differentiation depth (added HOW/WHY templates)
- Patronizing tone (replaced "you're wrong" with "let's explore together")

### Added v4.4 (2025-01-06)
- **Question-First Format**: Replaced abstract fork pattern templates with explicit question lists
  - Users now see the actual 4 questions that will be asked instead of generic fork options
  - Clearer value proposition: "To [outcome], I need to explore:"
  - Simpler call-to-action with 3 clear options (yes/show me/ask anything)
  - Eliminates confusion when fork templates don't match decision context
- **Documentation**: Created [tier1-format-improvement.md](docs/design/tier1-format-improvement.md) with design rationale and before/after examples

### Changed
- **Tier 1 Format**: Updated `.claude/commands/explore.md` with v4.4 question-first template
- **Fork Patterns**: Converted from user-facing options to internal guidance for question generation
- **Formatting**: Added numbered lists for questions, maintained all v4.3 formatting improvements

### Fixed
- Meta decisions (about the product itself) no longer receive confusing generic fork options
- Strategic planning questions now show relevant exploration territory
- Open-ended questions present clear structure instead of abstract alternatives

## [4.3.0] - 2025-01-05

### Added
- **Adaptive Fork Patterns**: 5 patterns (Existence, Prioritization, Execution, Timing, Audience) that replace hardcoded "validation vs guidance" fork
- **Fork Detection Logic**: Uses language cues and context signals to determine appropriate fork pattern
- **Improved Formatting**:
  - `#` for title, `###` for headers
  - `>` blockquotes for key reframes
  - `---` horizontal rules between sections
  - **Bold** for option headers
  - Blank lines between all elements
- **"Show me" option emphasized**: Reduces decision fatigue by allowing users to skip fork selection

### Changed
- Tier 1 structure shortened and clarified for easier scanning
- Fork patterns now adapt to decision type instead of generic intent check

## [4.2.0] - 2025-01-03

### Added
- **Intent Check Before Questions**: Tier 1 now asks "validation on WHETHER vs guidance on HOW" to tailor discovery
- **"Create Hunger" Required**: Tier 1 must hint at complexity without solving (40-60 words)
- **Question Preview**: Shows example questions tailored to validation vs execution seekers
- **Formatting Guidelines**: Explicit formatting rules for readability (headers, spacing, word counts)

### Changed
- Word count increased to 160 max for Tier 1 (to accommodate intent check + formatting)

## [4.1.0] - 2024-11-05

### Added
- **Intent Check After Tier 1**: Distinguishes validation seekers ("should I?") from execution seekers ("how do I?")
- **"Show Me" Questions**: Emphasis on requesting real data/artifacts instead of assumptions
  - "Show me the error", "Paste the relevant section", "Send a screenshot"
- **Summary Step Before Recommendation**: Separate listening from advocating
  - List 3-4 key facts without judgment
  - Wait for user confirmation before recommending
- **Co-Creation Offer**: After recommendation, explicitly offer: "Want me to help you create [artifact] together?"
- **Special Probes**:
  - Building/creating → Ask: "Do you have something reviewable (demo, video, screenshot)?"
  - Constraints mentioned → Ask: "Walk me through your typical workflow"
- **Evidence Gathering**: Don't accept descriptions when actual artifacts are available

### Changed
- Tier 2 now includes explicit summary step before recommendation
- Questions should request personal situation/data, not external research

## [4.0.0] - 2024-11-04

### Changed
- **Renamed**: `/brief` → `/explore` (action verb, Stage 1 of journey)
- **Three-Stage Vision**: Explore → Design → Build journey clarified
- **Stage 1 Focus**: Understanding before alignment
- **Current Scope**: Stage 1 only (Stages 2 & 3 to be built after nailing Stage 1)

## [3.5.0] - 2024-10-29

### Removed
- 3-option fork (Option 1/2/3) - too much choice
- "Quick answer" option - low-quality shortcut

### Changed
- **Default path is Tier 2**: Discovery is the primary value
- **Show questions upfront**: Transparency about what will be asked
- **Escape hatch for validation only**: "If you just want validation..."
- **NO Tier 3 offer from Tier 1**: Too premature, only offer after Tier 2

### Added
- Progressive disclosure ladder: Tier 1 → Tier 2 → Tier 3 → Tier 4
- Honest evidence framework: Clear rules about what can/cannot be claimed

## [3.0.0] - 2024-10-15

### Added
- Four-tier progressive disclosure system
- Honest evidence framework
- Pattern recognition as default entry point

## [2.0.0] - 2024-09-20

### Added
- Multi-tier structure (Tier 1/2/3)
- Pattern library system

## [1.0.0] - 2024-08-30

### Added
- Initial release with basic decision exploration
- Question-answer format
- Simple recommendation engine

[Unreleased]: https://github.com/user/outcomist/compare/v4.3.0...HEAD
[4.3.0]: https://github.com/user/outcomist/compare/v4.2.0...v4.3.0
[4.2.0]: https://github.com/user/outcomist/compare/v4.1.0...v4.2.0
[4.1.0]: https://github.com/user/outcomist/compare/v4.0.0...v4.1.0
[4.0.0]: https://github.com/user/outcomist/compare/v3.5.0...v4.0.0
[3.5.0]: https://github.com/user/outcomist/compare/v3.0.0...v3.5.0
[3.0.0]: https://github.com/user/outcomist/compare/v2.0.0...v3.0.0
[2.0.0]: https://github.com/user/outcomist/compare/v1.0.0...v2.0.0
[1.0.0]: https://github.com/user/outcomist/releases/tag/v1.0.0
