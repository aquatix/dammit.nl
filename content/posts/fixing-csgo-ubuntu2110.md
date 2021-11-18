Title: Fixing CS:GO on Ubuntu 21.10
Started: 2021-11-18 10:36:51
Date: 2021-11-18 10:36:51
Slug: fixing-csgo-ubuntu2110
Location: Home
Authors: Michiel Scholten
Status: published
Category: howto
Tags: desktop, energy, gaming, howto, linux, ubuntu

Yesterday evening, my little gaming group came together online to play some Counter Strike: Global Offence (CS:GO), as a deviation from our regular battles in [OpenRA](https://www.openra.net/) (which is great fun by the way).

We played CS:GO before, but for some reason when I launched it from Steam now, it would show a black screen (or window when launched with the `-windowed` option) for some seconds, then crash to desktop. The output when run from a terminal (just launch `steam` there, it's easiest) was not particularly helpful and first sent me on a red herring chase that cost me way too much time, as I saw a bunch of mentions of messages like `from LD_PRELOAD cannot be preloaded (wrong ELF class: ELFCLASS32)` which means issues with 32-bit libraries. I thought that updating to Ubuntu 21.10 a while ago had hosed the 32-bit libraries needed to run games.

Turned out, that was just fine. Portal 2 ran fine too, which was a good sign, as it is also a native version on Linux, and basically using the same engine. So... that was odd. I had already tried switching to the Windows version by manually setting Compatibility to some Proton version, but that didn't help either.

I proceeded to uninstall the game and reinstall, which meant re-downloading about 13GB of data (while the others were having fun being killed by too many bots in our server). Of course I then stumbled upon mentions on [ProtonDB](https://www.protondb.com/app/730) that this was a problem for a lot of others too, so - er - yeah. Thankfully [there was a fix](https://www.protondb.com/app/730#3sdJcdGT5K):

```bash
# Go to the CS:GO dir in your steam library; this might be located somewhere else, check
# 'Local files' in the game's properties ('Browse')
cd ~/.steam/steamapps/common/Counter-Strike Global Offensive/bin
ln -s /usr/lib/x86_64-linux-gnu/libtcmalloc_minimal.so.4.5.9  libtcmalloc_minimal.so.0
# or:
cp /usr/lib/x86_64-linux-gnu/libtcmalloc_minimal.so.4.5.9  libtcmalloc_minimal.so.0
```

This will cause CS:GO to use the right tcmalloc library, which apparently was the problem. Presto, game time!

*N.B.:* I already was using the `-nojoy` launch option, as without that, CS:GO would not launch either (this let it ignore the joystick/controller stuff from Steam). Also of help might be the `-novid` launch option to skip some videos.
