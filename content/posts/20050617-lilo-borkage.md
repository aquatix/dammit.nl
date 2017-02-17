Title: LILO borkage
Date: 2005-06-17 11:43:02
Slug: 20050617-lilo-borkage
Location: Home
Authors: Michiel Scholten
Tags: olddammit

<p>OK, I managed to modify my kernel configuration without updating LILO [by forgetting to do a simple 'lilo' at the root prompt]. Result? An unbootable GNU/Linux installation. Go me. Thank Light I have always a copy of the <a href="/page/linux/aquamorph/">aquamorph livecd</a> laying around, so I went trying to update the bootrecord from that booted cd.</p>

<p>At first it wouldn't work, but then I remembered some things about an earlier rescue operation. Here's what you need to do:</p>

<p>Boot your <a href="/page/linux/aquamorph/">aquamorph</a>, <a href="http://morphix.org/">Morphix</a> or whatever livecd, do a 'sudo bash' in a terminal [or at least get yourself a root terminal] and then mount the partition of your linux install [in my case /mnt/hda5]. Edit the /etc/lilo.conf file to represent this modified path to the kernel image [use nano instead of vim if you want ;)]</p>

<pre>
mount /mnt/hda5
vim /mnt/hda5/etc/lilo.conf
 [change
  image=/boot/vmlinuz-2.6.10-kanotix-4
  to
  image=/mnt/hda5/boot/vmlinuz-2.6.10-kanotix-4
  or whatever kernel you are using]
lilo -C /mnt/hda5/etc/lilo.conf -i /mnt/hda5/boot/boot.b -m /mnt/hda5/boot/map -b /dev/hda
</pre>

<p>Reboot and boot your fixed installation. Don't forget to remove the "/mnt/hda5" again from the path to the kernel image in /etc/lilo.conf, otherwise you'll end up with a nonfunctional config file. Fetch yourself a beer.</p>