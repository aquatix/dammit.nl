Title: Converting Mercurial to Git(hub)
Date: 2014-04-06 18:15:21
Slug: 20140406-converting-mercurial-to-git-hub
Location: Home
Authors: Michiel Scholten
Category: howto
Tags: tech, opensource, howto, dev

I'm a fan of version control systems, as they allow me to thinker with my files (both source code and text files with notes and such) to my heart's delight without having to worry about thing getting lost. I can change and update programs, websites and such and can see what the previous versions looked like in the logs.

For my private stuff, I use three different vcs's: Subversion ('svn'), Mercurial ('hg') and Git ('git'). Subversion I've generally migrated away from in favour of more modern alternatives, but it still contains my dotfiles, as it's the only one that can check out a subdir (the repository contains subdirs per machine, between which I can copy config files; my machines differ a bit too much in scope to share one set of dotfiles; this might change in the future).

I took a fancy for hg and when at work we started using mercurial too, I converted the rest of my projects from svn to hg. The repositories I continued to host on my private server, not sharing with the rest of the world (I know, selfish). However, before I started using hg full out, I thinkered a bit with git and found it working just fine too.

Then Github started booming and I started following and starring projects to keep up to date with them. The social aspect of the service is quite interesting and the activity diagram on the user's homepage is intriguing. Slowly I started using it to create forks of projects and for the hosting of some new, small-ish projects I wanted to share with the world. The little activity blocks the commits for these projects caused to appear in [my account timeline](https://github.com/aquatix) didn't reflect my overall hobby activity. Combined with the growing wish to spend more time on hobby projects again and to open up my projects to the world - something I've wanted to do since the beginning, I decided to move my other, older, active projects to Github too. The stats somehow get me hooked on getting my hands dirty again.

There are a few hg-git modules to convert mercurial repos to git ones and back; you can clone the one to the other and then push and pull changes back and forth, quite nifty if you think about it. The one I found working the best is the one from [https://bitbucket.org/durin42/hg-git](https://bitbucket.org/durin42/hg-git) (same as the one on [https://github.com/schacon/hg-git](https://github.com/schacon/hg-git)).

Go to a directory where you keep modules and clone this repository. E.g.,:

	cd ~/workspace/application_addons/mercurial
	hg clone https://bitbucket.org/durin42/hg-git

Now edit your `~/.hgrc` to add it as a module:

	[extensions]
	hggit = ~/workspace/application_addons/mercurial/hg-git/hggit

	[git]
	authors = /home/<youruser>/authors.txt

This last line refers to a file that contains a mapping of your hg usernames to git username/email combinations. Git [needs a username and email address](https://github.com/schacon/hg-git#gitauthors) in its `author` field of each commit, while hg generally only uses a username.

My `~/authors.txt` looks like this:

	mbscholt = Michiel Scholten <michiel@aquariusoft.org>
	m.scholten = Michiel Scholten <michiel@aquariusoft.org>
	Michiel Scholten = Michiel Scholten <michiel@aquariusoft.org>
	convert-repo = svnconvert <michiel@aquariusoft.org>

The nice thing about this, is that even though the history of my hg repositories might not contain a consistent username for my checkins (even containing old ones from its svn days and the `convert-repo` entry of the svn-to-hg conversion), they will all be mapped on my preferred author info when converting to git.

hg-git depends on the `dulwich` module, which you have to install first if you don't have it already. This can be done in various ways (virtualenv etc come to mind), but I installed it system-wide on my Debian-based machine by running `apt-get install python-dulwich`. As a sidenote, I discovered that my acquaintance [Jelmer Vernooij](http://www.samba.org/~jelmer/) (of Samba fame) is author of that libary. The world is small.

Now the scenery has been set up and we can continue to our goal: pushing the mercurial repo to a git one and ultimately publishing this one on Github. Head inside your local clone of the hg repository and add a new remote to its `[paths]` configuration section:

	cd ~/workspace/theproject
	vim .hg/hgrc
	# add the line:
	convgit = /home/youruser/workspace/github/theproject

The latter directory you can either create by cloning a new Github project (be sure not to initialise that repository with a license or anything) or creating the directory with a `mkdir` and a `git init --bare`. You now have an empty git repository ready to receive a push from the existing hg project:

	hg bookmarks hg
	hg push convgit

The hg bookmark is necessary to prevent problems as otherwise hg-git pushes to the currently checked out branch confusing git. This will create a branch named hg in the git repository. The next command pushes your changes to the remote `convgit` you just configured. As the destination is an empty repository, hg-git will happily push the complete history to it. To unconfuse git, go to the directory of the git repository and do:

	git checkout -b master hg

If you created an empty repository by hand and you want to push it to a destination somewhere, add a new remote. For example, if you want to have its origin on Github (this is an alternative way of doing things), do:

	git remote add origin git@github.com:youruser/theproject.git

Alternatively, you can do either of these:

	git remote add origin login@yourserver.net/path/to/repository
	git remote add origin http://yourserver.net/path/to/repository

Instead of `origin` you can have other labels if you have multiple destinations you want to be able to push to and pull from.

Now push the local git repository to its online faith with a `git push --tags`. The `--tags` takes care of pushing all your tags. A second `git push` without the `--tags` pushes the data. That's it. Check the results online and rejoice.

Double check whether everything has been migrated correctly; also you might want to add a `.gitignore` based on your `.hgignore`.

Done :)
