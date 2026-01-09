"""Type definitions for LLM provider module."""

from dataclasses import dataclass, field
from typing import List, Dict, Any, Optional, AsyncIterator
from enum import Enum


class LLMProvider(Enum):
    """Supported LLM providers."""
    ANTHROPIC = "anthropic"
    OPENAI = "openai"
    LOCAL = "local"


@dataclass
class LLMMessage:
    """A message in the conversation."""
    role: str  # "user", "assistant", "system"
    content: str


@dataclass
class LLMRequest:
    """Request to an LLM provider."""
    system: str
    messages: List[LLMMessage]
    temperature: float = 0.7
    max_tokens: int = 2000
    model: Optional[str] = None
    metadata: Dict[str, Any] = field(default_factory=dict)


@dataclass
class LLMResponse:
    """Response from an LLM provider."""
    content: str
    model: str
    tokens_used: Optional[int] = None
    metadata: Dict[str, Any] = field(default_factory=dict)
