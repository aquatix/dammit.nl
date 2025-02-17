Title: Silent corruption
Started: 2025-02-17 09:19:39
Date: 2025-02-17 17:06:58
Slug: silent-corruption
Location: Work
Authors: Michiel Scholten
Status: draft
Category: howto
Tags: desktop, howto, linux, tech
Tags-examples: autism, backups, books, communication, conference, copyright, covid-19, desktop, dev, digimarks, energy, ethics, europython, family, fosdem, gadgets, gaming, health, hosting, howto, journal, kids, life, link, linux, meta, mobile, music, networking, notifications, opensource, photography, python, rant (fallback), reading, science, secondbrain, social, space, sync, tech, trip, ubuntu, vim, web, work
Image: 
Link: 

Last week I had a revelation. I had been having odd issues with my workstation for years, which I wrote down to storage being iffy. It ranged from games complaining about corrupt files (of course while trying to play them online, together with friends) to Firefox or Electron apps suddenly crashing.

It was weird, as I had since replaced the original nvme SSD with another one, from another brand, and even reinstalled all the packages of my Ubuntu installation.

The revelation last week was that I was an idiot, and had not thought about running a memtest against my RAM yet. Five minutes later, memtest86+ was telling me that of course there was something wrong with at least one of the 4 DIMMs in my system. Sigh.


--- 8< --- Cheat-sheet: --- >8 ---

[books page]({filename}../pages/books.md)
[hello post]({filename}../posts/hello.md)
[![Linked image](https://dammit.nl/images/content/example.png)](https://dammit.nl/images/content/example.png)
[![Linked gallery image](https://shuttereye.org/images/70/707272f27b6b7a68_2000-2000.jpg)](https://shuttereye.org/gallery/subgallery/IMG_example.jpg/view/)
