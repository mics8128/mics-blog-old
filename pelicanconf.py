#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

# add path
import os
import sys
sys.path.append(os.curdir)


AUTHOR = u'Mics'
SITENAME = u"Mics Blog"
SITEURL = ''

PATH = 'content'

TIMEZONE = 'Asia/Taipei'

DEFAULT_LANG = u'zh-TW'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS = (('Pelican', 'http://getpelican.com/'),
         ('Python.org', 'http://python.org/'),)

# Social widget
SOCIAL = (('Facebook', 'https://www.facebook.com/mics8128'),
        ('GitHub', 'https://github.com/mics8128'),)

DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
RELATIVE_URLS = True

STATIC_PATHS = ['images', 'extra/CNAME']
EXTRA_PATH_METADATA = {'extra/CNAME': {'path': 'CNAME'},}

#Added setting
USE_FOLDER_AS_CATEGORY = True
DEFAULT_CATEGORY = "others"
DISPLAY_PAGES_ON_MENU = True
DISPLAY_CATEGORIES_ON_MENU = False
DEFAULT_DATE = 'fs'
DEFAULT_DATE_FORMAT = "%Y-%m-%d (%a)"
THEME = "pelican-bootstrap3"




#URLs
ARTICLE_URL = 'articles/{date:%Y}/{date:%m}/{slug}/'
ARTICLE_SAVE_AS = 'articles/{date:%Y}/{date:%m}/{slug}/index.html'
