from juriidilisedjuured.base import *

DEBUG = False

SECRET_KEY = get_env_variable('SECRET')

ADMINS = [
    ('Lauri Elias', 'laurileet@gmail.com')
]

ALLOWED_HOSTS = [
    '*',
]