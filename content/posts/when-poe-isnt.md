Title: When Power-over-Ethernet isn't
Started: 2024-07-14 21:40:53
Date: 2024-07-14 23:04:53
Slug: when-poe-isnt
Location: Home
Authors: Michiel Scholten
Status: published
Category: projects
Tags: gadgets, networking, tech
Image: https://dammit.nl/images/content/edgerouter-x.webp

At the start of this year I bought this cute little bugger:

![EdgeRouter-X](https://dammit.nl/images/content/edgerouter-x.webp)

It replaced an ancient Netgear WNDR 3700v2 WiFi router running DD-WRT that had been serving our home internet for ages, but was showing fraying around the edges by not being able to fullfill QoS, for example when Steam decided to update all the games, gobble up all the bandwidth and leave all the other devices without internet.

At the time, I thought it was nice that it had a PoE (Power-over-Ethernet) out on one of its ports, which could come in handy to power some remote device.

Fast forward to last week when I finally decided to get a video doorbell I have been thinking about for years, and narrowed it down to the one by Reolink. This one doesn't need anything from a cloud, can store images and clips on its built-in microsd card or sftp it someplace safe, and apparently has great integration with Home Assistant which is at the heart of our home.

When getting a Reolink doorbell, you have to choose between the WiFi version that's powered by the 12V doorbell adapter (ours is 8V), or the Power-over-Ethernet (PoE) version that can also be powered by that doorbell adapter. Because I want the connection to be rock-solid, I opted for the PoE version, also remembering the PoE-out port on the router which is nicely situated next to the little duct with the cable to the doorbell. By replacing the 2-wired cable with UTP, I would be able to get a data connection *and* power to that outside spot next to our front door.

[![Reolink Doorbell and wireless chime on 8BitDo C64 keyboard](https://shuttereye.org/images/fc/fc9c0ccccd97977f_2000-2000.jpg)](https://shuttereye.org/home/tech/PXL_20240713_183246674.jpg/view/)

Yesterday evening I unpacked the doorbell, took a quick look at the accessories and opened the admin dashboard of the EdgeRouter. Then I plugged a cat5e cable into the PoE port of the EdgeRouter and into the camera and enabled 'PoE' in the web interface of the router.

A whole lot of nothing happened.

Checking the cable, trying another cable - no life in the camera. Slightly miffed, I started searching the web and found [a Reddit thread](https://www.reddit.com/r/Ubiquiti/comments/clxyq2/want_to_power_a_poe_reolink_camera_with/) with something very similar to my situation.

The Ubiquity Edgerouter-X does 24V passive PoE, which after wondering about the 'passive' for a while, I learned means 'power 24V on those two wires no matter what', which also causes a stern warning in the router's web interface when enabling.

According to [the spec sheet of the Reolink Doorbell](https://dammit.nl/images/content/reolink_doorbell_poe_specsheet.pdf), it wants `IEEE 802.3af, 48V Active`, or `12-24VAC 50/60Hz, 24VDC`; the 24V is also shown pretty clearly on the backside of the camera. So I become confused a bit more. Is that 24V PoE just not working with the 24V of the router? No wait, '802.3af' PoE always does that 48V, the 24V is really only when connecting to two wires from an existing doorbell.

Which means... PoE != PoE. Which should not have been surprising to me, but not having done anything with it prior in my life, I always had assumed it was a compatible standard.

However, the camera really wants this 48V on an active connection, with 'active' meaning the devices negotiate for the exact power delivered, similar to how USB does its thing.

After raging for a bit - I really should have done some more due diligence - I decided to get a PoE injector that also does 802.3af. These devices have two UTP ports - 1 in, 1 out - and takes care of the power delivery part. When it arrives early next week, I'll finally know if the camera survived the nonvoluntary 24V, or if it works at all. Hopefully it's smart enough :)

Then comes the interesting part: replacing the 2-wired cable running through the ceiling and walls by a cat5e cable. Let's hope that will not catch a snag.
