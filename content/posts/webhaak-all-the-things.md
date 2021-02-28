Title: webhaak all the things
Started: 2019-07-15 10:45:18
Date: 2019-07-15 10:45:18
Slug: webhaak-all-the-things
Location: Work
Authors: Michiel Scholten
Category: projects
Tags: dev, linux, notifications, python, web, work
Image: https://shuttereye.org/images/7f/7f5f7ebfbfbf8fdf_2000-2000.jpg
Status: published

![Literal screenshot of Python sourcecode of webhaak project](https://shuttereye.org/images/7f/7f5f7ebfbfbf8fdf_2000-2000.jpg)

If you're not using [webhooks](https://en.wikipedia.org/wiki/Webhook) yet to automate things from automatically generating documentation, running tests, updating websites and web applications based on events, please go read up on them.

In the meanwhile, I've basically hooked up all my personal projects based on webhooks in GitHub and [gitea](https://gitea.io/en-us/), powered by my own [webhaak](https://github.com/aquatix/webhaak/) webhook processor. webhaak can update Git repository checkouts, run commands, send push notifications [and more](https://github.com/aquatix/webhaak/tree/master/example_config), all based on a fairly simple [yaml based config file](https://github.com/aquatix/webhaak/blob/master/example_config/examples.yaml). I even hooked up Sentry messages to notifications in our work Telegram chat. Reminds me that I'll add that as another example.

I'm rather happy with it, and adding new functionalities or tie-in scripts whenever I need them. Maybe it's useful for you too. Of course, [requests are welcome](https://github.com/aquatix/webhaak/issues) :)
