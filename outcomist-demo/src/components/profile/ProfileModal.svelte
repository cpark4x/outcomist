<script lang="ts">
  import { onMount } from 'svelte';

  export let show: boolean = false;
  export let onClose: () => void;

  let profile = {
    name: '',
    age: null as number | null,
    role: '',
    goals: [] as string[],
    constraints: [] as string[],
    skills: [] as string[],
    values: [] as string[],
    personalFacts: [] as string[]
  };

  let loading = true;
  let generatingSummary = false;
  let askingQuestion = false;
  let summary = '';
  let searchQuery = '';
  let searchResponse = '';
  let showDetails = false;
  let editMode = false;
  let editedProfile = { ...profile };

  // Load profile when modal opens
  $: if (show) {
    loadProfile();
  }

  async function loadProfile() {
    loading = true;
    summary = '';
    searchQuery = '';
    searchResponse = '';
    showDetails = false;
    editMode = false;

    try {
      const response = await fetch('http://localhost:3001/api/profile');
      const data = await response.json();

      profile = {
        name: data.name || '',
        age: data.age || null,
        role: data.role || '',
        goals: data.goals || [],
        constraints: data.constraints || [],
        skills: data.skills || [],
        values: data.values || [],
        personalFacts: data.preferences?.personalFacts || []
      };

      // Auto-generate summary if there's data
      if (hasAnyData()) {
        await generateSummary();
      }
    } catch (error) {
      console.error('Failed to load profile:', error);
    } finally {
      loading = false;
    }
  }

  async function generateSummary() {
    generatingSummary = true;
    try {
      const response = await fetch('http://localhost:3001/api/profile/summarize', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify(profile)
      });
      const data = await response.json();
      summary = data.summary;
    } catch (error) {
      console.error('Failed to generate summary:', error);
      summary = 'Unable to generate summary.';
    } finally {
      generatingSummary = false;
    }
  }

  async function saveProfile() {
    try {
      const response = await fetch('http://localhost:3001/api/profile', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({
          name: editedProfile.name || null,
          age: editedProfile.age || null,
          role: editedProfile.role || null,
          goals: editedProfile.goals,
          constraints: editedProfile.constraints,
          skills: editedProfile.skills,
          values: editedProfile.values,
          preferences: {
            personalFacts: editedProfile.personalFacts
          }
        })
      });

      if (response.ok) {
        profile = { ...editedProfile };
        profile.personalFacts = [...editedProfile.personalFacts];
        editMode = false;
        // Regenerate summary with new data
        await generateSummary();
      } else {
        console.error('Failed to save profile');
      }
    } catch (error) {
      console.error('Error saving profile:', error);
    }
  }

  function removeItem(section: 'personalFacts' | 'goals' | 'constraints', index: number) {
    editedProfile[section] = [...editedProfile[section].slice(0, index), ...editedProfile[section].slice(index + 1)];
  }

  function addItem(section: 'personalFacts' | 'goals' | 'constraints') {
    const value = prompt(`Add new item:`);
    if (value?.trim()) {
      editedProfile[section] = [...editedProfile[section], value.trim()];
    }
  }

  async function askQuestion(e: Event) {
    e.preventDefault();
    if (!searchQuery.trim() || askingQuestion) return;

    askingQuestion = true;
    searchResponse = '';

    try {
      const response = await fetch('http://localhost:3001/api/profile/ask', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({
          profile,
          question: searchQuery
        })
      });
      const data = await response.json();
      searchResponse = data.answer;
    } catch (error) {
      console.error('Failed to ask question:', error);
      searchResponse = 'Unable to answer question.';
    } finally {
      askingQuestion = false;
    }
  }

  function handleKeydown(e: KeyboardEvent) {
    if (e.key === 'Escape') {
      onClose();
    }
  }

  const isEmpty = (arr: any[]) => !arr || arr.length === 0;
  const hasAnyData = () => {
    return profile.name || profile.age || profile.role ||
           !isEmpty(profile.goals) || !isEmpty(profile.constraints) ||
           !isEmpty(profile.skills) || !isEmpty(profile.values) ||
           !isEmpty(profile.personalFacts);
  };
</script>

<svelte:window on:keydown={handleKeydown} />

{#if show}
  <div
    class="modal-overlay"
    on:click={onClose}
    style="
      position: fixed;
      top: 0;
      left: 0;
      right: 0;
      bottom: 0;
      background: rgba(0, 0, 0, 0.5);
      display: flex;
      align-items: center;
      justify-content: center;
      z-index: 1000;
      padding: 24px;
    "
  >
    <div
      class="modal-content"
      on:click|stopPropagation
      style="
        background: white;
        border-radius: 16px;
        max-width: 720px;
        width: 100%;
        max-height: 90vh;
        overflow: hidden;
        box-shadow: 0 20px 60px rgba(0, 0, 0, 0.3);
        display: flex;
        flex-direction: column;
      "
    >
      <!-- Header -->
      <div style="
        padding: 32px 32px 24px 32px;
        border-bottom: 1px solid #E4E6E8;
      ">
        <h2 style="
          font-size: 24px;
          font-weight: 600;
          color: #0D0F11;
          margin: 0 0 8px 0;
        ">What I Know About You</h2>

        <p style="
          font-size: 14px;
          color: #6B6F73;
          margin: 0;
          line-height: 1.5;
        ">
          Automatically learned from your conversations. Ask me anything about what I know.
        </p>
      </div>

      <!-- Content -->
      <div style="
        flex: 1;
        overflow-y: auto;
        padding: 24px 32px 32px 32px;
      ">
        {#if loading}
          <div style="
            text-align: center;
            padding: 48px 24px;
            color: #6B6F73;
          ">
            <div style="font-size: 15px;">Loading...</div>
          </div>
        {:else if !hasAnyData()}
          <div style="
            text-align: center;
            padding: 48px 24px;
            color: #6B6F73;
          ">
            <div style="font-size: 48px; margin-bottom: 16px; opacity: 0.3;">💭</div>
            <p style="font-size: 15px; margin: 0 0 8px 0;">No profile data yet</p>
            <p style="font-size: 14px; margin: 0; opacity: 0.7;">
              As you chat, I'll automatically learn about you and remember important details.
            </p>
          </div>
        {:else}
          <!-- AI Summary -->
          <div style="
            background: linear-gradient(135deg, #F0F4FF 0%, #E8F0FF 100%);
            border-radius: 12px;
            padding: 20px 24px;
            margin-bottom: 24px;
          ">
            <div style="
              font-size: 13px;
              font-weight: 600;
              color: #3B7FE8;
              text-transform: uppercase;
              letter-spacing: 0.5px;
              margin-bottom: 12px;
            ">Summary</div>

            {#if generatingSummary}
              <div style="color: #6B6F73; font-size: 14px;">Generating summary...</div>
            {:else if summary}
              <div style="
                color: #3D4043;
                font-size: 15px;
                line-height: 1.6;
              ">{summary}</div>
            {/if}
          </div>

          <!-- Ask Questions -->
          <div style="margin-bottom: 24px;">
            <div style="
              font-size: 13px;
              font-weight: 600;
              color: #6B6F73;
              text-transform: uppercase;
              letter-spacing: 0.5px;
              margin-bottom: 12px;
            ">Ask About Your Profile</div>

            <form on:submit={askQuestion}>
              <div style="
                display: flex;
                gap: 8px;
                margin-bottom: 12px;
              ">
                <input
                  type="text"
                  bind:value={searchQuery}
                  placeholder="e.g., Who's traveling with me to Vegas?"
                  disabled={askingQuestion}
                  style="
                    flex: 1;
                    padding: 12px 16px;
                    border: 1px solid #E4E6E8;
                    border-radius: 8px;
                    font-size: 14px;
                    color: #0D0F11;
                    transition: all 200ms;
                  "
                />
                <button
                  type="submit"
                  disabled={!searchQuery.trim() || askingQuestion}
                  style="
                    padding: 12px 20px;
                    border-radius: 8px;
                    border: none;
                    background: {searchQuery.trim() && !askingQuestion ? '#3B7FE8' : '#E4E6E8'};
                    color: {searchQuery.trim() && !askingQuestion ? 'white' : '#9BA0A5'};
                    font-size: 14px;
                    font-weight: 500;
                    cursor: {searchQuery.trim() && !askingQuestion ? 'pointer' : 'not-allowed'};
                    white-space: nowrap;
                  "
                >
                  {askingQuestion ? 'Asking...' : 'Ask'}
                </button>
              </div>
            </form>

            {#if searchResponse}
              <div style="
                padding: 16px 20px;
                background: #F9FAFB;
                border-radius: 8px;
                border-left: 3px solid #3B7FE8;
              ">
                <div style="
                  font-size: 14px;
                  color: #3D4043;
                  line-height: 1.6;
                ">{searchResponse}</div>
              </div>
            {/if}

            <!-- Example questions -->
            {#if !searchResponse}
              <div style="
                display: flex;
                flex-wrap: wrap;
                gap: 8px;
                margin-top: 12px;
              ">
                <button
                  on:click={() => { searchQuery = "When did I last visit Vegas?"; askQuestion(new Event('submit')); }}
                  style="
                    padding: 6px 12px;
                    border: 1px solid #E4E6E8;
                    background: white;
                    color: #6B6F73;
                    border-radius: 6px;
                    font-size: 13px;
                    cursor: pointer;
                  "
                >
                  When did I last visit Vegas?
                </button>
                <button
                  on:click={() => { searchQuery = "Who are my kids?"; askQuestion(new Event('submit')); }}
                  style="
                    padding: 6px 12px;
                    border: 1px solid #E4E6E8;
                    background: white;
                    color: #6B6F73;
                    border-radius: 6px;
                    font-size: 13px;
                    cursor: pointer;
                  "
                >
                  Who are my kids?
                </button>
                <button
                  on:click={() => { searchQuery = "What are my goals?"; askQuestion(new Event('submit')); }}
                  style="
                    padding: 6px 12px;
                    border: 1px solid #E4E6E8;
                    background: white;
                    color: #6B6F73;
                    border-radius: 6px;
                    font-size: 13px;
                    cursor: pointer;
                  "
                >
                  What are my goals?
                </button>
              </div>
            {/if}
          </div>

          <!-- Toggle to show raw details -->
          <div style="margin-top: 24px; padding-top: 24px; border-top: 1px solid #E4E6E8;">
            <div style="display: flex; gap: 12px; align-items: center;">
              <button
                on:click={() => showDetails = !showDetails}
                style="
                  padding: 8px 14px;
                  border: 1px solid #E4E6E8;
                  background: white;
                  color: #6B6F73;
                  border-radius: 6px;
                  font-size: 13px;
                  font-weight: 500;
                  cursor: pointer;
                  display: flex;
                  align-items: center;
                  gap: 8px;
                "
              >
                {showDetails ? '▼' : '▶'} {showDetails ? 'Hide' : 'Show'} Raw Data
              </button>

              {#if showDetails && !editMode}
                <button
                  on:click={() => editMode = true}
                  style="
                    padding: 8px 14px;
                    border: 1px solid #3B7FE8;
                    background: white;
                    color: #3B7FE8;
                    border-radius: 6px;
                    font-size: 13px;
                    font-weight: 500;
                    cursor: pointer;
                  "
                >
                  Edit Data
                </button>
              {/if}
            </div>

            {#if showDetails}
              <div style="margin-top: 16px;">
                <!-- Goals -->
                {#if !isEmpty(profile.goals) || editMode}
                  <div class="section">
                    <h3 class="section-title">Goals</h3>
                    {#if editMode}
                      <div class="edit-list">
                        {#each editedProfile.goals as goal, i}
                          <div class="edit-item">
                            <input type="text" bind:value={editedProfile.goals[i]} />
                            <button on:click={() => removeItem('goals', i)} class="remove-btn">×</button>
                          </div>
                        {/each}
                        <button on:click={() => addItem('goals')} class="add-btn">+ Add goal</button>
                      </div>
                    {:else}
                      <ul class="simple-list">
                        {#each profile.goals as goal}
                          <li>{goal}</li>
                        {/each}
                      </ul>
                    {/if}
                  </div>
                {/if}

                <!-- Constraints -->
                {#if !isEmpty(profile.constraints) || editMode}
                  <div class="section">
                    <h3 class="section-title">Constraints</h3>
                    {#if editMode}
                      <div class="edit-list">
                        {#each editedProfile.constraints as constraint, i}
                          <div class="edit-item">
                            <input type="text" bind:value={editedProfile.constraints[i]} />
                            <button on:click={() => removeItem('constraints', i)} class="remove-btn">×</button>
                          </div>
                        {/each}
                        <button on:click={() => addItem('constraints')} class="add-btn">+ Add constraint</button>
                      </div>
                    {:else}
                      <ul class="simple-list">
                        {#each profile.constraints as constraint}
                          <li>{constraint}</li>
                        {/each}
                      </ul>
                    {/if}
                  </div>
                {/if}

                <!-- Personal Facts -->
                {#if !isEmpty(profile.personalFacts) || editMode}
                  <div class="section">
                    <h3 class="section-title">Personal Details ({editMode ? editedProfile.personalFacts.length : profile.personalFacts.length})</h3>
                    {#if editMode}
                      <div class="edit-list">
                        {#each editedProfile.personalFacts as fact, i}
                          <div class="edit-item">
                            <input type="text" bind:value={editedProfile.personalFacts[i]} />
                            <button on:click={() => removeItem('personalFacts', i)} class="remove-btn">×</button>
                          </div>
                        {/each}
                        <button on:click={() => addItem('personalFacts')} class="add-btn">+ Add fact</button>
                      </div>
                    {:else}
                      <div class="fact-list">
                        {#each profile.personalFacts as fact}
                          <div class="fact-item">{fact}</div>
                        {/each}
                      </div>
                    {/if}
                  </div>
                {/if}

                {#if editMode}
                  <div style="
                    display: flex;
                    gap: 12px;
                    justify-content: flex-end;
                    margin-top: 20px;
                    padding-top: 20px;
                    border-top: 1px solid #E4E6E8;
                  ">
                    <button
                      on:click={() => {
                        editMode = false;
                        editedProfile = { ...profile };
                        editedProfile.personalFacts = [...profile.personalFacts];
                      }}
                      style="
                        padding: 10px 20px;
                        border-radius: 8px;
                        border: 1px solid #E4E6E8;
                        background: white;
                        color: #3D4043;
                        font-size: 14px;
                        font-weight: 500;
                        cursor: pointer;
                      "
                    >
                      Cancel
                    </button>
                    <button
                      on:click={saveProfile}
                      style="
                        padding: 10px 20px;
                        border-radius: 8px;
                        border: none;
                        background: #3B7FE8;
                        color: white;
                        font-size: 14px;
                        font-weight: 500;
                        cursor: pointer;
                      "
                    >
                      Save Changes
                    </button>
                  </div>
                {/if}
              </div>
            {/if}
          </div>
        {/if}
      </div>

      <!-- Footer -->
      <div style="
        padding: 20px 32px;
        border-top: 1px solid #E4E6E8;
        display: flex;
        justify-content: flex-end;
        background: #F9FAFB;
      ">
        <button
          on:click={onClose}
          style="
            padding: 10px 24px;
            border-radius: 8px;
            border: 1px solid #E4E6E8;
            background: white;
            color: #3D4043;
            font-size: 14px;
            font-weight: 500;
            cursor: pointer;
          "
        >
          Close
        </button>
      </div>
    </div>
  </div>
{/if}

<style>
  .section {
    margin-bottom: 20px;
  }

  .section-title {
    font-size: 12px;
    font-weight: 600;
    color: #6B6F73;
    text-transform: uppercase;
    letter-spacing: 0.5px;
    margin: 0 0 8px 0;
  }

  .simple-list {
    margin: 0;
    padding-left: 20px;
  }

  .simple-list li {
    font-size: 13px;
    color: #3D4043;
    line-height: 1.6;
  }

  .fact-list {
    display: flex;
    flex-direction: column;
    gap: 6px;
  }

  .fact-item {
    padding: 10px 14px;
    background: #F9FAFB;
    border-radius: 6px;
    font-size: 13px;
    color: #3D4043;
    line-height: 1.5;
  }

  .edit-list {
    display: flex;
    flex-direction: column;
    gap: 8px;
  }

  .edit-item {
    display: flex;
    gap: 8px;
  }

  .edit-item input {
    flex: 1;
    padding: 10px 12px;
    border: 1px solid #E4E6E8;
    border-radius: 6px;
    font-size: 13px;
    color: #0D0F11;
  }

  .edit-item input:focus {
    outline: none;
    border-color: #3B7FE8;
    box-shadow: 0 0 0 3px rgba(59, 127, 232, 0.06);
  }

  .remove-btn {
    width: 32px;
    height: 32px;
    padding: 0;
    border: 1px solid #E4E6E8;
    background: white;
    color: #9BA0A5;
    border-radius: 6px;
    font-size: 20px;
    line-height: 1;
    cursor: pointer;
    display: flex;
    align-items: center;
    justify-content: center;
    transition: all 150ms;
  }

  .remove-btn:hover {
    background: #FEF2F2;
    border-color: #FCA5A5;
    color: #DC2626;
  }

  .add-btn {
    padding: 8px 14px;
    border: 1px dashed #D1D5D9;
    background: white;
    color: #6B6F73;
    border-radius: 6px;
    font-size: 13px;
    font-weight: 500;
    cursor: pointer;
    transition: all 150ms;
    align-self: flex-start;
  }

  .add-btn:hover {
    border-color: #3B7FE8;
    color: #3B7FE8;
    background: #F0F4FF;
  }
</style>
