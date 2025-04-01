Title: Pretty Gnome
Started: 2016-02-24, 2017-04-26 16:17:00, 2017-06-03, 2018-11-25, 2018-11-26, 2019-02-26, 2019-08-06, 2025-03-30, 2025-03-31
Date: 2025-04-01 13:37:00
Slug: pretty-gnome
Authors: Michiel Scholten
Category: howto
Tags: linux, desktop, howto
Status: draft
Image: https://dammit.nl/images/content/20250331_gnomeshell_overview.png

[![GNOME Shell overview](https://dammit.nl/images/content/20250331_gnomeshell_overview.png)](https://dammit.nl/images/content/20250331_gnomeshell_overview.png)

This howto has been stewing for the greater part of a decade, and I finally came around to writing it as I was freshly installing Ubuntu 25.04 on my ThinkPad T480s hacktop. Most of the tweaks apply for Gnome 48 (and probably 47 still) on whatever distribution you like, but there are a few additional steps to decrustify Ubuntu.

To show you how far back this draft goes, the second version started like this:

> This little howto has been long in the making, as I wanted to do a write-up of how I themed and tweaked my Gnome (Shell) based desktops to my liking for quite a while. My desktop environments are based on Ubuntu, but this howto can be applied to any distribution and OS that runs Gnome Shell. The setup described here is tested on at least Gnome 3.28, 3.30 and 3.32 (latest Gnome release), so for example works on Ubuntu 18.04 LTS and 19.04.

Yeah.

The first version was from February 2016, before Ubuntu even switched (back) to Gnome 3 from Unity, after it ditched Gnome in its version 2 days.

So anyway!

On Ubuntu, I started with installing the 'vanilla' version of Gnome Shell by installing the `ubuntu-gnome-desktop` package and choosing the `GNOME` or `GNOME on Xorg` session in the GDM login screen after selecting my user. Otherwise, you get the Ubuntu tweaked version of Gnome Shell, which might suite your tastes, but has the bar on the left side and some other tweaks I do not necessarily want (and previously some garish orange-based colours). I like orange, but the changes that `ubuntu-gnome-desktop` does to the bootscreen and the login screens are welcome, and it gives a bare-bones Gnome Shell to work with.

Speaking of Ubuntu, first we now really have to...


## Nuke snap from orbit

I have feelings for Snap. They consist of me liking `.deb` files and even Flatpak a lot better, and not liking the weird (resource) issues that the Snap daemon and its packages tend to bring to the table. Yes, things have grown better; no, I'm still not going to use it.

Assuming that you want to keep Firefox (I still love my little fox), follow the instructions on [the Mozilla howto](https://support.mozilla.org/en-US/kb/install-firefox-linux#w_install-firefox-deb-package-for-debian-based-distributions) to prepare using the 'real' `.deb` version, but do not install Firefox from there just yet.

After that, close Firefox, then `sudo apt remove firefox* thunderbird*` to remove the snap-based Deb packages from Ubuntu.

Now it's time to nuke snap:

```bash
# Get a list of everything that's installed
snap list
Name                       Version          Rev    Tracking         Publisher   Notes
bare                       1.0              5      latest/stable    canonical✓  base
core22                     20250210         1802   latest/stable    canonical✓  base
desktop-security-center    0+git.a2963a9    51     1/stable/…       canonical✓  -
firefox                    136.0.3-1        5947   latest/stable/…  mozilla✓    -
firmware-updater           0+git.22198be    167    1/stable/…       canonical✓  -
gnome-42-2204              0+git.38ea591    202    latest/stable/…  canonical✓  -
gtk-common-themes          0.1-81-g442e511  1535   latest/stable/…  canonical✓  -
prompting-client           0+git.1756bbf    87     1/stable/…       canonical✓  -
snap-store                 0+git.7a3a49a6   1248   2/stable/…       canonical✓  -
snapd                      2.67.1           23771  latest/stable    canonical✓  snapd
snapd-desktop-integration  0.9              253    latest/stable/…  canonical✓  -
thunderbird                128.8.1esr-1     684    latest/stable/…  canonical✓  -

# One by one remove the snap packages
sudo snap remove firefox thunderbird desktop-security-center firmware-updater
sudo snap remove prompting-client snapd-desktop-integration gtk-common-themes gnome-42-2204
sudo snap remove snap-store bare
sudo snap remove core22 snapd
sudo snap remove core22
sudo snap remove snapd

# Now remove the snapd package
sudo apt remove --purge snapd
```

Now we got rid of that... thing, we can install the Deb package for Firefox, straight from the Mozilla repository we configured at the start.

```bash
sudo apt update
sudo apt install firefox
```


## Making it pretty and pretty useful

To be able to get our fingers more dirty and being able to reach more buttons to push and knobs to fiddle, some useful applications have to be installed first.

```bash
# Gnome Tweaks, to set extra configuration for fonts, theming and other things
sudo apt install gnome-tweaks
# Extensions application
sudo apt install gnome-shell-extension-manager
# Browser connector to be able to use the Gnome Extensions website
sudo apt install gnome-browser-connector
```

Previously, I had some extensions to declutter the environment, but Gnome has been taking care of that itself and is really usable already without additions; I think it cleaned up quite nicely in recent times. Most of the extensions I will list here and which I use will actually add functionality, but in such a way that it keeps out of your way while still providing extra information or convenience.

Let's start with the [User Themes](https://extensions.gnome.org/extension/19/user-themes/) extension, as that enables custom themes for Gnome Shell, about which I'll speak later on.

Now launch the Extension Manager application or navigate to [the Gnome Extension site](https://extensions.gnome.org/). There you find a lot of additions and tweaks for Gnome Shell to be installed with a single click.

My suggestions:

- [AppIndicator and KStatusNotifierItem Support](https://extensions.gnome.org/extension/615/appindicator-support/) - statusbar icons for certain applications
- [Astra Monitor](https://extensions.gnome.org/extension/6682/astra-monitor/) - useful graphs showing how busy your device is (needs `sudo apt install nethogs iotop gir1.2-gtop-2.0` to be more effective)
- [Bluetooth Battery Meter](https://extensions.gnome.org/extension/6670/bluetooth-battery-meter/) - show battery status for your various devices straight in the Bluetooth panel, or even the top panel if you want; also for non-Bluetooth devices like mice, through Upower
  ![Battery indicator mouse](https://dammit.nl/images/content/20250401_battery_indicator.png)
- [Blur my Shell](https://extensions.gnome.org/extension/3193/blur-my-shell/) (this by default blurs the top bar. If you like that, do not install the Transparent Top Bar extension; otherwise config to not blur the top panel and use that extension)
- [Caffeine](https://extensions.gnome.org/extension/517/caffeine/) - (automatically) keep the screen from going blank/off
- [GSConnect](https://extensions.gnome.org/extension/1319/gsconnect/) - super handy connector with your mobile phone, showing notifications, sending files to and fro, auto pausing music on incoming calls, showing battery status and lots more
- [Just Perfection](https://extensions.gnome.org/extension/3843/just-perfection/) - tweak Gnome Shell
- [No overview at start-up](https://extensions.gnome.org/extension/4099/no-overview/) - do not stay on zoomed-out 'overview' mode when you log into Gnome, but show the desktop
- [OpenWeather Refined](https://extensions.gnome.org/extension/6655/openweather/) - weather, of course
- [Quick Settings Audio Panel](https://extensions.gnome.org/extension/5940/quick-settings-audio-panel/) - creates a new panel (or puts the bars in the existing panel) containing volumes and media control in the quick settings
- [Rounded Window Corners Reborn](https://extensions.gnome.org/extension/7048/rounded-window-corners-reborn/) - adjustable border radius for your windows, to add that playful effect
- [Tiling Shell](https://extensions.gnome.org/extension/7065/tiling-shell/) - very well executed tiling window system with both great keyboard and mouse support, definable layouts and other handy quality-of-life things
- [Transparent Top Bar (Adjustable transparency](https://extensions.gnome.org/extension/3960/transparent-top-bar-adjustable-transparency/) - use to make the top bar completely transparent, or slightly less so; also it can become opace when you maximise a window
- [User Themes](https://extensions.gnome.org/extension/19/user-themes/) - to be able to theme the shell portion of Gnome Shell

**Bonus:** [Day Progress](https://extensions.gnome.org/extension/7042/day-progress/) - configure this to show a bar from 09:00-17:00 on your work laptop ;)


!!! hint

    Now is a good time to log out and log back in again, to make sure all extensions apply correctly. After that, we can do some tweaking in their settings.


### Adjusting the default settings of the extensions

Open Extensions, or [the Gnome installed Extensions page](https://extensions.gnome.org/local/)

Astra Monitor:

- Processors > Header: History Graph, Width: 50
- Memory > Header: History Graph, Show: yes, Width: 50; Realtime Bar, Show: no
- Network > Headers: IO, IO History Graph Width: 50

Blur my Shell:

- Panel: disable if you like to use the Transparent Top Bar extension instead

Day Progress:

- Time Elapsed: enable
- Start time: 09:00
- Reset time: 17:00 ;)

GSConnect:

- Whatever you like to enable or disable when using it with your phone (use the excellent KDE Connect app)

Just Perfection:

- Visibility: disable elements you don't want to see (myself I keep everything default)
- Behavior: enable 'Window Demands Attention Focus' to have focus shift to the relevant window when something happens, for example when you click a link in an application, Gnome will switch to your browser. If you use the Element app, you really want to disable its Notifications > 'Enable audible notifications for this session' setting
- Customize: I use the defaults, but you can tinker around with positions of elements and such here

OpenWeather Refined:

- Adjust the Units to your locale/preferences
- Choose a Weather Provider (I use OpenWeather myself, with a free custom API key)
- In Layout, choose the position in the panel; this can be with the clock in the middle of the bar, or for example at the right
- Forecast: Keep Forecast Expanded, to be able to see the forecast immediately once you click on the temperature in the top bar

Quick Settings Audio Panel:

- Where the panel should be: 'In the main panel'
- Panel position: 'Bottom'

Tiling Shell:

- Inner gaps: 4
- Outer gaps: 4
- Whatever else you like to customise

Transparent Top Bar (Adjustable transparency):

- (If you don't use the blur from Blur My Shell on the top panel)
- Top bar opacity: 25% (or 0 for full transparency)
- Opaque top bar when a window touches it: keep enabled when you want it to have a solid colour on touching windows, disable if you like it to be more transparent

User Themes:

- Orchis-Orange-Dark


... wait, where does that theme come from? Oh right, let's get that [from its repository](https://github.com/vinceliuice/Orchis-theme), where the excellent vinceliuice maintains it (be sure to check out their other themes too, Vince is very talented).

```bash
# Go to a suitable directory
cd ~/workspace/gnome-shell

git clone https://github.com/vinceliuice/Orchis-theme.git

cd Orchis-theme

# Install the dark and light variants with orange details, compact versions, and link (use) the light variant for applications
./install.sh -c dark -t orange --tweaks compact; ./install.sh -c standard -t orange --tweaks compact -l

# Of course, there's a lot to try out here; check ./install.sh to see what the possibilities are and choose your favourite colour and other tweaks
```

Open the Tweaks application, go to Appearance and choose 'Orchis-Orange-Dark' for Shell (probably already set through the User Themes config ;) ), and 'Orchis-Orange' for Legacy Applications (substitute your own choices here).

Ah yes, icons, those can be themed too! That brings us to my long-time favourite.


## Papirus icon theme

This is a very [comprehensive and well-designed icon theme](https://github.com/PapirusDevelopmentTeam/papirus-icon-theme) that is not too flat, has distinctive figures for the icons and just looks pleasant. There's an easy way of installing it on Ubuntu-based/-like distributions, through the [Papirus PPA](https://launchpad.net/~papirus/+archive/ubuntu/papirus):

```bash
sudo add-apt-repository ppa:papirus/papirus
sudo apt update
sudo apt install papirus-icon-theme
```

Close the Tweaks application window and open it again to have the new theme option show up under Appearance. At Icons, choose Papirus-Dark.


## Terminal

Yes, we're going deeper. The terminal is in my top 3 most used applications, and I want it to look the part.

I use a Gnome Terminal colour theme by [Gogh](https://github.com/Mayccoll/Gogh). Gogh [supports a lot of colour schemes](https://gogh-co.github.io/Gogh/), so choose one to your liking. I found Argonaut to match nicely with the overall theme, and providing enough contrast to be easily readable while also using pleasant colours. Gogh supports multiple terminal emulators, so you're not stuck with Gnome Terminal.

```bash
# Prepare so Gogh can do its thing
sudo apt-get install dconf-cli uuid-runtime

# Make sure you are not in a tmux session or something, but 'directly' in Gnome Terminal or another support terminal
# Use the Gogh theme manager/downloader interactively:
bash -c "$(wget -qO- https://git.io/vQgMr)"
# (yes, this executes code straight from the web...)

# Choose option 10, Argonaut, or another pretty set of colours that suits your fashion
```

Right click the terminal, click Preferences. Under General, uncheck 'Enable the menu accelerator key (F10 by default)' so we can use `mc` and other applications correctly.

There should be an Argonaut entry under the Profiles in the left bar. Select it, click its little arrow button and make it the default. In the Text tab right next to it, you can make the default size of the terminal window a bit bigger by increasing the columns and rows settings (I use 120 and 40 for example).


!!! warning

    The rest of the configuration assumes the Fish shell, but most of it also works under Bash or zsh, whatever rows your boat.


A very versatile (and potentially pretty) prompt tool (yes, that's a thing) is the [Starship prompt](https://starship.rs/):

```bash
# Install and enable
curl -sS https://starship.rs/install.sh | sh

# Sigh, another script that you run straight from the tubes
```

You can use my starship config by [clone my dotfiles](https://github.com/aquatix/dotfiles) or [just getting the raw version of the toml config file](https://github.com/aquatix/dotfiles/blob/master/.config/starship.toml) and putting it in your `~/.config` directory.


![Fish Starship prompt](https://dammit.nl/images/content/20250401_fish_starship.png)

_My custom Starship prompt, with Git, virtualenv support (and more)._


The [tmux terminal multiplexer](https://github.com/tmux/tmux/wiki) is better than `screen`, and provides a way of tiling in your terminal, and/or having multiple windows inside of it. Apart from that, it's great for being able to detach from that session and continue later - especially handy when run on a remote computer.

[My tmux config](https://github.com/aquatix/dotfiles/blob/master/.tmux.conf) has not changed for more than six years, and serves me every day in various forms and ways.


![tmuxinator config for dammIT](https://dammit.nl/images/content/20250401_tmuxinator_dammit.png)

_tmux session started through tmuxinator, with setup for this weblog. Mind the bar at the bottom_


Other useful tooling for (automating) CLI work are [direnv](https://direnv.net/) and [tmuxinator](https://github.com/tmuxinator/tmuxinator). `tmuxinator` helps automatically configuring `tmux` sessions, while `direnv` can load and unload environment variables depending on the current directory, so for example automatically enabling a Node and Python venv environment when you `cd` into a directory.

Installing them is pretty easy:

```bash
sudo apt install direnv tmuxinator
```

An example tmuxinator config that sets up a little development/writing environment for my weblog:

```yaml
# ~/.tmuxinator/dammit.yml

name: dammit
root: ~/workspace/projects/github/dammit.nl

# Runs before everything. Use it to start daemons etc.
on_project_start: git pull

# Runs in each window and pane before window/pane specific commands. Useful for setting up interpreter versions.
pre_window: vf activate pelican

# Pass command line options to tmux. Useful for specifying a different tmux.conf.
# tmux_options: -f ~/.tmux.mac.conf
tmux_options: -2

# Change the command to call tmux.  This can be used by derivatives/wrappers like byobu.
# tmux_command: byobu

windows:
  - server: make devserver
  - dammit:
  - theme:
      root: ~/workspace/projects/github/pelican-alchemy
```

This creates a `tmux` session with three windows, one with a running devserver, one with a prompt in the working dir ready to add a post, or edit something with for example `vim`, and one with a prompt in the theme directory.

Split view:

```yaml
windows:
  - notes:
      #layout: layout af31,363x97,0,0{182x97,0,0,0,180x97,183,0[180x48,183,0,1,180x48,183,49,4]}
      layout: main-vertical
      panes:
        - sudo -i
        - opennotes
  - example:
      root: ~/workspace/projects/private/example-project
      panes:
        - vim tryout.py
        - vf activate somethingelse; nvm use node

# The latter window splits into two panes, opens a Python file in the one,
# and activates a different venv and node env in the second
```


## Python terminal tooling

For Python virtualenvs, [Virtualfish](https://github.com/justinmayer/virtualfish) is a useful helper, with functions like `vf new whatever_venv_you_want` for creating, `vf activate that_venv` for activating, and `vf upgrade an_old_venv` for updating an existing virtualenv to a new Python version.

VirtualFish itself is a Python package, and to be able to install this 'system wide', or at least for your user, these days you have to specify `--break-system-packages` to convince `pip` you really want this package installed outside of a virtualenv.

```bash
sudo apt install python3-pip
# Install virtualfish outside of a virtualenv
python3 -m pip install --break-system-packages --user virtualfish
vf install
# Reload fish shell to enable in current terminal:
exec fish
```


If you are familiar with modern Python development, [uv](https://github.com/astral-sh/uv/) will likely be on your radar. I like having it available outside of virtualenvs (so I can manage themselves), so I install it in my user home:

```bash
curl -LsSf https://astral.sh/uv/install.sh | sh

# Yet another script that you run straight from the tubes
```


## Alternative universal applications

As we got rid of Snap, and not all applications are provided as a `.deb` package from a (Ubuntu or PPA) repository, we can use the universal AppImage and Flatpak formats instead.


### AppImage applications

Running the [PlexAmp AppImage](https://www.plex.tv/media-server-downloads/?cat=computer&plat=linux#plex-plexamp) or the excellent [Open Red Alert](https://www.openra.net/) or its [Combined Arms mod](https://github.com/Inq8/CAmod) can give you the following error:

```
dlopen(): error loading libfuse.so.2

AppImages require FUSE to run.
```

That's because AppImage needs FUSE, and version 2 to boot (version 3 is proably already installed by default). Fix it by:

```bash
sudo apt install libfuse2
```


### Flatpak applications

[Flathub has excellent documentation for setting up](https://flathub.org/setup), but I'll summarise here:

```bash
# Install flatpak itself
sudo apt install flatpak

# Install GNOME Software Flatpak plugin
sudo apt install gnome-software-plugin-flatpak

# Add the Flathub repository
# Flathub is the best place to get Flatpak apps. To enable it, run:
flatpak remote-add --if-not-exists flathub https://dl.flathub.org/repo/flathub.flatpakrepo
```

A restart will ensure everything falls in place.

Afterwards, why not try the Gnome native Matrix client 'Fractal'?

```bash
flatpak install fractal
# Choose the option with app/org.gnome.Fractal/x86_64/stable
# You can also install this directly by doing:
flatpak install org.gnome.Fractal
```


## Wrapping up

This scope-creeped a bit from tweaking GNOME to 'how to set up my laptop/workstation', but I hope it will provide some extra inspiration for your own environment.
