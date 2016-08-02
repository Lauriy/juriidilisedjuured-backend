from juriidilisedjuured.base import *

DEBUG = False

SECRET_KEY = get_env_variable('SECRET_KEY')

ADMINS = [
    ('Lauri Elias', 'laurileet@gmail.com')
]

ALLOWED_HOSTS = [
    '*',
]