# Outcomist Shared Prompt Library

**Single source of truth for all Outcomist prompts across web app and CLI command.**

## Purpose

This package contains all prompts used by the Outcomist system to ensure consistency between the web app and CLI command. Any prompt improvements automatically apply to both interfaces.

## Architecture

```
outcomist_shared/
├── __init__.py          # Package initialization
├── prompts.py           # All prompts (SINGLE SOURCE OF TRUTH)
├── pyproject.toml       # Package metadata
└── README.md            # This file
```

## Usage

### Web App (Direct Import)

The web app imports prompts directly from this package:

```python
# In outcomist_web/backend/engine.py
from backend.prompts import (
    TIER_1_SYSTEM_PROMPT,
    TIER_2_ROUND_1_SYSTEM_PROMPT,
    get_tier_1_prompt,
    # ... other prompts
)
```

The `backend/prompts.py` file is a thin compatibility wrapper:

```python
# outcomist_web/backend/prompts.py
from outcomist_shared.prompts import *
```

**Advantage**: Zero runtime overhead, automatic updates when prompts change.

### CLI Command (Manual Sync)

The CLI command at `.claude/commands/explore.md` uses a manual sync approach:

1. Prompts are copied from `prompts.py` into the markdown file
2. A comment marks the synced section:
   ```markdown
   <!-- Prompts synced from outcomist_shared/prompts.py - SINGLE SOURCE OF TRUTH -->
   ```

**When to sync**: After making changes to `prompts.py`, manually update the CLI command file.

**Advantage**: Simple, explicit, easy to review changes in git diffs.

## Prompt Organization

### Tier 1: Pattern Recognition (30 seconds)
- `TIER_1_SYSTEM_PROMPT` - Pattern recognition system instructions
- `get_tier_1_prompt(decision)` - Build Tier 1 prompt with user decision

### Tier 2: Discovery & Recommendation (5-10 minutes)
- `TIER_2_ROUND_1_SYSTEM_PROMPT` - First discovery question instructions
- `TIER_2_ANALYSIS_SYSTEM_PROMPT` - Analysis between rounds
- `TIER_2_ROUND_2_SYSTEM_PROMPT` - Second discovery question instructions
- `TIER_2_SUMMARY_SYSTEM_PROMPT` - Summary before recommendation
- `TIER_2_RECOMMENDATION_SYSTEM_PROMPT` - Final recommendation instructions
- Helper functions: `get_tier_2_round_1_prompt(session)`, etc.

### Tier 3 & 4
Not yet implemented.

## Key Features

### Anti-Research Rules
Both Round 1 and Round 2 prompts include:
- **"NEVER ask users to research factual data you should know (market trends, prices, etc.)"**
- Ensures questions focus on PERSONAL context, not external data gathering

### Capability Checking
Round 2 prompt includes:
- **"Check capabilities - don't assume user lacks skills"**
- Prevents assumptions about user's abilities or experience

### Summary Without Judgment
Summary prompt enforces:
- **"NO JUDGMENT - just state what they told you"**
- Separates listening from advocating

## Making Changes

### 1. Update prompts.py
Edit the prompts in `outcomist_shared/prompts.py`:

```python
TIER_2_ROUND_1_SYSTEM_PROMPT = """You are conducting Tier 2 Discovery - Round 1.

Your task is to ask ONE simple, easy-to-answer question to understand the landscape.

CRITICAL RULES:
- Ask only ONE question
- Make it LOW EFFORT - easy to answer in 1-2 sentences
- Ask about their PERSONAL situation, feelings, or constraints
- NEVER ask users to research factual data you should know (market trends, prices, etc.)
...
"""
```

### 2. Test web app
The web app automatically uses the updated prompts (restart backend if needed):

```bash
cd outcomist_web
uv run uvicorn backend.main:app --reload
```

### 3. Sync CLI command
Manually update `.claude/commands/explore.md` with the new prompt content:

1. Find the section marked with `<!-- Prompts synced from outcomist_shared/prompts.py -->`
2. Copy the updated prompt content from `prompts.py`
3. Paste into the CLI command file
4. Test with `/explore` command

### 4. Validate
Confirm both interfaces work correctly:

```python
# Check prompts loaded
python -c "from backend.prompts import TIER_2_ROUND_1_SYSTEM_PROMPT; print('NEVER ask users to research' in TIER_2_ROUND_1_SYSTEM_PROMPT)"

# Check CLI synced
grep -q "NEVER ask users to research" .claude/commands/explore.md && echo "CLI synced"
```

## Testing

See [SHARED_PROMPTS_TEST_REPORT.md](../SHARED_PROMPTS_TEST_REPORT.md) for comprehensive test results.

**Key Validations**:
- ✅ Web app imports from shared library
- ✅ CLI command synced with source
- ✅ Anti-research rules present in both
- ✅ Capability checking present in both
- ✅ Backend server running successfully

## Troubleshooting

### Web app can't import outcomist_shared

**Symptom**: `ModuleNotFoundError: No module named 'outcomist_shared'`

**Solution**: Ensure the Python path includes the parent directory.

Check `.venv/lib/python3.11/site-packages/_outcomist_shared.pth`:
```
/Users/chrispark/amplifier/outcomist
```

If missing, recreate it:
```bash
echo "/Users/chrispark/amplifier/outcomist" > outcomist_web/.venv/lib/python3.11/site-packages/_outcomist_shared.pth
```

### CLI prompts don't match web app

**Symptom**: Different behavior between interfaces

**Solution**: Manually sync CLI command from `prompts.py`.

1. Check when `prompts.py` was last modified
2. Check when `.claude/commands/explore.md` was last modified
3. If prompts.py is newer, manually sync the CLI file

## Version History

- **v1.0.0** (Nov 5, 2025) - Initial shared prompt library
  - Moved all prompts from `outcomist_web/backend/prompts.py` to `outcomist_shared/prompts.py`
  - Added anti-research rules
  - Added capability checking
  - Synced CLI command

## Future Improvements

- [ ] Automated CLI sync (consider using Python imports for CLI too)
- [ ] Version tracking for prompt changes
- [ ] Automated tests to validate prompt consistency
- [ ] Prompt changelog for tracking improvements over time
