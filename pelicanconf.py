#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

THEME = 'pelican-mg'
AUTHOR = 'Shingo Yamazaki'
SITENAME = 'Salesforce Developers.info'
SITEURL = ''

MD_EXTENSIONS = [
    'nl2br',
    'linkify',
    # 'markdown_checklist.extension',
    # 'markdown_newtab',
    # 'embedly',
    'codehilite(css_class=highlight)', 'extra',  # default
]

PLUGIN_PATHS = []
PLUGINS = []

FAVICON = 'favicon.ico'
FAVICON_TYPE = 'image/vnd.microsoft.icon'
IPHONE_ICON = 'apple-touch-icon.png'

PATH = 'content'
STATIC_PATHS = ['images', 'extra']
EXTRA_PATH_METADATA = {
    'extra/' + FAVICON: {'path': FAVICON},
    'extra/' + IPHONE_ICON: {'path': IPHONE_ICON},
}

LOCALE = 'en_US'
TIMEZONE = 'Asia/Tokyo'
DATE_FORMATS = {
    'en': '%Y-%m-%d(%a)',
    'ja': '%Y-%m-%d(%a)',
}

TAG_SAVE_AS = ''
AUTHOR_SAVE_AS = ''
DIRECT_TEMPLATES = ('index', 'categories', 'archives', 'search', 'tipue_search')
TIPUE_SEARCH_SAVE_AS = 'tipue_search.json'

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
SOCIAL = (('twitter', 'https://twitter.com/zaki___yama'),
          ('github', 'https://github.com/zaki-yama'),
          ('pencil', 'http://dackdive.hateblo.jp'),
          )

SHARE = True

DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True


# Display pages list on the top menu
DISPLAY_PAGES_ON_MENU = True

# Display categories list on the top menu
DISPLAY_CATEGORIES_ON_MENU = True

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
GITHUB_URL = 'https://github.com/zaki-yama/salesforce-developers.info'

# Display "Tweet" button in the article
TWITTER_USERNAME = 'zaki___yama'
