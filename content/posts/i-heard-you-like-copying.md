Title: I heard you like copying
Started: 2025-10-11 20:08:07
Date: 2025-10-11 20:56:36
Slug: i-heard-you-like-copying
Location: Home
Authors: Michiel Scholten
Status: published
Category: howto
Tags: dev, howto, meta, web

I heard you like copying, so I put some copy buttons in my codes.

As you may have noticed, I am fond of sharing code snippets, which I put inside `<pre><code>` blocks and which are then automagically highlighted by [highlight.js](https://highlightjs.org/), often even correctly so. Copying of those snippets was then a manual task left to the reader though. Of course, selecting lines with the mouse pointer and hitting the 'copy' shortcut is not a lot of work, but things could be made a bit more comfortable.

Enter this magical thing: the 'copy this code' button.

Having a button inside the code block which let the reader copy the contents in one go sounded like a good idea, and after playing with [clipboard.js](https://clipboardjs.com/) for [alfagok](https://alfagok.diginaut.net/), I knew it should not be that hard. Also, after looking into the matter a bit more, I figured that Javascript nowadays had a native way of copying contents of an element or block to the user's clipboard through the `navigator.clipboard.write()` method.

I found [an article online](https://www.roboleary.net/2022/01/13/copy-code-to-clipboard-blog) that went almost where I wanted to go and I started adjusting where my needs drove me to, resulting in the following implementation:

```javascript
/* Automatic copy-to-clipboard buttons, inspired by https://www.roboleary.net/2022/01/13/copy-code-to-clipboard-blog */
/* Add copy to clipboard to all code blocks */
let blocks = document.querySelectorAll("pre:has(code)");
// You can just make this read 'Copy code' for example too
let copyButtonLabel = '<i class="fa-solid fa-copy"></i>';

blocks.forEach((block) => {
    // Add a copy button to all blocks by adding it to a pre's header
    let codeHeader = document.createElement("header");
    let button = document.createElement("button");
    codeHeader.appendChild(button);
    // You can use .innerText to just change the text if you do not use HTML in the label
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
  // You can use .innerText to just change the text if you do not use HTML in the label, e.g. to say 'Code copied'
  button.innerHTML = '<i class="fa-solid fa-square-check"></i>';

  setTimeout(() => {
    button.innerHTML = copyButtonLabel;
  }, 1500);
}
```

This iterates over all `<pre><code>...</code></pre>` blocks and automatically adds a `<header><button>` combo to the `<pre>` block right before the `<code>` one so it sits nicely on top of the content. This way I do not need to add this HTML myself, which is useful as I write articles in fairly standard Markdown, using its simple codeblocks without extra markup. Of course, I could look into making the Markdown parser used by [Pelican](https://getpelican.com/) to generate this HTML server side, but that sounded like work.

This button can take all kinds of form, from a simple button-like element with a text lable like in the article I found, to a more subtle and integrated style like I ended up implementing with the use of two [Font Awesome](https://fontawesome.com/) icons (the 'copy' icon and a checkbox that is shown for 1.5 seconds when you actually copy something).

Anyway, the accompanying styling looks like this:

```css
/* Automatic copy-to-clipboard buttons, inspired by https://www.roboleary.net/2022/01/13/copy-code-to-clipboard-blog */
/* Header sticks to top of pre code blocks  */
pre header
{
    position: sticky;
    top: 0;
    left: 0;

    width: 100%;

    padding-bottom: 0;

    /* Copy button is placed at right side/end of header  */
    display: flex;
    justify-content: end;
}

/* Code block */
pre:has(code)
{
    position: relative;

    /* Add scrollbar if there is overflow */
    overflow-y: auto;

    background-color: black;
    color: white;
    padding-inline: 0.25rem;
    /* Some extra whitespace at the end of the code block to make it look more balanced */
    padding-block-end: 1rem;
}

/* Needed to not have even more whitespace at the top/heading of the code block added by highlight.js */
pre code.hljs
{
    padding-top: 0 !important;
}

/* Copy button */
pre:has(code) button
{
    margin-block: 0.25rem 0.5rem;

    border: 1px solid #333;
    border-radius: 0.25rem;
    padding: 0 .5rem;
}
```

It is the little details :)

[![Linked image](https://dammit.nl/images/content/20251011_highlighted_code_block_copybtn.png)](https://dammit.nl/images/content/20251011_highlighted_code_block_copybtn.png)
