Title: Second brain part 0
Started: 2020-01-27 16:57:37, 2020-01-28 11:35:00
Date: 2020-01-28 14:53:00
Slug: second-brain-part0
Location: Home
Authors: Michiel Scholten
Category: projects
Tags: dev, digimarks, gadgets, secondbrain, sync, tech, vim
Image: https://shuttereye.org/galleries/various/dammit/building_a_second_brain_logo.png
Status: published

![Building a Second Brain logo](https://shuttereye.org/galleries/various/dammit/building_a_second_brain_logo.png)

I have been thinking lately about how I organise my thoughts, notes, files, todo's, incoming messages, and much more. This was partly fed by [Ryan Rix](https://rix.si/) and his quest for the ultimate way of organising data, be it [org-mode](https://orgmode.org/) or a variant, [TiddlyWiki](https://tiddlywiki.com/), or something entirely self-built.

I have quite a bunch of tools that help me in my daily (digital|analogue) life. Currently I use:

- Various Git repositories for documents that are best kept versioned (notes, planning, etc)
- A few big-ish directories that I keep in sync over my various machines using [syncthing](https://syncthing.net/), mostly for binary files
- TickTick for todo's, (shared) shopping list
- Google Keep for quick notes (also to share with my significant other)
- [digimarks](https://github.com/aquatix/digimarks) for bookmarks
- Evolution for email on 'desktop', aquamail on mobile clients
- Google Calendar for appointments
- [Inoreader](https://www.inoreader.com/) for RSS news feeds
- [Pocket](https://getpocket.com) for articles to read later (or never)

These are all moving parts in my 'second brain', in which I keep my notes, appointments, and basically everything. Well, there are more people interested in [Building A Second Brain (BASB)](https://www.buildingasecondbrain.com/). One of the authors/teachers of this initial concept has a [nice intro article in the matter](https://praxis.fortelabs.co/basboverview/). I also like the [CODE](https://www.keepproductive.com/blog/how-to-build-a-second-brain) acronym: Collect, Organise, Distill, Express.

I collect useful methods and other links [on my 'building a second brain' link page](https://marks.diginaut.net/pub/f45a9fd1b6b8735399018e1b8b653b5d).


## So, what now?

My [vim-reloaded]({filename}../posts/vim-reloaded.md) article showed a lot of love for vim, and that's because I find it such a fun text editor to work in. It works everywhere, from remote servers, to laptops, and my phone (go [termux](https://termux.com/)).

That's why I would like to incorporate some of this brain offloading into my vim setup. I started with [Markdown file navigation](https://github.com/chmp/mdnav), which I quickly [forked](https://github.com/aquatix/mdnav/tree/fixes) so it works correctly with Python 3 and my preferred style of Pelican links. This way I can link various notes together, simply by adding a (relative) link from one file to another.

Apart from those notes, it would be nice to have 'relevancy filters' in my incoming messages/news feeds. I have to investigate in how smart Inoreader can be. This reminds me of the ['overload' feedreader](https://aquariusoft.org/page/html/overload/) I wrote ages ago, and abandoned. Its goal was rather similar: deduplicating news, trying to find interesting articles. I would also like to be offered interesting new stuff, from outside my filter bubble.

For mail, I already have extensive filtering in place, which helps me a lot with reading relevant messages. Creating actionable items (todo's or similar) from an email is something that is still on my wish list though, especially because I would love to have it link back to the original email.

This post really is an initial brain-dump (hrr hrr) of thoughts, current tools, and such. I would like to have it bootstrap an effort in making my life better.


## Naming is hard, what will it be called?

Does this project need to have a name? Oh well, why not? :)

I am inclined to call my project [Phren](https://en.wikipedia.org/wiki/Phren), after the ancient Greek word φρήν for the location of thought or contemplation.
