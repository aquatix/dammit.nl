#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

# This file is only used if you use `make publish` or
# explicitly specify it as your config file.

import os
import sys
sys.path.append(os.curdir)
from pelicanconf import *

SITEURL = 'https://dammit.nl'
RELATIVE_URLS = False

FEED_ALL_ATOM = 'feeds/all.atom.xml'
CATEGORY_FEED_ATOM = 'feeds/{slug}.atom.xml'
TAG_FEED_ATOM = 'feeds/tag_{slug}.atom.xml'

FEED_MAX_ITEMS = 20

DELETE_OUTPUT_DIRECTORY = True

# Following items are often useful when publishing

# DISQUS_SITENAME = ""
ISSO_URL = 'https://dammit.nl/comments'

# GOOGLE_ANALYTICS = 'UA-10643901-3'

# PIWIK_URL = 'https://aquariusoft.org/r00t/webstats/'
# PIWIK_SSL_URL = ''
# PIWIK_SITE_ID = '2'
