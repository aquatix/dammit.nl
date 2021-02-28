Title: projectM on Ubuntu
Started: 2020-04-25 14:41:37, 20200427 10:07:00
Date: 2020-04-25 14:41:37
Slug: projectm-ubuntu
Location: Home
Authors: Michiel Scholten
Category: howto
Tags: desktop, howto, linux, music, tech, ubuntu
Image: https://shuttereye.org/images/7d/7d6c6c3e91998d1c_2000-2000.jpg
Status: published

![projectM on external monitor next to laptop](https://shuttereye.org/images/7d/7d6c6c3e91998d1c_2000-2000.jpg)

Lately, I was thinking back to the time when I had my 15" CRT monitor (and later my whopping 19" flat CRT) tuned to the beats that Winamp was playing for me. It was a famous plugin called [Milkdrop](https://en.wikipedia.org/wiki/MilkDrop), and it provided nicely psychedelic looking visuals based on the audio and beats that Winamp was playing at that moment. I often had it just running during music playback while doing homework, reading or otherwise just chilling in my room.

I knew about [projectM](https://github.com/projectM-visualizer/projectm), which is an opensource re-implementation of all of this, with support for the original presets and visualisations. It both provides libraries to include in a music application, as some stand-alone binaries that plug into PulseAudio or Jack. The fun part of the latter is that you can use whatever audio source you want (including Youtube and such), run projectM and have it all work seamlessly together. Count me in!

After some digging around, I came to the conclusion that pre-built binaries in Debian and Ubuntu were ancient, and basically only Arch had up-to-date stuff. No worries, lets build from source. Oh, that has a few gotcha's, as the various [howto](https://livingthelinuxlifestyle.wordpress.com/2019/06/03/how-to-install-projectm-audio-visualizations/)'s I found online were already outdated, or tried to do too much (I do not need Jack integration, PulseAudio will suffice).

I successfully built and used the visualisations on Ubuntu 19.10 and the new 20.04, with the same steps.

So here goes:

```
# Install the packages that are needed for building; Qt5 for the GUI, PulseAudio as the audio server.
sudo apt install libtool pkg-config libglm-dev qt5-default qtdeclarative5-dev libgles2-mesa-dev libpulse-dev
```

Then clone [the project](https://github.com/projectM-visualizer/projectm) or [download the latest release](https://github.com/projectM-visualizer/projectm/releases), and `cd` into the directory. From there, do:

```
autoreconf --install    # only needed if this is a git clone
./configure --enable-pulseaudio --enable-qt --enable-gles LIBS="-lQt5Gui -lQt5OpenGL"
```

This will list the things that will be enabled in this build. Make sure both Qt and PulseAudio have a `yes` behind them, like here:

```
Applications:
=====

libprojectM:            yes
Threading:              yes
SDL:                    no
Qt:                     yes
Pulseaudio:             yes
Jack:                   no
OpenGLES:               yes
Emscripten:             no
llvm:                   no
Preset subdirs:         no
```

This means the [Qt](https://www.qt.io/) frontend will be built, and Pulseaudio support will be included.

Now do:

```
make
sudo make install
```

The first command will take a while, the second will take care of installing the binaries, libraries and all the plugins, and will be done a tad faster. You might see some warnings during the `make`, especially in the Qt code, but as long as it's just warnings, you will be fine.

You can now start projectM by launching `projectM-pulseaudio`. Right click the window that appears and fiddle with the settings as you please. Play some music and ensure the right Pulseaudio output is selected. Enjoy!

PS: if you get a message about the presets not being found in `/usr/share/projectM/presets`, close projectM, open `~/.projectM/config.inp` in a text editor and change the `Preset Path` to `/usr/local/share/projectM/presets`.
