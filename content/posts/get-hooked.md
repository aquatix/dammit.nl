Title: Get Hooked
Started: 2023-06-22 21:00:24
Date: 2023-06-22 21:00:24
Slug: get-hooked
Location: Home
Authors: Michiel Scholten
Status: published
Category: projects
Tags: dev, energy, hosting, linux, opensource, work
Image: https://shuttereye.org/images/40/4030b0b8999b9f9b_2000-2000.jpeg

![Actual code of the amazing webhook project](https://shuttereye.org/images/40/4030b0b8999b9f9b_2000-2000.jpeg)

Are you tired of doing everything by hand, having to remote into a build server to switch to that certain user account, then type in a bunch of commands, looking them up in your shell's history?

Or has your CI failed you again? Is the company behind it forcing some big update on you, or has that update just brought down half of your infra? Did you fall asleep halfway through reading how to set up the building of artifacts? Or do you just want to update some Git repository checkouts on a handful of servers instead of investing so many of your precious lunch time investigating how to do the easy stuff with that piece of garbage? Especially since the documentation is from before you where born and has the same coherence as your thoughts before coffee?

"Mike," you say "I recognise some of what you are talking about above, but what on earth are you gearing up to?"

Glad you asked!

Let me introduce to you: [webhaak](https://github.com/aquatix/webhaak/)! Yes, that's a fancy spelling of 'webhook', the technology glue behind a lot of online automation. Fancy because it is actually the Dutch spelling of the word, and we all know that the Dutch are fancy with their windmills, Turkish tulips, wooden shoes, weed, waterworks, electric cars and such. (Well, actually, they do not spell it like that in The Netherlands, as they just use 'webhook' too, like they long ago stopped saying 'rekenmachine' to a computer and 'gegevensbank' to databases. But I digress).

"Fancy words, Mike!"

Thanks.

`webhaak` is something that should not be missing from your toolkit. It slices, it dices, it takes an incoming URL call and executes the commands you configured it to do on that trigger; it updates Git checkouts, performs checks, builds whatever you want it to build [^1], all done asynchronously because that is fashionable and also because it is not good design to perform bigger tasks in the view of a web application, so it uses [a queueing backend](https://python-rq.org/) that is actually easy to install and maintain, with a worker that does all that hard work for you. Whenever it is done, it notifies you if you want. Support for PushOver and Telegram, all those developer friendly notification channels! Or just have it fire a webhook instead, it is what it is good at, those webhooks.

This product is 100% Python [^2] because why not? Of course, it is also [pushed to PyPI](https://pypi.org/project/webhaak/), so you can install it with a simple `pip install webhaak`!

"Mike, it errors on download!"

That is because it is so bleeding edge! It makes your edge bleed because it is such a sharp tool! Now look at [this user friendly yaml configuration file](https://github.com/aquatix/webhaak/blob/master/example_config/examples.yaml).

"Mike, this is amazing!"

But wait, there is more! There even is functionality coming that creates informational notifications about new pull requests and updates of those, so you can finally make sure your team mates are taking part in the process.

Apart from that, [documentation can be found on Read the Docs](https://webhaak.readthedocs.io/en/latest/), not even connected through webhaak itself, but updates *are* kicked off through the magic of webhooks originating from GitHub, as that is all we are here for.

There even is [a web frontend](https://github.com/aquatix/webhaak-ui) for the REST goodness that is `webhaak`. Just host this HTML file wherever you want and the actions really become a single click action.

Now, get hooked too, and start using [webhaak](https://github.com/aquatix/webhaak/) in production! Or even on your dev tryout machine! Maybe hook it up to your documentation repository and have it build your Sphinx documentation on push, or go out on a limb, glue it to [Fabric](https://www.fabfile.org/) and go wild!

We love to hear your success stories [in the issue tracker](https://github.com/aquatix/webhaak/issues).

[^1]: As long as you tell it how to do so
[^2]: With a healthy dose of shell scripts
