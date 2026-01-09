"""Pattern matching engine for Outcomist.

This module implements pattern detection using a hybrid approach:
1. Heuristic/keyword matching for fast, obvious pattern detection
2. LLM-based analysis for ambiguous or complex cases (optional)

The matcher analyzes user's decision text and returns matching patterns
with confidence scores.
"""

from typing import List, Optional, Dict, Set
import re
from dataclasses import dataclass

from .types import Pattern, PatternMatch, Signal, PatternType
from .library import get_all_patterns
from ..context.types import DecisionContext


@dataclass
class SignalMatch:
    """A signal that was detected in the text."""
    signal: Signal
    matched_keywords: List[str]
    confidence: float


class PatternMatcher:
    """Detects decision patterns from user input using heuristic matching.
    
    This is a Phase 2 implementation using keyword/phrase matching.
    Can be enhanced with LLM-based detection later.
    """
    
    def __init__(self):
        """Initialize the pattern matcher."""
        self.patterns = get_all_patterns()
        self._signal_keywords = self._build_signal_keywords()
    
    def _build_signal_keywords(self) -> Dict[PatternType, Dict[str, List[str]]]:
        """Build keyword index for each pattern's signals.
        
        Returns a nested dict: {pattern_id: {signal_desc: [keywords]}}
        """
        index = {}
        for pattern in self.patterns:
            signal_keywords = {}
            for signal in pattern.signals:
                keywords = self._extract_keywords(signal.description)
                signal_keywords[signal.description] = keywords
            index[pattern.id] = signal_keywords
        return index
    
    def _extract_keywords(self, signal_text: str) -> List[str]:
        """Extract matching keywords from a signal description.
        
        This is an improved implementation that:
        - Extracts quoted strings
        - Adds semantic variations
        - Handles specific pattern-based keywords
        """
        keywords = []
        
        # Extract quoted strings (e.g., 'inspiring,' 'proud,' 'excited')
        quoted = re.findall(r"['\"]([^'\"]+)['\"]", signal_text)
        keywords.extend(quoted)
        
        # Clean up quoted strings (remove punctuation for matching)
        for q in quoted:
            cleaned = q.rstrip('.,;:!?')
            if cleaned != q:
                keywords.append(cleaned)
        
        # PERSONAL SANCTUARY PATTERN keywords
        if "Emotional language" in signal_text:
            keywords.extend(["inspiring", "proud", "excited", "inspiration", 
                           "inspire", "pride", "excitement", "excited about"])
        
        if "Multi-use space" in signal_text:
            keywords.extend(["work", "games", "gaming", "personal storage", 
                           "multiple uses", "workspace", "play", "hobbies"])
        
        if "'Mine' ownership language" in signal_text:
            keywords.extend(["my space", "my office", "my room", "my own",
                           "where I can", "mine", "belongs to me"])
        
        if "Renovation appetite" in signal_text:
            keywords.extend(["redesign", "renovation", "transform", "remodel",
                           "makeover", "willing to invest", "ready to spend"])
        
        # EMPLOYABILITY ANXIETY keywords
        if "Age concerns:" in signal_text or "been doing this" in signal_text:
            keywords.extend(["I'm", "years", "age", "old", "been doing", 
                           "been working", "career", "45", "years old"])
        
        if "AI/disruption fears" in signal_text:
            keywords.extend(["AI", "automation", "replacing", "disruption",
                           "automated", "technology", "replaced by"])
        
        if "security language" in signal_text or "Job security" in signal_text:
            keywords.extend(["secure", "tough", "just in case", "to be safe",
                           "security", "job security", "uncertain", "market is tough"])
        
        if "High-effort option" in signal_text and "additional" in signal_text:
            keywords.extend(["additional revenue", "extra income", "side income",
                           "additional money", "extra cash"])
        
        # HEALTH ANXIETY keywords
        if "Family history" in signal_text:
            keywords.extend(["family", "relatives", "mother", "father", "diagnosed",
                           "family history", "runs in family", "hereditary"])
        
        if "Recent diagnosis" in signal_text:
            keywords.extend(["friend", "colleague", "recently", "diagnosed", "stage",
                           "just diagnosed", "found out", "cancer"])
        
        if "Urgency language" in signal_text or "feel like I should" in signal_text:
            keywords.extend(["I feel like I should", "I need to", "I should",
                           "urgent", "right now", "immediately"])
        
        if "'Catch it early'" in signal_text:
            keywords.extend(["catch it early", "early detection", "preventative",
                           "prevent", "screening", "catch early"])
        
        # POPULARITY CONTEST keywords
        if "Framed as COUNT vs VALUE" in signal_text:
            keywords.extend(["customers want", "vs", "vs.", "customers",
                           "10 customers", "2 customers", "many customers", "few customers"])
        
        if "Features serve opposite stakeholders" in signal_text:
            keywords.extend(["employers", "employees", "workplace", "surveillance",
                           "stakeholders", "different audiences", "contradicts"])
        
        if "controversial" in signal_text or "politically loaded" in signal_text:
            keywords.extend(["controversial", "politically", "loaded", "sensitive",
                           "political", "contentious"])
        
        if "positioning contradiction" in signal_text.lower():
            keywords.extend(["positioning", "employees first", "contradict",
                           "mission", "values", "claim to serve"])
        
        # SCARCITY MINDSET keywords
        if "Fear-based language" in signal_text:
            keywords.extend(["tough", "thankful", "playing it safe", "scary",
                           "market is tough", "grateful", "safe option", "risky"])
        
        if "Strong fundamentals contradicting" in signal_text:
            keywords.extend(["growth", "revenue", "MRR", "savings", "runway",
                           "growing", "traction", "users", "retention"])
        
        if "Underpriced" in signal_text:
            keywords.extend(["$/hour", "rate", "underpriced", "below market",
                           "/hour", "hourly rate", "cheap", "low rate"])
        
        if "Inflection point" in signal_text or "momentum" in signal_text:
            keywords.extend(["momentum", "inflection point", "growth momentum",
                           "traction", "scaling", "growing fast"])
        
        # SOLUTION LOOKING FOR PROBLEM keywords
        if "'I had an idea" in signal_text:
            keywords.extend(["had an idea", "thought it would", "cool", "useful",
                           "I thought", "came up with", "sounds good"])
        
        if "No research done" in signal_text:
            keywords.extend(["no research", "haven't validated", "haven't asked",
                           "haven't checked", "no validation", "didn't research"])
        
        if "Lists features before" in signal_text:
            keywords.extend(["features", "feature list", "all the features",
                           "functionality", "capabilities"])
        
        if "Can't articulate core pain point" in signal_text:
            keywords.extend(["comprehensive", "all the features", "feature list",
                           "many features", "lots of functionality"])
        
        if "First-time builder" in signal_text or "limited time" in signal_text:
            keywords.extend(["first time", "never built", "limited time",
                           "side project", "nights and weekends"])
        
        # PREMATURE PRESENTATION keywords
        if "No measurable results yet" in signal_text:
            keywords.extend(["no results", "just started", "handful of users", "not sure",
                           "few users", "early stage", "no metrics", "no data"])
        
        if "Unclear what they're asking for" in signal_text:
            keywords.extend(["not sure", "check-in", "unclear", "don't know what",
                           "maybe", "I think", "possibly", "not sure what"])
        
        if "Skeptics already exist" in signal_text:
            keywords.extend(["skeptics", "doubters", "pushback", "resistance",
                           "not convinced", "doubt"])
        
        if "Wants adoption" in signal_text and "without proof" in signal_text:
            keywords.extend(["adoption", "behavior change", "buy-in", "support",
                           "get people to use", "convince"])
        
        # STUCK IN BUILD PHASE keywords
        if "Cannot get ONE flow" in signal_text:
            keywords.extend(["can't finish", "stuck", "not working", "broken",
                           "can't get", "unable to", "can't complete",
                           "nothing works", "can't ship", "can't demo"])
        
        if "Ambitious roadmap" in signal_text:
            keywords.extend(["epics", "stories", "roadmap", "comprehensive",
                           "user stories", "many features", "big roadmap",
                           "100+ stories", "179 stories", "lots of work"])
        
        if "'LLM limitations'" in signal_text:
            keywords.extend(["LLM", "AI limitations", "Claude", "ChatGPT", "can't build",
                           "AI can't", "tool limitations", "AI limitations"])
        
        if "Has infrastructure but no end-to-end" in signal_text:
            keywords.extend(["infrastructure", "no demo", "end-to-end", "nothing to show",
                           "backend only", "no UI", "not working end-to-end"])
        
        if "Non-technical" in signal_text or "no-code" in signal_text:
            keywords.extend(["no-code", "non-technical", "can't code", "vibe code",
                           "using AI to code", "AI to build"])
        
        if "Focuses on features" in signal_text:
            keywords.extend(["features", "stories", "feature list", "functionality",
                           "building features", "feature by feature"])
        
        if "Stuck in build phase" in signal_text:
            keywords.extend(["stuck", "can't finish", "build phase", "not shipping",
                           "can't complete", "can't get done"])
        
        if "reviewable" in signal_text or "demo state" in signal_text:
            keywords.extend(["reviewable", "demo", "show", "demonstrate",
                           "working demo", "prototype", "something to show"])
        
        return keywords
    
    def _count_signal_matches(
        self, 
        text: str, 
        pattern: Pattern
    ) -> List[SignalMatch]:
        """Count how many signals match in the text."""
        text_lower = text.lower()
        signal_matches = []
        
        for signal in pattern.signals:
            keywords = self._signal_keywords[pattern.id][signal.description]
            matched_keywords = []
            
            for keyword in keywords:
                keyword_lower = keyword.lower()
                if keyword_lower in text_lower:
                    matched_keywords.append(keyword)
            
            if matched_keywords:
                # Confidence based on how many keywords matched
                confidence = min(1.0, len(matched_keywords) / max(1, len(keywords)))
                signal_matches.append(SignalMatch(
                    signal=signal,
                    matched_keywords=matched_keywords,
                    confidence=confidence
                ))
        
        return signal_matches
    
    def _calculate_pattern_confidence(
        self,
        signal_matches: List[SignalMatch],
        pattern: Pattern
    ) -> float:
        """Calculate overall confidence for a pattern match.
        
        Uses weighted average of signal matches and signal weights,
        with improved boosting for multiple strong signals.
        """
        if not signal_matches:
            return 0.0
        
        # Weight each signal match by the signal's weight
        weighted_sum = sum(
            match.confidence * match.signal.weight 
            for match in signal_matches
        )
        
        # Normalize by total possible weight
        total_weight = sum(signal.weight for signal in pattern.signals)
        
        if total_weight == 0:
            return 0.0
        
        base_confidence = weighted_sum / total_weight
        
        # Calculate match ratio
        match_ratio = len(signal_matches) / len(pattern.signals)
        
        # IMPROVED: Multi-signal boost with progressive scaling
        # - 2 signals: +20%
        # - 3 signals: +40%
        # - 4+ signals: +60%
        if len(signal_matches) >= 4:
            multi_signal_boost = 1.6
        elif len(signal_matches) == 3:
            multi_signal_boost = 1.4
        elif len(signal_matches) == 2:
            multi_signal_boost = 1.2
        else:
            multi_signal_boost = 1.0
        
        # IMPROVED: Strong signal boost
        # If any signal has confidence > 0.5, boost by 15%
        strong_signal_boost = 1.0
        if any(match.confidence > 0.5 for match in signal_matches):
            strong_signal_boost = 1.15
        
        # IMPROVED: Coverage boost
        # Reward patterns where matched signals cover high weight
        matched_weight = sum(match.signal.weight for match in signal_matches)
        coverage_ratio = matched_weight / total_weight
        if coverage_ratio > 0.5:
            coverage_boost = 1.0 + (coverage_ratio * 0.2)  # Up to 20% boost
        else:
            coverage_boost = 1.0
        
        # Combine all boosts
        total_boost = multi_signal_boost * strong_signal_boost * coverage_boost
        
        return min(1.0, base_confidence * total_boost)
    
    def match(
        self,
        decision_text: str,
        context: Optional[DecisionContext] = None,
        min_confidence: float = 0.15
    ) -> List[PatternMatch]:
        """Match patterns against decision text.
        
        Args:
            decision_text: User's decision statement
            context: Optional DecisionContext for richer analysis
            min_confidence: Minimum confidence threshold (0.0 to 1.0)
        
        Returns:
            List of PatternMatch objects, sorted by confidence (highest first)
        """
        matches = []
        
        for pattern in self.patterns:
            signal_matches = self._count_signal_matches(decision_text, pattern)
            
            if signal_matches:
                confidence = self._calculate_pattern_confidence(signal_matches, pattern)
                
                if confidence >= min_confidence:
                    reasoning = self._generate_reasoning(signal_matches)
                    matches.append(PatternMatch(
                        pattern=pattern,
                        confidence=confidence,
                        matched_signals=[sm.signal for sm in signal_matches],
                        reasoning=reasoning
                    ))
        
        # Sort by confidence (highest first)
        matches.sort(key=lambda m: m.confidence, reverse=True)
        
        return matches
    
    def _generate_reasoning(self, signal_matches: List[SignalMatch]) -> str:
        """Generate human-readable reasoning for the match."""
        if not signal_matches:
            return "No signals matched"
        
        reasons = []
        for sm in signal_matches[:3]:  # Top 3 signals
            keywords_str = ", ".join(f"'{kw}'" for kw in sm.matched_keywords[:3])
            reasons.append(f"{sm.signal.description[:50]}... (matched: {keywords_str})")
        
        return " | ".join(reasons)
    
    def get_top_match(
        self,
        decision_text: str,
        context: Optional[DecisionContext] = None
    ) -> Optional[PatternMatch]:
        """Get the single best pattern match.
        
        Args:
            decision_text: User's decision statement
            context: Optional DecisionContext
        
        Returns:
            PatternMatch with highest confidence, or None if no matches
        """
        matches = self.match(decision_text, context)
        return matches[0] if matches else None
    
    def get_questions_for_pattern(self, pattern_id: PatternType) -> List[str]:
        """Get recommended questions for a specific pattern.
        
        Args:
            pattern_id: The pattern ID
        
        Returns:
            List of question strings, sorted by priority
        """
        patterns = {p.id: p for p in self.patterns}
        if pattern_id not in patterns:
            return []
        
        pattern = patterns[pattern_id]
        
        # Sort questions by priority (1 = highest)
        sorted_questions = sorted(pattern.questions, key=lambda q: q.priority)
        
        return [q.text for q in sorted_questions]
