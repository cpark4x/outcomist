# Changelog

All notable changes to Outcomist will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/).

## [Unreleased]

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
