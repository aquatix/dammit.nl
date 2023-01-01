#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = 'Michiel Scholten'
SITENAME = 'dammIT'
#SITENAME = '<img src="/images/dammit.svg" alt="dammIT" />'
#SITEIMAGE = '/images/dammit_field_transparent.svg'
SITEIMAGE = '/images/dammit.svg'
SITEURL = ''  # Set in publishconf.py

SITEIMAGE_AS_TITLE = True

# Sub-title that goes underneath site name in jumbotron.
SITESUBTITLE = 'A rantbox'
SITETAG = 'dammIT'

PATH = 'content'

TIMEZONE = 'Europe/Paris'

DEFAULT_LANG = 'en'

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

# Add 'archives' to the top navigation
LINKS = [
    ('archives', '/archives.html'),
]

ICONS = [
    ('fab fa-github', 'https://github.com/aquatix/dammit.nl'),
    ('fas fa-rss', '/feeds/all.atom.xml'),
    ('fab fa-mastodon', 'https://mastodon.social/@diginaut'),
    ('fas fa-coffee', 'https://ko-fi.com/aquatix'),
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

DESCRIPTION = 'Weblog/rantbox of Michiel Scholten, software developer, photography enthousiast and all around nerd. Expect howtos, ramblings and random findings'

# The default metadata you want to use for all articles and pages.
DEFAULT_METADATA = {
    # 'description': 'Weblog/rantbox of Michiel Scholten, software developer, photography enthousiast and all around nerd. Expect howtos, ramblings and random findings',
    # 'status': 'draft'
}

# Uncomment following line if you want document-relative URLs when developing
# RELATIVE_URLS = True

THEME = '../pelican-alchemy/alchemy'
BOOTSTRAP_CSS = 'https://bootswatch.com/4/lux/bootstrap.min.css'

# Enable highlight.js
THEME_CSS_OVERRIDES = [
    '/css/dammit_bootstrap.css?20221110',
    #'https://cdn.jsdelivr.net/gh/highlightjs/cdn-release@11.2.0/build/styles/base16/3024.min.css',
    'https://cdn.jsdelivr.net/gh/highlightjs/cdn-release@11.7.0/build/styles/devibeans.min.css',
]
THEME_JS_OVERRIDES = [
    'https://cdn.jsdelivr.net/gh/highlightjs/cdn-release@11.7.0/build/highlight.min.js',
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
        'markdown.extensions.admonition': {},
    },
    'output_format': 'html5',
}

DISPLAY_PAGES_ON_MENU = True
DEFAULT_PAGINATION = 20

# YEAR_ARCHIVE_SAVE_AS = 'posts/{date:%Y}/index.html'

#PLUGINS = ['summary']

STATIC_PATHS = ['images', 'css', 'js']

DIRECT_TEMPLATES = ['index', 'tags', 'categories', 'authors', 'archives', 'sitemap']
SITEMAP_SAVE_AS = 'sitemap.xml'

# Generate JSON 'API'
THEME_TEMPLATES_OVERRIDES = [
    'templates',
]
TEMPLATE_PAGES = {'recent.json': 'api/recent.json', }
