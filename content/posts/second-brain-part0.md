Title: Second brain part 0
Started: 2020-01-27 16:57:37, 2020-01-28 11:35:00
Date: 2020-01-27 16:57:37
Slug: second-brain-part0
Location: Home
Authors: Michiel Scholten
Category: projects
Tags: dev, digimarks, gadgets, secondbrain, sync, tech, vim
Image: 
Status: draft

I have been thinking lately about how I organise my thoughts, notes, files, todo's, incoming messages, and much more. This was partly fed by [Ryan Rix](https://rix.si/) and his quest for the ultimate way of organising data, be it [org-mode](https://orgmode.org/) or variant, [TiddlyWiki](https://tiddlywiki.com/) or something entirely self-built.

I have quite a bunch of tools that help me in my daily (digital|analogue) life. Currently I use:

- TickTick for todo's, (shared) shopping list
- Google Keep for quick notes (also to share with my significant other)
- [digimarks](https://github.com/aquatix/digimarks) for bookmarks
- Various Git repositories for documents that are best kept versioned (notes, planning, etc)
- A few big-ish directories that I keep in sync over my various machines using [syncthing](https://syncthing.net/), mostly for binary files
- Evolution for email on 'desktop', aquamail on mobile clients
- Google Calendar for appointments
- [Inoreader](https://www.inoreader.com/) for RSS news feeds
- [Pocket](https://getpocket.com) for articles to read later (or never)

These are all moving parts in my 'second brain', in which I keep my notes, appointments, and basically everything. Well, there are more people interested in [Building A Second Brain (BASB)](https://www.buildingasecondbrain.com/). One of the authors/teachers of this initial concept has a [nice intro article in the matter](https://praxis.fortelabs.co/basboverview/). I also like the [CODE](https://www.keepproductive.com/blog/how-to-build-a-second-brain) acronym: Collect, Organise, Distill, Express.

I collect useful methods and other links [on my 'building a second brain' link page](https://marks.diginaut.net/pub/f45a9fd1b6b8735399018e1b8b653b5d).

My [vim-reloaded]({filename}../posts/vim-reloaded.md) article showed a lot of love for vim, and that's because I find it such a fun text editor to work in. It works everywhere, from remote servers, to laptops, and my phone (go [termux](https://termux.com/)).

That's why I would like to incorporate some of this brain offloading into my vim setup. I started with [Markdown file navigation](https://github.com/chmp/mdnav), which I quickly [forked](https://github.com/aquatix/mdnav/tree/fixes) so it works correctly with Python 3 and my preferred style of Pelican links.
