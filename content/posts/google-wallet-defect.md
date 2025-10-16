Title: Google Wallet: broken
Started: 2025-10-02 14:37:33
Updated: 2025-10-16 14:23-14:40
Date: 2025-10-16 12:48:33
Modified: 2025-10-16 14:40:00
Slug: google-wallet-broken
Location: Home
Authors: Michiel Scholten
Status: published
Category: thoughts
Tags: communication, freedom, life, mobile, tech
Image: https://shuttereye.org/images/b8/b8f03e9ecf43c7d7_2000-2000.jpg

I am disappointed. One could even say I am peeved. Sad and slightly angry. Not very surprised though.

[![Card holder on top of keyboard](https://shuttereye.org/images/b8/b8f03e9ecf43c7d7_2000-2000.jpg)](https://shuttereye.org/various/dammit/PXL_20251015_101819345.jpg/view/)
_Card holder on top of keyboard_

For several very convenient years I have been using my phone for contactless payments, to the point that I was frequently unsure of the exact whereabouts of my debit card, or even what its PIN code was again.

Then, it starting to get unreliable by *out of the blue* stating that my device was not passing security checks and refusing to let me pay while standing in line. Force closing the Wallet app often was enough to make it work again, sometimes tinkering a bit with Magisk Hide so Wallet would not see it.

After it left me high and dry deep underground in a parking garage where I was saved by a friendly guy advancing me the ticket payment (with his Apple Watch even...), I vowed to never not have a debit card on me again. I was ***so*** let down by this system.

I thought it was because I had rooted my phone and was running Magisk to handle some programs that use root for extra functionality for my phone, like actually having a decent backup program like Swift Backup, being able to reach some files from for example WhatsApp through a file manager, NFC Tools to make use of the NFC reader and some minor stuff (I used to have a theming app in the past too for example, which made better use of Material You colours).

But no, it is simply because I **unlocked my bootloader** when I got my phone. Google apparently decided that that means no security and Google Wallet has been started to comply with this more stringently, because the device 'doesn't pass Google Play Integrity checks (Basic/Device)'. Well, that explains why Google VPN never worked for me either. Not that they bother to tell the user why. That one recently started to pop up notifications about not working without any explanation too, so, good job everyone. At least it is not just silently failing any more.

It used to be that it was very OK to have an unlocked bootloader. The [Android documentation documents it clearly](https://source.android.com/docs/core/architecture/bootloader/locking_unlocking) and it was good practice if you wanted to be able to easily flash even factory firmware.

Now, Google decided to crack down on this freedom I have with a device I bought for over 1200EUR and cripple functionality I had been relying on for years, and which *actually worked on this device* for years!

When researching my issues, I found out that of course, having unlocked my bootloader has been frowned upon by Google for years, but I had to infer that mostly by posts on Reddit, XDA Developers and such. Also, the Android Project and Google itself had in the past encouraged this open behaviour.

It would also not have been such a big problem when you could just unlock your bootloader when you want to, but ***unlocking your bootloader will destroy your data, even though the device guarantees it was not tempered with before***, so I would logically do that as soon as I get a new phone to prevent me having to go through the pains of setting up a new phone **again** later on.

I deleted Magisk, reverted everything to stock firmware (apart from re-locking the bootloader which would also nuke all my stuff) and still "Electronic wallet says 'no'".

To add insult to injury, after this period of not being able to use my cards (which by the way, were migrated from my bank's own application which always worked fine to Google Wallet because... reasons?), I got an email from Google stating:

> Your payment cards were deleted from your Google Pixel 8 Pro, an inactive device

No, that device is not inactive, you have deliberately vandalised perfectly good functionality making it impossible for me to use it like it was designed and for which I paid good money!

Not only that, but they are now restricting your freedom even more by [cracking down on developers to register with their name and everything](https://f-droid.org/de/2025/09/29/google-developer-registration-decree.html) to be able to make their application run on your Android device. Oh, you make open source software that is published through a trusted installer like f-droid? Well, though luck, you have not registered.

Google’s move to break free app distribution and their hostile stance against applications like [termux](https://termux.dev/en/) which are so very useful for me and a lot of other folks who just like to tinker with *their devices* and chose Android because it lets them makes me want to **give up on everything Google**, especially this mobile platform which I have cherished and tinkered with since I got my HTC Hero in 2009. That makes me sad.

But where do I go?

Well, at least back to <del>the middle ages</del> physical cards. Also, I have [started tinkering with hardware to build a Linux PDA](https://shuttereye.org/home/tech/zyberdeck/PXL_20250919_100237353.jpg/view/), so at least something positive came out of this all I guess :)

It reminds me of my [Planet Mobile]({filename}../posts/20140420-planet-mobile.md) post from eleven years ago. In 2014 I was already talking about the good old time of having a modular set of devices, each with their own forte, and that the current convergence - both with smart phones and tablets - was great, but that it seemed to discourage *creating*. Maybe being forced to use different form factor mobile devices will be a catalyst for mobile creativity and creation; I know that I had a lot of fun already going from discovering the [very interesting and fun looking uConsole](https://www.clockworkpi.com/uconsole) to getting myself a tiny Pi, keyboard and touchscreen and basically building/prototyping such a console myself with Lego.

If I even go further down this route, it would mean using my phone a lot less like the very useful pocket computer it is now, and - having a locked bootloader and no useful apps like termux - just use it as my agenda and photo camera. It really feels like going back in time... Let's hope this course can be averted. Please Google and other phone manufacturers, let us have the freedom to tinker with our **own** devices and use them as the powerful personal computers that they are.

**Bonus:** Interesting read about [bootloader locking/unlocking... AKA I want to relock my bootloader, should I?](https://www.reddit.com/r/LineageOS/comments/n7yo7u/a_discussion_about_bootloader_lockingunlocking/)
