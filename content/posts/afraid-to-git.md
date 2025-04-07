Title: Afraid to Git
Started: 2025-04-07 11:31:24
Date: 2025-04-07 14:09:49
Slug: afraid-to-git
Location: Home
Authors: Michiel Scholten
Status: published
Category: projects
Tags: copyright, dev, ethics, hosting, networking, opensource, tech
Image: https://shuttereye.org/images/6d/6ded664a26222018_2000-2000.jpg

[![Trees with flowering branches](https://shuttereye.org/images/6d/6ded664a26222018_2000-2000.jpg)](https://shuttereye.org/photolog/PXL_20250407_064910075.jpg/view/)

I have been running a Git server for over a decade now (before that it was mercurial and before that versioning system I rocked [SVN](https://en.wikipedia.org/wiki/Apache_Subversion), dating back at least twenty years). It has hosted my private repositories and served as a mirror for [my GitHub](https://github.com/aquatix/) projects.

More recently though I have been shifting away from GitHub and I started two open source projects that do not have a repository on GitHub, just on my Gitea instance.

Notice how I did not link to any repositories or servers in the above paragraph? There are a few reasons.

Xe Iaso tells it best when they [introduced their Anubis tool](https://xeiaso.net/blog/2025/anubis/) and its workings:

> A majority of the AI scrapers are not well-behaved, and they will ignore your `robots.txt`, ignore your `User-Agent` blocks, and ignore your `X-Robots-Tag` headers. They will scrape your site until it falls over, and then they will scrape it some more. They will click every link on every link on every link viewing the same pages over and over and over and over. Some of them will even click on the same link multiple times in the same second. It's madness and unsustainable.

Xe has [been mentioned on Arstechnica](https://arstechnica.com/ai/2025/03/devs-say-ai-crawlers-dominate-traffic-forcing-blocks-on-entire-countries/) and [TechCrunch](https://techcrunch.com/2025/03/27/open-source-devs-are-fighting-ai-crawlers-with-cleverness-and-vengeance/) in the light of AI crawlers harassing websites and infrastructure, and the tool they wrote in response to it, which effectively and intentionally blocks a lot of the crawlers.

Part of the README of [Anubis](https://github.com/TecharoHQ/anubis):

> Installing and using this will likely result in your website not being indexed by some search engines. This is considered a feature of Anubis, not a bug.
>
> This is a bit of a nuclear response, but AI scraper bots scraping so aggressively have forced my hand. I hate that I have to do this, but this is what we get for the modern Internet because bots don't conform to standards like robots.txt, even when they claim to.

These web crawlers are dumb and malicious, ignoring things like the mentioned `robots.txt` and for example hammering all `git blame`, [history](https://drewdevault.com/2025/03/17/2025-03-17-Stop-externalizing-your-costs-on-me.html) and `diff` links they can find, bringing down Git services and causing thousands of dollars of network traffic bills.

I mean, to quote a small part of the Arstechnica article linked above:

> GNOME sysadmin Bart Piotrowski [shared](https://social.treehouse.systems/@barthalion/114190930216801561) on Mastodon that only about 3.2 percent of requests (2,690 out of 84,056) passed their challenge system, suggesting the vast majority of traffic was automated. KDE's GitLab infrastructure was temporarily knocked offline by crawler traffic originating from Alibaba IP ranges, according to LibreNews, citing a KDE Development chat.

And as recently as last Thursday, [Linux' kernel.org is behind Anubis too](https://mastodon.social/@cadey@pony.social/114275376056593763), because of the exact same reasons.

However, this leads to a little conundrum I am currently having in private: I would really like to move away from GitHub as that is owned by Microsoft, is extensively scraped by the OpenAI bots and most likely all other 'AI' bots in existence, and I like hosting my *own* work on my *own* little garden, outside of reach/ownership of certain states and/or big tech.

That is part of why I am putting more use in my own Git server, but as sketched out above, this puts me at risk of effectively being [Slashdotted](https://en.wikipedia.org/wiki/Slashdot_effect) by run-away misbehaving bots. Of course, I can just #YOLO it and find out if it is really going to be a problem, but when that (inevitably?) happens, how am I going to save my little garden from being trampled to oblivion, other than also deploying an instance of Anubis or similar counter measures? Why do I and other tech enthusiasts even need to consider this?

Friends of mine consider going entirely offline with both their versioning hosting and their weblogs and other websites, just to escape this hell of both misbehaving scrapers and the LLM's just mindlessly absorbing everyone's work and regurgitating it as their own; they would then resort to [Tailscaling](https://tailscale.com/) it all together with private connections, and sharing their own articles and interesting links only in some private chatrooms, which would effectively mean going dark with all kinds of interesting write-ups.

For me, it makes me reconsider even writing about this nifty little tool I wrote recently to fix a problem I had, and which can help others as well. But do I want to link to my Git server with the code and examples, putting it at risk of being reduced to smoke?

It is both amazing what you can create with those LLM tools, be it the text-based ones, or the versions creating imagery. However, as things currently stand, it is destroying the internet to its soul as well.


<!-- -- Cheat-sheet ------

[books page]({filename}../pages/books.md)
[hello post]({filename}../posts/hello.md)
[![Linked image](https://dammit.nl/images/content/example.png)](https://dammit.nl/images/content/example.png)
[![Linked gallery image](https://shuttereye.org/images/70/707272f27b6b7a68_2000-2000.jpg)](https://shuttereye.org/gallery/subgallery/IMG_example.jpg/view/)
-->
