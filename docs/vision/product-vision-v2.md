# Outcomist Product Vision v2

**Last Updated**: 2025-01-10
**Status**: Aligned with Ken (Product Strategy Session)
**Supersedes**: Original 5-epic model

---

## The Core Problem

**AI drives activity, not outcomes.**

People ask AI to do things, but they often don't know:
1. What they actually want (the real outcome)
2. How to articulate it clearly enough for AI to help
3. Whether what they're asking for will achieve the outcome

The result? Lots of activity, but not the outcomes they're seeking.

---

## Core Value Proposition

**Outcomist helps you figure out what you actually want before taking action.**

Users arrive with vague questions. Outcomist asks the right questions to surface what matters, helps you understand the decision space, and turns unclear intentions into clear, executable proposals you can validate before committing.

---

## The Three-Epic Model

### **Epic 1: Deep Discovery**
**Goal**: Understand deeply enough to propose a really great solution

**What it includes**:
- Pattern recognition (30 seconds)
- Discovery questions (5-10 minutes)
- Deep analysis when needed (optional, 20-30 minutes for comparing alternatives)
- **Executability validation**: AI only proposes what it can actually deliver

**Output**: "Here's what I'll build for you" (AI's proposal)

**Key principle**: This is ONE continuous discovery process. Sometimes quick (pattern + discovery), sometimes thorough (includes deep analysis), but always in service of arriving at a solid, executable proposal.

---

### **Epic 2: Proposal Review**
**Goal**: Get user to "Yes, this is exactly what I want"

**What it includes**:
- Show tangible outcome (what user will have at the end)
- Enough polish to evaluate quality
- Explicitly identify gaps/holes
- Walk through proposal, gather feedback iteratively
- Refine collaboratively until validated

**Output**: "This is the right plan, I'm ready to proceed"

**Critical insight**: Users want to get to Epic 2 as quickly as possible. Epic 1 exists solely to make Epic 2 proposals high-quality and executable.

---

### **Epic 3: Build & Track** (Optional)
**Goal**: Execute validated proposal and track to completion

**What it includes**:
- Execute the validated proposal
- Track progress and milestones
- Handle blockers as they arise
- Measure outcomes against success criteria
- Capture learning for future decisions

**Output**: Done + learned

---

## Key Principles

### 1. **Outcome-Oriented Proposals**

Not "here's what we'll do" but "here's what you'll have at the end"

**Bad**: "We'll build a web dashboard with tracking features"
**Good**: "Here's a working prototype you can click through. Every screen, every button, every interaction. This is exactly what you'll get."

Focus on the end state, make it tangible, provide enough polish to evaluate quality.

### 2. **No "Floating Countertop" Proposals**

AI only proposes what it can **actually execute** within user's constraints.

**Bad**: AI proposes custom ML recommendation engine (user can't deploy ML, no training data, too complex)
**Good**: AI proposes Shopify's built-in filtering with custom tags (AI can write templates, user can manage in admin)

**Discovery must validate executability**:
- What's user's tech stack?
- What can they deploy?
- What's their technical comfort level?
- Budget for services?
- Who will maintain this?

### 3. **Quality Over Speed**

Epic 2 proposals should have enough quality that users can confidently evaluate them.

What "quality" means depends on project type (see Winning Scenarios below), but generally:
- **Software**: Working prototype (clickable, functional)
- **Content**: Polished drafts (ready to publish or near-ready)
- **Process**: Complete templates with real examples
- **Documents**: Fully working artifacts (can use immediately)
- **Strategy**: Complete documents with clear recommendations

### 4. **Context-Dependent Excellence**

"What would an expert agency do for this topic?"

- Software agency → Working prototype
- Strategy consultant → Complete deliverables
- Content agency → Finished examples
- Process consultant → Templates + real examples

Match the standard users expect from domain experts.

### 5. **Iterative Review Process**

Walk through proposal, gather feedback along the way. Depends on project type:
- Software: Click through prototype, comment on screens
- Content: Read pieces, comment inline
- Process: Walk through template, test with scenarios
- Documents: Use with real data, identify gaps
- Strategy: Review thinking, challenge assumptions

Not one big review at the end—progressive refinement.

---

## Epic 1: Deep Discovery (Detailed)

### What AI Must Learn

**1. The Real Problem**
- Pattern recognition reveals deeper issues
- Discovery questions uncover constraints and priorities
- Evidence gathering validates facts
- Deep analysis compares alternatives (when needed)

**2. Executability Constraints**

**Technical constraints**:
- Current tech stack (WordPress? Shopify? Custom?)
- Deployment capabilities (Vercel? Heroku? Shared hosting?)
- Maintenance capabilities (Can edit code? Need no-code?)

**Skill/Resource constraints**:
- Technical comfort level
- Budget for services ($10/month? $100/month? $1000/month?)
- Hiring capabilities (Freelancer? Agency? No one?)

**Access/Permission constraints**:
- Admin access (DNS? Database? APIs?)
- Integration requirements (CRM? Payment processor?)
- Compliance requirements (HIPAA? GDPR? SOC2?)

### AI's Internal Decision

Based on discovery answers:
- ✅ **I can execute this** (within user's constraints) → Proceed to proposal
- ❌ **I cannot execute this** (beyond user's capabilities) → Either:
  - Simplify the solution to fit constraints
  - Tell user "this requires X which is outside my scope, here's what I CAN do"

### Output of Epic 1

"Based on our discovery, here's what I'll build for you: [specific, executable proposal]"

User transitions to Epic 2 to review the proposal in detail.

---

## Epic 2: Proposal Review (Detailed)

### What AI Delivers

Epic 2 is a **complete project proposal** with these sections:

#### **Section 1: What You'll Get (Tangible Outcome)**

Not abstract descriptions—concrete, evaluable artifacts:

**Software projects**:
- Working prototype (deployed, clickable)
- All screens implemented
- All interactions working
- Real or realistic demo data
- Proof AI can build this

**Content projects**:
- Finished drafts (polished, ready to use)
- Examples showing range and quality
- Style/tone demonstrated

**Process projects**:
- Complete templates (ready to use)
- Real examples (5+ scenarios)
- Before/after comparisons

**Document/Artifact projects**:
- Fully working documents (can use immediately)
- Populated with realistic data
- Instructions for customization

**Strategy projects**:
- Complete strategy document
- Clear recommendations
- Supporting analysis/research
- Actionable next steps

**Key**: Enough polish that user can evaluate "is this what I want?" with confidence.

#### **Section 2: What It Takes**

**Your commitment**:
- Specific actions required from user
- Time investment (hours/week, duration)
- Decisions user needs to make
- Training/learning required

**Resources needed**:
- Budget/costs (itemized breakdown)
- Tools/services required
- People/skills needed
- Infrastructure requirements

**Timeline**:
- Milestones with dates
- Critical path items
- When you'll see results
- Dependencies and blockers

#### **Section 3: Explicitly Identified Gaps/Holes**

"This proposal covers X, Y, Z. It does NOT include A, B, C."

Be honest about:
- Features not included in this scope
- Assumptions being made
- Risks or unknowns
- Optional enhancements available

#### **Section 4: Options & Trade-offs**

**Core proposal**: [The main recommendation]

**Optional add-ons**:
- Enhancement A: [What + Why + Cost/Time]
- Enhancement B: [What + Why + Cost/Time]

**Alternative approaches**:
- Alternative 1: [Different path with trade-offs]
- Alternative 2: [Different path with trade-offs]

**Trade-offs made**:
- "I'm recommending X over Y because: [reasoning]"
- "This optimizes for [priority] at the expense of [other priority]"

### Review Process

**Iterative walkthrough** (format depends on project type):

1. **Present proposal section by section**
2. **Gather feedback at each stage**
3. **Refine based on feedback**
4. **Re-present refined version**
5. **Iterate until validated**: "Yes, this is exactly what I want"

**Key questions during review**:
- "Does this outcome match your vision?"
- "Is the timeline realistic?"
- "Any constraints I'm missing?"
- "Which options interest you?"
- "What concerns you?"
- "What would make this proposal better?"

### Output of Epic 2

User says: "Yes, this is the right plan. I'm ready to proceed."

Proposal is locked and ready for execution (Epic 3).

---

## Epic 3: Build & Track (Detailed)

### When This Epic Happens

Epic 3 is **optional**. Users choose to continue when they want:
- Execution support
- Progress tracking
- Blocker handling
- Outcome measurement

**Note**: Production deployment happens in Epic 3, not Epic 2.

**Why separate deployment from proposal?**
- Epic 2 focus: Get user to "yes"
- Allow refinement without production concerns
- User commits before deployment
- Can iterate proposal without production issues

### What Happens in Epic 3

**1. Execute validated proposal**
- Deploy to production
- Handle real-world integration
- Configure services
- Set up monitoring

**2. Track progress**
- Milestone completion
- Task status
- Timeline adherence
- Blocker identification

**3. Handle blockers**
- Identify issues preventing progress
- Troubleshoot problems
- Adjust plan as needed
- Escalate when necessary

**4. Measure outcomes**
- Track against success criteria
- Gather performance data
- User feedback collection
- Result validation

**5. Capture learning**
- Document what worked
- Document what didn't
- Lessons for future projects
- Pattern updates for Epic 1

### Output of Epic 3

- ✅ Working solution deployed to production
- ✅ Outcomes measured against success criteria
- ✅ Learning documented
- ✅ User can maintain/operate independently

---

## Winning Scenarios (First 5)

**Strategy**: Win a few scenarios first, not all. Pick 5 where we can demonstrate clear value and AI can execute end-to-end.

### **Scenario 1: Simple Web Feature/Tool**

**Examples**: Order tracking page, contact form, pricing calculator, booking widget

**Why this wins**:
- AI can build working prototype
- User can click through and evaluate
- Clear success criteria
- Deployable outcome
- High value if done well

**Epic 2 proposal format**:
- Live working prototype (deployed, clickable)
- Complete code repository
- Deployment instructions
- Service configuration details
- Cost breakdown

**Quality bar**: Working prototype with enough polish to evaluate UX and functionality

---

### **Scenario 2: Content Package**

**Examples**: Blog post series, email sequence, social media campaign, newsletter content

**Why this wins**:
- AI can write complete drafts
- User can read and evaluate quality
- Clear quality bar
- Immediately usable
- High-value if content is good

**Epic 2 proposal format**:
- Finished content drafts (polished, near-ready to publish)
- Editorial calendar
- SEO optimization included
- Distribution strategy
- Performance tracking plan

**Quality bar**: Polished drafts that need minimal editing before publication

---

### **Scenario 3: Process/Meeting Structure**

**Examples**: Decision framework, weekly sync structure, project intake process, review workflow

**Why this wins**:
- AI can create complete templates
- User can see real examples
- Clear before/after comparison
- Can start using immediately
- High value if process improves efficiency

**Epic 2 proposal format**:
- Complete templates (meeting agendas, decision logs, workflows)
- 5+ real examples demonstrating use
- Before/after process comparison
- Training materials for team
- Rollout plan

**Quality bar**: Templates complete enough to use immediately with real scenarios

---

### **Scenario 4: Document/Artifact Creation**

**Examples**: Proposal template, pricing calculator, project plan, client onboarding doc

**Why this wins**:
- AI can build working document/tool
- User can test with real data
- Clear utility
- Immediately useful
- High value if well-designed

**Epic 2 proposal format**:
- Fully working document or tool
- Populated with realistic demo data
- Instructions for customization
- Template for reuse
- Maintenance guide

**Quality bar**: Working artifact that user can immediately use with their real data

---

### **Scenario 5: Strategy/Plan Document**

**Examples**: Go-to-market plan, pricing strategy, content strategy, growth plan

**Why this wins**:
- AI can draft complete document
- User can evaluate thinking quality
- Clear recommendations
- Actionable next steps
- High value if strategy is sound

**Epic 2 proposal format**:
- Complete strategy document (10-20 pages)
- Executive summary
- Supporting research/analysis
- Clear recommendations
- Implementation roadmap
- Success metrics

**Quality bar**: Complete document with depth of thinking that demonstrates expertise

---

## Open Questions to Resolve

### For Each Winning Scenario

**1. Exact quality bar definition**
- How complete is "complete enough"?
- How polished is "polished enough"?
- What gaps are acceptable to leave?

**2. Review process specifics**
- What does iterative review look like?
- How many refinement rounds?
- What feedback mechanisms?

**3. Production deployment approach**
- Does deployment happen in Epic 2 or Epic 3?
- What's the handoff process?
- Who maintains after deployment?

**4. Success criteria**
- How do we know Epic 2 proposal is "good enough"?
- What metrics validate quality?
- How do we measure user satisfaction?

### General Product Questions

**1. Discovery process refinement**
- What questions reliably validate executability?
- How to identify "floating countertop" proposals early?
- When to push back vs adapt solution?

**2. Proposal templates**
- Should we have templates per scenario type?
- How much standardization vs customization?
- What format works best for review?

**3. Epic transitions**
- How to guide users from Epic 1 → Epic 2?
- What signals indicate readiness for Epic 3?
- Can users skip Epic 3 and execute independently?

**4. Pricing/Business model**
- How to price by epic?
- Subscription vs per-project?
- What's included vs what costs extra?

---

## Success Criteria

### For Epic 1 (Deep Discovery)
- ✅ AI understands real problem (not just stated problem)
- ✅ Executability validated (AI can actually build this)
- ✅ User's constraints captured accurately
- ✅ Proposal direction is clear and specific

### For Epic 2 (Proposal Review)
- ✅ User can confidently evaluate proposal quality
- ✅ No major surprises during execution
- ✅ Gaps/holes explicitly identified upfront
- ✅ User says "Yes, this is exactly what I want"

### For Epic 3 (Build & Track)
- ✅ Solution deployed to production
- ✅ Outcomes measured against criteria
- ✅ User can maintain/operate independently
- ✅ Learning captured for future use

---

## What Changed from Original Vision

### **Old Model**: 5 Separate Epics
1. Pattern Recognition (30 sec)
2. Discovery (5-10 min)
3. Deep Analysis (20-30 min)
4. Design (variable)
5. Build & Track (ongoing)

**Problem**: Felt like 5 separate stages, unclear when to use each, too complex

### **New Model**: 3 Clear Epics

**Epic 1: Deep Discovery** (combines old 1-2-3)
- One continuous discovery process
- Depth adapts to decision complexity
- Validates executability
- Output: Executable proposal

**Epic 2: Proposal Review** (replaces old 4)
- Not "design" but "review proposal"
- Working prototypes, not concepts
- Iterative refinement
- Output: Validated plan

**Epic 3: Build & Track** (same as old 5)
- Execute validated proposal
- Track to completion
- Output: Done + learned

**Why this is better**:
- Clearer purpose for each epic
- Faster path to value (get to Epic 2 quickly)
- Less confusing for users
- Easier to explain and understand

---

## Next Steps

### Immediate (Documentation)
1. ✅ Capture this vision document
2. ⏳ Update end-to-end-flow.md with new model
3. ⏳ Create Epic 1, 2, 3 detailed docs
4. ⏳ Document winning scenarios in detail

### Near-term (Validation)
1. Pick ONE winning scenario to build first
2. Design Epic 2 proposal format for that scenario
3. Build complete Epic 1 → Epic 2 → Epic 3 flow
4. Test with real users
5. Validate quality and process

### Medium-term (Expansion)
1. Build remaining 4 winning scenarios
2. Refine Epic 2 proposal templates
3. Document learnings and patterns
4. Expand to new scenario types

---

## Document Status

**Created**: 2025-01-10
**Authors**: Chris Park (Founder) + Ken (Product Strategy)
**Status**: Aligned and validated
**Audience**: Product team, AI assistants, future builders
**Maintenance**: Living document, update as we learn from real usage

---

**Key Insight**: Users want to get to Epic 2 (proposal review) as quickly as possible. Epic 1 exists solely to make Epic 2 proposals high-quality, executable, and gap-free. Quality of the proposal is the #1 goal.
