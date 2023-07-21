from .settings import *
from decouple import config

DEBUG = False

INTERNAL_IPS = config('INTERNAL_IPS_PROD')

ALLOWED_HOSTS = config('ALLOWED_HOSTS_PROD', cast=lambda v: [s.strip() for s in v.split(',')])

SE_X_FORWARDED_HOST = True
SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')
