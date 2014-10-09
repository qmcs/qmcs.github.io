#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

import pelicanium


AUTHOR = 'Contributors'
SITENAME = 'EECS Society'
SITESUBTITLE = 'Queen Mary University of London'
SITEURL = ''
SITE_TITLE = 'EECS Society at Queen Mary University of London'

TIMEZONE = 'Europe/London'

DEFAULT_LANG = 'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None

THEME = pelicanium.theme_path
EXTRA_TEMPLATES_PATHS = 'templates',

ARTICLE_EXCLUDES = ('pages', 'authors')
PAGE_EXCLUDES = ('authors',)

PLUGIN_PATH = 'src/pelican-plugins'
PLUGINS = (
    'pelican_edit_url',
    'pelican_extended_authors',
    'summary',
)

SUMMARY_BEGIN_MARKER = '-- PELICAN_BEGIN_SUMMARY --'
SUMMARY_END_MARKER = '-- PELICAN_END_SUMMARY --'

# Menu
DISPLAY_CATEGORIES_ON_MENU = False
MENUITEMS = (
    ('Blog', 'archives.html'),
    ('People', 'authors.html'),
)

# Blogroll
LINKS = (
    ('Pelican', 'http://getpelican.com/'),
    ('Python.org', 'http://python.org/'),
    ('Jinja2', 'http://jinja.pocoo.org/'),
)

# Social widget
SOCIAL = (
    ('Facebook', 'https://www.facebook.com/groups/eecssoc/'),
    ('Twitter', 'https://twitter.com/EECSSoc'),
)

DEFAULT_PAGINATION = False

LOGO = "static/images/main.png"
FAVICON = "static/images/favicon.ico"
COVER_IMG = 'static/images/cover.jpg'

# Uncomment following line if you want document-relative URLs when developing
# RELATIVE_URLS = True

DISQUS_SITENAME = 'qmcs'
GITHUB_URL = 'https://github.com/qmcs/qmcs.github.io'
GOOGLE_ANALYTICS = 'UA-49253245-1'
TWITTER_USERNAME = 'QMComputing'

STATIC_PATHS = (
    'static/author_images',
    'static/images',
    'static/cv',
    'static/article_covers',
    'extra/CNAME',
)

EXTRA_PATH_METADATA = {
    'extra/CNAME': {'path': 'CNAME'},
}

EDIT_CONTENT_URL = 'https://github.com/qmcs/qmcs.github.io/edit/pelican/{file_path}'
