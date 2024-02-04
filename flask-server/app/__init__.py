# Description: Flask server for the application
# Author: Andrew Tomich

from flask import Flask
from config import Config
from flask_cors import CORS
from .models import db

cors = CORS()

def create_app(config_class=Config):
    app = Flask(__name__,
                # static_url_path='/flask-server/app/static',
                # static_url_path='/home/at/SOURCE/jatFlaskNextAPI/flask-server/app/static',
                # static_folder='/app/static'
    ) 
    app.config.from_object(config_class)
    db.init_app(app)
    cors.init_app(app)

    with app.app_context():
        db.create_all()
        from . import routes, models

    

    return app
