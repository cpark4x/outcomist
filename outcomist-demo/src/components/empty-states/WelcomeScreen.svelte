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
      src="/src/assets/outcomist-wordmark.png"
      alt="Outcomist"
      style="height: 26.4px; width: auto; display: block;"
    />
  </div>

  <!-- Centered content (headline + input like Manus) -->
  <div
    class="welcome-content"
    style="
      display: flex;
      flex-direction: column;
      align-items: center;
      justify-content: center;
      min-height: 100vh;
      padding: 48px 24px;
      padding-bottom: 25vh;
      animation: fadeIn 600ms ease-out;
    "
  >
    <h1
      style="
        font-size: 32px;
        color: #0D0F11;
        font-weight: 500;
        margin-bottom: 40px;
        text-align: center;
      "
    >
      What are you deciding?
    </h1>

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
    padding: 20px 24px;
    padding-right: 100px;
    font-size: 16px;
    border: 1px solid #E4E6E8;
    border-radius: 12px;
    outline: none;
    transition: all 200ms ease-out;
    background: white;
    color: #0D0F11;
    font-family: system-ui, -apple-system, sans-serif;
    resize: vertical;
    min-height: 120px;
    line-height: 1.5;
  }

  .main-input:focus {
    border-color: #3B7FE8;
    box-shadow: 0 0 0 3px rgba(59, 127, 232, 0.06);
  }

  .main-input::placeholder {
    color: #B8BABD;
  }

  .button-group {
    position: absolute;
    bottom: 16px;
    right: 16px;
    display: flex;
    gap: 8px;
    align-items: center;
  }

  .explore-link {
    transition: color 150ms ease-out;
  }

  .explore-link:hover {
    color: #3B7FE8;
  }
</style>
