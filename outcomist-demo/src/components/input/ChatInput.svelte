<script lang="ts">
  import SendButton from './SendButton.svelte';
  import VoiceButton from './VoiceButton.svelte';

  export let onSubmit: (content: string) => void;
  export let disabled: boolean = false;
  export let placeholder: string = 'Type your message...';

  let value: string = '';

  function handleSubmit(e: Event) {
    e.preventDefault();
    if (value.trim() && !disabled) {
      onSubmit(value.trim());
      value = '';
    }
  }

  function handleKeydown(e: KeyboardEvent) {
    // For single-line input: Enter submits (Shift+Enter, Command+Enter, Ctrl+Enter would need textarea)
    if (e.key === 'Enter' && !e.shiftKey && !e.metaKey && !e.ctrlKey) {
      e.preventDefault();
      handleSubmit(e);
    }
  }

  function handleVoiceTranscript(transcript: string) {
    // Populate the input but don't auto-submit - let user review and edit
    value = transcript;
  }
</script>

<div class="input-container">
  <div class="input-inner">
    <form on:submit={handleSubmit}>
      <div class="input-wrapper">
        <textarea
          class="main-input"
          bind:value
          on:keydown={handleKeydown}
          {disabled}
          {placeholder}
          rows="4"
        ></textarea>
        <div class="button-group">
          <VoiceButton
            {disabled}
            onTranscript={handleVoiceTranscript}
          />
          <SendButton
            {disabled}
            canSubmit={value.trim().length > 0}
            on:click={handleSubmit}
          />
        </div>
      </div>
    </form>
  </div>
</div>

<style>
  .input-container {
    width: 100%;
    background: var(--bg-page);
    padding: var(--space-5);
  }

  .input-inner {
    max-width: 900px;
    margin: 0 auto;
  }

  .input-wrapper {
    position: relative;
    width: 100%;
  }

  .main-input {
    width: 100%;
    padding: var(--space-5) var(--space-6);
    padding-right: 100px;
    font-size: var(--font-size-base);
    font-family: var(--font-family-base);
    border: 1px solid var(--border-default);
    border-radius: var(--radius-lg);
    outline: none;
    transition: all var(--duration-fast) var(--ease-out);
    background: var(--bg-primary);
    color: var(--text-primary);
    resize: vertical;
    min-height: 120px;
    line-height: var(--line-height-base);
  }

  .main-input:hover {
    border-color: var(--border-emphasis);
  }

  .main-input:focus {
    border-color: var(--blue-500);
    box-shadow: var(--shadow-focus);
  }

  .main-input::placeholder {
    color: var(--text-placeholder);
  }

  .button-group {
    position: absolute;
    bottom: var(--space-4);
    right: var(--space-4);
    display: flex;
    gap: var(--space-2);
    align-items: center;
  }
</style>
