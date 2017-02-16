Title: update_repos: keep up-to-date with your projects
Date: 2014-10-07 20:52:26
Slug: 20141007-update-repos-keep-up-to-date-with-your-projects
Location: Home
Authors: Michiel Scholten

While I was standardising [my dotfiles](https://github.com/aquatix/dotfiles) I wanted to have an easy and quick way to update my projects so repositories weren't out of date when I wanted to use them (for example when being offline on the train), and I didn't want to go through them by hand every time. Same thing with new projects: I just wanted them to appear on my machines without having to think about cloning them everywhere.

The little script called [`update_repos`](https://github.com/aquatix/dotfiles/blob/master/bin/update_repos) was born.

It takes a file `~/.git_repos` which configures what repositories you want to follow. Yes, it's Git only at the moment, as I stopped using Mercurial (hg) for my own projects, and [tmuxinator](https://github.com/tmuxinator/tmuxinator) takes care of updating the projects at work when I open the relevant configuration (which automatically opens the files in vim, which completely replaced pycharm for my Python development needs).

A typical ~/.git_repos files looks like this:

    # Homedir as workspace:
    workspace=
    group=
    ssh://myserver/srv/git/mydocs.git

    group=.dot
    git@github.com:aquatix/dotfiles.git
    ssh://myserver/srv/git/privdotfiles.git

    workspace=workspace/projects
    group=github
    git@github.com:aquatix/ns-api.git
    #git@github.com:aquatix/dotfiles.git
    git@github.com:aquatix/dammit.git

The first lines result in a repository `mydocs` in ~/mydocs; the second group clones or updates `dotfiles` and `privdotfiles` in ~/.dot It then continuous to a bunch of repositories in ~/workspace/projects/github. Comments can be added by a simple # at the start of the line. Workspaces and groups are parsed from top to bottom, so in the example above, the first two groups are in the same workspace (homedir root) and the third group in ~/workspace/projects; adding another group below would make another subdir inside ~/workspace/projects.

Running it looks like this:

![update_repos](//dammit.nl/images/content/update_repos.png)

When a repository has outstanding changes, a notification shows that status:

![A repo has changed](//dammit.nl/images/content/update_repos_changed.png)

It's very useful to me, so I hope it's useful to some of you too :)
