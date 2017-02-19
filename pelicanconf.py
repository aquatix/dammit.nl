#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = u'Michiel Scholten'
SITENAME = u'dammIT'
SITEURL = ''

PATH = 'content'

TIMEZONE = 'Europe/Paris'

DEFAULT_LANG = u'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS = (('Ryan Rix', 'http://whatthefuck.computer/blog/'),
         ('Python.org', 'http://python.org/'),
         ('Jinja2', 'http://jinja.pocoo.org/'),
        )

# Social widget
#SOCIAL = (('You can add links in your config file', '#'),
#          ('Another social link', '#'),)
SOCIAL = (
    ('<i class="fa-li fa fa-twitter"></i> Twitter', 'https://twitter.com/michielscholten'),
    ('<i class="fa-li fa fa-github"></i> Github', 'https://github.com/aquatix'),
)

#GITHUB_URL = 'https://github.com/aquatix'

DEFAULT_PAGINATION = False

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True

THEME = '../../github/w3-personal-blog'

DISPLAY_PAGES_ON_MENU = True
#DEFAULT_PAGINATION = 10

PLUGIN_PATHS = ['../pelican-plugins']
PLUGINS = ['neighbors', 'summary']
