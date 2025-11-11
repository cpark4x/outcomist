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
    values: [] as string[]
  };

  let goalsText = '';
  let constraintsText = '';
  let skillsText = '';
  let valuesText = '';

  // Load profile when modal opens
  onMount(async () => {
    if (show) {
      await loadProfile();
    }
  });

  $: if (show) {
    loadProfile();
  }

  async function loadProfile() {
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
        values: data.values || []
      };

      // Convert arrays to text
      goalsText = profile.goals.join('\n');
      constraintsText = profile.constraints.join('\n');
      skillsText = profile.skills.join('\n');
      valuesText = profile.values.join('\n');
    } catch (error) {
      console.error('Failed to load profile:', error);
    }
  }

  async function saveProfile() {
    try {
      // Convert text to arrays
      const updatedProfile = {
        ...profile,
        goals: goalsText.split('\n').filter(g => g.trim()),
        constraints: constraintsText.split('\n').filter(c => c.trim()),
        skills: skillsText.split('\n').filter(s => s.trim()),
        values: valuesText.split('\n').filter(v => v.trim())
      };

      const response = await fetch('http://localhost:3001/api/profile', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json'
        },
        body: JSON.stringify(updatedProfile)
      });

      if (response.ok) {
        onClose();
      } else {
        console.error('Failed to save profile');
      }
    } catch (error) {
      console.error('Error saving profile:', error);
    }
  }

  function handleKeydown(e: KeyboardEvent) {
    if (e.key === 'Escape') {
      onClose();
    }
  }
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
    "
  >
    <div
      class="modal-content"
      on:click|stopPropagation
      style="
        background: white;
        border-radius: 12px;
        padding: 32px;
        max-width: 600px;
        width: 90%;
        max-height: 90vh;
        overflow-y: auto;
        box-shadow: 0 20px 60px rgba(0, 0, 0, 0.3);
      "
    >
      <h2 style="
        font-size: 24px;
        font-weight: 600;
        color: #0D0F11;
        margin: 0 0 8px 0;
      ">Your Profile</h2>

      <p style="
        font-size: 14px;
        color: #6B6F73;
        margin: 0 0 24px 0;
      ">
        Tell Outcomist about yourself so it can personalize conversations and avoid asking the same questions.
      </p>

      <form on:submit|preventDefault={saveProfile}>
        <div class="form-group">
          <label for="name">Name</label>
          <input
            id="name"
            type="text"
            bind:value={profile.name}
            placeholder="Your name"
          />
        </div>

        <div class="form-row">
          <div class="form-group">
            <label for="age">Age</label>
            <input
              id="age"
              type="number"
              bind:value={profile.age}
              placeholder="Age"
            />
          </div>

          <div class="form-group">
            <label for="role">Role</label>
            <input
              id="role"
              type="text"
              bind:value={profile.role}
              placeholder="e.g., Founder, Engineer"
            />
          </div>
        </div>

        <div class="form-group">
          <label for="goals">Goals</label>
          <textarea
            id="goals"
            bind:value={goalsText}
            placeholder="One goal per line&#10;e.g., Launch my product&#10;Build side income"
            rows="3"
          ></textarea>
        </div>

        <div class="form-group">
          <label for="constraints">Constraints</label>
          <textarea
            id="constraints"
            bind:value={constraintsText}
            placeholder="One constraint per line&#10;e.g., Limited budget&#10;Want validation in 2 months"
            rows="3"
          ></textarea>
        </div>

        <div class="form-group">
          <label for="skills">Skills</label>
          <textarea
            id="skills"
            bind:value={skillsText}
            placeholder="One skill per line&#10;e.g., Python development&#10;AI/ML expert"
            rows="3"
          ></textarea>
        </div>

        <div class="form-group">
          <label for="values">Values</label>
          <textarea
            id="values"
            bind:value={valuesText}
            placeholder="One value per line&#10;e.g., Outcome-focused&#10;Learning matters"
            rows="3"
          ></textarea>
        </div>

        <div style="
          display: flex;
          gap: 12px;
          justify-content: flex-end;
          margin-top: 24px;
        ">
          <button
            type="button"
            on:click={onClose}
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
            type="submit"
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
            Save Profile
          </button>
        </div>
      </form>
    </div>
  </div>
{/if}

<style>
  .form-group {
    margin-bottom: 20px;
  }

  .form-row {
    display: grid;
    grid-template-columns: 1fr 1fr;
    gap: 16px;
  }

  label {
    display: block;
    font-size: 14px;
    font-weight: 500;
    color: #3D4043;
    margin-bottom: 8px;
  }

  input,
  textarea {
    width: 100%;
    padding: 10px 12px;
    border: 1px solid #E4E6E8;
    border-radius: 8px;
    font-size: 14px;
    color: #0D0F11;
    font-family: system-ui, -apple-system, sans-serif;
    transition: all 200ms ease-out;
  }

  input:focus,
  textarea:focus {
    outline: none;
    border-color: #3B7FE8;
    box-shadow: 0 0 0 3px rgba(59, 127, 232, 0.06);
  }

  textarea {
    resize: vertical;
    line-height: 1.5;
  }

  input::placeholder,
  textarea::placeholder {
    color: #B8BABD;
  }
</style>
