from .settings import *
from decouple import config

DEBUG = True

ALLOWED_HOSTS = config('ALLOWED_HOSTS_DEV', cast=lambda v: [s.strip() for s in v.split(',')])

INTERNAL_IPS = config('INTERNAL_IPS_DEV')

INSTALLED_APPS += [

    'debug_toolbar',

]
MIDDLEWARE += [

    'debug_toolbar.middleware.DebugToolbarMiddleware',

]
