/* Initialise highlight.js */
hljs.highlightAll();

/* Add copy to clipboard to all code blocks */
let blocks = document.querySelectorAll("pre:has(code)");
let copyButtonLabel = '<i class="fa-solid fa-copy"></i>';

blocks.forEach((block) => {
    // Add a copy button to all blocks by adding it to a pre's header
    let codeHeader = document.createElement("header");
    let button = document.createElement("button");
    codeHeader.appendChild(button);
    button.innerHTML = copyButtonLabel;
    block.prepend(codeHeader);

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
  button.innerHTML = '<i class="fa-solid fa-square-check"></i>';

  setTimeout(() => {
    button.innerHTML = copyButtonLabel;
  }, 1500);
}
