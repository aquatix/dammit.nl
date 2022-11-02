Title: OpenSSL gave everyone alarm fatigue
Started: 2022-11-02 09:28:26
Date: 2022-11-02 09:28:26
Slug: link-alarm-fatigue
Location: Office
Authors: Michiel Scholten
Status: published
Category: responses
Tags: hosting, link, linux, networking, opensource, security
Link: https://xeiaso.net/blog/openssl-alarm-fatigue

> I'm worried that this is going to be seen as a reason to not take "CRITICAL" disclosures seriously at first glance like we should. A "CRITICAL" bug MUST be treated as if it was critically bad. From a community health perspective, people have been told that something really bad is about to come out for a week and then had the rug pulled out from under them and now it's "nah we were wrong you're probably fine".

I totally agree. For a week, I was slightly anxious about the impact this vulnerability would have on our systems at work and my own private services. I relaxed a bit when I realised Debian 11 ships with OpenSSL 1.1.1 which is not impacted, but still was keeping my eye out for everything else.

Then, yesterday it turned out that - yes - it is bad, but in really specific, not even that often occurring circumstances. Combined with the re-framed impact level of 'high', that takes away believability of the initial 'this is really impactful!' news and the accompanying hype.

[The information provided by the devs themselves on the OpenSSL blog](https://www.openssl.org/blog/blog/2022/11/01/email-address-overflows/)
