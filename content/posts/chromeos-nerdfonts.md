Title: NerdFonts on ChromeOS
Started: 2023-12-06 13:24:02
Date: 2023-12-06 16:40:02
Modified: 2025-10-03 10:40:00
Slug: chromeos-nerdfonts
Location: Home
Authors: Michiel Scholten
Status: published
Category: howto
Tags: dev, energy, fonts, gadgets, howto, linux, mobile, opensource, web
Image: https://shuttereye.org/images/49/4941616121616125_2000-2000.png

![ChromeOS hterm with NerdFonts-enabled vim](https://shuttereye.org/images/49/4941616121616125_2000-2000.png)

I get way too much 'kick' out of a [good font]({filename}../posts/monaspaced.md), and the [Nerd Fonts](https://www.nerdfonts.com/) project has been doing an awesome job at combining about every monospace font with glyphs/icons from FontAwesome, Devicons etc, for use in vim, terminal prompts and more. Of course I combine my frequent use of terminals with the lovely fonts above and my wielding of a variety of gadgets, among which two ChromeOS-based 2-in-1 tablets, which means the default configuration of the terminal on these devices falls short of expectations.

The built-in monospace fonts in the so-called `hterm` terminal on Chromebooks has some extra glyphs, but by far not the complete set of icons that we have grown to expect from the likes of NerdFonts.

How to fix?

Start with opening the extended terminal/SSH preferences by pasting (or typing) this URL in Chrome: `chrome-untrusted://terminal/html/nassh_preferences_editor.html` and point the 'Custom CSS (URI)' field to a URL hosting a CSS file with content this one:

```css
@font-face {
    font-family: "Hack Sans Mono Nerd";
    src: url("https://cdn.example.com/chromeos/HackNerdFontMono-Regular.ttf");
    font-weight: normal;
    font-style: normal;
}

@font-face {
    font-family: "JetBrains Sans Mono Nerd";
    src: url('https://cdn.example.com/chromeos/JetBrainsMonoNerdFontMono-Regular[opsz,wght].woff2') format('woff2');
    font-weight: normal;
    font-style: normal;
}

@font-face {
    font-family: "DejaVu Sans Mono Nerd";
    src: url("https://raw.githubusercontent.com/ryanoasis/nerd-fonts/master/patched-fonts/DejaVuSansMono/Regular/complete/DejaVu%20Sans%20Mono%20Nerd%20Font%20Complete%20Mono.ttf");
    font-weight: normal;
    font-style: normal;
}

/* Regular and italic variants for the same font have the same font-family */
@font-face {
    font-family: "Lilex Nerd";
    src: url("https://cdn.example.com/chromeos/LilexNerdFont-Medium.ttf");
    font-weight: normal;
    font-style: normal;
}
@font-face {
    font-family: "Lilex Nerd";
    src: url("https://cdn.example.com/chromeos/LilexNerdFont-MediumItalic.ttf");
    font-weight: normal;
    font-style: italic;
}
```

This of course assumes you have access to a webserver to host such a file on, preferably with some of the fonts too. We'll skip over that part here for scope's sake, but you can even use a Raspberry Pi Zero on your home line to serve it.

In the 'Text font family' input field, type the name of the font you'd like to use, for example `'Hack Sans Mono Nerd', monospace` (this falls back to the default `monospace`).

Now comes the fun part, as serving this file is pretty easy, but the `hterm` ChromeOS terminal does not load the styling or the font files if the relevant cross-origin headers are not set correctly on the webserver; this would mean that the server would tell the client (generally the browser, in our case the terminal-that's-really-just-a-browser-window) that it is not allowed to load the content when it is not from the same domain name/server/location. As the ChromeOS terminal loads from a local resource on the Chromebook, of course it will never match your webserver's location, so we will have to take that into account.

Thankfully, the mentioned headers are there to tell the webserver what to - er, well - tell the client. [Access-Control-Allow-Origin](https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/Access-Control-Allow-Origin) is needed to accept loading the files from any location, and the [Cross-Origin-Embedder-Policy](https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/Cross-Origin-Embedder-Policy) ('COEP') related headers are there to tell the client that it is allowed to use the files as resources in whatever it is trying to show. This latter one would normally prevent the loading of the stylesheet file with a line about 'COEP'; you can check that by typing <kbd>ctrl</kbd>+<kbd>shift</kbd>+<kbd>j</kbd> to open the dev tools while having a terminal window opened. The messages show up in the Console.

Now, to configure the webserver.

nginx config, for example:

```
    location / {
        root /srv/www/cdn.example.com/;

        location ~* \.(css|eot|ttf|woff|woff2)$ {
            # Allow remote loading of fonts, e.g., when developing
            add_header Access-Control-Allow-Origin *;
            add_header Cross-Origin-Resource-Policy cross-origin;
            add_header Cross-Origin-Embedder-Policy require-corp;
            add_header Cross-Origin-Opener-Policy same-origin;
        }
    }
```

Apache config, for example:

```
    DocumentRoot /srv/www/cdn.example.com
    <Directory />
        # Header add Access-Control-Allow-Origin "*"
        Header add Access-Control-Allow-Origin *
        Header set Access-Control-Allow-Methods "GET,POST,PUT,DELETE,OPTIONS"
        Header set Access-Control-Allow-Headers "Content-Type,Authorization,X-Requested-With"
        Header set Access-Control-Allow-Credentials "true"

        Header add Cross-Origin-Resource-Policy "cross-origin"
        Header add Cross-Origin-Embedder-Policy "require-corp"
        Header add Cross-Origin-Opener-Policy "same-origin"
    </Directory>
```

Restart the webserver software, close all terminal windows on your Chromebook, and try the font by opening a fresh ChromeOS terminal.


![starship.rs prompt](https://dammit.nl/images/content/20231206_chromeos_terminal_starship_prompt.png)


## Other ways, not always working

<kbd>ctrl</kbd>+<kbd>shift</kbd>+<kbd>j</kbd> to open the dev tools while having a terminal window opened. Go to the Javascript Console. Paste these commands, first adjusting to your wishes:

```javascript
term_.prefs_.set('font-family', 'JetBrains Mono Nerd Font, monospace');
term_.prefs_.set('user-css-text', '@font-face {font-family: "JetBrains Mono Nerd Font"; src: url("https://cdn.example.com/chromeos/JetBrainsMonoNerdFontMono-Regular.ttf)"); font-weight: normal; font-style: normal;} x-row {text-rendering: optimizeLegibility;font-variant-ligatures: normal;}')

// or:

term_.prefs_.set('user-css-text', '@font-face {font-family: "JetBrains Mono Nerd Font"; src: url("https://raw.githubusercontent.com/ryanoasis/nerd-fonts/master/patched-fonts/JetBrainsMono/Ligatures/Regular/JetBrainsMonoNerdFont-Regular.ttf)"); font-weight: normal; font-style: normal;} x-row {text-rendering: optimizeLegibility;font-variant-ligatures: normal;}')


term_.prefs_.set('font-family', 'DejaVu Sans Mono Nerd');
term_.prefs_.set('user-css-text', '@font-face {font-family: "DejaVu Sans Mono Nerd"; src: url("https://raw.githubusercontent.com/ryanoasis/nerd-fonts/master/patched-fonts/DejaVuSansMono/Regular/complete/DejaVu%20Sans%20Mono%20Nerd%20Font%20Complete%20Mono.ttf"); font-weight: normal; font-style: normal;}')
```

This method should work too, but might need re-applying after a reboot. It has as pre that you do not need to host a stylesheet somewhere.

<div class="edit">edited at 2025-10-03 10:40</div>

Added Lilex font as example for `font-family` for variants, changed the JetBrains example to a woff2 font.
