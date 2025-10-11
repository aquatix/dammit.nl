/* Initialise highlight.js */
hljs.highlightAll();

/* Add copy to clipboard to all code blocks */
let blocks = document.querySelectorAll("pre:has(code)");
let copyButtonLabel = "Copy Code";

blocks.forEach((block) => {
  // Add a copy button to all blocks.
  let button = document.createElement("button");
  button.innerText = copyButtonLabel;
  block.prepend(button);

  // handle click event
  button.addEventListener("click", async () => {
    await copyCode(block, button);
  });
});

async function copyCode(block, button) {
  let code = block.querySelector("code");
  let text = code.innerText;

  await navigator.clipboard.writeText(text);

  // visual feedback that task is completed
  button.innerText = "Code Copied";

  setTimeout(() => {
    button.innerText = copyButtonLabel;
  }, 700);
}
