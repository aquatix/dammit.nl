Title: Upgrading to kanotix' 2.6.13
Date: 2005-08-20 16:34:06
Slug: 20050820-upgrading-to-kanotix-2-6-13
Location: Home
Authors: Michiel Scholten

<p>While studying for some upcoming re-examinations, I installed <a href="http://kanotix.com/">Kanotix'</a> <a href="http://kanotix.com/files/kernel/">linux kernel 2.6.13</a> on my laptop, and removed Lilo in favour of Grub. The kernel was already running fine at my desktop, but laptops are, well, tricky. At first my Centrino based wifi card wouldn't work [<a href="http://ipw2200.sourceforge.net/">ipw2200 chipset</a>]. Turned out I needed to download the latest firmware from <a href="http://ipw2200.sourceforge.net/">the module's website</a> and unpack it to /usr/lib/hotplug/firmware/ . Besides that, I needed both the ipw2200 .deb and the ieee80211 one from the Kanotix driver package.</p>

<p>So, now I could upgrade the ATI Radeon driver [was getting a tad dated], for which apparantly the kernel source where still needed [grab the install-kernel-source-vanilla.sh from <a href="http://kanotix.com/files/">the script page</a>, along with the install-radeon-debian.sh or install-nvidia-debian.sh script]. Downloaded the kernel sources through that nice script [needed to comment out the untarring of an old patch, adm8211, otherwise the script would fail], then installed the fglrx driver through install-radeon-debian.sh. Logged into X again and ran glxgears, the default benchmark.</p>

<p>My mouth felt open. Instead of the 1410 frames per second I first got with my Mobility Radeon 9700 featuring 64MiB of RAM, I now get 2210 frames per second! Talking about better drivers :) /me is happy.</p>

<p>OK, back to studying.</p>