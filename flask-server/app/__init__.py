# Description: Flask server for the application
# Author: Andrew Tomich

from flask import Flask
from config.custom_config import Config
from app.models import db, check_or_load_data


def create_app(config_class: Config = Config):
    app = Flask(__name__,
                static_url_path='/home/at/Documents/CODE/jatFlaskNextAPI/flask-server/app/static',
                static_folder='/app/static',
    ) 
    app.config.from_object(config_class)
    db.init_app(app)

    with app.app_context():
        from . import routes
        check_or_load_data()

    return app
