Title: How to fix Secure Settings on Android devices with SuperSU systemless root
Date: 2016-04-06 11:23:31
Modified: 2017-01-21 16:05:00
Slug: 20160406-how-to-fix-secure-settings-on-android-devices-with-supersu-systemless-root
Location: Work
Authors: Michiel Scholten
Tags: rant, howto, mobile
Category: howto

Edit at 2017-01-21: see the comments about better ways, especially [comment 6]({filename}20160406-how-to-fix-secure-settings-on-android-devices-with-supersu-systemless-root.md#isso-592).

[Secure Settings](http://securesettings.intangibleobject.com/) ([Google Play](https://play.google.com/store/apps/details?id=com.intangibleobject.securesettings.plugin&hl=en)) is a really helpful app to help [Tasker](http://tasker.dinglisch.net/) ([Google Play](https://play.google.com/store/apps/details?id=net.dinglisch.android.taskerm&hl=en)) do things automatically on your Android device.

However, it has not been updated for quite a while (January 2015 at the time of this writing) and since then SuperSU has changed its way of installing the `su` binary to your device, by preferring not to install this on the `system` partition.

As some older apps hardcode the complete path of this binary in their checks, and Secure Settings is one of these, it thinks it can not get root access.

On my quest of a fix for this problem, I [found this post on XDA](http://forum.xda-developers.com/showpost.php?p=66190182&postcount=2707) where a [comment on Reddit](https://www.reddit.com/r/tasker/comments/3uf5bn/secure_settings_doesnt_recognize_root_even_though/cxtvflb) was referenced, stating the following fix, running the commands from a command line (terminal) on your machine, having `adb` installed:

```
adb shell
su
mount -o remount,rw /system
touch /sbin/su /system/bin/su /system/xbin/su
mount -o remount,ro /system
exit
reboot
```

[source](https://www.reddit.com/r/tasker/comments/3uf5bn/secure_settings_doesnt_recognize_root_even_though/cxtvflb)

This creates some empty files in locations that older (incorrect) apps check for the `su` binary, so Secure Settings (and likely other applications) are made to believe they can get root (which they actually can, as you can not make those files without being root through `su` anyway).

You can also do this on your device by just omitting the first line and starting with `su` in a Terminal app (or for example [JuiceSSH](https://play.google.com/store/apps/details?id=com.sonelli.juicessh&hl=en) in a local session).

I hope this helps other people looking for a solution too.
