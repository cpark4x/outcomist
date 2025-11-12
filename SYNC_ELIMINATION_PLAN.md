# Manual Sync Elimination Plan

**Issue**: explore.md manually duplicates prompts from prompts.py, causing frequent drift and errors.

**Goal**: Automate sync so prompts.py remains single source of truth.

---

## Problem Analysis

### Current Architecture
```
outcomist_shared/prompts.py (269 lines)
  → Single source of truth for prompts
  → Python module imported by web app
  → Clean, well-organized, exemplary (9/10 quality)

.claude/commands/explore.md (991 lines)
  → CLI command specification
  → Contains DUPLICATED prompts from prompts.py
  → PLUS guidance, examples, instructions, flow logic
  → Too large (should be ~50 lines)
```

### The Sync Problem
When a prompt changes in prompts.py:
1. Developer must remember to update explore.md
2. Must find and update correct section (error-prone in 991 lines)
3. Easy to miss, causing bugs
4. No validation that sync occurred

**Evidence of Impact**: Architecture review noted this as highest-ROI fix (4 hours, eliminates major error source).

---

## Solution: Build Script Approach

### Overview
Generate explore.md from prompts.py automatically, making prompts.py the only place to edit prompts.

### Architecture
```
prompts.py (source of truth)
    ↓ (via build script)
explore.md (generated file)
    = template + injected prompts + guidance
```

### Implementation Components

#### 1. Template File: `.claude/commands/explore.template.md`
```markdown
---
description: Outcomist - Turns unclear decisions into clear next steps.
---

You are running the `/explore` command - Outcomist v4.8 decision exploration tool.

[... guidance, instructions, flow logic ...]

<!-- PROMPTS_INJECTED_HERE -->

[... rest of guidance ...]
```

**Key Points**:
- Contains all the guidance, examples, flow logic
- Has placeholder markers for prompt injection
- ~100-150 lines (guidance only, no prompts)
- This is what humans edit for CLI behavior changes

#### 2. Build Script: `scripts/sync_cli.py`
```python
#!/usr/bin/env python3
"""
Generate .claude/commands/explore.md from prompts.py

This script reads prompts from outcomist_shared/prompts.py and injects them
into the explore.template.md file to generate the final explore.md CLI command.

Usage:
  python scripts/sync_cli.py
  make sync-cli
"""

import re
from pathlib import Path

def extract_prompts(prompts_py_path: Path) -> dict[str, str]:
    """Extract all prompt constants from prompts.py."""
    content = prompts_py_path.read_text()

    prompts = {}
    # Match: CONSTANT_NAME = """...""" or '''...'''
    pattern = r'([A-Z_]+_PROMPT)\s*=\s*["\'][\"\'][\"\'](.+?)["\'][\"\'][\"\']'

    for match in re.finditer(pattern, content, re.DOTALL):
        name = match.group(1)
        value = match.group(2).strip()
        prompts[name] = value

    return prompts

def inject_prompts(template: str, prompts: dict[str, str]) -> str:
    """Inject prompts into template at marked locations."""

    # Build prompts section
    prompts_section = "\n## System Prompts\n\n"
    prompts_section += "<!-- GENERATED FROM outcomist_shared/prompts.py -->\n"
    prompts_section += "<!-- DO NOT EDIT DIRECTLY - RUN: make sync-cli -->\n\n"

    for name, content in sorted(prompts.items()):
        prompts_section += f"### {name}\n\n"
        prompts_section += f"```\n{content}\n```\n\n"

    # Replace placeholder
    return template.replace("<!-- PROMPTS_INJECTED_HERE -->", prompts_section)

def main():
    # Paths
    root = Path(__file__).parent.parent
    prompts_py = root / "outcomist_shared" / "prompts.py"
    template = root / ".claude" / "commands" / "explore.template.md"
    output = root / ".claude" / "commands" / "explore.md"

    # Validate inputs exist
    if not prompts_py.exists():
        raise FileNotFoundError(f"prompts.py not found: {prompts_py}")
    if not template.exists():
        raise FileNotFoundError(f"Template not found: {template}")

    # Extract and inject
    prompts = extract_prompts(prompts_py)
    template_content = template.read_text()
    final_content = inject_prompts(template_content, prompts)

    # Write output
    output.write_text(final_content)

    print(f"✅ Generated {output.name} from prompts.py")
    print(f"   {len(prompts)} prompts injected")
    print(f"   {len(final_content.splitlines())} lines total")

if __name__ == "__main__":
    main()
```

**Key Points**:
- Extracts all `*_PROMPT` constants from prompts.py
- Injects into template at marked location
- Adds header warning not to edit generated file
- Simple, readable, maintainable

#### 3. Makefile Target: `Makefile`
```makefile
.PHONY: sync-cli
sync-cli:
	@echo "Syncing CLI command from prompts.py..."
	python scripts/sync_cli.py
	@echo "Done. explore.md updated."
```

#### 4. Git Configuration: `.gitignore`
```
# Generated file - do not commit
.claude/commands/explore.md
```

**Alternative**: Keep explore.md in git but add pre-commit hook to verify sync.

#### 5. Pre-commit Hook (Optional): `.git/hooks/pre-commit`
```bash
#!/bin/bash
# Verify explore.md is synced with prompts.py before commit

if git diff --cached --name-only | grep -q "outcomist_shared/prompts.py"; then
  if ! grep -q "GENERATED FROM outcomist_shared/prompts.py" .claude/commands/explore.md; then
    echo "❌ ERROR: prompts.py changed but explore.md not synced"
    echo "   Run: make sync-cli"
    exit 1
  fi
fi
```

---

## Implementation Steps

### Phase 1: Create Template (30 min)
1. Copy explore.md → explore.template.md
2. Remove all prompt content (keep only guidance/instructions)
3. Add placeholder marker: `<!-- PROMPTS_INJECTED_HERE -->`
4. Verify template has all non-prompt content
5. Reduce from 991 lines → ~150 lines

### Phase 2: Build Script (60 min)
1. Create `scripts/` directory
2. Write `scripts/sync_cli.py` (extract + inject logic)
3. Test: `python scripts/sync_cli.py`
4. Verify generated explore.md matches original functionality
5. Add to Makefile: `make sync-cli`

### Phase 3: Validation (30 min)
1. Run web app - verify prompts still work
2. Run `/explore` CLI - verify commands still work
3. Compare generated explore.md with original
4. Fix any injection logic bugs

### Phase 4: Documentation (30 min)
1. Update README: "Editing prompts" section
2. Add developer note to prompts.py header
3. Update CLAUDE.md if needed
4. Add pre-commit hook setup instructions

### Phase 5: Cleanup (30 min)
1. Decide: gitignore explore.md or keep with verification?
2. Add pre-commit hook if keeping in git
3. Delete old explore.md (will be regenerated)
4. Commit: template, script, Makefile, docs

**Total Estimated Time: 3 hours** (vs 4 hours in original estimate)

---

## Decision Points

### Should explore.md be in git?

**Option A: Generate Only (Recommended)**
- Add explore.md to .gitignore
- CI/CD regenerates on deploy
- Clearer: "this is generated, don't touch"
- **Downside**: Can't see changes in git history

**Option B: Keep in Git with Verification**
- Commit explore.md to git
- Pre-commit hook verifies sync
- Git history shows changes
- **Downside**: Risk of forgetting to sync

**Recommendation**: Option A (gitignore) for simplicity. CI regenerates.

### What about helper functions in prompts.py?

**Current Issue**: prompts.py has helper functions like `get_tier_2_round_1_prompt(session)` that build dynamic prompts.

**Options**:
1. **Inject only constants** - Skip helper functions (recommended for MVP)
2. **Document separately** - Add "Dynamic Prompt Functions" section in template
3. **Generate Python code** - Include function signatures in explore.md

**Recommendation**: Option 1 for MVP. Helper functions are for Python API, not CLI command file.

---

## Testing Plan

### Unit Tests
```python
# tests/test_sync_cli.py

def test_extract_prompts():
    """Test prompt extraction from prompts.py"""
    prompts = extract_prompts(Path("outcomist_shared/prompts.py"))
    assert "TIER_1_SYSTEM_PROMPT" in prompts
    assert len(prompts) >= 7  # Known prompts

def test_inject_prompts():
    """Test prompt injection into template"""
    template = "Header\n<!-- PROMPTS_INJECTED_HERE -->\nFooter"
    prompts = {"TEST_PROMPT": "Test content"}
    result = inject_prompts(template, prompts)
    assert "TEST_PROMPT" in result
    assert "Test content" in result
    assert "Header" in result
    assert "Footer" in result
```

### Integration Tests
1. Run `make sync-cli`
2. Start web app → verify prompts work
3. Run `/explore` CLI → verify command works
4. Make change to prompts.py → re-sync → verify change propagates

---

## Success Criteria

- ✅ prompts.py remains only place to edit prompts
- ✅ Running `make sync-cli` regenerates explore.md
- ✅ Web app and CLI both work with generated file
- ✅ explore.md reduced from 991 lines → ~300 lines (150 template + 150 prompts)
- ✅ Documentation updated
- ✅ No manual sync steps required

---

## Rollout Plan

### Week 1: Implementation
- Day 1: Phase 1 (template creation)
- Day 2: Phase 2 (build script)
- Day 3: Phase 3 (validation)
- Day 4: Phase 4 (documentation)
- Day 5: Phase 5 (cleanup & commit)

### Week 2: Validation
- Test with real usage
- Monitor for issues
- Refine if needed

---

## Future Enhancements

**After MVP stabilizes**:

1. **CI Integration**: Auto-generate explore.md in CI/CD
2. **Version Checking**: Add version numbers to track prompt changes
3. **Diff Reporting**: Show what changed in generated file
4. **Multi-format Support**: Generate other formats (JSON API, REST endpoints)
5. **Prompt Versioning**: Track prompt evolution over time

---

## Alternatives Considered

### Dynamic Import Approach
**Concept**: explore.md imports from prompts.py at runtime

**Pros**: Automatic sync, simpler
**Cons**: Runtime Python dependency in markdown, breaks modular design

**Decision**: Rejected. Build script is cleaner architecture.

### Unified Format Approach
**Concept**: Move everything to single Python file

**Pros**: Zero sync needed
**Cons**: Violates prompt library architecture, web app can't import

**Decision**: Rejected. Breaks current well-designed architecture.

---

## Impact Assessment

**Before**:
- Manual sync required after every prompt change
- 991-line file hard to navigate
- Frequent drift between prompts.py and explore.md
- High error rate

**After**:
- Zero manual sync (automated)
- ~150-line template (guidance only)
- Impossible for prompts to drift
- Zero error rate for prompt sync

**ROI**:
- Implementation: 3 hours
- Saves: ~30 min per prompt change × 10 changes/month = 5 hours/month
- Payback: < 1 month
- Risk reduction: Eliminates entire class of bugs

---

## Questions for User

1. **Git strategy**: Gitignore explore.md or keep with pre-commit hook?
2. **Rollout**: Implement immediately or wait for specific milestone?
3. **Scope**: Just prompts or include other duplicated content?

---

**Status**: Ready to implement. Awaiting user approval to proceed.
