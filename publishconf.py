#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

# This file is only used if you use `make publish` or
# explicitly specify it as your config file.

import os
import sys
sys.path.append(os.curdir)
from pelicanconf import *

SITEURL = 'http://zaki-yama.github.io/salesforce-developers-info'
RELATIVE_URLS = False

# FEED_ALL_ATOM = 'feeds/all.atom.xml'
# CATEGORY_FEED_ATOM = 'feeds/%s.atom.xml'
FEED_ALL_RSS = 'feeds/all.rss.xml'
CATEGORY_RSS_ATOM = 'feeds/%s.rss.xml'

DELETE_OUTPUT_DIRECTORY = True

# Following items are often useful when publishing

DISQUS_SITENAME = 'salesforce-developers-info'
GOOGLE_ANALYTICS = 'UA-46209909-3'
