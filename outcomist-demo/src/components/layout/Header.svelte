<script lang="ts">
  export let projectTitle: string = '';
</script>

<header
  style="
    background: white;
    border-bottom: 1px solid #E4E6E8;
    padding: 16px 24px;
    display: flex;
    justify-content: space-between;
    align-items: center;
  "
>
  <div>
    <img
      src="/src/assets/outcomist-logo-web.svg"
      alt="Outcomist"
      style="height: 28px; width: auto; display: block;"
    />
  </div>

  <div
    style="
      font-size: 14px;
      color: #64676B;
      font-weight: 500;
    "
  >
    {projectTitle || 'Untitled Project'}
  </div>
</header>
