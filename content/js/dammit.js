/* Initialise highlight.js */
hljs.highlightAll();

/* Add copy to clipboard to all code blocks */
let blocks = document.querySelectorAll("pre:has(code)");

blocks.forEach((block) => {
  let button = block.querySelector("button");

  // handle click event
  button.addEventListener("click", async () => {
    await copyCode(block);
  });
});

async function copyCode(block) {
  let code = block.querySelector("code");
  let text = code.innerText;

  await navigator.clipboard.writeText(text);
}
