# Django settings for leeps_website project.

import os
ROOT_DIR = os.getcwd()

DEVEL = ROOT_DIR != '/opt/local/var/leeps_website/'

DEBUG = DEVEL
TEMPLATE_DEBUG = DEBUG

ADMINS = (
    ('James Pettit', 'james.l.pettit@gmail.com'),
)

MANAGERS = ADMINS

# ENGINE: 'postgresql_psycopg2', 'postgresql', 'mysql', 'sqlite3'
# NAME: Or path to database file if using sqlite3. or 'oracle'.
if DEVEL:
    DATABASE_ENGINE = 'sqlite3'
    DATABASE_USER = ''
    DATABASE_NAME = os.path.join(ROOT_DIR, 'leeps_website.db')
    DATABASE_PASSWORD = ''
else:
    DATABASE_ENGINE = 'mysql'
    DATABASE_USER = 'leeps'
    DATABASE_NAME = 'leeps_website'
    DATABASE_PASSWORD = '*leeps*'
# Set to empty string for localhost. Not used with sqlite3.
DATABASE_HOST = ''
# Set to empty string for default. Not used with sqlite3.
DATABASE_PORT = ''

# Local time zone for this installation. Choices can be found here:
# http://en.wikipedia.org/wiki/List_of_tz_zones_by_name
# although not all choices may be avilable on all operating systems.
# If running in a Windows environment this must be set to the same as your
# system time zone.
TIME_ZONE = 'America/Pacific'

# Language code for this installation. All choices can be found here:
# http://www.i18nguy.com/unicode/language-identifiers.html
LANGUAGE_CODE = 'en-us'

SITE_ID = 1

# If you set this to False, Django will make some optimizations so as not
# to load the internationalization machinery.
USE_I18N = True

# Absolute path to the directory that holds media.
# Example: "/home/media/media.lawrence.com/"
if DEVEL:
    MEDIA_ROOT = os.path.join(ROOT_DIR, 'site_media')
else:
    MEDIA_ROOT = '/opt/local/var/leeps_website/site_media'
FILE_UPLOAD_MAX_MEMORY_SIZE=10485760

# URL that handles the media served from MEDIA_ROOT. Make sure to use a
# trailing slash if there is a path component (optional in other cases).
# Examples: "http://media.lawrence.com", "http://example.com/media/"
if DEVEL:
    MEDIA_URL = '/site_media/'
else:
    MEDIA_URL = 'http://leeps.ucsc.edu/site_media/'

# URL prefix for admin media -- CSS, JavaScript and images. Make sure to use a
# trailing slash.
# Examples: "http://foo.com/media/", "/media/".
ADMIN_MEDIA_PREFIX = '/media/'

# Make this unique, and don't share it with anybody.
SECRET_KEY = 'uaeq(7p8p!3bzq8+mhwq*!l46*uyfnlcn*821e^_l5=s=ak@1@'

# List of callables that know how to import templates from various sources.
TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.load_template_source',
    'django.template.loaders.app_directories.load_template_source',
#     'django.template.loaders.eggs.load_template_source',
)

MIDDLEWARE_CLASSES = (
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.flatpages.middleware.FlatpageFallbackMiddleware',
    'django.middleware.doc.XViewMiddleware',
)

ROOT_URLCONF = 'leeps_website.urls'

TEMPLATE_DIRS = (
    # Put strings here, like "/home/html/django_templates" or "C:/www/django/templates".
    # Always use forward slashes, even on Windows.
    # Don't forget to use absolute paths, not relative paths.
    os.path.join(ROOT_DIR, 'templates'),
)

TEMPLATE_CONTEXT_PROCESSORS = (
    'django.core.context_processors.auth',
    'django.core.context_processors.media',
)

INSTALLED_APPS = (
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.admin',
    'django.contrib.markup',
    'django.contrib.sitemaps',
    'django.contrib.flatpages',
    'leeps_website.papers',
    'leeps_website.people',
    'leeps_website.projects',
    'leeps_website.classes',
    'leeps_website.misc',
    'leeps_website',
)
