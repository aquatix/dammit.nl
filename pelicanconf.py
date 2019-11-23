#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = 'Michiel Scholten'
SITENAME = 'dammIT'
#SITENAME = '<img src="/images/dammit.svg" alt="dammIT" />'
SITEIMAGE = '/images/dammit_field_transparent.svg'
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
LINKS_disabled = (
    ('Felienne', 'http://www.felienne.com/'),
    ('Rands in Repose', 'http://randsinrepose.com/'),
    ('Ryan Rix', 'http://whatthefuck.computer/blog/'),
    ('Tibo Beijen', 'https://www.tibobeijen.nl/'),
    ('Vermyndax', 'http://galaxycow.com/'),
    ('Pixls.us FLOSS photography', 'https://pixls.us/'),
    ('Python.org', 'https://python.org/'),
    ('Jinja2', 'http://jinja.pocoo.org/'),
)

LINKS = [
    ('archives', '/archives.html'),
]

ICONS = [
    ('github', 'https://github.com/aquatix/dammit.nl'),
    ('feed', '/feeds/all.atom.xml'),
]

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
CUSTOM_FOOTER_TEXT = "&copy; 2003 - 2019 {} under a " \
                     "<a href=\"http://creativecommons.org/licenses/by-nc-sa/3.0/\">" \
                     "Creative Commons Attribution-NonCommercial-ShareAlike 3.0 license</a>".format(AUTHOR)

THEME = '../pelican-alchemy/alchemy'
BOOTSTRAP_CSS = 'https://bootswatch.com/4/lux/bootstrap.min.css'
THEME_CSS_OVERRIDES = [
    '/css/dammit_bootstrap.css',
    '//cdn.jsdelivr.net/gh/highlightjs/cdn-release@9.16.2/build/styles/darcula.min.css',
]
THEME_JS_OVERRIDES = [
    '//cdn.jsdelivr.net/gh/highlightjs/cdn-release@9.16.2/build/highlight.min.js',
    '/js/dammit.js',
]

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
DEFAULT_PAGINATION = 20

PLUGIN_PATHS = ['../../others/pelican-plugins', '../pelican-plugins']
PLUGINS = ['neighbors', 'summary', 'similar_posts']

STATIC_PATHS = ['images', 'css', 'js']

DIRECT_TEMPLATES = ['index', 'tags', 'categories', 'authors', 'archives', 'sitemap']
SITEMAP_SAVE_AS = 'sitemap.xml'

# Generate JSON 'API'
#TEMPLATE_PAGES = {'recent.json': 'api/recent.json', }
