<div
  class="welcome-screen"
  style="
    display: flex;
    flex-direction: column;
    align-items: center;
    justify-content: center;
    min-height: calc(100vh - 180px);
    padding: 48px 24px;
    animation: fadeIn 600ms ease-out;
  "
>
  <!-- Subtle accent line -->
  <div style="
    width: 48px;
    height: 3px;
    background: linear-gradient(90deg, #3B7FE8 0%, #5E8FF5 100%);
    border-radius: 2px;
    margin-bottom: 32px;
    opacity: 0.9;
  "></div>

  <div style="margin-bottom: 16px;">
    <img
      src="/src/assets/outcomist-logo.svg"
      alt="Outcomist"
      style="height: 48px; width: auto; display: block; margin: 0 auto;"
    />
  </div>

  <p
    style="
      font-size: 17px;
      color: #64676B;
      text-align: center;
      max-width: 520px;
      line-height: 1.6;
      font-weight: 400;
    "
  >
    Navigate complex decisions with clarity.
    <br>
    <span style="opacity: 0.75;">Ask about any choice you're facing.</span>
  </p>

  <!-- Subtle example prompts -->
  <div style="
    margin-top: 48px;
    display: flex;
    flex-direction: column;
    gap: 12px;
    max-width: 560px;
    width: 100%;
  ">
    <div class="example-prompt">
      Should I switch careers?
    </div>
    <div class="example-prompt">
      How do I prioritize competing projects?
    </div>
    <div class="example-prompt">
      Is now the right time to start my business?
    </div>
  </div>
</div>

<style>
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

  .example-prompt {
    padding: 14px 18px;
    background: white;
    border: 1px solid #E4E6E8;
    border-radius: 8px;
    font-size: 14px;
    color: #64676B;
    cursor: pointer;
    transition: all 150ms ease-out;
  }

  .example-prompt:hover {
    border-color: #3B7FE8;
    background: #F8F9FC;
    color: #0D0F11;
    transform: translateY(-1px);
  }
</style>
