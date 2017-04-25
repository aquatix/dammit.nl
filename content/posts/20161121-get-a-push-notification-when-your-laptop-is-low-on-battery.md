Title: Get a push notification when your laptop is low on battery
Date: 2016-11-21 13:38:06
Slug: 20161121-get-a-push-notification-when-your-laptop-is-low-on-battery
Location: Work
Authors: Michiel Scholten
Category: howto
Tags: howto, mobile, notifications
related_posts: 20150307-getting-a-push-message-on-your-phone-or-watch-when-your-laptop-battery-is-running-low, 20150919-i-made-a-thing-to-make-your-phone-go-pling-when-your-train-goes-whatever

A while ago [I wrote about getting notified on battery low]({filename}20150307-getting-a-push-message-on-your-phone-or-watch-when-your-laptop-battery-is-running-low.md). It is quite useful when you leave your laptop unattended for a while, to get a notification on your phone and/or smartwatch when that laptop is about to run out of juice. It has saved me a few hard shutdowns (or interrupted tasks because of forced hibernation).

The `udev` rule in that article should still work (if your device/battery emits those kinds of events at least), but for me the PushBullet method used there stopped working.

As I recently started using [PushOver](https://pushover.net/) next to PushBullet, I decided to redo the little setup with a cronjob and [a PushOver shell script](https://github.com/jnwatts/pushover.sh). The cronjob works around the battery subsystem not emitting an event when you need it, the shell script has less dependencies than a Python script.

An example *with* the `udev` rule could look like this:

    /etc/udev/rules.d/99-lowbat.rules

    # Suspend the system when battery level drops to 5% or lower
    SUBSYSTEM=="power_supply", ATTR{status}=="Discharging", ATTR{capacity}=="[0-5]", RUN+="/home/youruser/bin/powerlow_notification.sh"

(Rule based on a snippet found on [this handy wikipage](https://wiki.archlinux.org/index.php/Laptop#hibernate_on_low_battery_level))

Myself, I wrote a cronjob to be run every 5 minutes (you can use whatever interval you prefer of course), which looks like this:

    #!/bin/bash

    BATTERYLEVEL=$(cat /sys/class/power_supply/BAT0/capacity)

    if [ $BATTERYLEVEL -lt 15 ]; then
        /home/youruser/workspace/pushover.sh/pushover.sh -t "Power low on $HOSTNAME" "Battery power now is ${BATTERYLEVEL}%"
    fi

This takes the current battery level from the `udev` system path, checks whether the value is less than 15 (percent) and sends a message through PushOver if it is. It will do so every 5 minutes until it's over 15 again, but that's fine with me (and a small price to pay on a system without the battery events). It might be made a bit more clever with keeping track of 'did I just send a message already' state files, but that exercise is left for the reader :)

Then, the crontab entry looks thusly:

    # Check battery level every five minutes, PushOver message when below a certain percentage
    */5 * * * * /home/youruser/bin/cron/check_battery_level

*N.B.:* the little [`pushover.sh`](https://github.com/jnwatts/pushover.sh)) script that I used, has a config file, located in `${HOME}/.config/pushover.conf`, which takes your PushOver application token, your user token and optional CURL options:

    TOKEN="your application's token here"
    USER="your user/group key here"
    CURL_OPTS="options to pass to curl"

Your user token is on the [homepage of PushOver](https://pushover.net/) if you are logged in. The Application Token ('TOKEN') you can create by scrolling down that page and create a new application in Your Applications. There you can give it a nice icon and such too.
