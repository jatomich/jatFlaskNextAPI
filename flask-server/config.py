# Description: Configuration file for Flask app
# Author: Andrew Tomich

import os

basedir = os.path.join(os.path.abspath(os.path.dirname(__file__)), '..')


class Config(object):
    SECRET_KEY=os.environ.get('FLASK_SECRET_KEY', 'better-fix-this-asap')
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL', 'sqlite:///' + os.path.join(basedir, 'flask-server/app/app.db'))
    SQLALCHEMY_TRACK_MODIFICATIONS=False
    TESTING=os.environ.get('TESTING', False)
    FLASK_ENV='development' if TESTING else os.environ.get('FLASK_ENV', 'production')
    FLASK_DEBUG=0 if FLASK_ENV == 'production' else 1
    FLASK_APP=os.environ.get('FLASK_APP', 'app.py')
    CORS_HEADERS='Content-Type',
    CORS_RESOURCES={r"/*": {"origins": "*"}},
    CORS_ORIGINS='*',
    # CORS_SUPPORTS_CREDENTIALS=True,
    CORS_EXPOSE_HEADERS='*',
    CORS_MAX_AGE=86400,
    CORS_SEND_WILDCARD=True,
    CORS_ALWAYS_SEND=True,
    CORS_AUTOMATIC_OPTIONS=True,
    CORS_ALLOW_HEADERS='*',
    CORS_ALLOW_METHODS='*',

    # STATIC_FOLDER=os.path.join(basedir, 'app/static')
    # STATIC_URL_PATH='/static'
