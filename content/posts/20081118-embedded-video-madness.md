Title: (Embedded) Video Madness
Date: 2008-11-18 00:15:03
Slug: 20081118-embedded-video-madness
Location: Home
Authors: Michiel Scholten
Tags: olddammit

<p>I just spent an evening debugging the girlfriend's laptop as it somehow flat-out rejected to play video in Totem (ever since upgrading her xubuntu install from 8.04 to 8.10). Totem has a convenient browser plugin for Firefox, so this is kind of a problem if I don't want her booting to windows just to see some streaming video of TV series reruns. Thankfully, just before giving up, <a href="https://bugs.launchpad.net/ubuntu/+source/totem/+bug/262494">I found this Ubuntu bugreport</a> talking about the same issue. Turned out, you just need to install a bunch of gvfs packages (virtual file system stuff, providing GIO, which Totem needs to look up both the url and the codecs it turned out). I installed:</p>

<ul>
<li>gvfs</li>
<li>gvfs-backends</li>
<li>gvfs-bin</li>
<li>gvfs-fuse</li>
<li>libgvfscommon0</li>
</ul>

<p>... and everything was back to normal again. Stupid !@#$ :)</p>