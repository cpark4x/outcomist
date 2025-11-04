# Outcomist Cleanup & Documentation Plan

**Date**: 2025-11-04
**Purpose**: Organize learnings, remove obsolete artifacts, create proper documentation structure

---

## Current State Issues

1. **190 references to "brief"** across markdown files (command renamed to /explore)
2. **Scattered learnings** - Test logs, changelogs, specs all mixed together
3. **No organized docs** - Vision, patterns, principles not easily discoverable
4. **Obsolete files** - BRIEF_* files, old specs, redundant test logs

---

## Proposed Structure

```
outcomist/
├── docs/                          # Organized documentation
│   ├── vision/
│   │   ├── product-vision.md      # What we're building & why
│   │   ├── three-stage-journey.md # explore → design → build
│   │   └── user-personas.md       # Who this is for
│   ├── patterns/
│   │   ├── pattern-library.md     # All 6+ patterns documented
│   │   └── question-framework.md  # Question quality heuristics
│   ├── principles/
│   │   ├── progressive-disclosure.md  # Tier 1-4 architecture
│   │   ├── honest-evidence.md         # No fake statistics
│   │   └── adaptive-questioning.md    # How questions evolve
│   └── testing/
│       ├── test-strategy.md       # How we validate changes
│       └── test-scenarios.md      # The 20 test scenarios
├── archive/                       # Historical context (not active)
│   ├── test-logs/                 # All TEST_LOG_*.md files
│   │   ├── TEST_LOG_NOV3_OFFICE.md
│   │   ├── TEST_LOG_NOV3_PASSIVE_INCOME.md
│   │   ├── TEST_LOG_NOV3_CANCER_PREVENTION.md
│   │   ├── TEST_LOG_NOV4_FEATURE_DECISION.md
│   │   └── TEST_LOG_NOV4_CLIENT_VS_PRODUCT.md
│   ├── changelogs/                # Version history
│   │   ├── BRIEF_V3_CHANGELOG.md
│   │   └── BRIEF_V3.1_CHANGELOG.md
│   ├── specs/                     # Old spec experiments
│   │   ├── ARTIFACT_SPECIFICATION.md
│   │   └── ARTIFACT_SPEC_3FILES.md
│   └── discovery-sessions/
│       └── DISCOVERY_SESSION_NOV3.md
├── .claude/commands/
│   └── explore-command.md         # The /explore command (v4.0)
├── README.md                      # Project overview + links to docs
└── MUST_HAVES.md                  # Active implementation roadmap

```

---

## Files to Delete

**Obsolete BRIEF_* files** (command renamed):
- [ ] BRIEF_V3_CHANGELOG.md → archive/changelogs/
- [ ] BRIEF_V3.1_CHANGELOG.md → archive/changelogs/
- [ ] BRIEF_README.md → DELETE (replaced by README.md)
- [ ] BRIEF_PERFECTION_ROADMAP.md → DELETE (replaced by MUST_HAVES.md)
- [ ] BRIEF_TESTING_STRATEGY.md → archive/testing/ or DELETE

**Obsolete spec files**:
- [ ] ARTIFACT_SPECIFICATION.md → archive/specs/
- [ ] ARTIFACT_SPEC_3FILES.md → archive/specs/
- [ ] brief/Brief.md → DELETE (example output, no longer relevant)
- [ ] Brief.md → DELETE (duplicate)

**Obsolete command files**:
- [ ] .claude/commands/brief.md → DELETE (replaced by explore-command.md)

---

## Files to Archive

**Test logs** (historical validation, not active docs):
- [ ] TEST_LOG_NOV3_OFFICE.md → archive/test-logs/
- [ ] TEST_LOG_NOV3_PASSIVE_INCOME.md → archive/test-logs/
- [ ] TEST_LOG_NOV3_CANCER_PREVENTION.md → archive/test-logs/
- [ ] TEST_LOG_NOV4_FEATURE_DECISION.md → archive/test-logs/
- [ ] TEST_LOG_NOV4_CLIENT_VS_PRODUCT.md → archive/test-logs/

**Discovery sessions**:
- [ ] DISCOVERY_SESSION_NOV3.md → archive/discovery-sessions/

---

## New Docs to Create

### docs/vision/product-vision.md
**Content**: What Outcomist is, why it exists, what problem it solves
- Three-stage journey (explore → design → build)
- Stage 1 focus: Understanding decisions through pattern recognition
- Future vision: Alignment (Stage 2) and execution (Stage 3)

### docs/vision/three-stage-journey.md
**Content**: Deep dive on the three stages
- Stage 1 (Explore): Uncover, inform, or challenge user understanding
- Stage 2 (Design): Show what will be built, iterate before executing
- Stage 3 (Build): Execute and track implementation

### docs/vision/user-personas.md
**Content**: Who uses Outcomist and for what
- Scenarios: Personal decisions, workplace conflicts, business strategy, product decisions
- User states: Confused (uncover), has context (inform), wrong belief (challenge)

### docs/patterns/pattern-library.md
**Content**: All 6 patterns extracted from test logs
1. Personal sanctuary pattern (office redesign)
2. Employability anxiety pattern (passive income)
3. Health anxiety pattern (cancer prevention)
4. Additional revenue misframing (passive income)
5. Popularity contest hiding identity crisis (feature decision)
6. Scarcity mindset hiding opportunity (client vs product)

Each with: signals, real problem, key questions, pitfalls, example scenarios

### docs/patterns/question-framework.md
**Content**: Question quality heuristics
- Trigger questions (health/anxiety/career)
- Constraint questions (resource decisions)
- Usage/context questions (space/design/product)
- Pattern questions (medical/technical)

### docs/principles/progressive-disclosure.md
**Content**: Tier 1-4 architecture
- Tier 1: Pattern recognition (30 sec)
- Tier 2: Discovery (5-10 min) - default path
- Tier 3: Analysis (20-30 min) - offered after Tier 2
- Tier 4: Comprehensive (45-60 min) - offered after Tier 3

### docs/principles/honest-evidence.md
**Content**: No invented statistics
- What you CAN say (pattern recognition, inference)
- What you CANNOT say ("studies show", "40% of teams")

### docs/principles/adaptive-questioning.md
**Content**: How questions evolve
- After revealing constraint → probe implications
- After revealing anxiety → probe depth
- After revealing multi-use context → probe priorities

### docs/testing/test-strategy.md
**Content**: How we validate changes
- One-by-one questioning validation
- Pattern recognition validation
- User validation ("Great", "okay, thanks")
- Success criteria (10+ scenarios, 6+ patterns)

### README.md (rewrite)
**Content**: Project overview with links
- What is Outcomist?
- Quick start: Try `/explore`
- Documentation links
- Current status (Stage 1 complete, Stages 2-3 planned)

---

## Migration Steps

1. **Create docs structure**
   ```bash
   mkdir -p docs/{vision,patterns,principles,testing}
   mkdir -p archive/{test-logs,changelogs,specs,discovery-sessions}
   ```

2. **Create new docs** (extract from MUST_HAVES.md, test logs, explore-command.md)

3. **Move files to archive**
   ```bash
   mv TEST_LOG_*.md archive/test-logs/
   mv BRIEF_V3*.md archive/changelogs/
   mv ARTIFACT_*.md archive/specs/
   mv DISCOVERY_SESSION_*.md archive/discovery-sessions/
   ```

4. **Delete obsolete files**
   ```bash
   rm BRIEF_README.md BRIEF_PERFECTION_ROADMAP.md BRIEF_TESTING_STRATEGY.md
   rm Brief.md brief/Brief.md
   rm .claude/commands/brief.md
   ```

5. **Update README.md** with new structure

6. **Update MUST_HAVES.md** to reference docs/ structure

---

## Benefits

✅ **Clear documentation hierarchy** - Vision, patterns, principles organized
✅ **Easy onboarding** - New contributors can find product vision quickly
✅ **Historical context preserved** - Test logs archived but not deleted
✅ **No "brief" confusion** - Command is /explore everywhere
✅ **Active vs archived** - Clear separation between what's current and what's historical

---

**Next**: Proceed with migration?
