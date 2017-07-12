# Django settings for leeps_website project.
import os

DEBUG = False
TEMPLATE_DEBUG = DEBUG

ADMINS = (
    ('James Pettit', 'james.l.pettit@gmail.com'),
)

MANAGERS = ADMINS

# ENGINE: 'postgresql_psycopg2', 'postgresql', 'mysql', 'sqlite3'
# NAME: Or path to database file if using sqlite3. or 'oracle'.
DATABASES = {
	'default': {
		  'ENGINE': 'django.db.backends.sqlite3',
		  'USER': '',
		  'NAME': '/var/www/leeps_website/sqlite.db',
		  'PASSWORD': '',
	}
}
# Set to empty string for localhost. Not used with sqlite3.

#"HOST":'',
# Set to empty string for default. Not used with sqlite3.
#"PORT":''

# Local time zone for this installation. Choices can be found here:
# http://en.wikipedia.org/wiki/List_of_tz_zones_by_name
# although not all choices may be avilable on all operating systems.
# If running in a Windows environment this must be set to the same as your
# system time zone.
TIME_ZONE = 'America/Los_Angeles'

# Language code for this installation. All choices can be found here:
# http://www.i18nguy.com/unicode/language-identifiers.html
LANGUAGE_CODE = 'en-us'

SITE_ID = 1

# If you set this to False, Django will make some optimizations so as not
# to load the internationalization machinery.
USE_I18N = True

# Absolute path to the directory that holds media.
# Example: "/home/media/media.lawrence.com/"
MEDIA_ROOT = '/var/www/leeps_website/media'

# URL that handles the media served from MEDIA_ROOT. Make sure to use a
# trailing slash if there is a path component (optional in other cases).
# Examples: "http://media.lawrence.com", "http://example.com/media/"
MEDIA_URL = '/media/'

# URL prefix for admin media -- CSS, JavaScript and images. Make sure to use a
# trailing slash.
# Examples: "http://foo.com/media/", "/media/".
ADMIN_MEDIA_PREFIX = '/static/admin/'

STATIC_ROOT = os.path.join(os.getcwd(), 'static')
STATIC_URL = '/static/'
STATICFILES_DIRS = (
    # Put strings here, like "/home/html/static" or "C:/www/django/static".
    # Always use forward slashes, even on Windows.
    # Don't forget to use absolute paths, not relative paths.
)

# Make this unique, and don't share it with anybody.
SECRET_KEY = 'uaeq(7p8p!3bzq8+mhwq*!l46*uyfnlcn*821e^_l5=s=ak@1@'

# List of callables that know how to import templates from various sources.
TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.Loader',
    'django.template.loaders.app_directories.Loader',
)

MIDDLEWARE_CLASSES = (
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.flatpages.middleware.FlatpageFallbackMiddleware',
    'django.middleware.doc.XViewMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
)

ROOT_URLCONF = 'leeps_website.urls'

TEMPLATE_DIRS = ('/var/www/leeps_website/templates',)

if os.getcwd() == '/home/www/leeps_website':
    TEMPLATE_DIRS = ('/home/www/leeps_website/templates',)

TEMPLATE_CONTEXT_PROCESSORS = (
    'django.contrib.auth.context_processors.auth',
    'django.core.context_processors.media',
    'django.contrib.messages.context_processors.messages',
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
    'django.contrib.staticfiles',
    'leeps_website.papers',
    'leeps_website.people',
    'leeps_website.projects',
    'leeps_website.classes',
    'leeps_website.misc',
    'south')

# disabled until SSL is working
#SESSION_COOKIE_SECURE = True
