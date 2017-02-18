Title: No X, you know, means I don't want X
Date: 2009-03-09 11:10:41
Slug: 20090309-no-x-you-know-means-i-don-t-want-x
Location: Work
Authors: Michiel Scholten
Tags: rant

<pre>
apt-get dist-upgrade
Reading package lists... Done
Building dependency tree
Reading state information... Done
Calculating upgrade... Done
The following NEW packages will be installed
  cpp cpp-4.3 dbus fontconfig gconf2-common libatk1.0-0 libcairo2 libcups2 libdatrie0 libdbus-1-3 libdbus-glib-1-2 libdirectfb-1.0-0 libdrm2 libgconf2-4 libgl1-mesa-glx
  libglu1-mesa libgmp3c2 libgstreamer-plugins-base0.10-0 libgstreamer0.10-0 libgtk2.0-0 libgtk2.0-common libidl0 libjasper1 libmpfr1ldbl liborbit2 libpango1.0-0
  libpango1.0-common libpixman-1-0 libsysfs2 libthai-data libthai0 libts-0.0-0 libwxbase2.8-0 libwxgtk2.8-0 libxcb-render-util0 libxcb-render0 libxcomposite1 libxcursor1
  libxdamage1 libxfixes3 libxft2 libxi6 libxinerama1 libxrandr2 libxrender1 libxxf86vm1
The following packages will be upgraded:
  gnuplot-nox
1 upgraded, 46 newly installed, 0 to remove and 0 not upgraded.
Need to get 24.7MB of archives.
After this operation, 64.2MB of additional disk space will be used.
Do you want to continue [Y/n]? n
Abort.
</pre>

<p><a href="http://en.wikipedia.org/wiki/Advanced_Packaging_Tool">apt</a>, what exactly didn't you 'get' from the -nox part of gnuplot-nox? (It seems <a href="http://packages.debian.org/sid/groff">groff</a> is the culprit here btw)</p>