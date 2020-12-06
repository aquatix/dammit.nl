Title: Ripping a DVD, Linux style
Started: 2020-12-06 19:56:54
Date: 2020-12-06 19:56:54
Slug: ripping-dvd
Location: Home
Authors: Michiel Scholten
Status: published
Category: howto
Tags: backups, gadgets, howto, linux, opensource, tech

Recently we got a DVD. After turning it around in our hands a few times and giggling at our reflections, we ordered an external USB DVD/CD eater so we actually could ingest some of its contents.

As the hip techy people we are, having this material available to us in a less physical way made me look up the exact `dd` usage to dump the contents of the disk to an image file.

As a wise person on the internet said:

> You should really use `isoinfo -d -i /dev/cdrom` (ed: or `/dev/sr0` or whatever your device is) to find out the logical block size (almost always 2048) and the number of blocks ("Volume size is" line) on the volume to pass as arguments to dd. Which makes the dd command look like `dd if=/dev/cdrom bs=2048 count=1621535 of=filename.iso`

[[source of those pointers](https://askubuntu.com/questions/147800/ripping-dvd-to-iso-accurately)]

Be advised that the `if=` and `of=` parameters do not expand file paths, so using `of=~/Videos/interesting_dvd.iso` will not work; use the full path in that case.
