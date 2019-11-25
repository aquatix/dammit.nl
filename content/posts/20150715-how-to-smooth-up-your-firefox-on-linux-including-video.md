Title: How to smooth up your Firefox on Linux, including video
Date: 2015-07-15 15:31:05
Slug: 20150715-how-to-smooth-up-your-firefox-on-linux-including-video
Location: Work
Authors: Michiel Scholten
Category: howto
Tags: desktop, tech, opensource, howto

After having one of our Hangouts videocalls, I started looking into why the browser plugin takes so much CPU-time (and makes the laptop hot and breezy in the process). Is stumbled upon the article [How to tell if you're using hardware acceleration](https://blog.mozilla.org/joe/2010/11/10/how-to-tell-if-youre-using-hardware-acceleration/) and dove into my own `about:support` page in Firefox. Lo and behold, the information behind 'GPU Accelerated Windows' told me it did no hardware acceleration (it showed the 0/1). OK, so how to fix?

[Mozilla decided a while ago to blacklist Intel GPU's](https://support.mozilla.org/en-US/kb/upgrade-graphics-drivers-use-hardware-acceleration) from hardware acceleration, based on the state of the Intel drivers. However, as I'm running Ubuntu 15.04 on this machine with a recent enough graphical stack, I'd say that my Intel driver would be recent enough. Still, Firefox says no.

On to force enabling it then. More digging revealed that some settings in `about:config` could be turned to `true` to enable rendering through hardware. Open a new tab, type `about:config` and search for those two:

    layers.offmainthreadcomposition.enabled
    layers.acceleration.force-enabled

If they are `false`, just double click them to toggle the value to `true`. It seems that only the first is really necessary, but lots of people need the second to be enabled to, so I did that. Restarting Firefox didn't show any improvement though, as it needs an environment variable too.

On a terminal, type `export MOZ_USE_OMTC=1` and then start Firefox from there (`firefox`). Now, if you open `about:support` again, you should now see something better than '0/1' behind the 'GPU Accelerated Windows'. Of course, we want this environment variable be automatically set so we can start Firefox from a menu item; I looked at [this forum thread discussing some ways of making this persistent](https://bbs.archlinux.org/viewtopic.php?id=178757) and choose to add it to `~/.profile`.

Source that most forum threads ultimately pointed to: [No more main-thread OpenGL in Firefox (important note for Linux users who use OpenGL)](http://featherweightmusings.blogspot.co.uk/2013/11/no-more-main-thread-opengl-in-firefox.html)

So, recap:

    - set environment variable MOZ_USE_OMTC=1
    - set firefox setting layers.offmainthreadcomposition.enabled = true
    (both are necessary)

    Most likely layers.acceleration.force-enabled = true is also required

It might be me (or the placebo effect), but scrolling and video's (and even Google Maps) seem to be more responsive after all of this.
