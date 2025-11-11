# Profile System Design Specification

**Status**: Design Phase
**Version**: 1.0
**Created**: 2025-01-10
**Owner**: Chris Park

---

## Executive Summary

The Profile System enables Outcomist to learn from each conversation and provide increasingly personalized decision guidance. It solves the "cold start" problem where every session starts from scratch, delivering on Test #17's insight that users want accumulated context to inform future conversations.

**Core Value**: Transform Outcomist from a one-time consultant into a long-term decision partner.

---

## Problem Statement

### Current State
- Every `/explore` session starts with no context
- Users must re-explain their role, goals, constraints repeatedly
- No memory of past decisions or patterns
- Generic guidance that doesn't improve over time

### Test #17 Evidence
In a single conversation, we learned:
- User is 46, wants to retire at 55 (9-year runway)
- Strong AI capabilities
- Values outcome-focused approach + learning
- Budget/time constraints

**User expectation**: "Remember this for next time"

### Requirements
1. **Automatic learning** from conversations
2. **Multi-profile support** (user vs. people they help)
3. **User control** (review/edit data)
4. **Privacy/security** (zero data leakage)

---

## Solution Overview

### Three-Phase Progressive Enhancement

```
Phase 1: Single Profile (v1.0) → 2 weeks
  ↓
Phase 2: Multi-Profile Detection (v1.5) → +4 weeks
  ↓
Phase 3: Full Profile Management (v2.0) → +8 weeks
```

**Philosophy**: Start simple (files), grow as needed (database), deliver value at each phase.

---

## Phase 1: Single Profile (v1.0)

### Goal
User's own profile persists across sessions, enabling personalized discovery.

### Scope
- ✅ Single "self" profile per user
- ✅ Automatic extraction with user review
- ✅ File-based storage
- ✅ Basic profile viewing
- ✅ Pre-fill discovery with known facts
- ❌ Multiple profiles (Phase 2)
- ❌ Profile editing (Phase 3)
- ❌ Multi-tenant security (Phase 3)

### Data Model

```python
class UserProfile(BaseModel):
    """User's persistent profile data."""

    # Identity
    profile_id: str = "self"  # Phase 1: Always "self"
    name: Optional[str] = None

    # Demographics (if relevant to decisions)
    age: Optional[int] = None
    role: Optional[str] = None  # "Founder", "Engineer", "Manager"
    industry: Optional[str] = None

    # Goals & Context
    goals: list[str] = []  # "Retire at 55", "Build side income"
    constraints: list[str] = []  # "Budget $500/mo", "No-code only"
    values: list[str] = []  # "Outcome-focused", "Learning matters"
    preferences: dict[str, str] = {}  # {"risk_tolerance": "moderate"}

    # Skills & Capabilities
    skills: list[str] = []  # "AI expert", "Python developer"
    tech_stack: list[str] = []  # "Shopify", "Custom React"

    # History & Patterns
    past_decisions: list[str] = []  # Session IDs for reference
    common_patterns: list[str] = []  # Observed patterns across sessions

    # Metadata
    created_at: datetime
    updated_at: datetime
    last_session_id: Optional[str] = None
    confidence_scores: dict[str, float] = {}  # Field → confidence (0-1)
```

**Storage**: `~/.outcomist/profiles/self.json`

**Example Profile**:
```json
{
  "profile_id": "self",
  "name": "Chris",
  "age": 46,
  "role": "Founder",
  "goals": [
    "Retire at 55 (9-year runway)",
    "Build residual side income"
  ],
  "skills": ["AI expert", "Technical background"],
  "constraints": [
    "Want validation in 1-2 months",
    "Willing to invest money and time"
  ],
  "values": [
    "Outcome-focused",
    "Learning matters (double benefit)"
  ],
  "past_decisions": ["session_20250110_143022"],
  "created_at": "2025-01-10T14:30:22Z",
  "updated_at": "2025-01-10T14:45:18Z",
  "confidence_scores": {
    "age": 1.0,
    "goals": 0.9,
    "skills": 0.8
  }
}
```

### Extraction Strategy

#### Post-Conversation Synthesis (Not Real-Time)

**Why post-conversation**: Better accuracy, full context, user can review before saving.

**Process**:
```
1. User completes discovery session
2. System analyzes full transcript
3. Proposes profile updates
4. User reviews and confirms
5. Profile saved with confidence scores
```

**Extraction Prompt** (used with Claude):
```python
def extract_profile_updates(session_transcript: str, existing_profile: UserProfile) -> dict:
    """
    Extract learnings from conversation.

    Prompt to Claude:
    ---
    Review this conversation transcript and extract facts about the user.

    Focus on:
    - Demographics: Age, role, industry (if mentioned)
    - Goals: What they want to achieve
    - Constraints: Budget, time, skill limitations
    - Values: What matters to them (revealed through choices)
    - Skills: Capabilities they mention or demonstrate
    - Tech stack: Tools/platforms they use

    RULES:
    - Only extract HIGH CONFIDENCE facts (explicitly stated)
    - Don't infer beyond what's directly stated
    - Mark confidence: "stated" (1.0) vs "implied" (0.7)
    - New facts only (not already in existing profile)

    Return JSON with proposed updates and confidence scores.
    ---
    """
    # Claude extracts structured data
    # Returns: {"goals": [...], "skills": [...], "confidence_scores": {...}}
```

### User Experience

#### 1. Post-Session Profile Update

**After recommendation delivered**:
```
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

📝 Profile Update

I learned a lot about you today. Here's what I'd like to remember for next time:

New Information:
• Age: 46, planning to retire at 55
• Skills: Strong AI capabilities
• Goals: Build residual side income
• Values: Outcome-focused, learning matters

Already Knew:
• [None - first conversation]

This will help me personalize future conversations.

[✓ Save These] [✗ Skip] [✎ Edit Before Saving]
```

**User choices**:
- **Save These**: Accept all updates
- **Skip**: Don't save (session still recorded)
- **Edit Before Saving**: Opens editing interface (Phase 3)

#### 2. Profile-Aware Discovery (Second Session)

**First session**:
```
User: "I want to start a side hustle"

Outcomist: "I can help you think through this. I'll ask a few questions
to understand your situation - what's driving this, what you're considering,
and what matters most. (~10-15 min)

Let's start: What's your current situation?"
```

**Second session** (with profile):
```
User: "I'm considering a different side hustle idea"

Outcomist: "Good to see you again! Based on what we discussed before
(9-year retirement runway, AI expertise, outcome-focused), let me understand
this new idea.

What's changed or different about this opportunity compared to what we
explored last time?"
```

**Key difference**:
- Skip redundant questions (age, goals, constraints)
- Reference past context
- Focus on new information

#### 3. Profile Viewing

**Command**: `/profile` or `/profile view`

**Output**:
```
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

Your Profile

Identity:
• Age: 46
• Role: Founder

Goals:
• Retire at 55 (9-year runway)
• Build residual side income

Skills:
• AI expert
• Technical background

Constraints:
• Want validation in 1-2 months
• Willing to invest money and time

Values:
• Outcome-focused
• Learning matters (double benefit)

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

Last updated: Today from "side hustle" conversation
Sessions: 3 total

[Clear Profile] - Start fresh (data deleted)

Note: You can review and update your profile after each conversation.
```

### Technical Implementation

#### File Structure
```
~/.outcomist/
  profiles/
    self.json          # User's profile
  sessions/
    <session_id>.json  # Existing session storage
```

#### Core Functions

```python
# profile_manager.py

def load_profile() -> UserProfile:
    """Load user's profile from disk."""
    path = Path.home() / ".outcomist" / "profiles" / "self.json"
    if path.exists():
        return UserProfile.model_validate_json(path.read_text())
    return UserProfile()  # Empty profile

def save_profile(profile: UserProfile) -> None:
    """Save profile to disk."""
    path = Path.home() / ".outcomist" / "profiles" / "self.json"
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(profile.model_dump_json(indent=2))
    path.chmod(0o600)  # Read/write for user only

def extract_profile_updates(
    session: Session,
    existing_profile: UserProfile
) -> dict:
    """
    Use Claude to extract profile updates from session transcript.
    Returns proposed updates for user review.
    """
    # Build prompt with transcript + existing profile
    # Call Claude API
    # Parse structured output
    # Return updates dict with confidence scores

def apply_profile_updates(
    profile: UserProfile,
    updates: dict
) -> UserProfile:
    """Apply approved updates to profile."""
    # Merge updates into profile
    # Update timestamps
    # Update confidence scores
    return profile

def get_profile_context_for_discovery(profile: UserProfile) -> str:
    """
    Generate context string to prepend to discovery.
    Returns: "Based on what we discussed before..."
    """
    if not profile.goals and not profile.skills:
        return ""  # First time, no context

    context_parts = []
    if profile.goals:
        context_parts.append(f"goals: {', '.join(profile.goals[:2])}")
    if profile.skills:
        context_parts.append(f"skills: {', '.join(profile.skills[:2])}")

    return f"Based on what we discussed before ({', '.join(context_parts)})"
```

### Discovery Integration

**Modified Tier 1 flow**:
```python
# In .claude/commands/explore.md

## Step 0.5: Load Profile Context (NEW)

Before pattern recognition, check if user has existing profile:

profile = load_profile()
context = get_profile_context_for_discovery(profile)

If context exists:
- Prepend to Tier 1 response: "Good to see you again! {context}, ..."
- Adjust questions to avoid re-asking known facts
- Reference past decisions if relevant

If no context:
- Proceed with standard Tier 1 (first-time user experience)
```

**Modified Tier 2 discovery**:
```python
## Round 1: Landscape Question (PROFILE-AWARE)

Before asking Round 1 question, check profile for known facts:
- Skip questions about age, role, goals if already known
- Ask about NEW information or CHANGED circumstances
- Reference past context: "Last time you mentioned X. Is that still true?"

Example with profile:
  "Last time you mentioned retiring at 55. Is that still the goal,
   or has your timeline changed?"

Example without profile (first time):
  "What's your current situation?"
```

### Success Criteria

✅ **Functional**:
- [ ] Profile saves after first session
- [ ] Second session skips redundant questions
- [ ] Profile data persists across app restarts
- [ ] `/profile` command displays profile correctly

✅ **Quality**:
- [ ] Extraction accuracy >80% (manual review of 10 sessions)
- [ ] Zero data loss (profile survives crashes/errors)
- [ ] User sees value ("This is helpful" feedback)

✅ **Privacy**:
- [ ] File permissions 600 (user only)
- [ ] No sensitive data exposed in logs
- [ ] Clear profile deletion works

### Testing Plan

**Unit Tests**:
- Profile load/save
- Extraction logic (mock Claude responses)
- Update merging
- Confidence score calculations

**Integration Tests**:
- Full session → extraction → save → load → next session flow
- Profile viewing command
- Clear profile command

**User Testing**:
- 5 users complete 2+ sessions each
- Measure: redundancy reduction, satisfaction, accuracy

---

## Phase 2: Multi-Profile Detection (v1.5)

### Goal
Automatically detect when user is helping others, switch to appropriate profile.

### Scope
- ✅ Context detection (self vs. other)
- ✅ Multi-profile storage
- ✅ Profile creation flow
- ✅ Profile switching during conversation
- ✅ Profile list view
- ❌ Profile editing (Phase 3)
- ❌ Database backing (Phase 3)

### Context Detection

**Linguistic signals for profile switching**:

**"Self" profile**:
- "I want to...", "Should I...", "My goal is..."
- First-person throughout
- Personal pronouns: "I", "me", "my"

**"Other" profile**:
- "My boss wants...", "A client asked...", "My friend needs help with..."
- Third-person: "he", "she", "they", "the company"
- Helping language: "I'm helping someone who..."

**Detection prompt**:
```python
def detect_profile_context(decision_statement: str) -> tuple[str, float]:
    """
    Determine which profile this conversation is about.

    Returns: (profile_id, confidence)
    - ("self", 0.95) → User's own decision
    - ("other:boss", 0.85) → About their boss
    - ("ambiguous", 0.4) → Need to ask explicitly
    """
    # Use Claude to analyze linguistic patterns
    # Return profile_id and confidence score
```

### Multi-Profile Storage

**File structure**:
```
~/.outcomist/
  profiles/
    self.json                    # User's own profile
    other_boss.json              # Boss's profile
    other_client_abc_corp.json   # Client profile
```

**Profile naming convention**:
- `self` → User's own profile (special case)
- `other_<name>` → Someone else's profile
- Name: Slugified from user input ("My Boss" → "boss", "Client ABC Corp" → "client_abc_corp")

### User Experience

#### Profile Creation Flow

**When "other" detected**:
```
Outcomist: "I notice you're asking about someone else's decision
(based on phrases like 'my boss wants').

Who is this decision for?
• Type a name (e.g., 'my boss', 'Client ABC', 'friend Sarah')
• Or type 'me' if this is actually YOUR decision

→ "
```

**User enters**: "my boss"

```
Outcomist: "Got it. I'll create a profile for 'Your Boss' to track
their context separately from yours.

Let's understand their situation: [proceed with discovery]"
```

#### Profile List View

**Command**: `/profile list`

**Output**:
```
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

Your Profiles

• You (self)
  Last used: Today
  Sessions: 5

• Your Boss
  Last used: 3 days ago
  Sessions: 2
  Goals: Improve team efficiency

• Client ABC Corp
  Last used: 1 week ago
  Sessions: 1
  Goals: Migrate to cloud

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

Commands:
• /profile view <name> - View specific profile
• /profile switch <name> - Switch default profile
```

#### Profile Switching

**Command**: `/profile switch boss`

**Output**:
```
✓ Switched to profile: Your Boss

Next /explore session will use this profile's context.
To switch back: /profile switch self
```

### Success Criteria

✅ **Functional**:
- [ ] Detects "other" context >70% accuracy
- [ ] Can create and load multiple profiles
- [ ] Profile switching works correctly
- [ ] Profile list shows all profiles

✅ **Quality**:
- [ ] <20% false positives (wrong profile detected)
- [ ] User can easily correct mistakes
- [ ] Ambiguous cases prompt for clarification

---

## Phase 3: Full Profile Management (v2.0)

### Goal
Complete profile CRUD, database backing, multi-tenant security.

### Scope
- ✅ Profile editing (web UI)
- ✅ Database migration (SQLite/Postgres)
- ✅ Multi-tenant support (user_id scoping)
- ✅ Privacy controls
- ✅ Data export/deletion (GDPR)
- ✅ Profile merging/splitting
- ✅ Confidence decay over time

### Database Schema

```sql
CREATE TABLE users (
    user_id TEXT PRIMARY KEY,
    email TEXT UNIQUE NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE profiles (
    profile_id TEXT PRIMARY KEY,
    user_id TEXT NOT NULL,
    profile_type TEXT CHECK(profile_type IN ('self', 'other')),
    name TEXT,
    data JSONB NOT NULL,  -- Full profile data
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    last_session_id TEXT,
    FOREIGN KEY (user_id) REFERENCES users(user_id) ON DELETE CASCADE
);

CREATE INDEX idx_profiles_user_id ON profiles(user_id);
CREATE INDEX idx_profiles_type ON profiles(user_id, profile_type);

-- Row-level security for multi-tenant
ALTER TABLE profiles ENABLE ROW LEVEL SECURITY;

CREATE POLICY profiles_isolation ON profiles
    USING (user_id = current_setting('app.current_user_id'));
```

### Profile Editing UI

**Web interface** (React component):
```tsx
<ProfileEditor profile={profile}>
  <Section title="Identity">
    <Input label="Name" value={profile.name} />
    <Input label="Age" value={profile.age} type="number" />
    <Input label="Role" value={profile.role} />
  </Section>

  <Section title="Goals">
    <ListEditor items={profile.goals} />
    <Button>Add Goal</Button>
  </Section>

  <Section title="Skills">
    <ListEditor items={profile.skills} />
    <Button>Add Skill</Button>
  </Section>

  <Button primary onClick={save}>Save Changes</Button>
  <Button onClick={cancel}>Cancel</Button>
</ProfileEditor>
```

### Privacy Controls

**Settings page**:
```
Profile Privacy Settings

□ Automatically extract profile data from conversations
  └─ If unchecked, I'll ask before saving anything

□ Extract demographics (age, role, industry)
  └─ Some users prefer not to share this

□ Extract goals and constraints

□ Extract skills and tech stack

[Decay old data after]: [6 months ▾]
  └─ Information older than this gets flagged for review

[Export My Data] - Download all profile data (JSON)
[Delete All Profiles] - Permanently delete all data
```

### Success Criteria

✅ **Functional**:
- [ ] Multi-user system works (no data leakage)
- [ ] Profile editing persists correctly
- [ ] Privacy controls honored
- [ ] Data export includes all user data
- [ ] Profile deletion removes all traces

✅ **Security**:
- [ ] Zero cross-user data leakage (penetration test)
- [ ] Encryption at rest
- [ ] Audit logging for sensitive operations

✅ **Compliance**:
- [ ] GDPR: Right to access (data export)
- [ ] GDPR: Right to deletion
- [ ] GDPR: Right to rectification (editing)

---

## Edge Cases & Handling

### 1. Conflicting Data
**Problem**: User says different things across sessions

**Example**: "I'm 45" → later "I'm 46"

**Handling**:
- Update to most recent value
- Show in update summary: "Updated age: 45 → 46"
- Allow manual correction if wrong

### 2. False Profile Detection
**Problem**: System thinks "My boss wants..." is about user

**Handling**:
- Confidence threshold for auto-switching (>0.8)
- If <0.8: Ask explicitly
- Easy undo: "Actually, this is MY decision" button

### 3. Sensitive Information
**Problem**: User shares salary, health conditions, personal details

**Handling**:
- Mark sensitive fields (encrypted storage)
- Privacy controls: "Don't extract demographics"
- User reviews ALL extractions before saving

### 4. Profile Staleness
**Problem**: Goals/constraints change over time

**Example**: "Retire at 55" → now "Retire at 60"

**Handling**:
- Confidence decay: 6+ month old data flagged
- Periodic review: "Your profile says X. Still accurate?"
- Easy bulk update: "What's changed?"

---

## Technical Architecture

### Component Diagram

```
┌─────────────────────────────────────────────────┐
│              Outcomist CLI/Web                   │
├─────────────────────────────────────────────────┤
│  /explore command                                │
│  /profile view|list|switch                       │
└────────────────┬────────────────────────────────┘
                 │
                 ▼
┌─────────────────────────────────────────────────┐
│          Profile Manager Service                 │
├─────────────────────────────────────────────────┤
│  • load_profile()                                │
│  • save_profile()                                │
│  • extract_updates()                             │
│  • detect_context()                              │
│  • switch_profile()                              │
└────────────────┬────────────────────────────────┘
                 │
                 ▼
┌─────────────────────────────────────────────────┐
│          Storage Layer                           │
├─────────────────────────────────────────────────┤
│  Phase 1: File System (~/.outcomist/profiles/)   │
│  Phase 2: File System (multi-file)               │
│  Phase 3: Database (PostgreSQL)                  │
└─────────────────────────────────────────────────┘
```

### Integration Points

**1. Discovery System** (`.claude/commands/explore.md`):
- Load profile before Tier 1
- Inject context into pattern recognition
- Skip known facts in questions
- Reference past decisions

**2. Session Storage** (existing):
- Link sessions to profiles
- Track profile updates per session
- Enable decision history

**3. Claude API**:
- Extraction prompts
- Context detection
- Profile synthesis

---

## Implementation Roadmap

### Week 1-2: Phase 1 Core
- [ ] Data model (`UserProfile` class)
- [ ] File storage (load/save functions)
- [ ] Extraction logic (Claude integration)
- [ ] Post-session update flow

### Week 3-4: Phase 1 Integration
- [ ] Discovery integration (profile-aware questions)
- [ ] `/profile` view command
- [ ] Testing (unit + integration)
- [ ] User testing (5 users, 2+ sessions each)

### Week 5-8: Phase 2 Multi-Profile
- [ ] Context detection logic
- [ ] Multi-file storage
- [ ] Profile creation flow
- [ ] `/profile list|switch` commands
- [ ] Testing

### Week 9-16: Phase 3 Full Management
- [ ] Database migration
- [ ] Profile editing UI
- [ ] Privacy controls
- [ ] Multi-tenant security
- [ ] GDPR compliance
- [ ] Security audit

---

## Success Metrics

### Phase 1 Metrics
- **Adoption**: % of users who complete 2+ sessions (target: 60%+)
- **Efficiency**: % reduction in redundant questions (target: 50%+)
- **Accuracy**: Profile extraction accuracy (target: 80%+)
- **Satisfaction**: User feedback on personalization (qualitative)

### Phase 2 Metrics
- **Detection**: Multi-profile context detection accuracy (target: 70%+)
- **Usage**: Avg profiles per power user (target: 2-3)
- **Errors**: False positive rate (target: <20%)

### Phase 3 Metrics
- **Scale**: # of active users
- **Security**: Zero data leakage incidents
- **Compliance**: GDPR request handling time (target: <48 hours)

---

## Open Questions

**For Product Team**:
1. **Opt-in vs Opt-out**: Should profile extraction be default-on or require explicit consent?
2. **Verification**: User confirms every update, or trust automatic extraction?
3. **Sharing**: Allow profile sharing within teams? (e.g., shared client profiles)
4. **Retention**: Delete profiles after X months of inactivity?
5. **Monetization**: Free tier profile limits? Premium unlimited profiles?

**For Engineering**:
1. **Storage**: SQLite sufficient for Phase 3, or require Postgres?
2. **Encryption**: File-level encryption in Phase 1, or defer to Phase 3?
3. **Backup**: Automatic profile backups? Where stored?

---

## Dependencies

**Existing Systems**:
- Session storage (already implemented)
- Claude API integration (already implemented)
- `/explore` command flow (already implemented)

**New Dependencies**:
- Pydantic (already used) - Data validation
- Claude API - Extraction and context detection
- (Phase 3) Database ORM (SQLAlchemy or similar)
- (Phase 3) React components for editing UI

---

## Risk Assessment

| Risk | Impact | Likelihood | Mitigation |
|------|--------|------------|------------|
| Poor extraction accuracy | High | Medium | Manual review before saving, confidence scoring |
| Users don't see value | High | Low | User testing in Phase 1, iterate on UX |
| Privacy concerns | High | Low | Opt-in controls, clear data ownership, GDPR compliance |
| Profile staleness | Medium | High | Confidence decay, periodic review prompts |
| False context detection | Medium | Medium | Confidence thresholds, easy correction UI |
| Data loss (file corruption) | Medium | Low | Automatic backups, validation on load |

---

## Next Steps

1. **Review this spec** with team
2. **Answer open questions** (opt-in/out, retention, etc.)
3. **Create implementation tickets** for Phase 1
4. **Assign engineering resources**
5. **Set up user testing group** (5 users for Phase 1 validation)

---

## Appendix: Example Scenarios

### Scenario 1: First-Time User (Phase 1)

**Session 1**:
```
User: /explore "Should I start a side hustle?"

[Normal discovery flow - no profile context]

[After recommendation]
Outcomist: "📝 Profile Update

I learned about you today:
• Age: 46, planning to retire at 55
• Skills: Strong AI capabilities
• Goals: Residual side income
• Values: Outcome-focused

[✓ Save] [✗ Skip]"

User: [Clicks Save]
```

**Session 2** (3 days later):
```
User: /explore "Should I pivot to a different side hustle idea?"

Outcomist: "Good to see you again! Based on what we discussed
(9-year retirement runway, AI expertise, outcome-focused), let me
understand this new opportunity.

What's changed or different about this idea compared to the
AI-powered meal planning service we explored?"
```

### Scenario 2: Multi-Profile User (Phase 2)

**Session 1**:
```
User: /explore "My boss wants to reorganize the team structure"

Outcomist: "I notice you're asking about someone else's decision
(your boss).

Who is this decision for?
→ "

User: "my boss"

Outcomist: "Got it. I'll create a profile for 'Your Boss'.

Let's understand their situation: What's driving this reorganization?"
```

**Session 2** (later):
```
User: /explore "Should I ask for a raise?"

Outcomist: [Detects "I" = self profile]

"This sounds like YOUR decision (not your boss's).
Switching to your profile.

Based on what I know about you (AI expertise, outcome-focused),
let's think through this timing..."
```

---

**End of Specification**
