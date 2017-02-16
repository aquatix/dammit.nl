Title: When your Pebble doesn't want to talk web anymore
Date: 2016-09-07 09:49:22
Slug: 20160907-when-your-pebble-doesn-t-want-to-talk-web-anymore
Location: Train
Authors: Michiel Scholten

A few weeks ago I started noticing an odd problem: my Pebble Time Steel didn't want to update its various apps anymore. The watchface showed stale weather data, the public transports apps didn't want to tap into the latest departure times and so on. This of course annoyed me a bit, especially because I couldn't really find someone else with the same issue.

When I reinstalled a watchface that was bought through [KiezelPay](https://kiezelpay.com/) (yes, you can buy watch faces nowadays, and I think you should if you find a neat one; devs put a lot of time into their products), the only thing I got was a big error message that KiezelPay and the internet could not be reached. Cue me mailing the watchface developer, who in turn hooked up the people from KiezelPay. I got a test app, which of course was also not able to reach the webs. Colour us baffled.

Pebble customer support didn't seem to be able to help me either, as they asked me to look into battery saving settings and such. A valid course of action of course, but my Nexus 6P doesn't have the really aggressive battery savers of some vendors, and everything had been working just fine for years before.

The only thing that I could think of was me updating to Android 7.0. I didn't remember whether the issue had been around before that, so I was kind of focussing on that now.

Meanwhile, the Modular dev ([Modular](https://apps.getpebble.com/en_US/application/576f3601ba2fe5e1c8000118) is a great watch face, you should check it out if you have a Pebble, or buy a Pebble because of it), and the Kiezel devs were keeping contact with me, and reaching out to their contacts within Pebble. A suggestion came back about the Overlay permission. This "Draw over other apps" permission, as it's called in the Android settings, allows an app to draw a window or similar on top of the app you are currently viewing. This [can pose security problems](http://www.androidpolice.com/2015/09/07/android-m-begins-locking-down-floating-apps-requires-users-to-grant-special-permission-to-draw-on-other-apps/) as it can draw a fake button, so if you install an app, Android refuses the "Install" button to be enabled if it detects a screen overlay. Same when trying to change app permission settings.

As I had been experimenting with some apps and encountered the "Screen overlay detected!" warning a few too often times, I dove into the app permissions and found quite a few apps that had the "Draw over other apps" permission enabled. I disabled it for a few apps where I couldn't think of a good reason to have it and didn't think about it anymore until the suggestion from the Kiezel dev came in.

Low and behold, if I enabled it for the Pebble app again, all Javascript apps on my watch were able to connect to the internet again just fine. It only took me two weeks or something to find this out...

I still think it's a weird permission and I wonder how it is connected to the ability of Pebble apps to connect to the internet straight from the watch (of course, routed through your phone). In the meanwhile, I'm happy the issue has been resolved, as it was quite the mystery. Not having any related problems popping up on internet searches isn't something I'm used to anymore. I hope this little article might help any other persons that might run into this (admittedly, obscure) problem.