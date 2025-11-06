const API_BASE = 'http://localhost:8000/api';

class OutcomistApp {
    constructor() {
        this.sessionId = null;
        this.currentMessageType = null;
        this.currentStep = 1;
        this.questionCount = 0;
        this.totalQuestions = 5; // Estimated

        // Element references
        this.decisionInput = document.getElementById('decision-input');
        this.exploreBtn = document.getElementById('explore-btn');
        this.exploreBtnText = document.getElementById('explore-btn-text');
        this.inputSection = document.getElementById('input-section');
        this.conversationSection = document.getElementById('conversation-section');
        this.conversationHistory = document.getElementById('conversation-history');
        this.cursor = document.getElementById('streaming-cursor');

        this.progressStepper = document.getElementById('progress-stepper');
        this.steps = {
            1: document.getElementById('step-1'),
            2: document.getElementById('step-2'),
            3: document.getElementById('step-3'),
            4: document.getElementById('step-4')
        };

        this.intentSelection = document.getElementById('intent-selection');
        this.intentValidationBtn = document.getElementById('intent-validation');
        this.intentExecutionBtn = document.getElementById('intent-execution');

        this.userInputArea = document.getElementById('user-input-area');
        this.userResponse = document.getElementById('user-response');
        this.submitResponseBtn = document.getElementById('submit-response');
        this.submitBtnText = document.getElementById('submit-btn-text');

        this.proceedArea = document.getElementById('proceed-area');
        this.proceedBtn = document.getElementById('proceed-btn');

        // Refined intent selection elements
        this.insightText = document.getElementById('insight-text');
        this.insightHighlight = document.getElementById('insight-highlight');

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

    // ==========================================
    // Progress Stepper Management
    // ==========================================

    showProgressStepper() {
        this.progressStepper.classList.remove('hidden');
        this.updateStep(1, 'active');
    }

    updateStep(stepNumber, state) {
        const step = this.steps[stepNumber];
        if (!step) return;

        const circle = step.querySelector('.step-circle');
        const numberSpan = step.querySelector('.step-number');

        // Remove all states
        step.classList.remove('pending', 'active', 'completed');

        // Add new state
        step.classList.add(state);

        // Update circle content
        if (state === 'completed') {
            circle.innerHTML = getIcon('check', 20);
        } else if (state === 'active') {
            circle.innerHTML = `<span class="step-number">${stepNumber}</span>`;
        } else {
            circle.innerHTML = `<span class="step-number">${stepNumber}</span>`;
        }

        this.currentStep = stepNumber;
    }

    completeStep(stepNumber) {
        this.updateStep(stepNumber, 'completed');
        if (stepNumber < 4) {
            this.updateStep(stepNumber + 1, 'active');
        }
    }

    // ==========================================
    // Exploration Flow
    // ==========================================

    async startExploration() {
        const decision = this.decisionInput.value.trim();

        if (!decision) {
            this.decisionInput.focus();
            return;
        }

        this.setButtonLoading(this.exploreBtn, this.exploreBtnText, 'Exploring...');

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
            this.showProgressStepper();
            await this.streamTier1();
        } catch (error) {
            console.error('Error:', error);
            this.showError('Something went wrong. Please try again.');
            this.setButtonNormal(this.exploreBtn, this.exploreBtnText, 'Explore');
        }
    }

    showConversationSection() {
        this.inputSection.style.display = 'none';
        this.conversationSection.classList.remove('hidden');
        this.conversationHistory.innerHTML = '';
    }

    async streamTier1() {
        // Show loading state
        this.showThinkingState();

        // Don't show AI response as a message - we'll show it in the insight box instead
        const eventSource = new EventSource(`${API_BASE}/sessions/${this.sessionId}/stream`);
        let fullText = '';

        eventSource.addEventListener('message', (event) => {
            const chunk = event.data;
            fullText += chunk;
            // No visual update while streaming - we'll show it all at once in the insight box
        });

        eventSource.addEventListener('done', () => {
            eventSource.close();
            this.hideThinkingState();
            this.completeStep(1); // Understanding complete
            this.showIntentSelection(fullText); // Show refined intent selection with insight
        });

        eventSource.addEventListener('error', () => {
            eventSource.close();
            this.hideThinkingState();
            this.showError('Stream error occurred. Please try again.');
        });
    }

    // ==========================================
    // Message Handling
    // ==========================================

    addMessage(role, content, isStreaming = false) {
        const messageDiv = document.createElement('div');
        messageDiv.className = `message ${role}`;

        // Add message header with icon
        const header = document.createElement('div');
        header.className = 'message-header';

        const iconDiv = document.createElement('div');
        iconDiv.className = 'message-icon';
        iconDiv.innerHTML = this.getMessageIcon(role);

        const roleLabel = document.createElement('span');
        roleLabel.className = 'message-role';
        roleLabel.textContent = this.getMessageRoleLabel(role);

        header.appendChild(iconDiv);
        header.appendChild(roleLabel);

        // Add question counter for question messages
        if (role === 'question' && this.questionCount > 0) {
            const counter = document.createElement('span');
            counter.className = 'question-counter';
            counter.textContent = `Question ${this.questionCount} of ${this.totalQuestions}`;
            header.appendChild(counter);
        }

        messageDiv.appendChild(header);

        // Add content container
        const contentDiv = document.createElement('div');
        contentDiv.className = 'message-content';
        if (content) {
            contentDiv.innerHTML = this.formatMarkdown(content);
        }
        messageDiv.appendChild(contentDiv);

        this.conversationHistory.appendChild(messageDiv);
        this.scrollToBottom();

        return messageDiv;
    }

    updateMessage(messageDiv, text) {
        const contentDiv = messageDiv.querySelector('.message-content');
        contentDiv.innerHTML = this.formatMarkdown(text);
        this.scrollToBottom();
    }

    finalizeMessage(messageDiv, text) {
        const contentDiv = messageDiv.querySelector('.message-content');
        contentDiv.innerHTML = this.formatMarkdown(text);
    }

    getMessageIcon(role) {
        const iconMap = {
            'user': getIcon('user', 24),
            'assistant': getIcon('bot', 24),
            'question': '', // Empty for questions - no icon needed
            'summary': getIcon('document', 24),
            'recommendation': getIcon('checkCircle', 24)
        };
        return iconMap[role] || getIcon('bot', 24);
    }

    getMessageRoleLabel(role) {
        const labelMap = {
            'user': 'You',
            'assistant': 'Outcomist',
            'question': '', // Empty for questions - counter shows the info
            'summary': 'Summary',
            'recommendation': 'Recommendation'
        };
        return labelMap[role] || 'Outcomist';
    }

    // ==========================================
    // Intent Selection
    // ==========================================

    showIntentSelection(aiResponse = '') {
        if (aiResponse) {
            // Split response into paragraphs
            const paragraphs = aiResponse.trim().split('\n\n').filter(p => p.trim());

            // First paragraph(s) = insight, last paragraph = key question
            if (paragraphs.length >= 2) {
                // Main insight (all but last paragraph)
                const insightParagraphs = paragraphs.slice(0, -1);
                this.insightText.innerHTML = this.formatMarkdown(insightParagraphs.join('\n\n'));

                // Key question (last paragraph)
                const keyQuestion = paragraphs[paragraphs.length - 1].replace(/^\?+\s*/, '').trim();
                this.insightHighlight.textContent = keyQuestion;
            } else {
                // Single paragraph - use it as insight
                this.insightText.innerHTML = this.formatMarkdown(aiResponse);
                this.insightHighlight.textContent = "What are you actually optimizing for?";
            }
        } else {
            // Fallback if no response provided
            this.insightText.textContent = "Let me help you explore this decision from multiple angles.";
            this.insightHighlight.textContent = "What matters most to you in this situation?";
        }

        // Cards now show static sample questions (no dynamic text generation)
        this.intentSelection.classList.remove('hidden');
        this.updateStep(2, 'active'); // Move to Intent step
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
            this.completeStep(2); // Intent complete

            // Go directly to Tier 2 discovery (no intermediate button)
            await this.proceedToTier2();
        } catch (error) {
            console.error('Error setting intent:', error);
            this.showError('Failed to set intent. Please try again.');
        }
    }

    // ==========================================
    // Tier 2 Discovery
    // ==========================================

    async proceedToTier2() {
        this.proceedArea.classList.add('hidden');
        this.cursor.classList.remove('hidden');
        this.updateStep(3, 'active'); // Move to Discovery step
        this.questionCount = 1; // Start counting questions

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
            this.currentMessageType = 'question';
            this.showUserInput();
        });

        eventSource.addEventListener('error', () => {
            eventSource.close();
            this.cursor.classList.add('hidden');
            this.showError('Stream error occurred. Please try again.');
        });
    }

    // ==========================================
    // User Response
    // ==========================================

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
        this.hideOldMessages(); // Hide previous Q&A

        this.userInputArea.classList.add('hidden');
        this.setButtonLoading(this.submitResponseBtn, this.submitBtnText, 'Sending...');

        try {
            this.cursor.classList.remove('hidden');
            await this.streamResponse(answer);
        } catch (error) {
            console.error('Error:', error);
            this.showError('Failed to submit response. Please try again.');
        } finally {
            this.setButtonNormal(this.submitResponseBtn, this.submitBtnText, 'Send');
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
                } else if (session && session.state.recommendation_delivered) {
                    messageDiv.classList.add('recommendation');
                    this.completeStep(3); // Discovery complete
                    this.updateStep(4, 'completed'); // Recommendation complete
                    this.showRestartOption();
                } else if (this.isQuestion(fullText)) {
                    messageDiv.classList.add('question');
                    this.questionCount++; // Increment for next question
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

    // ==========================================
    // Message Type Detection
    // ==========================================

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

    // ==========================================
    // Markdown Formatting
    // ==========================================

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

    // ==========================================
    // UI Utilities
    // ==========================================

    setButtonLoading(button, textElement, loadingText) {
        button.disabled = true;
        button.classList.add('loading');
        textElement.textContent = loadingText;

        // Add spinner icon
        const spinner = document.createElement('span');
        spinner.innerHTML = getIcon('spinner', 20);
        button.insertBefore(spinner, textElement);
    }

    setButtonNormal(button, textElement, normalText) {
        button.disabled = false;
        button.classList.remove('loading');
        textElement.textContent = normalText;

        // Remove spinner if present
        const spinner = button.querySelector('.icon-spinner');
        if (spinner) {
            spinner.parentElement.remove();
        }
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
        errorDiv.innerHTML = `
            <div class="message-header">
                <div class="message-icon" style="color: var(--color-error);">${getIcon('circle', 24)}</div>
                <span class="message-role">Error</span>
            </div>
            <div class="message-content">
                <p style="color: var(--color-error);">${message}</p>
            </div>
        `;
        this.conversationHistory.appendChild(errorDiv);
        this.scrollToBottom();
    }

    hideOldMessages() {
        // Hide all but the last two messages (current question and user's answer)
        const messages = this.conversationHistory.querySelectorAll('.message');
        messages.forEach((msg, index) => {
            if (index < messages.length - 2) {
                msg.classList.add('hidden');
            }
        });
    }

    showRestartOption() {
        const restartDiv = document.createElement('div');
        restartDiv.className = 'restart-section';
        restartDiv.innerHTML = `
            <button class="primary-btn restart-decision-btn" onclick="location.reload()">
                <span>Explore Another Decision</span>
            </button>
        `;
        this.conversationHistory.appendChild(restartDiv);
        this.scrollToBottom();
    }

    showThinkingState() {
        const thinkingDiv = document.createElement('div');
        thinkingDiv.id = 'thinking-state';
        thinkingDiv.className = 'thinking-state';
        thinkingDiv.innerHTML = `
            <div class="thinking-content">
                <div class="thinking-spinner"></div>
                <div class="thinking-text">Analyzing your decision...</div>
            </div>
        `;
        this.conversationHistory.appendChild(thinkingDiv);
        this.scrollToBottom();
    }

    hideThinkingState() {
        const thinkingDiv = document.getElementById('thinking-state');
        if (thinkingDiv) {
            thinkingDiv.remove();
        }
    }
}

// Initialize app when DOM is ready
document.addEventListener('DOMContentLoaded', () => {
    new OutcomistApp();
});
