Title: Website framework: database driven or flat files?
Date: 2014-08-10 12:43:33
Slug: 20140810-website-framework-database-driven-or-flat-files
Location: Home
Authors: Michiel Scholten
Category: projects
Tags: tech, web, dev, python

To counterweigh my professional life in which I (thankfully) build nice things in Python/Django, I have hobby projects in which I can thinker with whatever I want to build. Python is still my preferred language, but Django is not a necessity.

I have some legacy projects of my own, which run some sites that are actually quite important for me; the first is [dammIT](http://dammit.nl) (this weblog), which is opensourced as [dammit](https://github.com/aquatix/dammit) on my Github. It's a database driven PHP project with a simple data model for blog posts and a thing I call blogmarks: snippets with url's to interesting articles/sites I found. These can be entered through the CMS, but also come in automatically through [IFTTT](https://ifttt.com/) every time I save an article to [Pocket](http://getpocket.com/). I'm thinking of rebuilding all of this in Django, maybe even with the Rest Framework in between, so I can do nifty things with the API (think an app, command-line posting and such).

As generic API-driven content management system, I have already designed [Kontent-API](https://github.com/aquatix/kontent-api) which I badly need to update and/or actually start building. Maybe I'll combine the two and rebuild dammIT on top of Kontent.

Another way of building websites I like a lot, is using flat files as a source. These can easily be added and maintained in version control and the stack does not need a database to be installed. This is the case for example in my little framework [Qik](https://github.com/aquatix/qik), which also is written in PHP (both projects are over a decade old already) and features for example in my software-projects site [aquariusoft.org](http://aquariusoft.org). The latter surely needs some tender loving care and a big update, so I'm playing with the idea of doing some Flask-based rebuild of it (with some Bootstrap magic or the like for the frontend).

I started working on this at [Qik.py](https://github.com/aquatix/qik.py), but that's at this moment only a bunch of stubs and ideas. It needs a clean way of dividing the logic and the site content (including the site-specific templates and other design elements), so these can be in seperate projects/repos. Also, this might open up possibilities of serving multiple sites from the same codebase install. The theme here is having everything in files that of course can be put in version control. It will not be an entirely static generated website, but it will not have a database backend either.

Both types of projects have their merits; a framework with a database enables a lot of flexibility regarding dynamic content (also automatically coming in from the web, like the blogmarks), but having a simple stack of static files (which can be edited offline through git and such), has a lot of charm in my eyes too. I'd like to thinker with both, but seeing how my free time is rather limited, I might have to choose. Of course, unifying the projects would be an interesting challenge too; I just am a bit stuck in how the automatic blogmarks would work in a system like Qik.py; it would take write access to the file system to add items to a blogmarks.md or create new files per entry for example. Any other ideas? :)
