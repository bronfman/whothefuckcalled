"""Common settings and globals."""


from os.path import abspath, basename, dirname, join, normpath


########## PATH CONFIGURATION
# Absolute filesystem path to the Django project directory:
DJANGO_ROOT = dirname(dirname(abspath(__file__)))

# Absolute filesystem path to the top-level project folder:
SITE_ROOT = dirname(DJANGO_ROOT)

# Site name:
SITE_NAME = basename(DJANGO_ROOT)
########## END PATH CONFIGURATION


########## DEBUG CONFIGURATION
# See: https://docs.djangoproject.com/en/1.3/ref/settings/#debug
DEBUG = False

# See: https://docs.djangoproject.com/en/1.3/ref/settings/#template-debug
TEMPLATE_DEBUG = DEBUG
########## END DEBUG CONFIGURATION


########## MANAGER CONFIGURATION
# See: https://docs.djangoproject.com/en/1.3/ref/settings/#admins
ADMINS = (
    ('Randall Degges', 'rdegges@gmail.com'),
)

# See: https://docs.djangoproject.com/en/1.3/ref/settings/#managers
MANAGERS = ADMINS
########## END MANAGER CONFIGURATION


########## DATABASE CONFIGURATION
# See: https://docs.djangoproject.com/en/1.3/ref/settings/#databases
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.',
        'NAME': '',
        'USER': '',
        'PASSWORD': '',
        'HOST': '',
        'PORT': '',
    }
}
########## END DATABASE CONFIGURATION


########## GENERAL CONFIGURATION
# See: https://docs.djangoproject.com/en/1.3/ref/settings/#time-zone
TIME_ZONE = 'America/Los_Angeles'

# See: https://docs.djangoproject.com/en/1.3/ref/settings/#language-code
LANGUAGE_CODE = 'en-us'

# See: https://docs.djangoproject.com/en/1.3/ref/settings/#site-id
SITE_ID = 1

# See: https://docs.djangoproject.com/en/1.3/ref/settings/#use-i18n
USE_I18N = True

# See: https://docs.djangoproject.com/en/1.3/ref/settings/#use-l10n
USE_L10N = True
########## END GENERAL CONFIGURATION


########## MEDIA CONFIGURATION
# See: https://docs.djangoproject.com/en/1.3/ref/settings/#media-root
MEDIA_ROOT = normpath(join(DJANGO_ROOT, 'media'))

# See: https://docs.djangoproject.com/en/1.3/ref/settings/#media-url
MEDIA_URL = '/media/'
########## END MEDIA CONFIGURATION


########## STATIC FILE CONFIGURATION
# See: https://docs.djangoproject.com/en/1.3/ref/settings/#static-root
STATIC_ROOT = normpath(join(DJANGO_ROOT, 'static'))

# See: https://docs.djangoproject.com/en/1.3/ref/settings/#static-url
STATIC_URL = '/static/'

# See: https://docs.djangoproject.com/en/1.3/ref/settings/#admin-media-prefix
ADMIN_MEDIA_PREFIX = '/static/admin/'

# See: https://docs.djangoproject.com/en/1.3/ref/contrib/staticfiles/#std:setting-STATICFILES_DIRS
STATICFILES_DIRS = (
    normpath(join(DJANGO_ROOT, 'assets')),
)

# See: https://docs.djangoproject.com/en/1.3/ref/contrib/staticfiles/#staticfiles-finders
STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
)
########## END STATIC FILE CONFIGURATION


########## DAJAXICE CONFIGURATION
# See: http://docs.dajaxproject.com/dajaxice/available-settings.html#dajaxice-media-prefix
DAJAXICE_MEDIA_PREFIX = 'dajaxice'
########## END DAJAXICE CONFIGURATION


########## FIXTURE CONFIGURATION
# Directories to search when loading fixture data.
FIXTURE_DIRS = (
    normpath(join(DJANGO_ROOT, 'fixtures')),
)
########## END FIXTURE CONFIGURATION


########## SECRET CONFIGURATION
# See: https://docs.djangoproject.com/en/1.3/ref/settings/#secret-key
SECRET_KEY = 'rj(k$z-@@kkhowzdrf)d(sv1w^d_a4twj1!4b0j(hyymu+v36h'
########## END SECRET CONFIGURATION


########## TEMPLATE CONFIGURATION
# See: https://docs.djangoproject.com/en/1.3/ref/settings/#template-context-processors
TEMPLATE_CONTEXT_PROCESSORS = (
    'django.contrib.auth.context_processors.auth',
    'django.core.context_processors.debug',
    'django.core.context_processors.i18n',
    'django.core.context_processors.media',
    'django.core.context_processors.static',
    'django.core.context_processors.request',
    'django.contrib.messages.context_processors.messages',
)

# See: https://docs.djangoproject.com/en/1.3/ref/settings/#template-loaders
TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.Loader',
    'django.template.loaders.app_directories.Loader',
    'django.template.loaders.eggs.Loader',
)

# See: https://docs.djangoproject.com/en/1.3/ref/settings/#template-dirs
TEMPLATE_DIRS = (
    normpath(join(DJANGO_ROOT, 'templates')),
)
########## END TEMPLATE CONFIGURATION


########## MIDDLEWARE CONFIGURATION
# See: https://docs.djangoproject.com/en/1.3/ref/settings/#middleware-classes
MIDDLEWARE_CLASSES = (
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
)
########## END MIDDLEWARE CONFIGURATION


########## URL CONFIGURATION
# See: https://docs.djangoproject.com/en/1.3/ref/settings/#root-urlconf
ROOT_URLCONF = 'wtf.urls'
########## END URL CONFIGURATION


########## APP CONFIGURATION
DJANGO_APPS = (
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    # Useful template tags:
    'django.contrib.humanize',

    # Admin panel and documentation:
    'django.contrib.admin',
    'django.contrib.admindocs',

    # AJAX helpers:
    'dajaxice',

    # South database migrations:
    'south',
)

LOCAL_APPS = (
    'apps.core',
)

# See: https://docs.djangoproject.com/en/1.3/ref/settings/#installed-apps
INSTALLED_APPS = DJANGO_APPS + LOCAL_APPS
########## END APP CONFIGURATION


########## LOGGING CONFIGURATION
# See: https://docs.djangoproject.com/en/1.3/ref/settings/#logging
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'handlers': {
        'mail_admins': {
            'level': 'ERROR',
            'class': 'django.utils.log.AdminEmailHandler'
        }
    },
    'loggers': {
        'django.request': {
            'handlers': ['mail_admins'],
            'level': 'ERROR',
            'propagate': True,
        },
    }
}
########## END LOGGING CONFIGURATION


########## CACHE CONFIGURATION
# See: http://jbalogh.me/projects/cache-machine/#settings
CACHE_COUNT_TIMEOUT = 60
########## END CACHE CONFIGURATION
