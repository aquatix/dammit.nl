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

# Ignore swap files and blogmarks digests
IGNORE_FILES = ['.#*', '.*.swp', '*blogmarks-for*']

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS = (
    ('Felienne', 'http://www.felienne.com/'),
    ('Rands in Repose', 'http://randsinrepose.com/'),
    ('Ryan Rix', 'http://whatthefuck.computer/blog/'),
    ('Tibo Beijen', 'https://www.tibobeijen.nl/'),
    ('Vermyndax', 'http://galaxycow.com/'),
    ('Pixls.us FLOSS photography', 'https://pixls.us/'),
    ('Python.org', 'https://python.org/'),
    ('Jinja2', 'http://jinja.pocoo.org/'),
)

# Social widget
SOCIAL = (
    ('Mastodon', 'https://mastodon.social/@diginaut',
     'fab fa-mastodon fa-fw fa-lg'),
    ('Twitter', 'https://twitter.com/michielscholten',
     'fab fa-twitter fa-fw fa-lg'),
    # ('LinkedIn', 'http://linkedin-url',
    #  'fab fa-linkedin fa-fw fa-lg'),
    # ('BitBucket', 'http://bitbucket.org/username',
    #  'fab fa-bitbucket-square fa-fw fa-lg'),
    ('GitHub', 'https://github.com/aquatix',
     'fab fa-github fa-fw fa-lg'),
    ('Google+', 'http://plus.google.com/u/0/+MichielScholten',
     'fab fa-google-plus fa-fw fa-lg'),
)

# Social metadata
OPEN_GRAPH = True
TWITTER_CARD = True
TWITTER_USERNAME = 'michielscholten'

TAGS_URL = 'tags.html'
# GITHUB_URL = 'https://github.com/aquatix'

SITE_SUMMARY = 'Weblog/rantbox of Michiel Scholten, software developer, photography enthousiast and all around nerd. Expect howtos, ramblings and random findings'

# The default metadata you want to use for all articles and pages.
DEFAULT_METADATA = {
    # 'description': 'Weblog/rantbox of Michiel Scholten, software developer, photography enthousiast and all around nerd. Expect howtos, ramblings and random findings',
    # 'status': 'draft'
}

# Uncomment following line if you want document-relative URLs when developing
# RELATIVE_URLS = True

# Show jumbotron page header with logo instead of plain text sitename
CUSTOM_SITE_HEADERS = ("jumbotron_logo.html", )

CUSTOM_ARTICLE_HEADERS = (
    "article_header_navigation.html",
    "article_header_date.html",
    "article_header_title.html",
    "article_header_info.html",
)

# Put taglist at end of articles, and use the default sharing button implementation.
# CUSTOM_ARTICLE_FOOTERS = ("taglist.html", "sharing.html", )
CUSTOM_ARTICLE_FOOTERS = ("taglist.html", )
# CUSTOM_SCRIPTS_ARTICLE = "sharing_scripts.html"

# Default sidebar template. Omit this setting for single column mode without sidebar.
SIDEBAR = "sidebar.html"
CUSTOM_SIDEBAR_MIDDLES = ("sb_links.html", )

# Footer config
SKIP_COLOPHON = True
CUSTOM_FOOTER = "footer_customtext.html"
CUSTOM_FOOTER_TEXT = "&copy; 2003 - 2018 {} under a " \
                     "<a href=\"http://creativecommons.org/licenses/by-nc-sa/3.0/\">" \
                     "Creative Commons Attribution-NonCommercial-ShareAlike 3.0 license</a>".format(AUTHOR)

THEME = '../voidy-bootstrap'
STYLE_COLOUR = '#5C6448'

# Extra stylesheets, for bootstrap overrides or additional styling.
# STYLESHEET_FILES = ("voidybootstrap.css", "darkblue.css", "pygment_native.css",)
STYLESHEET_FILES = ("voidybootstrap.css?20170807", "olive.css?20170807",)

# Extra Markdown options, https://github.com/getpelican/pelican/issues/1238#issuecomment-32821905
# MD_EXTENSIONS = ['fenced_code', 'codehilite(css_class=highlight, linenums=True)', 'extra']
# MD_EXTENSIONS = ['fenced_code', 'codehilite(css_class=highlight, linenums=False)', 'extra']
MARKDOWN = {
    'extension_configs': {
        # 'markdown.extensions.codehilite': {'css_class': 'highlight'},
        'markdown.extensions.extra': {},
        'markdown.extensions.meta': {},
    },
    'output_format': 'html5',
}

# Enable highlight.js
HIGHLIGHTJS = True

DISPLAY_PAGES_ON_MENU = True
DEFAULT_PAGINATION = 10

PLUGIN_PATHS = ['../../others/pelican-plugins']
PLUGINS = ['neighbors', 'summary', 'similar_posts']

STATIC_PATHS = ['images']

# Generate JSON 'API'
TEMPLATE_PAGES = {'recent.json': 'api/recent.json', }
