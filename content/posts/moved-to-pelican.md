Title: Moved to Pelican
Date: 2017-03-26 13:53:41
Slug: 20170326-moved-to-pelican
Location: Home
Authors: Michiel Scholten
Category: projects
Tags: rant, meta
Status: draft

This weblog has always been a self-built affair.

It [started off in 2003]({filename}20031221-my-very-own-rantbox.md) as a PHP website, and continued in that form for over thirteen years. I open sourced it a while ago (in March of 2014), with a colleague promptly finding a [security issue](https://github.com/aquatix/dammit/commit/348c185f40fac8988ffd5b9b20fc1106766bbe68) in the admin code. Frankly, I hadn't look at that code for almost a decade, so that's not good in any regard.

There have been [some]({filename}20151221-dammit-12-years-of-rants.md) [attempts]({filename}20141222-eleven-years-and-counting.md) at rewriting everything in Python, generally while keeping CMS functionality, but life was and is busy as it is, so I rather spend my time on writing content or doing other projects. Inspiration what way to go exactly was also a bit lacking.

I had been toying with [the difference between DB and flat files based sites]({filename}20140810-website-framework-database-driven-or-flat-files.md) for a while, and already had [a website](https://aquariusoft.org) that was rendered from static files that actually pre-dated this weblog. The flexibility of a database-driven CMS with edit possibilities from any browser and being able to dynamically generate pages based on all kinds of up-to-date info was what made dammIT into what it was in the first place, with a sidebar with blogmarks (links to articles and websites I wanted to share with the world) and more. Being able to have a simple set of flat files under a well-functioning version control system is the upside of the flat-file approach. Especially revision control in combination with being able to easily type (draft) in my favourite text editor are really nice-to-haves.

Apart from that, I got fed up by the constant security vulnerabilities in Wordpress, and the way it is technically designed (or not designed, if you look at those database tables).

Following people from around the webs (including for example [rrix](http://rix.si/blog/2013/06/04/moved-to-pelican/)), I decided to experiment with an export I did from the database of the PHP site, generating Markdown files including metadata in a format that Pelican approves of.
