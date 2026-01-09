"""LLM provider module for Outcomist.

This module provides abstractions for working with different LLM providers.
"""

from .types import (
    LLMProvider,
    LLMMessage,
    LLMRequest,
    LLMResponse,
)

from .provider import (
    BaseLLMProvider,
    MockLLMProvider,
)

try:
    from .anthropic import AnthropicProvider
    _anthropic_available = True
except ImportError:
    _anthropic_available = False
    AnthropicProvider = None

__all__ = [
    # Types
    "LLMProvider",
    "LLMMessage",
    "LLMRequest",
    "LLMResponse",
    # Providers
    "BaseLLMProvider",
    "MockLLMProvider",
    "AnthropicProvider",
]
