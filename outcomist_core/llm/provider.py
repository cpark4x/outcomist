"""LLM provider abstraction for Outcomist.

This module provides a unified interface for different LLM providers,
allowing the discovery flow to work with Claude, GPT-4, or local models.
"""

from typing import Protocol, Optional, AsyncIterator
from .types import LLMRequest, LLMResponse, LLMMessage


class BaseLLMProvider(Protocol):
    """Protocol for LLM providers.
    
    All LLM providers must implement this interface.
    """
    
    def complete(self, request: LLMRequest) -> LLMResponse:
        """Get a completion from the LLM.
        
        Args:
            request: LLMRequest with system prompt, messages, and settings
        
        Returns:
            LLMResponse with the completion
        """
        ...
    
    async def complete_async(self, request: LLMRequest) -> LLMResponse:
        """Get a completion asynchronously.
        
        Args:
            request: LLMRequest with system prompt, messages, and settings
        
        Returns:
            LLMResponse with the completion
        """
        ...
    
    async def stream(self, request: LLMRequest) -> AsyncIterator[str]:
        """Stream a completion from the LLM.
        
        Args:
            request: LLMRequest with system prompt, messages, and settings
        
        Yields:
            Chunks of the completion as they arrive
        """
        ...


class MockLLMProvider:
    """Mock LLM provider for testing without API calls.
    
    Returns canned responses for testing purposes.
    """
    
    def __init__(self, canned_responses: Optional[dict] = None):
        """Initialize mock provider.
        
        Args:
            canned_responses: Dict mapping system prompt keywords to responses
        """
        self.canned_responses = canned_responses or {}
        self.call_count = 0
    
    def complete(self, request: LLMRequest) -> LLMResponse:
        """Return a mock completion."""
        self.call_count += 1
        
        # Check for canned responses based on system prompt content
        for keyword, response in self.canned_responses.items():
            if keyword.lower() in request.system.lower():
                return LLMResponse(
                    content=response,
                    model="mock-model",
                    tokens_used=len(response.split())
                )
        
        # Default mock responses based on request type
        if "pattern recognition" in request.system.lower():
            return LLMResponse(
                content="You're framing this as [X], but the real question is [Y].",
                model="mock-model",
                tokens_used=15
            )
        elif "round 1" in request.system.lower():
            return LLMResponse(
                content="What's your current situation?",
                model="mock-model",
                tokens_used=5
            )
        elif "round 2" in request.system.lower():
            return LLMResponse(
                content="What matters most to you in this decision?",
                model="mock-model",
                tokens_used=8
            )
        elif "summary" in request.system.lower():
            return LLMResponse(
                content="Let me summarize:\n• Point 1\n• Point 2\n• Point 3\n\nDoes that capture it?",
                model="mock-model",
                tokens_used=15
            )
        elif "recommendation" in request.system.lower():
            return LLMResponse(
                content="Based on what you've shared, I recommend [X] because [reasoning].",
                model="mock-model",
                tokens_used=12
            )
        
        return LLMResponse(
            content="Mock response",
            model="mock-model",
            tokens_used=2
        )
    
    async def complete_async(self, request: LLMRequest) -> LLMResponse:
        """Return a mock completion asynchronously."""
        return self.complete(request)
    
    async def stream(self, request: LLMRequest) -> AsyncIterator[str]:
        """Stream a mock completion."""
        response = self.complete(request)
        for word in response.content.split():
            yield word + " "
