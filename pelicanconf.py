#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

def split(content, *args):
    return content.split(',')

JINJA_FILTERS = {
    'split': split,
}

AUTHOR = u'Masoko'
SITENAME = u'fun.masoko.net'
SITESUBTITLE = u'Подбрани вицове и мъдри мисли!'
SITEURL = ''

PATH = 'content'

TIMEZONE = 'Europe/Paris'

DEFAULT_LANG = u'bg'
HIDE_AUTHORS = True
# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS = ()

# Social widget
SOCIAL = (('You can add links in your config file', '#'),
          ('Another social link', '#'),)
SITEIMAGE = '/images/logo.png'
DEFAULT_PAGINATION = 10
PLUGIN_PATHS = ["plugins", "/home/pi/sites/pelican-plugins/pelican-plugins"]
PLUGINS = ['neighbors', 'metadataparsing', 'tipue_search']
THEME = '/home/pi/sites/fun/themes/pelican-alchemy/alchemy'
# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True
PAGE_SAVE_AS = '{slug}.html'
PAGE_URL = '{slug}.html'
### Theme specific settings
STATIC_PATHS = ['images', 'content']
RESPONSIVE_IMAGES = True

DIRECT_TEMPLATES = (('index', 'tags', 'categories', 'archives', 'search'))

