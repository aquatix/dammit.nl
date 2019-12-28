Title: NS API 2019 edition
Started: 2019-12-28 21:23:02
Date: 2019-12-28 21:23:02
Slug: ns-api-2019
Location: Home
Authors: Michiel Scholten
Category: projects
Tags: dev, opensource, python, tech
Status: published

I [just merged](https://github.com/aquatix/ns-api/pull/18) a [new version](https://pypi.org/project/nsapi/3.0.0/) of my [trusty old NS API Python library](https://github.com/aquatix/ns-api/). Last year I would have thought to not be touching it for quite a while, as nowadays I'm in the luxurious position of being able to bike to work and not wanting to do basically a rewrite now the NS re-did their API in JSON (it used to be a funny Dutch XML one). Discovering quite a bunch of people are using it in the excellent [Home Assistant](https://www.home-assistant.io/) home automation project, I decided to dust it off again anyway. Turned out, [Squixx](https://github.com/Squixx) wrote a really nice pull request, fixing basically All The Things(tm), which was a really pleasant surprise, as I am used to have to do all the work myself to my hobby projects.

Downside was, they converted all the files to Windows line endings for some reason, which broke the Git diffing (Everything Has Changed Sir), and added some Microsoft copyrighted Docker files, which was cool in itself, but the copyrightedness was not. After waiting for a bit on my review of said changes, I decided to go ahead and use the changes in a more useful pull request, which you find linked above.

I made some further adjustments and uploaded version 3.0.0 of the library to PyPi. It would be really cool if people could start using it again :)

I'm a fan of Home Assistant myself, but I really need to spend some time setting it up on the Pi I got for the purpose, together with the [rfxcom](http://www.rfxcom.com/) sender/receiver box (great little device by a fellow Dutchman).

First step would be to create a new API account on the [NS API Portal(https://apiportal.ns.nl/), which works through Microsoft Azure. Yay. Oh well, one can't have everything.
