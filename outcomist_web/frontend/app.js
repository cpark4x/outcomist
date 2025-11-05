const API_BASE = 'http://localhost:8000/api';

class OutcomistApp {
    constructor() {
        this.sessionId = null;
        this.currentMessageType = null;

        this.decisionInput = document.getElementById('decision-input');
        this.exploreBtn = document.getElementById('explore-btn');
        this.inputSection = document.getElementById('input-section');
        this.conversationSection = document.getElementById('conversation-section');
        this.conversationHistory = document.getElementById('conversation-history');
        this.cursor = document.getElementById('streaming-cursor');

        this.intentSelection = document.getElementById('intent-selection');
        this.intentValidationBtn = document.getElementById('intent-validation');
        this.intentExecutionBtn = document.getElementById('intent-execution');

        this.userInputArea = document.getElementById('user-input-area');
        this.userResponse = document.getElementById('user-response');
        this.submitResponseBtn = document.getElementById('submit-response');

        this.proceedArea = document.getElementById('proceed-area');
        this.proceedBtn = document.getElementById('proceed-btn');

        this.bindEvents();
    }

    bindEvents() {
        this.exploreBtn.addEventListener('click', () => this.startExploration());
        this.decisionInput.addEventListener('keypress', (e) => {
            if (e.key === 'Enter') {
                this.startExploration();
            }
        });

        this.intentValidationBtn.addEventListener('click', () => this.selectIntent('validation'));
        this.intentExecutionBtn.addEventListener('click', () => this.selectIntent('execution'));

        this.submitResponseBtn.addEventListener('click', () => this.submitUserResponse());
        this.userResponse.addEventListener('keypress', (e) => {
            if (e.key === 'Enter' && !e.shiftKey) {
                e.preventDefault();
                this.submitUserResponse();
            }
        });

        this.proceedBtn.addEventListener('click', () => this.proceedToTier2());
    }

    async startExploration() {
        const decision = this.decisionInput.value.trim();

        if (!decision) {
            this.decisionInput.focus();
            return;
        }

        this.exploreBtn.disabled = true;
        this.exploreBtn.textContent = 'Exploring...';

        try {
            const response = await fetch(`${API_BASE}/sessions/start`, {
                method: 'POST',
                headers: { 'Content-Type': 'application/json' },
                body: JSON.stringify({ decision })
            });

            if (!response.ok) {
                throw new Error('Failed to start session');
            }

            const data = await response.json();
            this.sessionId = data.session_id;

            this.showConversationSection();
            await this.streamTier1();
        } catch (error) {
            console.error('Error:', error);
            this.showError('Something went wrong. Please try again.');
            this.exploreBtn.disabled = false;
            this.exploreBtn.textContent = 'Explore';
        }
    }

    showConversationSection() {
        this.inputSection.style.display = 'none';
        this.conversationSection.classList.remove('hidden');
        this.conversationHistory.innerHTML = '';
    }

    async streamTier1() {
        const messageDiv = this.addMessage('assistant', '', true);
        this.cursor.classList.remove('hidden');

        const eventSource = new EventSource(`${API_BASE}/sessions/${this.sessionId}/stream`);
        let fullText = '';

        eventSource.addEventListener('message', (event) => {
            const chunk = event.data;
            fullText += chunk;
            this.updateMessage(messageDiv, fullText);
        });

        eventSource.addEventListener('done', () => {
            eventSource.close();
            this.cursor.classList.add('hidden');
            this.finalizeMessage(messageDiv, fullText);
            this.showIntentSelection();
        });

        eventSource.addEventListener('error', () => {
            eventSource.close();
            this.cursor.classList.add('hidden');
            this.showError('Stream error occurred. Please try again.');
        });
    }

    addMessage(role, content, isStreaming = false) {
        const messageDiv = document.createElement('div');
        messageDiv.className = `message ${role}`;

        if (content) {
            messageDiv.innerHTML = this.formatMarkdown(content);
        }

        this.conversationHistory.appendChild(messageDiv);
        this.scrollToBottom();

        return messageDiv;
    }

    updateMessage(messageDiv, text) {
        messageDiv.innerHTML = this.formatMarkdown(text);
        this.scrollToBottom();
    }

    finalizeMessage(messageDiv, text) {
        messageDiv.innerHTML = this.formatMarkdown(text);
    }

    showIntentSelection() {
        this.intentSelection.classList.remove('hidden');
        this.scrollToBottom();
    }

    async selectIntent(intent) {
        try {
            await fetch(`${API_BASE}/sessions/${this.sessionId}/intent`, {
                method: 'POST',
                headers: { 'Content-Type': 'application/json' },
                body: JSON.stringify({ intent })
            });

            this.intentSelection.classList.add('hidden');
            this.proceedArea.classList.remove('hidden');
            this.scrollToBottom();
        } catch (error) {
            console.error('Error setting intent:', error);
            this.showError('Failed to set intent. Please try again.');
        }
    }

    async proceedToTier2() {
        this.proceedArea.classList.add('hidden');
        this.cursor.classList.remove('hidden');

        const messageDiv = this.addMessage('question', '', true);

        const eventSource = new EventSource(`${API_BASE}/sessions/${this.sessionId}/proceed`);
        let fullText = '';

        eventSource.addEventListener('message', (event) => {
            const chunk = event.data;
            fullText += chunk;
            this.updateMessage(messageDiv, fullText);
        });

        eventSource.addEventListener('done', () => {
            eventSource.close();
            this.cursor.classList.add('hidden');
            this.finalizeMessage(messageDiv, fullText);
            messageDiv.classList.add('question');
            this.currentMessageType = 'question';
            this.showUserInput();
        });

        eventSource.addEventListener('error', () => {
            eventSource.close();
            this.cursor.classList.add('hidden');
            this.showError('Stream error occurred. Please try again.');
        });
    }

    showUserInput() {
        this.userInputArea.classList.remove('hidden');
        this.userResponse.value = '';
        this.userResponse.focus();
        this.scrollToBottom();
    }

    async submitUserResponse() {
        const answer = this.userResponse.value.trim();

        if (!answer) {
            this.userResponse.focus();
            return;
        }

        this.addMessage('user', answer);

        this.userInputArea.classList.add('hidden');
        this.submitResponseBtn.disabled = true;

        try {
            this.cursor.classList.remove('hidden');
            await this.streamResponse(answer);
        } catch (error) {
            console.error('Error:', error);
            this.showError('Failed to submit response. Please try again.');
        } finally {
            this.submitResponseBtn.disabled = false;
        }
    }

    async streamResponse(answer) {
        const eventSource = new EventSource(`${API_BASE}/sessions/${this.sessionId}/respond?message=${encodeURIComponent(answer)}`);

        let messageDiv = null;
        let fullText = '';
        let messageType = 'assistant';

        eventSource.addEventListener('message', (event) => {
            const chunk = event.data;
            fullText += chunk;

            if (!messageDiv) {
                messageType = this.detectMessageType(fullText);
                messageDiv = this.addMessage(messageType, '', true);
            }

            this.updateMessage(messageDiv, fullText);
        });

        eventSource.addEventListener('done', async () => {
            eventSource.close();
            this.cursor.classList.add('hidden');

            if (messageDiv) {
                this.finalizeMessage(messageDiv, fullText);

                const session = await this.getSession();

                if (this.isSummary(fullText)) {
                    messageDiv.classList.add('summary');
                    this.showUserInput();
                } else if (session.state.recommendation_delivered) {
                    messageDiv.classList.add('recommendation');
                } else if (this.isQuestion(fullText)) {
                    messageDiv.classList.add('question');
                    this.showUserInput();
                }
            }
        });

        eventSource.addEventListener('error', () => {
            eventSource.close();
            this.cursor.classList.add('hidden');
            this.showError('Stream error occurred. Please try again.');
        });
    }

    async getSession() {
        try {
            const response = await fetch(`${API_BASE}/sessions/${this.sessionId}`);
            if (!response.ok) {
                throw new Error('Failed to get session');
            }
            return await response.json();
        } catch (error) {
            console.error('Error getting session:', error);
            return null;
        }
    }

    detectMessageType(text) {
        if (this.isSummary(text)) {
            return 'summary';
        }
        if (this.isQuestion(text)) {
            return 'question';
        }
        return 'assistant';
    }

    isSummary(text) {
        return text.toLowerCase().includes('let me summarize') ||
               text.toLowerCase().includes('does that capture it');
    }

    isQuestion(text) {
        const lines = text.trim().split('\n');
        const lastLine = lines[lines.length - 1].trim();
        return lastLine.endsWith('?');
    }

    formatMarkdown(text) {
        let html = text
            .replace(/\*\*(.*?)\*\*/g, '<strong>$1</strong>')
            .replace(/\n\n/g, '</p><p>')
            .replace(/\n/g, '<br>');

        const lines = html.split('<br>');
        const formatted = [];
        let inList = false;

        for (let line of lines) {
            const trimmed = line.trim();

            if (trimmed.startsWith('•')) {
                if (!inList) {
                    formatted.push('<ul>');
                    inList = true;
                }
                formatted.push(`<li>${trimmed.substring(1).trim()}</li>`);
            } else {
                if (inList) {
                    formatted.push('</ul>');
                    inList = false;
                }
                if (trimmed) {
                    formatted.push(trimmed);
                }
            }
        }

        if (inList) {
            formatted.push('</ul>');
        }

        let result = formatted.join('');

        if (!result.startsWith('<p>')) {
            result = '<p>' + result;
        }
        if (!result.endsWith('</p>')) {
            result = result + '</p>';
        }

        return result;
    }

    scrollToBottom() {
        setTimeout(() => {
            window.scrollTo({
                top: document.body.scrollHeight,
                behavior: 'smooth'
            });
        }, 100);
    }

    showError(message) {
        const errorDiv = document.createElement('div');
        errorDiv.className = 'message assistant';
        errorDiv.innerHTML = `<p style="color: #ff3b30;">${message}</p>`;
        this.conversationHistory.appendChild(errorDiv);
        this.scrollToBottom();
    }
}

document.addEventListener('DOMContentLoaded', () => {
    new OutcomistApp();
});
