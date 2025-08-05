Title: Übersimpel containers
Started: 2025-03-04 21:09:40
Date: 2025-03-04 22:41:45
Slug: ubersimpel-containers
Location: Home
Authors: Michiel Scholten
Status: published
Category: howto
Tags: dev, howto, linux, opensource, debian, ubuntu
Image: https://shuttereye.org/images/50/50624f55a9af4b4b_2000-2000.jpg

Shall I tell you something nifty?

You know you can create and run containers really easily on any Linux machine, no Docker, LXC or Kubernetes (gasp!) needed?

[![Frozen leaves inside ice](https://shuttereye.org/images/50/50624f55a9af4b4b_2000-2000.jpg)](https://shuttereye.org/photolog/PXL_20250218_074550970.jpg/view/)
*Frozen leaves inside ice*

Maybe you have seen the term `chroot` before but are not sure what it is, or maybe you are and are now - hopefully - nodding along. Point is, chroot's are basically some kind of simple jails in which you can run code that has no notion of the filesystem world outside it. The essence of a container.

The term 'chroot' comes from 'change root', as a command to change the apparent root directory for the current running process and its children. It [has been around since 1979](https://en.wikipedia.org/wiki/Chroot#History) and is pretty useful in various cases. These range from limiting (s)ftp users to a certain directory tree, to installing a completely separate Operating Sytem inside a directory and running it, or programs inside it.

The latter is what I would like to talk about here. Mind you that jailbreaking has been a thing since 1999, so it might not be suited for running everything you found on the web; please do some due diligence before deciding whether using a `chroot` is the right tool. Anyway, on to some examples.

Recently, I needed so VPN into some pretty ancient Debian machine. It was using OpenVPN to give access to its services, but of course it being ancient, it relied on some ciphers and crypto that since has been disabled from use in modern versions of the client. Thankfully, Debian 11 (oldstable as of this writing) still has a client version that - with some config tweaks - is able to connect, whereas my laptop was not able to any more.

As I did not want to install a virtual machine with Debian 11 and then having to use the services from inside there or having to tunnel them out of it, I used a nifty tool called `debootstrap` which is installable in all Debian-based distro's, including Ubuntu and such. It provides an easy way to create a `chroot jail` with whatever Debian-based distro you want inside it.

```bash
sudo debootstrap --include=systemd,dbus oldstable /srv/debian http://deb.debian.org/debian/
```

This creates an 'oldstable' installation inside the `/srv/debian` directory. Using `sudo chroot /srv/debian bash` gives me a root shell inside it, from which I installed openvpn with a simple `apt install openvpn`. You can do whatever you like in there, just like in a VM or container. Also, of course you do not need to be chrooted inside it to do stuff; you can copy files inside it however you want, as it is just a bunch of directories itself. That is how I copied my keys, certificates and openvpn config file in there, in a subdirectory of root's homedir.

Then, to establish an OpenVPN connection, I created a little script called `chroot_debian_connect.sh` with this content:

```bash
#!/bin/bash
if [ "$EUID" -ne 0 ]
    then echo "Please run as root"
    exit
fi

echo
echo "== mounting ======"
echo
mount -t proc proc /srv/debian/proc
mount -t sysfs sys /srv/debian/sys
mount --rbind /dev/ /srv/debian/dev/

echo
echo "== starting openvpn ======"
echo
chroot /srv/debian bash -c "cd /root/workspace && /usr/sbin/openvpn --config myconfig.ovpn"

# Cleanup:
echo
echo "== unmounting ======"
echo
umount -R /srv/debian/dev
umount /srv/debian/sys
umount /srv/debian/proc

echo
echo "== goodbye ======"
echo
```

The line starting with `chroot` is key here, that is actually starting the process inside the chroot jail; in this case, we need to mount the `/dev` devices and such to be able to use the `/dev/tun/` network devices where OpenVPN will create its endpoint.

You can of course start whatever you like there; if you replace the line with `chroot /srv/debian bash` it drops you in a root shell again.

Now, if I `sudo` run this script, it starts a VPN session which I'm able to use from the host operating system, so I can just use my browser to go to websites tunnelled by OpenVPN, ssh to it, rsync files and such.

For the curious, `myconfig.ovpn` looked something like this:

```
client
dev tun
proto udp4
remote 12.34.56.78 1194
resolv-retry infinite
nobind
persist-key
persist-tun
ca ca.crt
cert myuser.crt
key myuser.key
comp-lzo
verb 3
tls-auth ta.key 1
tls-version-min 1.0
data-ciphers AES-256-GCM:AES-128-GCM:AES-256-CFB:BF-CBC
auth-user-pass
```

All of this to be able to revert time (and security).


## Bonus: fixing an unbootable machine

When something went sideways on your machine and the bootloader does not see your operating system anymore, or something else makes it not boot, you can use a live-usb to boot a Linux from USB thumbdrive. From there, you can use `chroot` to go 'into' your installation and fix things, for example by running `grub-install` to have the GRUB bootloader write its configuration to the drive(s) again, or install or remove applications.


```bash
# See what device you need, e.g., /dev/nvme0n1p2
blkid

mount /dev/sdXM /mnt/boot  # only if a separate boot partition is used
mount /dev/sdXN /mnt

mount -t proc proc /mnt/proc
mount -t sysfs sys /mnt/sys
# or, if grub-install says 'warning: EFI variables cannot be set on this system':
# mount --rbind /sys /mnt/sys

mount --rbind /dev/ /mnt/dev
# Alternatively, do those separately:
# mount -o bind /dev /mnt/dev
# mount -t devpts pts /mnt/dev/pts

# 'Activate' the chroot jail, so you're actually 'inside your system'
chroot /mnt

# ... do stuff ...
# For example, `update-grub` or install, remove, downgrade an application or something

exit / ctrl+d

# Cleanup (not really needed when you just restart right after anyway):
umount /mnt/dev/pts
umount /mnt/dev
umount /mnt/sys
umount /mnt/proc
```

[More reading](https://www.turnkeylinux.org/docs/chroot-to-repair-system)

!!! hint

    Better dev and pts binding

    In Ubuntu (and many other Linux distributions), PTYs are pseudo-devices identified under /dev/pts and thus a simple mount --bind won’t make it available in the target mount-point but, a recursive mount --rbind will.

    So you can solve this by either mount binding /dev/ recursively using the option --rbind like so:

    ```
    sudo mount --rbind /dev/ /mnt/dev/
    ```

Good luck and have fun!
