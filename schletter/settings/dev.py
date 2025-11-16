import os
from .base import *
from dotenv import load_dotenv
load_dotenv()

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

env = os.environ.copy()
SECRET_KEY = env['SECRET_KEY']

ALLOWED_HOSTS = ['*']

INTERNAL_IPS = ['127.0.0.1', ]

STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'static'),
]
