import os
from datetime import datetime
from flask import current_app as app
from flask_sqlalchemy import SQLAlchemy
from json import JSONEncoder

db = SQLAlchemy()


# This class is used to define the NetflixContent table in the database.
class NetflixContent(db.Model):
    # Override the default JSONEncoder class to handle serialization of NetflixContent objects
    class NetflixContentEncoder(JSONEncoder):
        def default(self, obj):
            if isinstance(obj, NetflixContent):
                return obj.__dict__
            return super().default(obj)
    """
    Represents a Netflix content item.

    Attributes:
        id (int): The unique identifier of the content.
        show_id (int): The unique identifier of the show.
        type (str): The type of the content (e.g., movie, TV show).
        title (str): The title of the content.
        director (str): The director of the content.
        cast (str): The cast members of the content.
        country (str): The country where the content was produced.
        release_year (int): The release year of the content.
        rating (str): The rating of the content.
        runtime (int): The runtime of the content.
        time_denomination (str): The time denomination of the content (e.g., min, season).
        listed_in (str): The categories in which the content is listed.
        description (str): The description of the content.
        created_at (datetime): The timestamp when the content was created.
        updated_at (datetime): The timestamp when the content was last updated.
    """

    __tablename__ = 'netflix_content'
    id = db.Column(db.Integer, primary_key=True)
    show_id = db.Column(db.Integer, unique=True)
    type = db.Column(db.String(10))
    title = db.Column(db.String(100))
    director = db.Column(db.String(100))
    cast = db.Column(db.String(100))
    country = db.Column(db.String(100))
    release_year = db.Column(db.Integer)
    rating = db.Column(db.String(10))
    runtime = db.Column(db.Integer)
    time_denomination = db.Column(db.String(10))
    listed_in = db.Column(db.String(100))
    description = db.Column(db.Text)
    year_added = db.Column(db.Integer)
    month_added = db.Column(db.String(10))
    day_added = db.Column(db.String(10))
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow)

    def __repr__(self):
        """
        Returns:
            str: A string representation of the NetflixContent object.
        """
        return f'<NetflixContent {self.title}>'
