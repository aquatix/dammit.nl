Title: Fixing sound in Firefox on cheap audiochips in Linux
Date: 2006-07-31 16:08:05
Slug: 20060731-fixing-sound-in-firefox-on-cheap-audiochips-in-linux
Location: Home
Authors: Michiel Scholten
Tags: olddammit

<p>OK, so you're already using the nice <a href="http://en.wikipedia.org/wiki/ALSA_%28Linux%29">ALSA</a> sound system on your Linux install, but when you're playing music etc you can't hear the sound of those YouTube movies? Edit /etc/firefox/firefoxrc and add/edit the FIREFOX_DSP setting to read "FIREFOX_DSP="aoss". Of course, you will need ALSA's OSS support too, so install alsa-oss and restart Firefox.</p>

<p>Enjoy!</p>