Title: Andromeda, Substratum and a Chromebook
Started: 2018-06-21 11:02:20
Date: 2018-06-21 11:02:20
Slug: andromeda-chromebook
Location: Home
Authors: Michiel Scholten
Category: gadgets
Tags: android, dev, gadgets, howto, linux

[Andromeda](https://forum.xda-developers.com/apps/substratum/andromeda-desktop-clients-release-notes-t3668682) is a way to theme an Android device with [Substratum](https://play.google.com/store/apps/details?id=projekt.substratum) without needing root. You need `adb` though, so a desktop or laptop computer is needed to initiate the connection between the Andromeda app and Substratum.

On regular machines this is not much of an issue, but Chromebooks are both nifty little tools as a bit restricted in what you can run there. Thankfully, even running `adb` is a breeze now, at least if you have put the Chromebook in dev mode (not dev channel). ChromeOS has been shipping an `adb` binary for quite some time already, but it's an outdated one (why?!), so it for example does not work with my Pixel 2XL running Android 8.1 Oreo.

However, the world would not be right if some enterprising developer would not create a way of updating both `adb` and `fastboot` on ChromeOS. That's exactly what [Nathan Chance did](https://forum.xda-developers.com/hardware-hacking/chromebooks/guide-setting-adb-fastboot-x8664-t3806428). [Download his installer script](https://raw.githubusercontent.com/nathanchance/chromeos-adb-fastboot/master/install.sh) and run it from the terminal:

<kbd>ctrl</kbd>+<kbd>alt</kbd>+<kbd>t</kbd> `shell` `bash ~/Downloads/install.sh` and enter your sudo password. Of course substitute the path to install.sh if you saved it somewhere else.

`source ~/.bashrc` to activate the aliases so you have a working `adb` and `fastboot`.

You now have an up-to-date `adb`, but the script that's linked from the Andromeda thread for use on Linux uses a mix of its own bundles `adb` and the system binary.

I created a fixed version of this script to always use the up-to-date system `adb` that Nathan's script downloads (and can update). Download the following and save as start_andromeda.sh then use as advertised in the Andromeda thread:

    #!/usr/bin/env bash
    echo "Andromeda Start Shell Script by [projekt.] development team"
    echo ""
    echo "This requires projekt.andromeda to be installed on the device"
    echo "Make sure the device is connected and ADB option enabled"
    echo "Please only have one device connected at a time to use this!"
    echo ""
    read -n 1 -s -r -p "Press any key to continue..."
    echo ""
    echo ""

    export USER_HOME=${HOME}

    function adb() {
        sudo su --preserve-environment -c "HOME=${USER_HOME} /usr/local/bin/adb ${*}"
    }

    # Get the current directory of the device running this script 
    ROOT=$(dirname $0)

    # ADB specific commands for termination
    adb kill-server
    adb start-server

    # Device configuration of the testing rack
    ADB="adb shell"

    # Let's first grab the location where Andromeda is installed
    pkg=$($ADB pm path projekt.andromeda)
    echo "$pkg"

    # Due to the way the output is formatted, we have to strip 10 chars at the start
    pkg=$(echo $pkg | cut -d : -f 2 | sed s/\\r//g)

    # Now let's kill the running Andromeda services on the mobile device
    kill=$($ADB pidof andromeda)

    # Check if we need to kill the existing pids, then kill them if need be
    if [[ "$kill" == "" ]]
    then echo
    $ADB << EOF
    am force-stop projekt.substratum
    appops set projekt.andromeda RUN_IN_BACKGROUND allow
    appops set projekt.substratum RUN_IN_BACKGROUND allow
    CLASSPATH=$pkg app_process /system/bin --nice-name=andromeda projekt.andromeda.Andromeda &
    echo "You can now remove your device from the computer!"
    exit
    EOF
    else echo
    $ADB << EOF
    am force-stop projekt.substratum
    kill -9 $kill
    appops set projekt.andromeda RUN_IN_BACKGROUND allow
    appops set projekt.substratum RUN_IN_BACKGROUND allow
    CLASSPATH=$pkg app_process /system/bin --nice-name=andromeda projekt.andromeda.Andromeda &
    echo "You can now remove your device from the computer!"
    exit
    EOF
    fi

    # We're done!
    adb kill-server
