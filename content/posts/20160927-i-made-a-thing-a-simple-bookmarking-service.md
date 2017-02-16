Title: I made a thing: a simple bookmarking service
Date: 2016-09-27 13:42:18
Slug: 20160927-i-made-a-thing-a-simple-bookmarking-service
Location: Home
Authors: Michiel Scholten

A while back I started scratching an itch that I had and that wasn't relieved by some existing software or services I could find: a central place to keep track of interesting places on the web I wanted to follow up on, without having them saved as read-later in Pocket (which is an excellent tool, but I'd like to keep it for articles only).

One of the requirements was that I should be able to easily add some URL from my phone, so I can remember it for when I have more time or a bigger screen to research something or watch a video. Also, it needed to be cross-browser, preferably environment agnostic. That ruled out the various bookmark syncing systems of the respective browsers, also because I tend to use Firefox on the desktop and Chrome or [Flyperlink](https://play.google.com/store/apps/details?id=com.flyperinc.flyperlink&hl=en) on my mobile devices.

A web application seemed like a good fit, so I started on a [Flask](http://flask.pocoo.org/) based website with [peewee](http://docs.peewee-orm.com/en/latest/) as uncomplicated ORM. To make it all look good, I used [MaterializeCSS](http://materializecss.com/) which is a great toolkit to create Google Material style websites (I also use it on [aquariusoft.org](https://aquariusoft.org/page/html/digimarks/) for example). As backend, instead of choosing a 'big' database management system like MariaDB or PostgreSQL, I decided that peewee would store its models in a SQLite file.

This all resulted in a project that is quite portable: after creating a virtualenv and filling it with the requirements, one is already able to run the web app by just running `python digimarks.py`, which will run Flask's debug server, but that's fine for the casual use that a bookmarking system gets. The frontend is fully responsive, so looks just fine on a phone screen and big desktop monitor.

Of course, running it under nginx/uwsgi or Apache/mod_wsgi in a central location is a bit more useful, so for myself [I did just that](https://marks.diginaut.net/3fefe73f95b029b4aafca0ed7b24eb1b333e0d6e0ef0a6b2).

While toying around with the functionality after having implemented automatic retrieval of the title of the linked page, tags and stars/favourites were among the first to go in. I would want to find things easily by having relevant labels attached to the bookmarks, and if I especially liked something, a star can be added. Filtering on these, along with search for text makes it easy to find things again.

As I now have tagging, and occasionally want to share research with friends and other people, I decided to make it easy to create a read-only view of a certain tag, where the bookmark cards are available for review by whoever you share the (private-ish) url with, but do not disclose any other information about them, like the other tags attached, 'star' status, or edit possibility. An example is [my list of useful Python resources](https://marks.diginaut.net/pub/db117141a2044cb85435219d67f65635).

All of this is [open sourced on its own GitHub page](https://github.com/aquatix/digimarks), so check it out if you're interested. Installation instructions are included (you can either pip install it, or clone the project and go from there). An [aquariusoft.org project page](https://aquariusoft.org/page/html/digimarks/) is online too, with currently slightly outdated screenshots.