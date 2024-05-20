Title: Fixing i915 display glitches
Started: 2024-05-20 22:19:06
Date: 2024-05-20 22:19:06
Slug: fix-i915-glitches-systemd-boot
Location: Couch
Authors: Michiel Scholten
Status: published
Category: howto
Tags: howto, linux

Lately I've had two laptops randomly glitch their screens at me. At first I worried their hinges were starting to give out (the connectors in those things are scarely fragile), but I noticed a message in `dmesg`:

```
i915 0000:00:02.0: [drm] *ERROR* CPU pipe A FIFO underrun
```

That sure looked related to seeing glitches on my display. Now, how to solve.

After some digging through Linux distribution forums (still existing and findable through Google *Web* search thankfully!), and having the [Arch forum](https://bbs.archlinux.org/viewtopic.php?pid=1956804#p1956804) and [Arch wiki](https://wiki.archlinux.org/title/Intel_graphics#Screen_flickering) saying the `i915.enable_psr=0` Linux kernel boot parameter could very likely help, I put that piece on the appropriate line in the `/etc/default/grub` file of my Kubuntu laptop. However, the ThinkPad that runs Pop!_OS does not have a grub 'defaults' file. Or... grub at all. Right. OK, so of course `systemd-boot` is a thing (I totally knew that!), especially in combination with the UEFI firmware loading mechanism of modern machines.

It has a config file too right, like grub? Hm no, EFI directly loads the kernel, so how does that... Ah here: `/boot/efi/loader/entries/` - that directory contains files like `Pop_OS-current.conf` and `Pop_OS-oldkern.conf`, which sound like they will surely be overwritten the next time there's a kernel update.

Long story short, use `kernelstub -a i915.enable_psr=0` to make it permanent. It persists the defaults in `/etc/kernelstub/configuration`, and immediately updates to EFI bootloader entries so next boot you're good to go. Now, fingers crossed it actually prevents the glitching.
