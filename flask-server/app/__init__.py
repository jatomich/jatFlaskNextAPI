# Description: Flask server for the application
# Author: Andrew Tomich

from flask import Flask
from flask_cors import CORS
from app.models import db, DataManager
from config import Config

cors = CORS()

def create_app(config_class=Config):
    app = Flask(__name__,
                static_url_path='/home/at/Documents/CODE/jatFlaskNextAPI/flask-server/app/static',
                static_folder='/app/static',
    ) 
    app.config.from_object(config_class)
    db.init_app(app)
    cors.init_app(app)

    with app.app_context():
        from . import routes
        db.create_all()
        netflix_manager = DataManager()
        netflix_manager.load_netflix_data()


    return app
