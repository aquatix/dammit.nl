#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = u'Michiel Scholten'
SITENAME = u'dammIT'
SITEURL = ''

# Sub-title that goes underneath site name in jumbotron.
SITESUBTITLE ='A rantbox'
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
         ('Python.org', 'http://python.org/'),
         ('Jinja2', 'http://jinja.pocoo.org/'),
        )

# Social widget
#SOCIAL = (('You can add links in your config file', '#'),
#          ('Another social link', '#'),)
#SOCIAL = (
#    ('<i class="fa-li fa fa-twitter"></i> Twitter', 'https://twitter.com/michielscholten'),
#    ('<i class="fa-li fa fa-github"></i> Github', 'https://github.com/aquatix'),
#)

#GITHUB_URL = 'https://github.com/aquatix'

#DEFAULT_PAGINATION = False

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True

# Put taglist at end of articles, and use the default sharing button implementation.
CUSTOM_ARTICLE_FOOTERS = ("taglist.html", "sharing.html", )
CUSTOM_SCRIPTS_ARTICLE = "sharing_scripts.html"

# Default sidebar template. Omit this setting for single column mode without sidebar.
SIDEBAR = "sidebar.html"

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

#THEME = '../../github/w3-personal-blog'
THEME = '../../others/voidy-bootstrap'

# Extra stylesheets, for bootstrap overrides or additional styling.
STYLESHEET_FILES = ("pygment.css", "voidybootstrap.css",)


DISPLAY_PAGES_ON_MENU = True
#DEFAULT_PAGINATION = 10

PLUGIN_PATHS = ['../pelican-plugins']
PLUGINS = ['neighbors', 'summary']
