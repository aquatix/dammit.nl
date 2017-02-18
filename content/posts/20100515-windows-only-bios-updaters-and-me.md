Title: Windows-only bios updaters and me
Date: 2010-05-15 14:01:31
Slug: 20100515-windows-only-bios-updaters-and-me
Location: Home
Authors: Michiel Scholten
Tags: rant

<p>So I have this nice shiny light laptop (the Samsung X360). It came with Microsoft Vista pre-installed, but I never even booted it; I wiped it and installed Ubuntu on it immediately. It's working quite fine, except for some minor issues with its screen's backlight being a bit quirky (it needs a <code>i915.modeset=0</code> part behind its kernel line in Grub's config).</p>

<p>Of course its manufacturer -- Samsung -- puts out bios updates (thankfully). It seems these could remedy these issues. However, instead of having some DOS-like application which can be run in FreeDOS or something, this is a Windows application which refuses to run under wine (bad idea anyway) and specifically checks whether it is being run on the specific laptop (so I can't extract things from it).</p>

<p>Problem is, Windows has been wiped clean from the machine and I have no intention to put the harddisk through a series of resizing tricks to install it again. I don't even have an install disk from the version it shipped with (a trend I quite hate, despite the laptop not even having an optical drive).</p>

<p>So, dear lazyweb, anyone having an idea how to flash the latest bios on it anyway? <a href="http://en.wikipedia.org/wiki/BartPE">A BartPE livecd</a> could be an idea, but I don't have WindowsXP handy...</p>