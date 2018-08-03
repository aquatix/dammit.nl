Title: Fixing the 'unix_listener too long for Unix domain socket' problem
Started: 2018-08-03 09:26:23
Date: 2018-08-03 09:26:23
Slug: ssh-unix-socket
Location: Home office
Authors: Michiel Scholten
Category: howto
Tags: howto, linux, tech

In my `~/.ssh/config` file, I have been using a socket file for every host that I connect to, so TCP sessions can be re-used for faster connecting to a host I already am connected to. I had several iterations of the exact filename for this, as with longer hostnames, the filename becomes too long.

So after `ControlPath ~/.ssh/sockets/%r@%h-%p` and `ControlPath ~/.ssh/sockets/%r@%h` I still ran into problems. Luckily, I came across [this helpful gist](https://gist.github.com/andyvanee/bcf95b1044b80e72b4a42933549a079b) which mentioned the `%C` formatting option to generate a hash of `%l%h%p%r` instead of printing the whole hostname including fully qualified domain name and such. The following snippet works wonders:

    Host *
        ControlPath ~/.ssh/control/%C
        ControlMaster auto
