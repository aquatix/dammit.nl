Title: Second brain part 1
Started: 2020-01-27 16:57:00
Updated: 2020-02-18 15:33:16, 2020-02-26 20:32:00
Date: 2020-02-26 22:02:16
Slug: second-brain-part1
Location: Work
Authors: Michiel Scholten
Category: projects
Tags: dev, digimarks, gadgets, hosting, secondbrain, sync, tech, vim
Image: https://shuttereye.org/images/0b/0b1313131b1b230e_2000-2000.jpeg
Status: published

After [the bootstrap post of this series]({filename}./second-brain-part0.md), I investigated quite some tools, and started building my initial framework of tools, just to play with the idea.

Like mentioned, I used the `mdnav` vim plugin to make jumping between note files frictionless. I added some more patches to it, so it now also understands \[\[wikilinks\]\], which is useful in my opinion, as they are even shorter than regular markdown links, and the Python markdown library understands them too.

This brought me to the topic of backlinks: notes/articles linking back to this particular note. In emacs' org-roam, this is kind of baked in, and I wanted a window with backlinks too. Then, I rediscovered [vimwiki](https://github.com/vimwiki/vimwiki), and tried its markdown mode, which I overlooked when I first encountered it. This enables some nifty functionality in vim. I configured my 'phren' directory as the first wiki, so vimwiki opens and uses it by default. The hotkey <kbd>&lt;leader&gt;ww</kbd> opens the 'wiki' index page, after which I can quickly add notes, search, and navigate. One of the integrations is that links can be created directly by pressing <kbd>enter</kbd> on a word (or a visual selection). vimwiki will create a (markdown) link based on that word, with it using that keyword both as title and as link, so I can then directly follow that link with another press on <kbd>enter</kbd>, and I have just created a new note file. Rock on \m/

Just today I found [notational-fzf](https://github.com/alok/notational-fzf-vim), which provides a quick way of grepping through a bunch of directories and files, using the excellent `fzf` and `rg` (ripgrep), which I [already raved about in my vim post]({filename}vim-reloaded.md). I mapped <kbd>&lt;leader&gt;n</kbd> to it, which opens the find-and-preview window like demoed on its GitHub page.

TL;DR: [.vimrc changes](https://github.com/aquatix/dotfiles/blob/9098575694e26ad60c6658620db79e30a94daea9/.vimrc#L410-L446)


## Mobile

Of course, having all kinds of nifty note taking stuff is fine, but when I would not be able to use it on my mobile, the whole exercise starts getting a lot less useful.

Thankfully, there's [termux]() which has vim, so I can do my vim thing there.

However, vim on a software keyboard is less fun, so I investigated several markdown editors and other systems, like [Joplin](https://joplinapp.org/) and [MindForger](https://www.mindforger.com/). You can find my continuously updated list of interesting links [on my second brain digimarks tag](https://marks.diginaut.net/pub/f45a9fd1b6b8735399018e1b8b653b5d).

The one I settled on, is called [Markor](https://gsantner.net/project/markor.html) and has some good tricks up its sleeve. It provides quick access to a quicknotes.md, a todo.txt (which I don't really use, but it's a good thing to have), and has two modes of viewing your notes: as text editor, or in html rendered mode, with smart rendering of links, including the aforementioned wikilinks. It renders tables correctly (also has some nice highlighting in text mode), and does table of contents. I like :)


## HTML and visual

I also started a [project to generate a static site](https://github.com/aquatix/corpus) from my second brain repository. This really needs a lot of work yet, but I want to have it generate a nice representation of the notes, including backlinks from other ones, and possibly enriched with other sources.

Thinks to ponder on :)
