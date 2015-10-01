#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

# add path
import os
import sys
sys.path.append(os.curdir)


AUTHOR = u'Mics'
SITENAME = u"Mics.tw"
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
LINKS = ()
#LINKS = (('Pelican', 'http://getpelican.com/'),
#         ('Python.org', 'http://python.org/'),)

# Social widget
SOCIAL = (('Facebook', 'https://www.facebook.com/mics8128'),
        ('GitHub', 'https://github.com/mics8128'),)

DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
RELATIVE_URLS = True

STATIC_PATHS = ['images', 'extra']
EXTRA_PATH_METADATA = {
                'extra/CNAME': {'path': 'CNAME'},
                'extra/favicon.ico': {'path': 'favicon.ico'},
                'extra/favicon.png': {'path': 'favicon.png'},
            }

# Direct theme
DIRECT_TEMPLATES = ['index', 'categories', 'authors', 'archives', 'search']

#Plugins
PLUGIN_PATHS = ['./pelican-plugins']
PLUGINS = ['tag_cloud', 'tipue_search', 'summary']

#Added setting
USE_FOLDER_AS_CATEGORY = False

DEFAULT_CATEGORY = "Post"
DISPLAY_PAGES_ON_MENU = True
DISPLAY_CATEGORIES_ON_MENU = False
DISPLAY_RECENT_POSTS_ON_SIDEBAR = True
# GITHUB_USER = "mics8128"


DEFAULT_DATE = 'fs'
DEFAULT_DATE_FORMAT = "%Y-%m-%d"

#URLs
ARTICLE_URL = 'posts/{date:%Y}/{date:%m}/{slug}/'
ARTICLE_SAVE_AS = 'posts/{date:%Y}/{date:%m}/{slug}/index.html'


#Theme setting
THEME = "./pelican-bootstrap3"
CC_LICENSE = "by-nc-sa"
FAVICON = "favicon.png"
FAVICON_IE = "favicon.ico"
