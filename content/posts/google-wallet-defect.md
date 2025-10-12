Title: Google Wallet: defect
Started: 2025-10-02 14:37:33
Date: 2025-10-02 14:37:33
Slug: google-wallet-defect
Location: Home
Authors: Michiel Scholten
Status: draft
Category: thoughts
Category-examples: conferences, family, gadgets, howto, photo, posts (fallback), projects, reading, responses, study, thoughts, trips
Tags: communication, freedom, life, mobile, tech
Tags-examples: autism, backups, books, communication, conference, copyright, covid-19, desktop, dev, digimarks, energy, ethics, europython, family, fosdem, gadgets, gaming, hackercamp, health, hosting, howto, journal, kids, life, link, linux, meta, mobile, music, networking, notifications, opensource, photography, python, rant (fallback), reading, science, secondbrain, social, space, sync, tech, trip, ubuntu, vim, web, work
Image: 

I am disappointed. One could even say I am peeved. Sad and slightly angry. Not very surprised though.

[![Card holder on top of keyboard](https://dammit.nl/images/content/example.png)](https://dammit.nl/images/content/example.png)
_Card holder on top of keyboard_

For several very convenient years I have been using my phone for contactless payments, to the point that I was frequently unsure of the exact whereabouts of my debit card, or even what its PIN code was again.

Then, it starting to get unreliable by out of the blue stating that my device was not passing security checks and refusing to let me pay while standing in line. Force closing the Wallet app often was enough to make it work again, sometimes tinkering a bit with Magisk Hide so Wallet would not see it.

After it left me high and dry deep underground in a parking garage where I was saved by a friendly guy advancing me the ticket payment (with his Apple Watch even...), I vowed to never not have a debit card on me again. I was so let down by this system.

I thought it was because I had rooted my phone and was running Magisk to handle some programs that use root for extra functionality for my phone, like actually having a decent backup program like Swift Backup, being able to reach some files from for example WhatsApp through a file manager, NFC Tools to make use of the NFC reader and some minor stuff (I used to have a theming app in the past too for example, which made better use of Material You).

But no, it is simply because I **unlocked my bootloader** when I got my phone. Google apparently decided that that means no security and Google Wallet has been started to comply with this more stringently, because the device 'doesn't pass Google Play Integrity checks (Basic/Device).'. Well, that explains why Google VPN never worked for me either. Not that they bother to tell the user why.

It used to be that it was very OK to have an unlocked bootloader. The [Android documentation documents it clearly](https://source.android.com/docs/core/architecture/bootloader/locking_unlocking) and it was good practice if you wanted to be able to easily flash even factory firmware.

Now, Google decided to crack down on this freedom I have with a device I bought for over 1200EUR and cripple functionality I had been relying on for years, and which *actually worked on this device* for years!

I deleted Magisk, reverted everything to stock firmware (apart from re-locking the bootloader which would nuke all my stuff) and still "Electronic wallet says 'no'".

To add insult to injury, after this period of not being able to use my cards (which by the way, were migrated from my bank's own application which always worked fine to Google Wallet because... reasons?), I got an email from Google stating:

> Your payment cards were deleted from your Google Pixel 8 Pro, an inactive device

No, that device is not inactive, you have deliberately vandalised perfectly good functionality making it impossible for me to use it like it was designed!

Not only that, but they are now [cracking down on developers to register with their name and everything](https://f-droid.org/de/2025/09/29/google-developer-registration-decree.html) to be able to make their application run on your Android device. Oh, you make open source software that is published through a trusted installer like f-droid? Well, though luck, you have not registered.

Google’s move to break free app distribution and their hostile stance against applications like [termux](https://termux.dev/en/) which are so very useful for me and a lot of other folks who just like to tinker with *their devices* and chose Android because it lets them makes me want to **give up on everything Google**, especially this mobile platform which I have cherished and tinkered with since I got my HTC Hero in 2009.

But where do I go?

Well, at least back to ~~the middleages~~ physical cards. Also, I have [started tinkering with hardware to build a Linux PDA](https://shuttereye.org/home/tech/zyberdeck/PXL_20250919_100237353.jpg/view/)



Interesting read about [bootloader locking/unlocking... AKA I want to relock my bootloader, should I?](https://www.reddit.com/r/LineageOS/comments/n7yo7u/a_discussion_about_bootloader_lockingunlocking/)

<!-- -- Cheat-sheet ------

[books page]({filename}../pages/books.md)
[hello post]({filename}../posts/hello.md)
[![Linked image](https://dammit.nl/images/content/example.png)](https://dammit.nl/images/content/example.png)
[![Linked gallery image](https://shuttereye.org/images/70/707272f27b6b7a68_2000-2000.jpg)](https://shuttereye.org/gallery/subgallery/IMG_example.jpg/view/)
-->
