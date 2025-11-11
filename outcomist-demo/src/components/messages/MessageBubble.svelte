<script lang="ts">
  import { marked } from 'marked';
  import StreamingIndicator from './StreamingIndicator.svelte';

  export let role: 'user' | 'assistant';
  export let content: string;
  export let isStreaming: boolean = false;

  // Configure marked to be synchronous and return HTML string
  let htmlContent = '';
  $: {
    if (role === 'assistant') {
      // marked.parse() is the synchronous method in v17
      htmlContent = marked.parse(content, { async: false }) as string;
    }
  }
</script>

<!-- Option C: Precise Elegance - Cool grays, compact, sophisticated -->
<div
  class="message"
  style="
    display: flex;
    justify-content: {role === 'user' ? 'flex-end' : 'flex-start'};
    margin-bottom: 20px;
    animation: slideIn 200ms ease-out;
  "
>
  <div class="message-content" style="
    padding: {role === 'user' ? '12px 16px' : '14px 18px'};
    border-radius: {role === 'user' ? '8px 8px 4px 8px' : '8px 8px 8px 4px'};
    background-color: {role === 'user' ? '#3B7FE8' : '#F3F5F7'};
    color: {role === 'user' ? 'white' : '#0D0F11'};
    max-width: 85%;
    font-size: {role === 'user' ? '14px' : '15px'};
    line-height: 1.5;
  ">
    {#if role === 'assistant'}
      <div class="prose">
        {@html htmlContent}
      </div>
    {:else}
      <div style="white-space: pre-wrap;">
        {content}
      </div>
    {/if}

    {#if isStreaming}
      <StreamingIndicator />
    {/if}
  </div>
</div>

<style>
  @keyframes slideIn {
    from {
      opacity: 0;
      transform: translateY(8px);
    }
    to {
      opacity: 1;
      transform: translateY(0);
    }
  }

  :global(.prose) {
    font-size: 15px;
    line-height: 1.5;
    color: #0D0F11;
  }

  :global(.prose p) {
    margin-bottom: 1em;
  }

  :global(.prose p:last-child) {
    margin-bottom: 0;
  }

  :global(.prose strong) {
    font-weight: 500;
    color: #1A1D21;
  }

  /* Enhanced list styling */
  :global(.prose ul), :global(.prose ol) {
    margin-top: 1em;
    margin-bottom: 1em;
    padding-left: 0;
    list-style: none;
  }

  :global(.prose li) {
    margin-bottom: 0.75em;
    padding-left: 1.75em;
    position: relative;
  }

  :global(.prose li:last-child) {
    margin-bottom: 0;
  }

  :global(.prose ul li::before) {
    content: "•";
    position: absolute;
    left: 0.5em;
    color: #3B7FE8;
    font-weight: 600;
    font-size: 1.1em;
  }

  :global(.prose ol) {
    counter-reset: item;
  }

  :global(.prose ol li::before) {
    content: counter(item) ".";
    counter-increment: item;
    position: absolute;
    left: 0.5em;
    color: #3B7FE8;
    font-weight: 600;
  }

  :global(.prose li strong) {
    display: inline-block;
    margin-bottom: 0.25em;
    color: #0D0F11;
  }
</style>
