from .settings_common import *

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []

# logging settings
LOGGING = {
    'version': 1,
    # ignore existing logger
    'disable_existing_loggers': False,

    # logger settings
    'Loggers': {
        # Logger Django uses
        'Django': {
            'handlers': ['console'],
            'level': 'INFO',
        },
        # Logger diary uses
        'diary': {
            'handlers': ['console'],
            'level': 'DEBUG',
        }
    },
    # handler settings
    'handlers': {
        'console': {
            'level': 'DEBUG',
            # output on console
            'class': 'logging.StreamHandler',
            'formatter': 'dev'
        },
    },

    # formatter settings
    'formatters': {
        'dev': {
            'format': '\t'.join([
                '%(asctime)s',
                '[%(levelname)s]',
                '%(pathname)s(Line:%(lineno)d)'
                '%(messages)s'
            ])
        }
    }
}

# required to send email
EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'