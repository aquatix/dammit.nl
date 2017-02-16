Title: Quicky: how to fix the weird dropshadow in Ubuntu Gnome 14.10
Date: 2015-03-09 08:23:08
Slug: 20150309-quicky-how-to-fix-the-weird-dropshadow-in-ubuntu-gnome-14-10
Location: Home
Authors: Michiel Scholten

If you get an ugly rectangular dropshadow in Ubuntu Gnome 14.10 with the [gnome-staging ppa](https://launchpad.net/~gnome3-team/+archive/ubuntu/gnome3-staging) (because Gnome 3.14 is so slick), install the Intel graphics driver from [ppa:mgedmin/ppa](https://launchpad.net/~mgedmin/+archive/ubuntu/ppa); this ppa has a patched xserver-xorg-video-intel that fixes this for Utopic users.

[source](https://bugs.launchpad.net/ubuntu/+source/xserver-xorg-video-intel/+bug/1378188)