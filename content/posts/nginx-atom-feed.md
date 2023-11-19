Title: nginx atom feed configuration
Started: 2023-11-19 15:45:08
Date: 2023-11-19 15:45:08
Slug: nginx-atom-feed
Location:  Home
Authors: Michiel Scholten
Status: published
Category: howto
Tags: dev, hosting, linux, opensource, reading
Image: https://shuttereye.org/images/74/74d23339c971695a_2000-2000.jpg

[![Spider web with dew drops](https://shuttereye.org/images/74/74d23339c971695a_2000-2000.jpg)](https://shuttereye.org/nature/morning_stroll/IMG_3249.jpg/view/)

Today I got an email from the Google Search Console about a page, or pages on dammIT that are "Duplicate without user-selected canonical". That generally means that a website has two (very) similar pages that contain the same content, without having a `<link rel="canonical">` element in the duplicating pages linking back (with the `href` property) to the 'original' [or something similar](https://developers.google.com/search/docs/crawling-indexing/consolidate-duplicate-urls), to make clear which is the 'source', and which are 'variants'. It's fine to have duplicates as long as one makes it clear that they are not just padding, and where a visitor can find the spring.

I was curious as to what I would have duplicated, as I tend to not repeat myself much. Following the link from the email and looking in the dashboard that opened, it turned out to be the `https://dammit.nl/feeds/all.atom.xml` file, which is the general [Atom feed](https://en.wikipedia.org/wiki/Atom_(web_standard)) that interested people can use to follow posts in all categories here on dammIT, in their favorite [feed reader/aggregator](https://en.wikipedia.org/wiki/News_aggregator) (myself, I use [Inoreader](https://www.inoreader.com/) as it has a great mobile app and decent web app and it saves all my read state and has handy features, but [there are plenty of others](https://en.wikipedia.org/wiki/Comparison_of_feed_aggregators)). I can recommend using a feed reader instead of some social media website to read your daily fix with.

Anyway, that was amusing, as _of course_ it duplicates stuff, it's the feed with all recent-ish content on my weblog after all. Apparently Google's crawler isn't all too aware about what this 'page' is about though, and a quick look at the headers in the 'Network' tab of my browser showed me that of course it was served as an item with mimetype `application/xml`, which could mean anything. As Atom has its own mimetype - `application/atom+xml` - I decided that it would a good idea to have the various Atom feeds be served with that mimetype, whether it would solve this particular 'issue' or not.

!!! hint

    For example all the [categories](https://dammit.nl/categories.html) have their own feed (e.g., [howto](https://dammit.nl/feeds/howto.atom.xml)), as do [the tags](https://dammit.nl/tags.html).

As all the Atom feeds on dammIT are of the format `NAME.atom.xml` it is easy enough to match the files and have nginx use a different mimetype than for regular `.xml` files, like so:

```
location ~* \.atom\.xml$ {
    types { } default_type "application/atom+xml; charset=utf-8";
}
```

So I did, and after a quick restart of nginx I refreshed my browser tab with the `https://dammit.nl/feeds/all.atom.xml` feed and was greeted with a 404 Not Found page, which was slightly surprising. It turned out that was because of the way I configured the various root directories/items in the dammIT nginx configuration:

```
server {
    listen [::]:443 ssl http2;
    listen 443 ssl http2;
    server_name dammit.nl;

    add_header Strict-Transport-Security 'max-age=31536000; includeSubDomains; preload';

    access_log  /var/log/nginx/access_dammit.nl.log;
    error_log  /var/log/nginx/error_dammit.nl.log  warn;

    location ~* \.atom\.xml$ {
        types { } default_type "application/atom+xml; charset=utf-8";
    }

    location / {
        root /path/to/dammit.nl/;
    }

    location /images/dammit.svg {
        alias /path/to/dammit.nl/images/dammit.svg;
    }

    location /images/ {
        root /other/path/to/www_data/dammit.nl/;
    }

    # ...
}
```

As you can see, there is some specific root and alias configurations going on here, and the `location` item for `*.atom.xml` does not contain a root. It also doesn't help to put this specific `location` item at the end (it doesn't magically inherit the correct root), but providing an explicit root that corresponds with the rest of the generated files *does* work:


```
location ~* \.atom\.xml$ {
    types { } default_type "application/atom+xml; charset=utf-8";
    root /srv/www/dammit.nl/;
}
```

So that's how it ended up looking.

As of writing, validating the page indexing issue is still pending, so I'm curious if it even fixes the original problem to begin with :)
