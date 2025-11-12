import { writable } from 'svelte/store';

export interface Message {
  id: string;
  role: 'user' | 'assistant';
  content: string;
  timestamp: Date;
  isStreaming?: boolean;
}

export type Phase = 'discover' | 'review' | 'execute';

export interface ConversationState {
  messages: Message[];
  isProcessing: boolean;
  projectTitle: string;
  currentPhase: Phase;
}

function createConversationStore() {
  const initialState: ConversationState = {
    messages: [],
    isProcessing: false,
    projectTitle: '',
    currentPhase: 'discover',
  };

  const { subscribe, set, update } = writable<ConversationState>(initialState);

  return {
    subscribe,
    set,
    update,

    reset: () => set(initialState),

    addMessage: (message: Omit<Message, 'id' | 'timestamp'>) => {
      update(state => ({
        ...state,
        messages: [
          ...state.messages,
          {
            ...message,
            id: crypto.randomUUID(),
            timestamp: new Date(),
          },
        ],
      }));
    },

    setProcessing: (isProcessing: boolean) => {
      update(state => ({ ...state, isProcessing }));
    },

    setProjectTitle: (projectTitle: string) => {
      update(state => ({ ...state, projectTitle }));
    },

    setPhase: (phase: Phase) => {
      update(state => ({ ...state, currentPhase: phase }));
    },
  };
}

export const conversation = createConversationStore();
