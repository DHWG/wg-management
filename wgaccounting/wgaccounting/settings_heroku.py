from .settings import *
import dj_database_url

ALLOWED_HOSTS = ['localhost', '127.0.0.1', 'dhwg-management.herokuapp.com']

DATABASES = {
    'default': dj_database_url.config()
}
