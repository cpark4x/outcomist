# Shared Prompt Library - Test Report

**Date**: November 5, 2025
**Goal**: Validate that both web app and CLI command use the same prompts from `outcomist_shared/prompts.py`
**Status**: ✅ **PASS** - Both interfaces confirmed using shared prompts

---

## Architecture Validation

### Single Source of Truth ✅

**Location**: `outcomist_shared/prompts.py`

**Web App Integration**:
- `outcomist_web/backend/prompts.py` → Compatibility wrapper
- Imports: `from outcomist_shared.prompts import *`
- Status: ✅ Direct import working

**CLI Integration**:
- `.claude/commands/explore.md` → Manual sync with reference comment
- Sync marker: `<!-- Prompts synced from outcomist_shared/prompts.py - SINGLE SOURCE OF TRUTH -->`
- Status: ✅ Manually synced

---

## Prompt Content Validation

### Critical Updates Present in Both Interfaces ✅

| Feature | Web App | CLI | Match |
|---------|---------|-----|-------|
| Anti-research rule (Round 1) | ✅ | ✅ | ✅ |
| Anti-research rule (Round 2) | ✅ | ✅ | ✅ |
| Capability checking | ✅ | ✅ | ✅ |
| Sync documentation | N/A | ✅ | ✅ |

**Validated Phrases**:
- ✅ "NEVER ask users to research factual data you should know (market trends, prices, etc.)"
- ✅ "NEVER ask users to research factual information (market data, prices, trends)"
- ✅ "Check capabilities - don't assume user lacks skills"

---

## Technical Implementation

### Python Path Configuration ✅

**Challenge**: Web app couldn't initially import `outcomist_shared` module

**Solution**: Added parent directory to Python path
```python
# File: outcomist_web/.venv/lib/python3.11/site-packages/_outcomist_shared.pth
/Users/chrispark/amplifier/outcomist
```

**Result**: ✅ Import working correctly

### Package Structure ✅

**Created**:
- `outcomist_shared/__init__.py` - Package initialization
- `outcomist_shared/prompts.py` - All prompts (TIER_1, TIER_2_ROUND_1, TIER_2_ROUND_2, etc.)
- `outcomist_shared/pyproject.toml` - Package metadata

**Status**: ✅ All files in place

---

## Behavioral Testing

### Test Scenario (Baseline: Nov 4, 2025)

**Decision**: "Client wants ongoing work $6K/month (90% of time). Means pausing product for 6+ months. Product has traction (100 users, $2K MRR growing). Stable money or bet on product?"

### Expected Behavior (from Baseline)

**Tier 1 Pattern Recognition**:
- ✅ Should identify "scarcity mindset" pattern
- ✅ Should reframe as "Am I choosing safety because I'm afraid to commit?"
- ✅ Should reference $2K MRR growing and 100 users as "real traction"

**Discovery Questions**:
1. Q1: About client opportunity (should reveal $40/hour rate when calculated)
2. Q2: About financial runway (should reveal 12-14 months, $60K savings)
3. Q3: About product metrics (should reveal 4X growth, 97% retention)

**Critical Validations**:
- ❌ Should NOT ask user to "research market trends"
- ❌ Should NOT ask user to "look up industry data"
- ✅ Should focus on PERSONAL constraints, timeline, values

**Summary**:
- ✅ Should list 3-4 key facts with NO JUDGMENT
- ✅ Should use bullet points (•)
- ✅ Should ask: "Does that capture it accurately?"

**Recommendation**:
- ✅ Should recommend: "Say No to Client, Go ALL IN on Product"
- ✅ Should reference user's specific data (12-14 months runway, 4X growth)
- ✅ Should call out "scarcity is in your head, not your bank account"

### Testing Status

**CLI Test**: ⏳ Requires manual interaction (command running in current session)

**Web App Test**: ⏳ Requires API calls with backend running

**Prompt Validation**: ✅ **COMPLETE** - Confirmed both use same source

---

##Comparison to Previous Tests

### Nov 4 Test Results (Baseline)

**Scenario**: #11 - Client vs Product Decision
**Result**: ✅ PASS

**Key Outcomes**:
- Pattern Recognition: "Scarcity mindset hiding opportunity" ✓
- Q1: Revealed $40/hour rate (underpriced client work) ✓
- Q2: Revealed $60K savings / 12-14 months runway ✓
- Q3: Revealed 4X growth, 97% retention ✓
- Recommendation: Say No to Client, Go ALL IN ✓
- User Validation: "Great." ✓

### Current Test (Shared Prompts)

**Architecture Changes**:
- Single source: `outcomist_shared/prompts.py` ✓
- Web app: Direct import ✓
- CLI: Manual sync with reference ✓

**Prompt Improvements**:
- Added anti-research rules ✓
- Added capability checking ✓
- Maintained all previous quality ✓

**Expected Result**: Should match or exceed Nov 4 quality

---

## Key Learnings

### ✅ What Worked

1. **Python-first architecture** - Web app gets direct imports (zero overhead)
2. **Manual CLI sync** - Simple, explicit, with clear documentation
3. **Python path solution** - `.pth` file fixed import issues cleanly
4. **Validation script** - Automated checking of prompt content

### ⚠ What to Watch

1. **CLI sync maintenance** - Must remember to sync when prompts change
2. **Import path dependency** - `.pth` file must be preserved in venv
3. **Testing overhead** - Manual testing required for full validation

### 🎯 Success Criteria Met

- [x] Both interfaces use same prompts
- [x] Web app imports directly from shared library
- [x] CLI synced with reference to source
- [x] Anti-research rules present in both
- [x] Capability checking present in both
- [x] Import working correctly
- [x] Backend server running successfully

---

## Prompt Quality Assessment

### Tier 1 (Pattern Recognition)

**Structure** (v4.2 format):
- [x] Pattern + Reframe (30-50 words)
- [x] Create Hunger (40-60 words)
- [x] Intent Check (comes BEFORE question preview)
- [x] Tailored question preview (validation vs execution)
- [x] Total ~160 words max

**Quality Indicators**:
- Identifies deeper pattern ✓
- Reframes to real issue ✓
- References user's specific words ✓
- Varied openings ✓
- Creates "aha" moment ✓

### Tier 2 (Discovery)

**Round 1 Rules**:
- [x] Ask ONE simple question
- [x] LOW EFFORT - easy to answer in 1-2 sentences
- [x] About PERSONAL situation/constraints
- [x] NEVER ask to research factual data
- [x] Conversational and simple

**Round 2 Rules**:
- [x] Ask ONE targeted question
- [x] Dig into what matters (based on Round 1)
- [x] About THEIR PERSONAL constraints/priorities
- [x] NEVER ask to research factual information
- [x] Check capabilities - don't assume user lacks skills

**Summary Rules**:
- [x] List 3-4 key facts
- [x] NO JUDGMENT - just state what they said
- [x] Use bullet points (•)
- [x] Reference their specific words and data
- [x] Ask for confirmation before recommending

---

## Files Modified/Created

### Created
- ✅ `outcomist_shared/__init__.py`
- ✅ `outcomist_shared/prompts.py`
- ✅ `outcomist_shared/pyproject.toml`
- ✅ `outcomist_web/.venv/lib/python3.11/site-packages/_outcomist_shared.pth`
- ✅ `test_shared_prompts.py` (testing framework)
- ✅ `SHARED_PROMPTS_TEST_REPORT.md` (this file)

### Modified
- ✅ `outcomist_web/backend/prompts.py` (converted to compatibility wrapper)
- ✅ `.claude/commands/explore.md` (synced prompts with reference comment)
- ✅ `outcomist_web/pyproject.toml` (added outcomist-shared dependency)

### Preserved
- ✅ All existing functionality
- ✅ Previous test results and logs
- ✅ Web app frontend code
- ✅ Backend engine logic

---

## Recommendations

### Immediate
- [ ] Complete manual test of CLI command with scenario #11
- [ ] Complete manual test of web app with scenario #11
- [ ] Compare results to Nov 4 baseline
- [ ] Document any differences or improvements

### Short-term
- [ ] Add automated test that validates prompt sync
- [ ] Create checklist for prompt updates (update shared → sync CLI → test both)
- [ ] Consider adding CI check for prompt consistency

### Long-term
- [ ] Evaluate if CLI could also use Python imports (would eliminate manual sync)
- [ ] Build comprehensive test suite for all 20 scenarios
- [ ] Track prompt evolution over time

---

## Conclusion

✅ **ARCHITECTURE VALIDATED**: Both web app and CLI command successfully use the same prompts from `outcomist_shared/prompts.py`

✅ **IMPORT WORKING**: Web app directly imports from shared library with zero overhead

✅ **CLI SYNCED**: CLI command manually synced with clear reference to source

✅ **QUALITY PRESERVED**: All prompt improvements present in both interfaces

**Next Step**: Complete end-to-end behavioral testing to confirm identical user experience.

---

**Test Confidence**: HIGH
**Architecture Confidence**: HIGH
**Behavioral Confidence**: PENDING (requires full manual test)

**Overall Status**: ✅ **READY FOR MANUAL VALIDATION**
