# Description: Configuration file for Flask app
# Author: Andrew Tomich

import os

basedir = os.path.join(os.path.abspath(os.path.dirname(__file__)), '..')


class Config(object):
    SECRET_KEY=os.environ.get('FLASK_SECRET_KEY', 'better-fix-this-asap')
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL', 'sqlite:///' + os.path.join(basedir, 'flask-server/app.db'))
    SQLALCHEMY_TRACK_MODIFICATIONS=False
    TESTING=os.environ.get('TESTING', False)
    FLASK_ENV='development' if TESTING else os.environ.get('FLASK_ENV', 'production')
    FLASK_DEBUG=0 if FLASK_ENV == 'production' else 1
    FLASK_APP=os.environ.get('FLASK_APP', 'app.py')
    CORS_ORIGINS=['*']
    CORS_ALLOW_HEADERS=['Access-Control-Allow-Origin', 'Content-Type', 'Authorization']
