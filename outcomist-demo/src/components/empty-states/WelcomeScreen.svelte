<script lang="ts">
  import SendButton from '../input/SendButton.svelte';
  import VoiceButton from '../input/VoiceButton.svelte';

  export let onSubmit: (content: string) => void;
  export let disabled: boolean = false;

  let value: string = '';

  function handleSubmit(e: Event) {
    e.preventDefault();
    if (value.trim() && !disabled) {
      onSubmit(value.trim());
      value = '';
    }
  }

  function handleKeydown(e: KeyboardEvent) {
    // Enter alone = submit
    // Shift+Enter, Command+Enter (Mac), or Ctrl+Enter (Windows/Linux) = new line
    if (e.key === 'Enter' && !e.shiftKey && !e.metaKey && !e.ctrlKey) {
      e.preventDefault();
      handleSubmit(e);
    }
    // Allow Command+Enter and Ctrl+Enter to create new lines (browser default behavior)
  }

  function handleVoiceTranscript(transcript: string) {
    // Populate the textarea but don't auto-submit - let user review and edit
    value = transcript;
  }
</script>

<div class="welcome-screen-wrapper">
  <!-- Logo at top left -->
  <div
    class="logo"
    style="
      position: absolute;
      top: 24px;
      left: 24px;
      z-index: 10;
    "
  >
    <img
      src="/src/assets/outcomist-wordmark.svg"
      alt="Outcomist"
      style="height: 26.4px; width: auto; display: block;"
    />
  </div>

  <!-- Centered content (headline + input like Manus) -->
  <div class="welcome-content">
    <h1 class="headline">
      Turn uncertainty into clarity
    </h1>
    <p class="subheadline">
      Your AI partner for structured decision-making
    </p>

    <!-- Centered input box (like Manus) -->
    <div class="input-container-centered">
      <form on:submit={handleSubmit}>
        <div class="input-wrapper-centered">
          <textarea
            class="main-input"
            bind:value
            on:keydown={handleKeydown}
            {disabled}
            placeholder="Describe your decision..."
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

    <div
      class="explore-link"
      style="
        font-size: 14px;
        color: #94969A;
        cursor: pointer;
        margin-top: 24px;
      "
    >
      Explore example decisions ↓
    </div>
  </div>
</div>

<style>
  .welcome-screen-wrapper {
    width: 100%;
    height: 100%;
    position: relative;
  }

  .welcome-content {
    display: flex;
    flex-direction: column;
    align-items: center;
    justify-content: center;
    min-height: 100vh;
    padding: var(--space-12) var(--space-6);
    padding-bottom: 25vh;
    animation: fadeIn var(--duration-slow) var(--ease-out);
  }

  @keyframes fadeIn {
    from {
      opacity: 0;
      transform: translateY(12px);
    }
    to {
      opacity: 1;
      transform: translateY(0);
    }
  }

  /* Headline Styling */
  .headline {
    font-size: var(--font-size-3xl);
    font-weight: var(--font-weight-semibold);
    line-height: var(--line-height-tight);
    color: var(--text-primary);
    margin-bottom: var(--space-4);
    text-align: center;
    letter-spacing: var(--letter-spacing-tight);
  }

  .subheadline {
    font-size: var(--font-size-md);
    font-weight: var(--font-weight-normal);
    line-height: var(--line-height-base);
    color: var(--text-secondary);
    text-align: center;
    margin-bottom: var(--space-12);
    max-width: 600px;
  }

  /* Input Styling */
  .input-container-centered {
    width: 100%;
    max-width: 700px;
  }

  .input-wrapper-centered {
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

  .explore-link {
    font-size: var(--font-size-sm);
    color: var(--text-tertiary);
    cursor: pointer;
    margin-top: var(--space-6);
    transition: color var(--duration-fast) var(--ease-out);
  }

  .explore-link:hover {
    color: var(--blue-500);
  }
</style>
