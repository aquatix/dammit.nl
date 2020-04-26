Title: projectM on Ubuntu 19.10
Started: 2020-04-25 14:41:37
Date: 2020-04-25 14:41:37
Slug: projectm-ubuntu-1910
Location: Home
Authors: Michiel Scholten
Category: howto
Tags: desktop, howto, music, tech
Image: 
Status: draft

apt install libtool pkg-config libglm-dev qt5-default qtdeclarative5-dev libgles2-mesa-dev libpulse-dev


```
autoreconf --install    # only needed if this is a git clone
./configure --enable-pulseaudio --enable-qt --enable-gles LIBS="-lQt5Gui -lQt5OpenGL"
```

This will list the things that will be enabled in this build. Make sure both Qt and Pulseaudio have a `yes` behind them, like here:

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

Now do:

```
make
sudo make install
```

The first command will take a while, the second will take care of installing the binaries, libraries and all the plugins, and will be done a tad faster.

You can now start projectM by launching `projectM-pulseaudio`. Right click the window that appears and fiddle with the settings as you please. Play some music and ensure the right Pulseaudio output is selected. Enjoy!
