<script lang="ts">
  import { Mic, MicOff } from 'lucide-svelte';

  export let onTranscript: (text: string) => void;
  export let disabled = false;

  let isRecording = false;
  let isSupported = false;
  let recognition: any = null;

  // Check if browser supports speech recognition
  $: {
    if (typeof window !== 'undefined') {
      const SpeechRecognition = (window as any).SpeechRecognition || (window as any).webkitSpeechRecognition;
      isSupported = !!SpeechRecognition;

      if (isSupported && !recognition) {
        recognition = new SpeechRecognition();
        recognition.continuous = false;
        recognition.interimResults = false;
        recognition.lang = 'en-US';

        recognition.onresult = (event: any) => {
          const transcript = event.results[0][0].transcript;
          onTranscript(transcript);
          isRecording = false;
        };

        recognition.onerror = (event: any) => {
          console.error('Speech recognition error:', event.error);
          isRecording = false;
        };

        recognition.onend = () => {
          isRecording = false;
        };
      }
    }
  }

  function toggleRecording() {
    if (disabled || !isSupported) return;

    if (isRecording) {
      recognition?.stop();
      isRecording = false;
    } else {
      recognition?.start();
      isRecording = true;
    }
  }
</script>

{#if isSupported}
  <button
    on:click={toggleRecording}
    disabled={disabled}
    class="voice-button"
    class:recording={isRecording}
    aria-label={isRecording ? 'Stop recording' : 'Start voice input'}
    type="button"
  >
    {#if isRecording}
      <MicOff size={20} />
    {:else}
      <Mic size={20} />
    {/if}
  </button>
{/if}

<style>
  .voice-button {
    width: 44px;
    height: 44px;
    border-radius: 50%;
    border: 1.5px solid #E4E6E8;
    background: white;
    color: #64676B;
    cursor: pointer;
    display: flex;
    align-items: center;
    justify-content: center;
    transition: all 150ms ease-out;
  }

  .voice-button:hover:not(:disabled) {
    border-color: #3B7FE8;
    color: #3B7FE8;
    background: #F8F9FC;
  }

  .voice-button:disabled {
    opacity: 0.5;
    cursor: not-allowed;
  }

  .voice-button.recording {
    background: #3B7FE8;
    color: white;
    border-color: #3B7FE8;
    animation: pulse 1.5s ease-in-out infinite;
  }

  @keyframes pulse {
    0%, 100% {
      box-shadow: 0 0 0 0 rgba(59, 127, 232, 0.4);
    }
    50% {
      box-shadow: 0 0 0 8px rgba(59, 127, 232, 0);
    }
  }
</style>
