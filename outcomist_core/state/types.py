"""Type definitions for state management module."""

from dataclasses import dataclass, field
from typing import List, Optional, Dict, Any
from datetime import datetime
from enum import Enum


class Tier(Enum):
    """Progressive disclosure tiers."""
    TIER_1 = 1  # Pattern Recognition (30 seconds)
    TIER_2 = 2  # Discovery (5-10 minutes)
    TIER_3 = 3  # Deep Analysis (20-30 minutes)
    TIER_4 = 4  # Comprehensive (45-60+ minutes)


class Intent(Enum):
    """User's intent for the exploration."""
    VALIDATION = "validation"  # "WHETHER to do this" - seeking decision validation
    EXECUTION = "execution"    # "HOW to do this well" - seeking implementation help
    UNKNOWN = "unknown"        # Not yet determined


@dataclass
class Message:
    """A message in the conversation."""
    role: str  # "user" or "assistant"
    content: str
    timestamp: datetime = field(default_factory=datetime.now)
    metadata: Dict[str, Any] = field(default_factory=dict)


@dataclass
class SessionState:
    """State tracking for a discovery session."""
    
    # Current position in flow
    tier: Tier = Tier.TIER_1
    round: int = 0  # Which round of questioning (Tier 2 has Round 1, Round 2)
    intent: Intent = Intent.UNKNOWN
    
    # Discovery artifacts
    questions_asked: List[str] = field(default_factory=list)
    user_answers: List[str] = field(default_factory=list)
    pattern_matches: List[str] = field(default_factory=list)  # Pattern IDs
    
    # Analysis artifacts
    tier_1_insight: Optional[str] = None
    summary_text: Optional[str] = None
    recommendation: Optional[str] = None
    
    # Flow control
    summary_confirmed: bool = False
    user_accepted_recommendation: bool = False
    
    metadata: Dict[str, Any] = field(default_factory=dict)
    
    def add_question(self, question: str) -> None:
        """Add a question to the session."""
        self.questions_asked.append(question)
    
    def add_answer(self, answer: str) -> None:
        """Add a user answer to the session."""
        self.user_answers.append(answer)
    
    def advance_to_tier(self, tier: Tier) -> None:
        """Advance to a new tier."""
        self.tier = tier
        self.round = 0
    
    def advance_round(self) -> None:
        """Advance to next round within current tier."""
        self.round += 1


@dataclass
class Session:
    """A complete discovery session with state and conversation history."""
    
    session_id: str
    decision_statement: str
    user_id: Optional[str] = None
    
    state: SessionState = field(default_factory=SessionState)
    conversation: List[Message] = field(default_factory=list)
    
    created_at: datetime = field(default_factory=datetime.now)
    updated_at: datetime = field(default_factory=datetime.now)
    
    metadata: Dict[str, Any] = field(default_factory=dict)
    
    def add_message(self, role: str, content: str) -> None:
        """Add a message to the conversation."""
        msg = Message(role=role, content=content)
        self.conversation.append(msg)
        self.updated_at = datetime.now()
    
    def update_state(self, **kwargs) -> None:
        """Update session state."""
        for key, value in kwargs.items():
            if hasattr(self.state, key):
                setattr(self.state, key, value)
        self.updated_at = datetime.now()
    
    def to_dict(self) -> dict:
        """Serialize session to dictionary."""
        return {
            "session_id": self.session_id,
            "decision_statement": self.decision_statement,
            "user_id": self.user_id,
            "state": {
                "tier": self.state.tier.value,
                "round": self.state.round,
                "intent": self.state.intent.value,
                "questions_asked": self.state.questions_asked,
                "user_answers": self.state.user_answers,
                "pattern_matches": self.state.pattern_matches,
                "tier_1_insight": self.state.tier_1_insight,
                "summary_text": self.state.summary_text,
                "recommendation": self.state.recommendation,
                "summary_confirmed": self.state.summary_confirmed,
                "user_accepted_recommendation": self.state.user_accepted_recommendation,
                "metadata": self.state.metadata,
            },
            "conversation": [
                {
                    "role": msg.role,
                    "content": msg.content,
                    "timestamp": msg.timestamp.isoformat(),
                    "metadata": msg.metadata,
                }
                for msg in self.conversation
            ],
            "created_at": self.created_at.isoformat(),
            "updated_at": self.updated_at.isoformat(),
            "metadata": self.metadata,
        }
    
    @classmethod
    def from_dict(cls, data: dict) -> "Session":
        """Deserialize session from dictionary."""
        state = SessionState(
            tier=Tier(data["state"]["tier"]),
            round=data["state"]["round"],
            intent=Intent(data["state"]["intent"]),
            questions_asked=data["state"]["questions_asked"],
            user_answers=data["state"]["user_answers"],
            pattern_matches=data["state"]["pattern_matches"],
            tier_1_insight=data["state"].get("tier_1_insight"),
            summary_text=data["state"].get("summary_text"),
            recommendation=data["state"].get("recommendation"),
            summary_confirmed=data["state"].get("summary_confirmed", False),
            user_accepted_recommendation=data["state"].get("user_accepted_recommendation", False),
            metadata=data["state"].get("metadata", {}),
        )
        
        conversation = [
            Message(
                role=msg["role"],
                content=msg["content"],
                timestamp=datetime.fromisoformat(msg["timestamp"]),
                metadata=msg.get("metadata", {}),
            )
            for msg in data["conversation"]
        ]
        
        return cls(
            session_id=data["session_id"],
            decision_statement=data["decision_statement"],
            user_id=data.get("user_id"),
            state=state,
            conversation=conversation,
            created_at=datetime.fromisoformat(data["created_at"]),
            updated_at=datetime.fromisoformat(data["updated_at"]),
            metadata=data.get("metadata", {}),
        )
