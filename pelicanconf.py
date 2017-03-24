#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = u'Michiel Scholten'
SITENAME = u'dammIT'
SITELOGO = u'<img src="/images/dammit.svg" alt="dammIT" />'
SITEURL = ''  # Set in publishconf.py

# Sub-title that goes underneath site name in jumbotron.
SITESUBTITLE = 'A rantbox'
SITETAG = 'dammIT'

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
         ('Vermyndax', 'http://galaxycow.com/'),
         ('Python.org', 'http://python.org/'),
         ('Jinja2', 'http://jinja.pocoo.org/'),
        )

# Social widget
SOCIAL = (('Google+', 'http://plus.google.com/u/0/+MichielScholten',
           'fa fa-google-plus-square fa-fw fa-lg'),
          ('Twitter', 'https://twitter.com/michielscholten',
           'fa fa-twitter-square fa-fw fa-lg'),
          #('LinkedIn', 'http://linkedin-url',
          # 'fa fa-linkedin-square fa-fw fa-lg'),
          #('BitBucket', 'http://bitbucket.org/username',
          # 'fa fa-bitbucket-square fa-fw fa-lg'),
          ('GitHub', 'http://github.com/aquatix',
           'fa fa-github-square fa-fw fa-lg'),
         )

# Social metadata
OPEN_GRAPH = True
TWITTER_CARD = True
TWITTER_USERNAME = 'michielscholten'

#GITHUB_URL = 'https://github.com/aquatix'

#DEFAULT_PAGINATION = False

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True

# Show jumbotron page header with logo instead of plain text sitename
CUSTOM_SITE_HEADERS = ("jumbotron_logo.html", )

# Put taglist at end of articles, and use the default sharing button implementation.
#CUSTOM_ARTICLE_FOOTERS = ("taglist.html", "sharing.html", )
CUSTOM_ARTICLE_FOOTERS = ("taglist.html", )
#CUSTOM_SCRIPTS_ARTICLE = "sharing_scripts.html"

# Default sidebar template. Omit this setting for single column mode without sidebar.
SIDEBAR = "sidebar.html"
CUSTOM_SIDEBAR_MIDDLES = ("sb_links.html", )

THEME = '../voidy-bootstrap'

# Extra stylesheets, for bootstrap overrides or additional styling.
STYLESHEET_FILES = ("pygment.css", "voidybootstrap.css", "darkblue.css",)


DISPLAY_PAGES_ON_MENU = True
DEFAULT_PAGINATION = 10

PLUGIN_PATHS = ['../../others/pelican-plugins']
PLUGINS = ['neighbors', 'summary']

STATIC_PATHS = ['images']
