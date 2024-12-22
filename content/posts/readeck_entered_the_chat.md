Title: Readeck enters the chat
Started: 2024-11-16 13:44:01
Date: 2024-12-22 22:22:22
Slug: readeck_entered_the_chat
Location: Home
Authors: Michiel Scholten
Status: published
Category: reading
Category-examples: conferences, family, gadgets, howto, photo, posts (fallback), projects, reading, responses, study, thoughts, trips
Tags: dev, energy, hosting, reading, secondbrain
Tags-examples: autism, backups, books, communication, conference, copyright, covid-19, desktop, dev, digimarks, energy, ethics, europython, family, fosdem, gadgets, gaming, health, hosting, howto, journal, kids, life, link, linux, meta, mobile, music, networking, notifications, opensource, photography, python, rant (fallback), reading, science, secondbrain, social, space, sync, tech, trip, ubuntu, vim, web, work
Image: https://shuttereye.org/images/40/4040100f2f220668_2000-2000.png

After my disappointed [RIP Omnivore]({filename}../posts/rip-omnivore.md) post, I of course started to look around for replacements in general, preferably one I had a bit more control over, which was for example [Wallabag](https://wallabag.org/) and encountered a ton of bookmarking tools. However, I already have [a bookmarking tool of my own](https://github.com/aquatix/digimarks) and Wallabag is a bit... I don't know, crufty?

Then someone on Reddit mentioned [Readeck](https://readeck.org/), which at least was not a bookmarking tool, but a proper read-it-later system, like I was looking for. When I discovered that the way to run it stand-alone (they have a proper Docker container too if you like), is just dumping a binary with some configuration on your machine, I was even more interested. When I joined the Matrix chat room, it turned out that there is a friendly atmosphere with a single developer that is just an amazing person, always happy to help. At the time he was just finishing the Omnivore import, which I was able to test successfully and I have been using it daily ever since.

I missed my [favourite serif typeface of this year]({filename}../posts/literata.md), so I [made a pull request](https://codeberg.org/readeck/readeck/pulls/284) that [was accepted](https://codeberg.org/readeck/readeck/releases/tag/0.15.6) :) That was nice, it made reading a lot more fun for me (I'm a simple person).

In the month since I started the draft for this post, it has steadily become better still, with read progress landing (big one for me, as I am kind of a scattered reader/consumer, so it's nice if my computers keep track of where I can continue) and other little quality of life improvements throughout the interface. The [browser extension](https://codeberg.org/readeck/browser-extension) works great too, and can even help you save articles from behind a paywall (thank you!). Oh, it works just as well on Android Firefox.

A nice thing about Omnivore was the Obsidian plugin which could be configured to download the entire article content too, so you could search your vault for even the contents of what you read (with less priority in Omnisearch so your own notes weigh more of course). This is not something that exists yet for Readeck, but I am tempted to dive into Obsidian plugin development for it.

All in all, I'm happy I discovered Readeck and can recommend it for everyone looking for alternatives for Pocket, Omnivore and such. Currently, you will have to run/host it yourself or find someone to do that for you, but little birds say that there are plans for a hosted solution for people less tech savvy (or even more lazy than me).

I have a small patch set with colours, because I think a hint of purple is nice (the official builds are more boring ;) ):

[![My unread items in Readeck](https://shuttereye.org/images/40/4040100f2f220668_2000-2000.png)](https://shuttereye.org/various/screenshots/20241222_readeck_unreads.png/view/)
