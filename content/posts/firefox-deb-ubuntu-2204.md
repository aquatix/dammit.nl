Title: Installing Firefox as a (real) .deb in Ubuntu 22.04
Started: 2022-09-18 13:56:28
Date: 2022-09-18 13:56:28
Slug: firefox-deb-ubuntu-2204
Location: Home
Authors: Michiel Scholten
Status: published
Category: howto
Tags: desktop, linux, opensource, tech, ubuntu

Canonical has a crush on `snap`. I don't. In Ubuntu 22.04 they replaced the native Firefox package with a snap package, making it slow and limited. It doesn't have to be that way.

Mozilla's Firefox team has their own [PPA for Firefox](https://launchpad.net/~mozillateam/+archive/ubuntu/ppa). As they use the same package name as the snap-based one, you'll need to both remove the latter, and configure the apt package manager to keep using the PPA-provided version.

First, remove the Ubuntu snap-based Firefox:

```
sudo apt purge firefox
sudo snap remove --purge firefox
```

Add the Mozilla PPA:

```
sudo add-apt-repository ppa:mozillateam/ppa
```

Add a pin file to the apt configuration so it keeps using the 'real' build of Firefox provided by the Mozilla team instead of re-installing the snap.

To do this, create a file `/etc/apt/preferences.d/mozillateam.pref` and put the following in there:

```
Package: *
Pin: release o=LP-PPA-mozillateam
Pin-Priority: 1001
```

(You can do this by for example using the `nano` editor: `sudo nano /etc/apt/preferences.d/mozillateam.pref`), but you are of course free to use vim like me ^_^ )

Now you can install the right Firefox package:

```
sudo apt install firefox
```

Note that this PPA does not provide localised (translated) versions, so installing for example `firefox-locale-nl` will install the snap again. If you prefer a translation or another edition of Firefox, you can use the alternative install method discussed next.


## Or use the version provided by Mozilla.org

Alternatively, you can use [the tarball from mozilla.org](https://www.mozilla.org/en-GB/firefox/all/#product-desktop-release) and copy its contents to for example `/usr/local/bin/firefox/`

For the sake of fun, lets say you want to run the Nightly version of Firefox. I've been daily driving this build for over 5 year now, and apart from a few minor hiccups here and there, it actually is serving me pretty well.

From the above download link, choose the [Firefox Nightly version](https://www.mozilla.org/en-GB/firefox/all/#product-desktop-nightly) that's right for your machine and preferred language and download this `.tar.bz2` file, say to your `~/Downloads` directory.

Now, move that file to `/usr/local/bin`:

```
sudo mv ~/Downloads/firefox-106.0a1.en-GB.linux-x86_64.tar.bz2 /usr/local/bin
```

(make sure the file name is for the version you downloaded, it's `106.0a1` today, but new versions keep magically appearing of course :) ).

Next, unpack this tarball (which is similar to a zip):

```
cd /usr/local/bin
sudo tar xf firefox-VERSION.tar.bz2
```

This will create a `firefox` directory with all the files inside. Make sure this directory belongs to your Linux user: `sudo chown -R YOURUSERNAME. firefox`, so for example `sudo chown -R aquatix. firefox` while you are inside the `/usr/local/bin` directory as done above with the `cd` command. Now, Firefox will be able to write its own files, which enables the auto-updater to function like it should.

Lastly, create a .desktop file that causes Nightly to show up in your launcher. `nano ~/.local/share/applications/firefox-nightly.desktop`:

```
[Desktop Entry]
Version=1.0
Name=Firefox Nightly
Name[fr]=Firefox Nightly
Comment=Browse the World Wide Web
Comment[fr]=Naviguer sur le Web
GenericName=Web Browser
GenericName[fr]=Navigateur Web
Keywords=Internet;WWW;Browser;Web;Explorer
Keywords[fr]=Internet;WWW;Browser;Web;Explorer;Fureteur;Surfer;Navigateur
Type=Application
#Exec=/usr/local/bin/firefox/firefox-bin -P MyNightlyProfile %u
#Exec=/usr/local/bin/firefox/firefox-bin %u
Exec=env MOZ_USE_XINPUT2=1 /usr/local/bin/firefox/firefox-bin %u
#Exec=env MOZ_USE_XINPUT2=1 MOZ_X11_EGL=1 /usr/local/bin/firefox/firefox-bin %u
Terminal=false
X-MultipleArgs=false
#Icon=/usr/local/bin/firefox/browser/chrome/icons/default/default128.png
Icon=/usr/share/icons/Papirus/64x64/apps/firefox-nightly.svg
Categories=GNOME;GTK;Network;WebBrowser;
Actions=ProfileManager;new-window;new-private-window;
MimeType=text/html;text/xml;application/xhtml+xml;application/xml;application/rss+xml;application/rdf+xml;image/gif;image/jpeg;image/png;x-scheme-handler/http;x-scheme-handler/https;x-scheme-handler/ftp;x-scheme-handler/chrome;video/webm;application/x-xpinstall;
StartupNotify=true
StartupWMClass=Nightly

[Desktop Action ProfileManager]
Name=Profile Manager
Name[fr]=Gestionnaire de profil
Exec=/usr/local/bin/firefox/firefox -P

[Desktop Action new-window]
Name=New window
Name[fr]=Nouvelle fenêtre
Exec=/usr/local/bin/firefox/firefox -new-window -P MyNightlyProfile

[Desktop Action new-private-window]
Name=New private window
Name[fr]=Nouvelle fenêtre privée
Exec=/usr/local/bin/firefox/firefox -private-window -P MyNightlyProfile
```

There are some added goodies in the above .desktop file, notably the Papirus icon theme icon (the `Icon=` line) and the few alternative `Exec=` lines. The one that is actually active (without the # in front) sets `MOZ_USE_XINPUT2=1` which enables touch input in Firefox, handy when your laptop (or 2-in-1 or tablet if you are lucky) has a touch screen.

The alternative with the `-P MyNightlyProfile` is an example to let you use a different profile directory for this Nightly edition of Firefox, so you can keep using regular Firefox and Nightly next to each other without having to worry that one will mess up the other's profile. Replace `MyNightlyProfile` with another name if you like, it's the directory name inside `~/.mozilla/firefox` that contains the settings, history, addons and such.
