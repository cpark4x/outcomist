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
  <div
    style="
      font-size: 18px;
      font-weight: 600;
      color: #0D0F11;
      letter-spacing: -0.02em;
    "
  >
    Outcomist
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
