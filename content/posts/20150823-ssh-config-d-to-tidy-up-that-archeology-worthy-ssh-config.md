Title: ssh config.d to tidy up that archeology-worthy ~/.ssh/config
Date: 2015-08-23 20:25:10
Slug: 20150823-ssh-config-d-to-tidy-up-that-archeology-worthy-ssh-config
Location: Home
Authors: Michiel Scholten

You might be in that same situation as I was until recently: you open up your ssh config file and start scrolling through the long list of nicely aliased private machines, that organically grown list of `work - project A` and the comment-section-divided `work - project B`, `work - misc`, `work - are these still even on?` and `work - I have no clue why these are even in here`.

At least you have them separated in sections.

However, to make my life a bit easier and to be able to generate parts of the list (for example), I decided that I would try my hand at a `config.d` directory with separate files that the real `~/.ssh/config` file is generated from.

Here it is:

    # SSH config merge
    if [ -e ~/.ssh/config.d ]; then
        #if find ~/.ssh/config.d -mindepth 1 -print -quit | grep -q .; then
        # Do we have config files in that directory?
        if find ~/.ssh/config.d -print -quit | grep -q .; then
            newestconfig=$(find ~/.ssh/config.d/* -printf '%T+ %p\n' | sort -r | head -n1 | awk '{print $2}')
            if [ "$newestconfig" -nt ~/.ssh/config ]; then
                # We found a config that's newer than the generated config file, re-generate
                [ -e ~/.ssh/config ] && mv ~/.ssh/config ~/.ssh/config.bak.$(date -Ins)
                # Lets preserve order, so you can have  00_generic 10_homestuff 20_work1 21_work2  and such
                find ~/.ssh/config.d/* -type f -print0 | sort -z | xargs -0 -n1 cat > ~/.ssh/config
            fi
        fi
    fi

Well, this is the supporting code that is supposed to go in your `~/.bashrc`. When a new shell is opened, it checks whether there is a file in `~/.ssh/config.d/` that is newer than the file `~/.ssh/config` is, and only then the files are concatenated together to that certain file. They are sorted alphanumerically, so you can have a naming scheme like:

    00_base
    10_homestuff
    20_work_project_a
    21_work_project_b
    22_work_still_no_clue
    30_sportclub

The `00_base` one in my list contains some ssh configuration that might be of interest:

    # == Generic config ======
    TCPkeepAlive yes
    ServerAliveInterval 30

    # Re-use existing ssh connections
    Host *
    ControlMaster auto
    ControlPath ~/.ssh/sockets/%r@%h-%p
    ControlPersist 600

If you are interested in my other dotfiles, [I have them online in version control](https://github.com/aquatix/dotfiles) like the coding hipster I am ;)