#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

THEME = 'pelican-blueidea'
AUTHOR = 'Shingo Yamazaki'
SITENAME = 'Salesforce Developers.info'
SITEURL = ''

### For `pelican-clean-blog`
# HEADER_COVER = 'static/my_image.png'  # TODO
GITHUB_URL = 'http://github.com/zaki-yama'
TWITTER_URL = 'http://twitter.com/zaki___yama'
FACEBOOK_URL = 'http://facebook.com/shingo.yamazaki.12'

COLOR_SCHEME_CSS = 'github.css'
###

PATH = 'content'

TIMEZONE = 'Asia/Tokyo'

DEFAULT_LANG = 'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS = (('Pelican', 'http://getpelican.com/'),
         ('Python.org', 'http://python.org/'),
         ('Jinja2', 'http://jinja.pocoo.org/'),
         ('You can modify those links in your config file', '#'),)

# Social widget
SOCIAL = (('Twitter', 'http://twitter.com/zaki___yama'),
          ('GitHub', 'https://github.com/zaki-yama'),)

DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True


# Display pages list on the top menu
DISPLAY_PAGES_ON_MENU = True

# Display categories list on the top menu
DISPLAY_CATEGORIES_ON_MENU = False

# Display categories list as a submenu of the top menu
DISPLAY_CATEGORIES_ON_SUBMENU = False

# Display the category in the article's info
DISPLAY_CATEGORIES_ON_POSTINFO = False

# Display the author in the article's info
DISPLAY_AUTHOR_ON_POSTINFO = False

# Display the search form
DISPLAY_SEARCH_FORM = False

# Sort pages list by a given attribute
# PAGES_SORT_ATTRIBUTE = 'Title'

# Display the "Fork me on Github" banner
GITHUB_URL = 'https://github.com/zaki-yama/salesforce-developers-info'

# Blogroll
# LINKS = []

# Social widget
# SOCIAL = []
