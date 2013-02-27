#!/usr/bin/env python
# -*- coding: utf-8 -*- #

AUTHOR = u'herlo'
SITENAME = u'The GoOSe Project'
SITESUBTITLE = u'A Community Enterprise Linux Rebuild'
INDEX_WELCOME = u'Welcome to the GoOSe Project'
SITEURL = 'http://gooseproject.org'

TIMEZONE = 'America/Denver'

DEFAULT_LANG = u'en'

# Blogroll
#LINKS = (('GoOSe Linux Github', 'https://github.com/organization/gooseproject'),
#        ('Pelican', 'http://docs.notmyidea.org/alexis/pelican/'),)

# Social widget
#SOCIAL = (('You can add links in your config file', '#'),
#          ('Another social link', '#'),)

THEME = 'themes/chunk'
LINKS = (('Download', 'downloads.html'), ('News', 'news.html'), ('Home', 'index.html'), )

INDEX_SAVE_AS = 'news.html'
PAGE_SAVE_AS = '{slug}.html'
PAGE_URL = '{slug}.html'

DELETE_OUTPUT_DIRECTORY = True

DISPLAY_CATEGORIES_ON_MENU = False
REVERSE_CATEGORY_ORDER = True
DEFAULT_PAGINATION = 5
DEFAULT_DATE = 'fs'
DEFAULT_CATEGORY = 'Community'
