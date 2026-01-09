"""Anthropic (Claude) LLM provider implementation."""

from typing import Optional, AsyncIterator
import os

from .types import LLMRequest, LLMResponse, LLMMessage


class AnthropicProvider:
    """LLM provider for Anthropic's Claude models."""
    
    def __init__(
        self,
        api_key: Optional[str] = None,
        model: str = "claude-3-5-haiku-20241022",
        default_max_tokens: int = 2000
    ):
        """Initialize Anthropic provider.
        
        Args:
            api_key: Anthropic API key (or set ANTHROPIC_API_KEY env var)
            model: Default model to use
            default_max_tokens: Default max tokens for completions
        """
        self.api_key = api_key or os.getenv("ANTHROPIC_API_KEY")
        if not self.api_key:
            raise ValueError(
                "Anthropic API key required. Set ANTHROPIC_API_KEY env var "
                "or pass api_key parameter."
            )
        
        self.model = model
        self.default_max_tokens = default_max_tokens
        
        # Import anthropic library (optional dependency)
        try:
            import anthropic
            self.client = anthropic.Anthropic(api_key=self.api_key)
        except ImportError:
            raise ImportError(
                "anthropic library not installed. "
                "Install with: pip install anthropic"
            )
    
    def complete(self, request: LLMRequest) -> LLMResponse:
        """Get a completion from Claude.
        
        Args:
            request: LLMRequest with system prompt, messages, and settings
        
        Returns:
            LLMResponse with the completion
        """
        # Convert messages to Anthropic format
        messages = []
        for msg in request.messages:
            messages.append({
                "role": msg.role,
                "content": msg.content
            })
        
        # Call Anthropic API
        response = self.client.messages.create(
            model=request.model or self.model,
            system=request.system,
            messages=messages,
            max_tokens=request.max_tokens or self.default_max_tokens,
            temperature=request.temperature,
        )
        
        # Extract response content
        content = response.content[0].text if response.content else ""
        
        return LLMResponse(
            content=content,
            model=response.model,
            tokens_used=response.usage.input_tokens + response.usage.output_tokens,
            metadata={
                "input_tokens": response.usage.input_tokens,
                "output_tokens": response.usage.output_tokens,
                "stop_reason": response.stop_reason,
            }
        )
    
    async def complete_async(self, request: LLMRequest) -> LLMResponse:
        """Get a completion asynchronously.
        
        Args:
            request: LLMRequest with system prompt, messages, and settings
        
        Returns:
            LLMResponse with the completion
        """
        # Convert messages to Anthropic format
        messages = []
        for msg in request.messages:
            messages.append({
                "role": msg.role,
                "content": msg.content
            })
        
        # Call Anthropic API asynchronously
        response = await self.client.messages.create(
            model=request.model or self.model,
            system=request.system,
            messages=messages,
            max_tokens=request.max_tokens or self.default_max_tokens,
            temperature=request.temperature,
        )
        
        # Extract response content
        content = response.content[0].text if response.content else ""
        
        return LLMResponse(
            content=content,
            model=response.model,
            tokens_used=response.usage.input_tokens + response.usage.output_tokens,
            metadata={
                "input_tokens": response.usage.input_tokens,
                "output_tokens": response.usage.output_tokens,
                "stop_reason": response.stop_reason,
            }
        )
    
    async def stream(self, request: LLMRequest) -> AsyncIterator[str]:
        """Stream a completion from Claude.
        
        Args:
            request: LLMRequest with system prompt, messages, and settings
        
        Yields:
            Chunks of the completion as they arrive
        """
        # Convert messages to Anthropic format
        messages = []
        for msg in request.messages:
            messages.append({
                "role": msg.role,
                "content": msg.content
            })
        
        # Stream from Anthropic API
        async with self.client.messages.stream(
            model=request.model or self.model,
            system=request.system,
            messages=messages,
            max_tokens=request.max_tokens or self.default_max_tokens,
            temperature=request.temperature,
        ) as stream:
            async for text in stream.text_stream:
                yield text
