<script lang="ts">
  // Navigation items will be added here as we build out features
  let activeItem = 'home';
</script>

<div class="sidebar">
  <!-- Navigation items -->
  <nav class="nav-items">
    <!-- Home/New chat -->
    <button
      class="nav-item"
      class:active={activeItem === 'home'}
      on:click={() => activeItem = 'home'}
      title="New decision"
    >
      <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
        <path d="M12 5v14M5 12h14"/>
      </svg>
    </button>

    <!-- Recent conversations (placeholder) -->
    <button
      class="nav-item"
      class:active={activeItem === 'recent'}
      on:click={() => activeItem = 'recent'}
      title="Recent decisions"
    >
      <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
        <path d="M12 8v4l3 3m6-3a9 9 0 11-18 0 9 9 0 0118 0z"/>
      </svg>
    </button>

    <!-- Search (placeholder) -->
    <button
      class="nav-item"
      class:active={activeItem === 'search'}
      on:click={() => activeItem = 'search'}
      title="Search"
    >
      <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
        <circle cx="11" cy="11" r="8"/>
        <path d="m21 21-4.35-4.35"/>
      </svg>
    </button>
  </nav>

  <!-- Bottom items -->
  <div class="bottom-items">
    <!-- Settings (placeholder) -->
    <button
      class="nav-item"
      class:active={activeItem === 'settings'}
      on:click={() => activeItem = 'settings'}
      title="Settings"
    >
      <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
        <circle cx="12" cy="12" r="3"/>
        <path d="M12 1v6m0 6v6M3 12h6m6 0h6"/>
      </svg>
    </button>

    <!-- Help (placeholder) -->
    <button
      class="nav-item"
      class:active={activeItem === 'help'}
      on:click={() => activeItem = 'help'}
      title="Help"
    >
      <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
        <circle cx="12" cy="12" r="10"/>
        <path d="M9.09 9a3 3 0 0 1 5.83 1c0 2-3 3-3 3m.08 4h.01"/>
      </svg>
    </button>
  </div>
</div>

<style>
  .sidebar {
    width: 60px;
    background: #FFFFFF;
    border-right: 1px solid #E4E6E8;
    display: flex;
    flex-direction: column;
    align-items: center;
    padding: 16px 0;
    flex-shrink: 0;
  }

  .nav-items {
    display: flex;
    flex-direction: column;
    gap: 8px;
    flex: 1;
  }

  .bottom-items {
    display: flex;
    flex-direction: column;
    gap: 8px;
    margin-top: auto;
  }

  .nav-item {
    width: 44px;
    height: 44px;
    display: flex;
    align-items: center;
    justify-content: center;
    border: none;
    background: transparent;
    color: #6B7280;
    cursor: pointer;
    border-radius: 8px;
    transition: all 150ms ease-out;
  }

  .nav-item:hover {
    background: #F3F4F6;
    color: #0D0F11;
  }

  .nav-item.active {
    background: #EEF2FF;
    color: #3B7FE8;
  }

  .nav-item:active {
    transform: scale(0.95);
  }
</style>
