Title: How to change the looks of Ubuntu 10.04's GDM
Date: 2010-04-30 14:01:31
Slug: 20100430-how-to-change-the-looks-of-ubuntu-10-04-s-gdm
Location: Home
Authors: Michiel Scholten
Category: howto
Tags: howto, opensource, desktop, linux

<p>Ubuntu's GDM still does not have a settings window where you can change looks to your liking. However, there are some tricks to still be able to do just that.</p>

<p>First, open a terminal and type the following command:</p>

<pre>sudo cp /usr/share/applications/gnome-appearance-properties.desktop /usr/share/gdm/autostart/LoginWindow</pre>

<p>You may also want to do the same with <code>display-properties.desktop</code> for setting the resolution of your screen and <code>gconf-editor.desktop</code> to change <code>apps &gt; metacity &gt; general &gt; button_layout</code> to something like "/apps/metacity/general/button_layout".</p>

<p>Then logout, and you'll see an Appearance window pop up (and the other windows if you have copied those .desktop files too). Change it to how you prefer it, then close it and login as usual.</p>

<p>Now, to prevent those windows from appearing every time you get to the login screen, remove the .desktop files again:</p>

<pre>sudo unlink /usr/share/gdm/autostart/LoginWindow/gnome-appearance-properties.desktop</pre>

<p>And repeat for the other one or two, if you used them:</p>

<pre>sudo unlink /usr/share/gdm/autostart/LoginWindow/display-properties.desktop
sudo unlink /usr/share/gdm/autostart/LoginWindow/gconf-editor.desktop
</pre>

<p>Done!</p>

<p>[Based on <a href="http://www.ubuntugeek.com/how-do-you-change-the-boot-splash-screen-image-for-10-04-lucid-lynx.html">this how-to</a>]</p>
