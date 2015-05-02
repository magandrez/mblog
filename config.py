WTF_CSRF_ENABLED = True
SECRET_KEY = 'Try-to-guess-it'

OPENID_PROVIDERS = [
    {'name': 'Yahoo', 'url': 'https://me.yahoo.com/'},
    {'name': 'Flickr', 'url': 'http://www.flickr.com/photos/<username>'}]

import os
basedir = os.path.abspath(os.path.dirname(__file__))

SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'app.db')
SQLALCHEMY_MIGRATE_REPO = os.path.join(basedir, 'db_repository')
