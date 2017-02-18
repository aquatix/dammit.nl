Title: Getting a push message on your phone or watch when your laptop battery is running low
Date: 2015-03-07 14:43:30
Slug: 20150307-getting-a-push-message-on-your-phone-or-watch-when-your-laptop-battery-is-running-low
Location: Home
Authors: Michiel Scholten
Tags: rant

When your laptop is sitting on a table and you're doing some other stuff in the meanwhile, it might quietly be running out of battery. In that case, you likely want to be nudged to find it a power outlet before it has to shut down or hibernate.

Wouldn't it be nice to get a push message on your phone (or even smartwatch, because hey, it's 2015)? You can :)

On Linux, there's `udev`, which takes care of a lot of the subsystems of your machines. Add a rule by creating a file called `90-lowbattery.rules` in `/etc/udev/rules.d/` and add the following line:

    SUBSYSTEM=="power_supply", ATTR{status}=="Discharging", ATTR{capacity}=="20", RUN+="/root/bin/pingphone.sh battery_20percent"

You can customise the exact RUN command of course. The 'capacity' part is the percentage of battery left; in this case 20%.

If you don't know [PushBullet](https://www.pushbullet.com/) yet, now is the time to introduce you to this excellent push platform. It's really quite nifty, cross-platform and has plenty of uses in day-to-day life. The `pingphone.sh` script looks like this:

    #!/bin/bash
    echo "`date +%Y%m%d_%H%M` $1" >> /root/bin/pingphone.log
    . /root/.virtualenvs/pushbullet/bin/activate
    python /root/bin/pyPushBullet/pushbullet_cmd.py yourpushbulletkey1234567890abcde note 123456 "laptop battery low" "$1"

Replace the `yourpushbulletkey1234567890abcde` part with your actual PushBullet API key and the `123456` with the deviceID you want the note to be pushed to. (Actually it's of the format `udeCmddJpl` and you can get the relevant one by doing a `python /root/bin/pyPushBullet/pushbullet_cmd.py yourpushbulletkey1234567890abcde getdevices`). The `$1` is the message `battery_20percent` of the RUN command, which you can of course let say anything you like.

As you see, it uses a Python script to push a note through PushBullet. Clone [pyPushBullet](https://github.com/Azelphur/pyPushBullet) into a dir (like `/root/bin`) and correct the above command line to have it point there. As pyPushBullet needs a few support libraries, the cleanest way to install these is by creating a [virtualenv](http://docs.python-guide.org/en/latest/dev/virtualenvs/) and `pip install` them in there:

    mkvirtualenv pushbullet
    pip install websocket-client
    pip install requests
    pip install python-magic 

This creates a `pushbullet` directory in `/root/.virtualenvs/` and installs the three dependencies in there that pyPushBullet needs to do its thing. This environment gets activated by sourcing the `activate` script on the third line in the `pingphone.sh` script, as seen above.

Now test the script by running:

    /root/bin/pingphone.sh test

This should land a push message on your device.

All kinds of other things can be fired by these `udev` triggers. If you'd like your machine to automatically suspend for example (if it is not already configured to do so), you can have it look like this: `RUN+="/usr/bin/systemctl suspend"`
