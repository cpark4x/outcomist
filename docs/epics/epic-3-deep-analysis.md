# Epic 3: Deep Analysis & Alternatives

**Status**: ⏳ Proposed (not yet implemented)
**Duration**: ~20-30 minutes (projected)
**Target Version**: TBD

---

## Overview

Epic 3 provides systematic exploration of alternatives, risk assessment, and scenario planning for complex, high-stakes decisions. Users walk away with clear option comparison, understood risks, and confident direction.

## User Story

**As a decision-maker facing a complex choice**, I systematically explore alternatives, assess risks, and plan scenarios, **so I** choose confidently even with uncertainty.

## Outcome

Users walk away with:
- **Multiple options** clearly compared across criteria
- **Risks identified** and assessed for each option
- **Scenarios planned** (best case, worst case, likely case)
- **Decision criteria** refined and explicit
- **Clear recommendation** with full rationale

## Design Principles

### Systematic (Structured comparison)
Options compared across consistent criteria. Not ad-hoc—systematic framework.

### Risk-Aware (Surface uncertainties)
Explicitly identify and assess risks for each option. Make uncertainty visible.

### Scenario-Based (Plan for multiple futures)
Explore best case, worst case, and most likely scenarios. Prepare for range of outcomes.

### Criteria-Driven (Define what matters)
Help users clarify what matters most. Use those criteria to recommend.

---

## Proposed Flow

### 1. Option Generation

**System generates 3-5 viable options** from Epic 2 insights

**Example** (from "Client vs Product" decision):
- Option A: Take client work, pause product
- Option B: Focus on product, decline client
- Option C: Hybrid approach (part-time client)
- Option D: Find different client (higher rate, fewer hours)

**User refines**: Add, remove, or modify options

### 2. Option Comparison

**System facilitates comparison across criteria**:
- Financial impact (short-term, long-term)
- Time investment required
- Alignment with goals
- Reversibility (easy to undo vs. hard to undo)
- Learning/growth potential

**Format**: Side-by-side comparison table or matrix

### 3. Risk Assessment

**For each option, identify risks**:
- What could go wrong?
- How likely is each risk?
- How severe if it happens?
- Can risks be mitigated?

**Example** (Product option):
- Risk: Product growth stalls → Medium likelihood, high severity
- Risk: Run out of runway → Low likelihood (12 months), high severity
- Mitigation: Can always find client work if needed

### 4. Scenario Planning

**For chosen direction(s), explore scenarios**:

**Best case**: Everything goes well
- Product: 10X growth continues, $10K MRR in 6 months, raises funding

**Worst case**: Things go poorly
- Product: Growth stalls, runway burns, back to client work

**Most likely**: Realistic middle ground
- Product: Steady growth to $5K MRR, breaks even in 9 months

**Purpose**: Prepare for range of outcomes, reduce surprise

### 5. Criteria Refinement

**System helps clarify what matters most**:
- "If money weren't a concern, which would you choose?" → Reveals values
- "Which option aligns best with who you want to become?" → Reveals identity
- "Which option would you regret NOT trying?" → Reveals priorities

**Output**: Explicit decision criteria ranked by importance

### 6. Recommendation with Rationale

**System recommends option with full reasoning**:

**Format**:
```
I recommend: [Option]

Reasoning:
- Aligns with your top criteria: [criteria]
- Risks are manageable: [how]
- Scenarios suggest: [insight]
- This positions you for: [future]

If you choose this option:
- Next steps: [actions]
- Watch for: [risks to monitor]
- Success looks like: [criteria]
```

---

## Features (Proposed)

### Feature 3.1: Option Generation & Comparison
- Generate 3-5 options from Epic 2 insights
- User refines options
- Side-by-side comparison across criteria

### Feature 3.2: Risk Assessment
- Identify risks per option
- Likelihood and severity assessment
- Mitigation strategies

### Feature 3.3: Scenario Planning
- Best case, worst case, likely case
- For chosen direction(s)
- Prepare for range of outcomes

### Feature 3.4: Trade-off Analysis
- Explicit trade-off evaluation
- "If X, then not Y" clarity
- Surface hidden costs

### Feature 3.5: Decision Criteria Refinement
- Clarify what matters most
- Rank criteria by importance
- Use to recommend option

---

## When to Use Epic 3

**Use when**:
- Decision is complex with multiple viable options
- Stakes are high (significant money, time, or impact)
- User needs systematic comparison
- Risk assessment valuable
- Epic 2 recommendation isn't sufficient clarity

**Skip when**:
- Epic 2 recommendation is clear and user feels confident
- Decision is straightforward (one obvious right answer)
- Stakes are low (easily reversible)
- Time pressure doesn't allow 20-30 minute exploration

---

## Implementation Approach (Future)

### Architecture
**Engine**: `AnalysisEngine` (similar to `ExplorationEngine` pattern)

**Methods**:
- `generate_options()`: Create option list from Epic 2
- `compare_options()`: Facilitate comparison
- `assess_risks()`: Risk identification and assessment
- `plan_scenarios()`: Best/worst/likely scenarios
- `refine_criteria()`: Clarify what matters most
- `recommend_option()`: Final recommendation

### Integration with Epic 2
**Input**: Epic 2 insights, constraints, priorities
**Output**: Options analyzed, risks assessed, recommendation

### Session State
```python
{
  "analysis": {
    "options": [Option],
    "comparison": ComparisonMatrix,
    "risks": [Risk],
    "scenarios": [Scenario],
    "criteria": [Criterion],
    "recommendation": "option + rationale"
  }
}
```

---

## Open Questions

**To resolve during implementation**:

1. **Option generation**: How many options? How to ensure they're genuinely different?
2. **Comparison criteria**: Fixed list or adaptive based on decision type?
3. **Risk assessment**: Qualitative (high/med/low) or quantitative (probabilities)?
4. **Scenario detail**: How deep to go in each scenario?
5. **User engagement**: How to keep 20-30 minutes engaging without fatigue?

---

## Success Criteria (When Implemented)

**Effective comparison**: Users see clear differences between options
**Risk clarity**: Users understand risks and feel prepared
**Scenario utility**: Scenarios help users prepare, not overwhelm
**Confident decisions**: Users choose with less uncertainty
**No regret**: Users feel they explored thoroughly before deciding

---

## Related Documentation

- **Epic 2 (Discovery)**: [epic-2-discovery.md](./epic-2-discovery.md) - Epic 3 builds on Epic 2 insights
- **Epic 4 (Design)**: [epic-4-design.md](./epic-4-design.md) - Next step after option chosen
- **Epic Transitions**: [../principles/epic-transitions.md](../principles/epic-transitions.md) - When to use Epic 3
- **End-to-End Flow**: [../vision/end-to-end-flow.md](../vision/end-to-end-flow.md) - Complete journey

---

## Document Status

**Last Updated**: 2025-01-10
**Status**: Proposed (directional, not prescriptive)
**Implementation**: TBD after Epic 1-2 documentation complete
**Next Review**: When Epic 3 implementation begins
