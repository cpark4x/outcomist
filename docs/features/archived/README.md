# Archived Feature Proposals

This directory contains feature designs that were explored but deferred or deprioritized.

## Why Archive?

- **Not "rejected"** - These designs may be valuable later
- **Capture thinking** - Preserve the analysis and design work
- **Future reference** - When signals change, revisit these proposals
- **Learn from it** - Document why we paused and what would trigger revival

---

## Archived Features

### Profile System (v1 - Deferred 2025-01-10)

**File**: [profile-system-v1-deferred.md](./profile-system-v1-deferred.md)

**Why Designed**: Test #17 revealed users want personalized guidance based on accumulated context.

**Why Deferred**:
- Retention signal exists (50-67%) but not strong enough yet (need 20+ returning users)
- Unclear value proposition - uncertain about friction tolerance and approach
- Multi-profile feature was solving testing workflow, not real user need
- Felt over-engineered for current stage (3 phases, 3 months vs. simpler alternatives)

**What Would Trigger Revival**:
1. **Strong retention signal**: 20+ users with 3+ sessions each
2. **User complaints**: "I wish you remembered X" feedback
3. **Measured redundancy**: Data showing 40%+ of questions are redundant
4. **Clear value prop**: Can articulate specific time/quality benefits

**Simpler Alternatives to Try First**:
- Session summaries (3-5 bullet points per session)
- Claude naturally referencing past transcripts
- Lightweight session tagging for testing workflow

**Key Insight from Analysis**:
> "You don't need structured profiles. You need conversation continuity."
>
> Claude is already excellent at understanding context from natural language summaries.
> Structured extraction (age, role, goals) might be premature optimization before
> validating that simple summaries work well.

**If Revived**: Start with Phase 1 only (single profile, file-based), validate thoroughly before Phase 2/3.

---

## Process for Archiving Features

When deferring a feature proposal:

1. **Move to archived/** - Don't delete the work
2. **Document reason** - Why deferred? What would trigger revival?
3. **Capture alternatives** - What simpler approaches could work?
4. **Update this README** - Keep the index current
5. **Reference in decisions/** if relevant - Link to decision records

This ensures we learn from the exploration without committing to premature implementation.
