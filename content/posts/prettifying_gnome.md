Title: Pretty Gnome
Started: 2016-02-24, 2017-04-26 16:17:00, 2017-06-03, 2018-11-25
Date: 2017-04-26 16:17:00
Slug: pretty-gnome
Authors: Michiel Scholten
Category: howto
Tags: linux, desktop, howto
Status: draft

This little howto has been long in the making, as I wanted to do a write-up of how I themed and tweaked my Gnome(-Shell) based desktops to my liking for quite a while.

I use a bunch of Gnome-Shell extensions to provide some extra convenience and declutter the environment.

Start with the [User Themes](https://extensions.gnome.org/extension/19/user-themes/) extension, as that enables custom themes for Gnome-Shell, about which I'll speak later on.

[Media player indicator](https://extensions.gnome.org/extension/55/media-player-indicator/): Control MPRIS Version 2 Capable Media Players. Shows cover art, remote control and some more handy stuff when you're playing your music (or clips).
Related, [Volume mixer](https://extensions.gnome.org/extension/858/volume-mixer/) is an extension for GNOME Shell allowing separate configuration of PulseAudio devices and output switches. It features a profile switcher to quickly switch between pinned profiles and devices.

Information at a glance I get from the [OpenWeather](https://extensions.gnome.org/extension/750/openweather/) extension, and the [System monitor](https://extensions.gnome.org/extension/120/system-monitor/) one. The former speaks for itself, the latter shows you information about how busy your CPU, memory, network, fans and so are. I found out that disabling the showing of information in the *disk* tab (just uncheck the three checkboxes) solves a long-standing annoyance I had with unlocking my systems when a network share was mounted: apparently the disk stats cause the lockscreen to wait for a long time (until something times out), which caused me to wait for sometimes longer than a minute to stare at the GDM lockscreen 'unlocking' itself. Especially annoying after a suspend and/or network change.

Some space can be saved and cleanness achieved by using the following few extensions:

[Remove dropdown arrows](https://extensions.gnome.org/extension/800/remove-dropdown-arrows/): Removes the dropdown arrows which were introduced in Gnome 3.10 from the App Menu, System Menu, Input Menu, Access Menu, Places Menu, Applications Menu and any other extension that wants to add dropdown arrows.

[No Title Bar](https://extensions.gnome.org/extension/1267/no-title-bar/): removes the title bar, moves the window title and buttons to the top panel.

[TopIcons Plus](https://extensions.gnome.org/extension/1031/topicons/): This extension moves legacy tray icons (bottom left of Gnome Shell) to the top panel. It is a fork from the original extension from ag with settings for icon opacity, saturation, padding, size and tray position, along with a few minor fixes and integration with the Skype integration extension.

[Darker overview](https://extensions.gnome.org/extension/1177/darker-overview/): Make overview background darker so even white text is readable on bright or colorful wallpapers. This also can remove the vignette. I set the darkness to 8, and disable the vignette.

Some useful additions are:

[Refresh wifi connections](https://extensions.gnome.org/extension/905/refresh-wifi-connections/): This extension adds a refresh button to the Wifi connection selection dialog to request for a network scan manually.

[Disconnect wifi](https://extensions.gnome.org/extension/904/disconnect-wifi/): Adds a Disconnect option for Wifi in status menu, when a network is connected. Shows a Reconnect option, after network is disconnected.

[Caffeine](https://extensions.gnome.org/extension/517/caffeine/): Disable the screensaver and auto suspend. Useful when giving a presentation, watching a movie or when you're staring too long at your code and the screen saver kicks in.

Theming is an essential part of user experience for my desktop environment. Both shell and GTK themes are provided by the excellent [Materia theme](https://github.com/nana-4/materia-theme). I clone the repository in a directory (for example in `~/workspace/themes`) with a `git clone https://github.com/nana-4/materia-theme.git` (you can use SSH if you have a GitHub account), and then from the `materia-theme` dir install the theme with `sudo ./install.sh`. With gnome-tweak-tool (Tweaks in the application menu), I chose the Materia-dark-compact variant, which provides a nice dark theme, and makes the widgets a bit more compact, so I can cram in more... stuff :)

The icons I use with this sleek theme, are the ones from the [Papirus project](https://github.com/PapirusDevelopmentTeam/papirus-icon-theme), which you can obtain rather easily. For example, on Ubuntu, add the PPA:

    sudo add-apt-repository ppa:papirus/papirus
    sudo apt-get update
    sudo apt-get install papirus-icon-theme


