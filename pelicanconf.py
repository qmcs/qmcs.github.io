#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

import pelicanium


AUTHOR = 'Contributors'
SITENAME = 'Computing'
SITESUBTITLE = 'Society at Queen Mary'
SITEURL = ''
SITE_TITLE = 'QM ' + SITENAME + ' Society'

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
    'summary',
    'pelican_extended_authors',
)

SUMMARY_BEGIN_MARKER = '-- PELICAN_BEGIN_SUMMARY --'
SUMMARY_END_MARKER = '-- PELICAN_END_SUMMARY --'


# Menu
DISPLAY_CATEGORIES_ON_MENU = False
MENUITEMS = (
    ('Archive', 'archives.html'),
    ('Tags', 'tags.html'),
    ('Authors', 'authors.html'),
)

# Blogroll
LINKS = (
    ('Pelican', 'http://getpelican.com/'),
    ('Python.org', 'http://python.org/'),
    ('Jinja2', 'http://jinja.pocoo.org/'),
)

# Social widget
SOCIAL = (
    ('Facebook', 'https://www.facebook.com/groups/723364331026623/'),
    ('Twitter', 'https://twitter.com/pyclub_qm'),
)

DEFAULT_PAGINATION = False

LOGO = "static/images/main.png"
FAVICON = "static/images/favicon.ico"
COVER_IMG = 'static/images/cover.jpg'

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True

DISQUS_SITENAME = 'qmcs'
GITHUB_URL = 'https://github.com/qmcs/qmcs.github.io'
GOOGLE_ANALYTICS = 'UA-49253245-1'
TWITTER_USERNAME = 'pyclub_qm'

STATIC_PATHS = (
    'static/author_images',
    'static/images',
    'extra/CNAME',
)

EXTRA_PATH_METADATA = {
    'extra/CNAME': {'path': 'CNAME'},
}
