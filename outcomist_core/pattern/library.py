"""Pattern library - 9 validated decision patterns from real usage.

Extracted from docs/patterns/pattern-library.md (Last Updated: 2025-01-07)
Status: 9 patterns captured from 13 documented test scenarios
"""

from typing import List
from .types import Pattern, PatternType, Signal, Question, Pitfall


def get_all_patterns() -> List[Pattern]:
    """Get all 9 validated patterns."""
    return [
        PERSONAL_SANCTUARY,
        EMPLOYABILITY_ANXIETY,
        HEALTH_ANXIETY,
        ADDITIONAL_REVENUE_MISFRAME,
        POPULARITY_CONTEST,
        SCARCITY_MINDSET,
        SOLUTION_LOOKING_FOR_PROBLEM,
        PREMATURE_PRESENTATION,
        STUCK_IN_BUILD_PHASE,
    ]


def get_pattern_by_id(pattern_id: PatternType) -> Pattern:
    """Get a specific pattern by ID."""
    patterns = {p.id: p for p in get_all_patterns()}
    return patterns[pattern_id]


# Pattern 1: Personal Sanctuary Pattern
PERSONAL_SANCTUARY = Pattern(
    id=PatternType.PERSONAL_SANCTUARY,
    name="Personal Sanctuary Pattern",
    surface_request="Home improvement, office redesign, space optimization",
    real_problem="Creating retreat/escape space, not optimizing productivity",
    signals=[
        Signal("Emotional language: 'inspiring,' 'proud,' 'excited' (not functional benefits)", weight=1.0),
        Signal("Multi-use space mentioned: work + games + personal storage", weight=0.9),
        Signal("'Mine' ownership language: 'my space,' 'where I can...'", weight=0.8),
        Signal("Renovation appetite: Willing to invest time/money in transformation", weight=0.7),
    ],
    questions=[
        Question("How will you actually use this space beyond work?", "Reveal true purpose", priority=1),
        Question("What activities make you feel most yourself?", "Uncover personal dimension", priority=1),
        Question("Who else uses or accesses this space?", "Understand constraints", priority=2),
        Question("What's your appetite for renovation vs. refresh?", "Gauge commitment level", priority=2),
    ],
    pitfalls=[
        Pitfall("Treating as pure work optimization (ergonomic chair, standing desk)", 
                "Miss the emotional/personal dimension"),
        Pitfall("Missing the emotional/personal dimension", 
                "Recommend functional improvements when transformation desired"),
        Pitfall("Recommending minimal changes when transformation desired", 
                "User feels unheard, solution doesn't match intent"),
    ],
    example_scenario="Test #2 - Office Redesign",
    test_link="../testing/test-scenarios.md#test-2-office-redesign",
)


# Pattern 2: Employability Anxiety Pattern
EMPLOYABILITY_ANXIETY = Pattern(
    id=PatternType.EMPLOYABILITY_ANXIETY,
    name="Employability Anxiety Pattern",
    surface_request="Side business, passive income, skill development, 'additional revenue'",
    real_problem="Hedging against career uncertainty, not entrepreneurship",
    signals=[
        Signal("Age concerns: 'I'm 45,' 'been doing this 20 years'", weight=1.0),
        Signal("AI/disruption fears: Mentions automation, AI replacing jobs", weight=1.0),
        Signal("Job security language: 'market is tough,' 'just in case'", weight=0.9),
        Signal("High-effort option framed as 'additional' (doesn't match)", weight=0.8),
        Signal("Innovation/cutting-edge team member feeling vulnerable", weight=0.7),
    ],
    questions=[
        Question("What triggered you thinking about this RIGHT NOW?", "Identify anxiety trigger", priority=1),
        Question("How secure does your current job feel? (1-10)", "Quantify security perception", priority=1),
        Question("If money weren't a concern, would you still want to do this?", "Separate money from motivation", priority=1),
        Question("What's your capital situation?", "Reveal better hedging strategies", priority=2),
    ],
    pitfalls=[
        Pitfall("Taking 'side business' request at face value",
                "Recommend entrepreneurship when real need is career insurance"),
        Pitfall("Missing that 'additional revenue' framing contradicts high effort required",
                "Validate effort mismatch without questioning"),
        Pitfall("Not exploring less-effort hedging options (savings, passive investments)",
                "Recommend high-effort solution when low-effort hedge better"),
    ],
    example_scenario="Test #3 - Passive Income",
    test_link="../testing/test-scenarios.md#test-3-passive-income",
)


# Pattern 3: Health Anxiety Pattern
HEALTH_ANXIETY = Pattern(
    id=PatternType.HEALTH_ANXIETY,
    name="Health Anxiety Pattern",
    surface_request="Prevention, screening, lifestyle optimization, 'catch it early'",
    real_problem="Control over health outcomes, avoiding being blindsided (not generic prevention)",
    signals=[
        Signal("Recent diagnosis in social circle: Friend, family member, colleague", weight=1.0),
        Signal("Family history mentioned: Multiple relatives with same condition", weight=1.0),
        Signal("Urgency language: 'I feel like I should,' 'I need to do something'", weight=0.9),
        Signal("'Catch it early' framing: Focus on detection over actual risk reduction", weight=0.8),
        Signal("Trigger timing: Right after someone else's diagnosis", weight=1.0),
    ],
    questions=[
        Question("What happened that's making you think about this RIGHT NOW?", "Identify anxiety trigger", priority=1),
        Question("What types of cancer/conditions run in your family?", "Understand hereditary patterns", priority=1),
        Question("At what ages were family members diagnosed?", "Assess risk timing", priority=1),
        Question("What's your ethnicity?", "Affects genetic testing recommendations", priority=2),
        Question("What screening are you currently doing?", "Understand baseline", priority=2),
    ],
    pitfalls=[
        Pitfall("Generic 'eat healthy, exercise' advice",
                "Miss the anxiety trigger and specific risk profile"),
        Pitfall("Missing the anxiety trigger (recent diagnosis)",
                "Provide general advice when specific reassurance needed"),
        Pitfall("Not recognizing hereditary patterns that change risk profile",
                "Recommend standard screening when genetic counseling indicated"),
        Pitfall("Treating all prevention the same (hereditary vs. lifestyle vs. random)",
                "One-size-fits-all approach misses risk stratification"),
    ],
    example_scenario="Test #4 - Cancer Prevention",
    test_link="../testing/test-scenarios.md#test-4-cancer-prevention",
)


# Pattern 4: "Additional Revenue" Misframing Pattern
ADDITIONAL_REVENUE_MISFRAME = Pattern(
    id=PatternType.ADDITIONAL_REVENUE_MISFRAME,
    name="'Additional Revenue' Misframing Pattern",
    surface_request="Starting business, side hustle, passive income",
    real_problem="Either security hedge OR wrong solution entirely",
    signals=[
        Signal("High-effort option (franchise, business) framed as 'additional' revenue", weight=1.0),
        Signal("Mismatch between effort and 'additional' language", weight=1.0),
        Signal("Core revenue already exists and stable", weight=0.8),
        Signal("No clear entrepreneurial passion mentioned", weight=0.7),
        Signal("Defensive/hedging language: 'just in case,' 'to be safe'", weight=0.9),
    ],
    questions=[
        Question("Why do you need additional revenue?", "Reveal security fears", priority=1),
        Question("How much time/effort are you willing to invest?", "Check effort alignment", priority=1),
        Question("What's your current financial situation? (capital, savings, runway)", "Assess resources", priority=1),
        Question("If you had $X already, would you still want to do this?", "Separate need from want", priority=2),
    ],
    pitfalls=[
        Pitfall("Not catching the effort/framing mismatch",
                "Accept high-effort 'additional' revenue at face value"),
        Pitfall("Assuming entrepreneurial motivation when it's security seeking",
                "Recommend business when investment better fits need"),
        Pitfall("Recommending business when passive investment better fits need",
                "High-effort solution when low-effort hedge available"),
        Pitfall("Missing capital availability that changes recommendation entirely",
                "Overlook that they have resources for better hedging"),
    ],
    example_scenario="Test #3 - Passive Income",
    test_link="../testing/test-scenarios.md#test-3-passive-income",
)


# Pattern 5: Popularity Contest Hiding Identity Crisis
POPULARITY_CONTEST = Pattern(
    id=PatternType.POPULARITY_CONTEST,
    name="Popularity Contest Hiding Identity Crisis",
    surface_request="Feature prioritization decision (customer count-based)",
    real_problem="Product identity crisis - must choose who you're building for",
    signals=[
        Signal("Framed as COUNT vs VALUE: '10 customers want X, 2 want Y'", weight=1.0),
        Signal("Features serve opposite stakeholders: Employers vs. employees, users vs. admins", weight=1.0),
        Signal("One feature described as 'controversial' or 'politically loaded'", weight=0.9),
        Signal("Product positioning contradiction: 'Employees first' but feature serves employers", weight=1.0),
        Signal("'Nice-to-have' from many vs. 'make-or-break' from few", weight=0.8),
    ],
    questions=[
        Question("What's your product positioning? Who do you claim to serve?", "Check stated values", priority=1),
        Question("Who actually requested the popular feature? (Top-down or bottom-up?)", "Understand request origin", priority=1),
        Question("What's the political/cultural context? Why is it controversial?", "Reveal values conflict", priority=1),
        Question("Does this feature align with your stated values?", "Force values check", priority=1),
        Question("What happens if you DON'T build the popular feature?", "Test actual consequences", priority=2),
    ],
    pitfalls=[
        Pitfall("Optimizing for customer count instead of values alignment",
                "Recommend popular feature that violates core values"),
        Pitfall("Treating feature prioritization as pure ROI calculation",
                "Miss that features lock you into positioning"),
        Pitfall("Missing that 'nice-to-have' from many < 'make-or-break' from few",
                "Optimize for volume over retention/values"),
        Pitfall("Not recognizing when features lock you into positioning",
                "Build features that define you in ways you don't want"),
        Pitfall("Assuming more customers = better decision",
                "Popularity contest ignores strategic positioning"),
    ],
    example_scenario="Test #5 - Feature Decision",
    test_link="../testing/test-scenarios.md#test-5-feature-decision",
)


# Pattern 6: Scarcity Mindset Hiding Opportunity
SCARCITY_MINDSET = Pattern(
    id=PatternType.SCARCITY_MINDSET,
    name="Scarcity Mindset Hiding Opportunity",
    surface_request="'Stable money vs risky thing' decision",
    real_problem="Fear preventing commitment to opportunity despite having resources and validation",
    signals=[
        Signal("Fear-based language: 'market is tough,' 'I'm thankful,' 'playing it safe'", weight=1.0),
        Signal("Strong fundamentals contradicting scarcity narrative: Growth, savings, runway", weight=1.0),
        Signal("Underpriced 'stable' option: Below-market rates framed as opportunity", weight=0.9),
        Signal("Inflection point timing: Growth momentum that would be lost if paused", weight=0.9),
        Signal("Framing choice as 'safety vs risk' when math shows risk is minimal", weight=1.0),
    ],
    questions=[
        Question("What's your actual financial runway?", "Reveal false scarcity", priority=1),
        Question("What are the fundamentals of what you're 'risking'?", "Reveal strength", priority=1),
        Question("What's the hourly rate of the 'stable' option?", "Reveal if underpriced", priority=1),
        Question("What happens if you pause momentum?", "Reveal opportunity cost", priority=1),
    ],
    pitfalls=[
        Pitfall("Accepting 'market is tough' without challenging with user's own metrics",
                "Validate fear-based narrative despite strong fundamentals"),
        Pitfall("Validating fear-based decision when fundamentals are strong",
                "Recommend 'safe' option that's actually opportunity cost"),
        Pitfall("Treating 'stable money' as inherently better than 'risky growth'",
                "Miss that 'stable' can be distraction from inflection point"),
        Pitfall("Missing that low-rate work can be distraction from inflection point",
                "Undervalue opportunity cost of momentum loss"),
        Pitfall("Not recognizing scarcity mindset despite substantial runway",
                "Accept fear narrative without checking bank account"),
    ],
    example_scenario="Test #7 - Client vs Product",
    test_link="../testing/test-scenarios.md#test-7-client-vs-product",
)


# Pattern 7: Solution Looking for Problem
SOLUTION_LOOKING_FOR_PROBLEM = Pattern(
    id=PatternType.SOLUTION_LOOKING_FOR_PROBLEM,
    name="Solution Looking for Problem",
    surface_request="Build a product/app/feature",
    real_problem="Wants to build something, picked an idea that sounds good, hasn't validated it's worth months of work",
    signals=[
        Signal("'I had an idea... thought it would be cool/useful'", weight=1.0),
        Signal("No research done upfront", weight=0.9),
        Signal("Lists features before identifying who/why", weight=0.9),
        Signal("Can't articulate core pain point when asked directly", weight=1.0),
        Signal("First-time builder with limited time", weight=0.8),
        Signal("Excitement-driven, not problem-driven", weight=0.9),
        Signal("Jumps to comprehensive feature list immediately", weight=0.8),
    ],
    questions=[
        Question("What triggered this idea RIGHT NOW?", "Reveal spontaneous vs researched", priority=1),
        Question("What's your track record with side projects?", "Reveal if serial starter or first-timer", priority=1),
        Question("How much time can you realistically commit?", "Reveal if timeline is feasible", priority=1),
        Question("Have you validated this with potential users?", "Reveal depth of validation", priority=1),
        Question("What's the ONE problem you're solving?", "Reveal if they know core pain point", priority=1),
    ],
    pitfalls=[
        Pitfall("Taking feature list at face value (they described WHAT, not WHY)",
                "Build features without validating problem worth solving"),
        Pitfall("Not challenging lack of validation",
                "Recommend 'just build it' when demand unvalidated"),
        Pitfall("Missing that first-time builders underestimate shipping time by 3-5x",
                "Accept timeline that's too aggressive"),
        Pitfall("Assuming excitement = validation",
                "Enthusiasm about solution doesn't prove problem exists"),
        Pitfall("Not asking about core pain point explicitly",
                "Miss that they can't articulate the 'why'"),
    ],
    example_scenario="Test #8 - Meal Planning App",
    test_link="../testing/test-scenarios.md#test-8-meal-planning-app",
)


# Pattern 8: Premature Presentation
PREMATURE_PRESENTATION = Pattern(
    id=PatternType.PREMATURE_PRESENTATION,
    name="Premature Presentation (Presenting Without Proof)",
    surface_request="Help me prepare a presentation for leadership/stakeholders",
    real_problem="Presenting too early out of excitement, not readiness. Will burn credibility on 'we might have something' when they could wait and present 'we DO have something.'",
    signals=[
        Signal("Excited about vision/project", weight=0.7),
        Signal("No measurable results yet to back up the ask", weight=1.0),
        Signal("Unclear what they're asking for ('just a check-in', 'not sure')", weight=1.0),
        Signal("Skeptics already exist in the audience", weight=0.9),
        Signal("Top-level support but middle management doubt", weight=0.8),
        Signal("Wants adoption/behavior change without proof", weight=0.9),
        Signal("Timing driven by excitement, not strategy", weight=1.0),
    ],
    questions=[
        Question("What does the audience currently know?", "Reveal awareness vs skepticism", priority=1),
        Question("What specific decision are you asking them to make?", "Reveal if ask is clear", priority=1),
        Question("What's the current adoption/results status?", "Reveal if they have proof", priority=1),
        Question("What happens if they say 'prove it first'?", "Reveal if timeline is flexible", priority=2),
        Question("What's driving the timing - why now vs later?", "Reveal if it's excitement vs necessity", priority=1),
        Question("Are you under threat that requires immediate action?", "Reveal true urgency", priority=2),
    ],
    pitfalls=[
        Pitfall("Taking 'prepare presentation' request at face value",
                "Help them present when they shouldn't present at all"),
        Pitfall("Not challenging whether they should present at all",
                "Polish presentation that will burn credibility"),
        Pitfall("Missing the credibility gap (big ask, no proof)",
                "Ignore that 'just a check-in' with big ask = credibility loss"),
        Pitfall("Not questioning unclear ask ('not sure what I want')",
                "Present without clear decision request = wasted opportunity"),
        Pitfall("Assuming excitement = readiness to present",
                "Enthusiasm about potential doesn't mean ready for stakeholders"),
        Pitfall("Not asking about strategic timing",
                "Miss that waiting 3-6 months for proof would be better"),
    ],
    example_scenario="Test #6 - Workplace Politics",
    test_link="../testing/test-scenarios.md#test-6-workplace-politics",
)


# Pattern 9: Stuck in Build Phase
STUCK_IN_BUILD_PHASE = Pattern(
    id=PatternType.STUCK_IN_BUILD_PHASE,
    name="Stuck in Build Phase (No-Code/LLM Builders)",
    surface_request="Help me finish/accelerate my product build",
    real_problem="Scope management, not technical limitations. Building 179 things when they need 1 working demo. Wrong prompt strategy for LLM (asking for 'features' instead of 'demo').",
    signals=[
        Signal("Ambitious roadmap (many epics, 100+ user stories)", weight=0.9),
        Signal("Cannot get ONE flow to reviewable/demo state", weight=1.0),
        Signal("Mentions 'LLM limitations' or tools as blocker", weight=0.8),
        Signal("Has infrastructure but no end-to-end demo", weight=1.0),
        Signal("Non-technical (no-code, uses AI to 'vibe code')", weight=0.7),
        Signal("Focuses on features/stories, not working product", weight=0.9),
        Signal("Stuck in build phase, can't reach review phase", weight=1.0),
        Signal("Needs to 'fail fast' but building comprehensive solution", weight=0.9),
    ],
    questions=[
        Question("Do you have something reviewable right now (demo, video, screenshot, prototype) or is it all in-progress?", 
                 "Reveal if stuck in build phase", priority=1),
        Question("Show me the docs that need scrubbing", "Reveal scope - often 100+ stories", priority=1),
        Question("Walk me through your typical workflow when you build with AI. Where does it usually break down?", 
                 "Reveal LLM is building infrastructure, not demos", priority=1),
        Question("What does 'complete' look like for ONE feature?", "Reveal definition is too comprehensive", priority=2),
        Question("What currently EXISTS vs what's BROKEN?", "Reveal if problem is scope vs bugs", priority=2),
    ],
    pitfalls=[
        Pitfall("Taking 'LLM limitations' at face value (it's usually scope, not AI capability)",
                "Focus on better prompts when real issue is ruthless scope cut"),
        Pitfall("Recommending better prompts when real issue is ruthless scope cut",
                "Technical solution to strategy problem"),
        Pitfall("Not probing for reviewable artifacts early",
                "Miss that they have zero demos after months of work"),
        Pitfall("Treating as technical problem when it's product strategy problem",
                "Debug infrastructure when they need scope validation"),
        Pitfall("Missing that no-code users need demo-first, not architecture-first approach",
                "Architecture patterns don't work for non-technical builders"),
        Pitfall("Not recognizing that LLMs are GREAT at demos, TERRIBLE at comprehensive systems",
                "Play to LLM weaknesses instead of strengths"),
    ],
    example_scenario="Test #9 - Ken's Workspaces",
    test_link="../testing/test-scenarios.md#test-9-kens-workspaces",
    metadata={
        "what_they_need": [
            "Scope reality check - 'You're building 179 things when you need 1 thing'",
            "Concrete 'done' definition - 'Demo-ready = 2-min screencast', not 'production-ready'",
            "Permission to fake it - 'Hardcode everything not in hero flow'",
            "Executable artifact - Not just advice, but DEMO_V1.md they can hand to LLM",
            "Co-creation support - Help them create the scoped spec together",
        ],
        "llm_builder_insights": [
            "Users who don't code rely on LLM for everything",
            "LLMs are GREAT at: copying patterns, hardcoding demos, vertical slices",
            "LLMs are TERRIBLE at: architecture, anticipating edge cases, knowing 'done'",
            "Users ask for 'features' → LLM builds infrastructure → never reaches reviewable state",
            "Users need to ask for 'demo' → LLM builds visible UI → can actually review",
        ]
    }
)
