Title: Mounting and fixing a LUKS-encrypted Linux installation
Date: 2014-04-12 17:03:42
Slug: 20140412-mounting-and-fixing-a-luks-encrypted-linux-installation
Location: Home
Authors: Michiel Scholten
Tags: rant

Lately my work laptop has been acting up a bit after installation of a graphical driver went wonky. As I'm running a beta of
Ubuntu Gnome on it, I don't blame anything but the flux in which the packages exist for the moment, so I took it in stride
and went on to fix it.

The problem was that after unlocking my LUKS logical volume group (the group of 'partitions' on the SSD of the machine which
exist inside a container encrypted with LUKS), nothing happened. The boot screen stayed on the 'successfully unlocked' status
and stayed there. I couldn't even switch to a tty by pressing ctrl+alt+F2. So, after a bit of 'WTF', I fetched a USB drive with
the Ubuntu Gnome livecd still on it and booted from it.

Luckily, I could mount the encrypted disks without problems and check the logs what the problem was about. As I wanted to
run `apt` to update some packages, I needed to chroot into the installation on the disk so `apt` would understand that I did
not want to update the livecd itself.

To do so (and for example being able to run GRUB to fix your boot sector when someone like you or Windows destroyed it), follow the recipe:

Open a terminal and `sudo -i` to a root shell. Makes life a lot easier. Then

`# modprobe dm-crypt`

Next you need to decrypt the partition. I know that sda3 is my LVM partition so my command was

`# cryptsetup luksOpen /dev/sda5 sda5_crypt`

Where 'sda5_crypt' is in my case the name the volume has when running normally; you can use an arbitrary name for the decrypted
volume, but for maximum compatibility with the installation, try to use the one it uses itself. You should get back:

	Enter LUKS passphrase:
	key slot 0 unlocked.
	Command successful.

To verify, run

`# vgscan`

	Reading all physical volumes.  This may take a while...
	Found volume group "ubuntu-gnome-vg" using metadata type lvm2

Where `ubuntu-gnome-vg` is the name of my volume group.

`# vgchange -a y main`
`# lvscan`

	ACTIVE     '/dev/ubuntu-gnome-vg/root' [151.53 GiB] inherit
	ACTIVE     '/dev/ubuntu-gnome-vg/swap_1' [15.91 GiB] inherit

Yes, I have one big root partition. To be more orderly I should/could have created a /home (and maybe /usr) volume which you
can always resize later with lvm, but I kept it simple.

Now I have access to the partitions I need to mount in order to chroot into the install.

	# mkdir /media/linux
	# mount /dev/ubuntu-gnome-vg/root /media/linux
	# mount -o bind /proc /media/linux/proc
	# mount -o bind /dev /media/linux/dev
	# mount -o bind /dev/pts /media/linux/dev/pts
	# mount -o bind /sys /media/linux/sys

Now we can chroot into the existing install From there we can mount the /boot parition.

`chroot /media/linux /bin/bash`

Now I need to mount my boot parition which is on /dev/sda1. If you don't know where yours is located, try fdisk or `cfdisk /dev/sda`.

`mount /dev/sda1 /boot`

Now we can do things like an `apt-get update; apt-get dist-upgrade` to get up-to-date, and for example reinstalling GRUB:

`grub-install /dev/sda`

When you are done, press ctrl+d to exit the shells and shut down the livecd, powering off your machine. Take out the USB drive,
power on your machine and all should be better.

[Inspired by this article by Stephen Tanner](http://stephentanner.com/index.php/2011/05/restoring-grub-for-an-encrypted-lvm/)