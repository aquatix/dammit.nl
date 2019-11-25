Title: A solution to some odd Gnome 3.16 issues
Date: 2015-04-26 13:21:38
Slug: 20150426-a-solution-to-some-odd-gnome-3-16-issues
Location: Home
Authors: Michiel Scholten
Category: howto
Tags: tech, desktop

I'm running [Ubuntu Gnome](http://ubuntugnome.org/) 15.04 with the ppa's to bring me Gnome 3.16 ([gnome3-team](https://launchpad.net/~gnome3-team/+archive/ubuntu/gnome3) and [gnome3-staging](https://launchpad.net/~gnome3-team/+archive/ubuntu/gnome3-staging)). After a bit of fiddling (removing some old extensions and packages), I got it to show me GDM. After getting into the desktop, there were some odd issues though. These issues also showed up on my laptop with Arch Linux installed, so apparently it wasn't Ubuntu specific.

First, it seemed a bit more sluggish than in 3.14. Also, shortcuts would randomly stop working, and themes would have odd issues, sometimes not wanting to apply at all. Also, logging out took quite a while, same as powering off. This all left me puzzled.

After fiddling around some more, I was left even more puzzled when I was switching around VTE's (or rather, TTY's) with ctrl+alt+Function keys and noticed that I had two GDM login screens. At last, a lead :)

I dove into Google some more, and found a setting for GDM to configure the TTY it should try to appear on first. I added this to `/etc/gdm/custom.conf`:

	[daemon]
	FirstVT = 7

as normally you would expect your graphical session to be launched in TTY 7 (go there by ctrl+alt+F7 or just alt+F7 when on a text prompt in another TTY).

I also tried the line `WaylandEnable=false` in the same section, but that didn't appear to have much effect.

Suddenly, it seems I have only one GDM again and things are running a lot better :) I *do* notice that GDM keeps showing its login screen on TTY 7 and just runs your logged in Gnome on TTY 8. Maybe it was doing so all along and it has to do with MultiSeat. Still, this appears to have helped with some issues.
