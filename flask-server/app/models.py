from sqlalchemy.ext.declarative import declarative_base
from datetime import datetime
from flask import jsonify
from flask_sqlalchemy import SQLAlchemy
from flask import Flask

db = SQLAlchemy()


Base = declarative_base()

# This class is used to define the NetflixContent table in the database.
class NetflixContent(Base):
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
        date_added (str): The date when the content was added to Netflix.
        release_year (int): The release year of the content.
        rating (str): The rating of the content.
        duration (str): The duration of the content.
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
    date_added = db.Column(db.String(100))
    release_year = db.Column(db.Integer)
    rating = db.Column(db.String(10))
    duration = db.Column(db.String(10))
    listed_in = db.Column(db.String(100))
    description = db.Column(db.Text)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow)

    def __repr__(self):
        return '<NetflixContent {}>'.format(self.title)
    
    def to_dict(self):
        """
        Converts the NetflixContent object to a dictionary.

        Returns:
            dict: A dictionary representation of the NetflixContent object.
        """
        return {
            'id': self.id,
            'show_id': self.show_id,
            'type': self.type,
            'title': self.title,
            'director': self.director,
            'cast': self.cast,
            'country': self.country,
            'date_added': self.date_added,
            'release_year': self.release_year,
            'rating': self.rating,
            'duration': self.duration,
            'listed_in': self.listed_in,
            'description': self.description,
            'created_at': self.created_at,
            'updated_at': self.updated_at
        }
    
    def to_json(self):
        """
        Converts the NetflixContent object to a JSON response.

        Returns:
            Response: A JSON response containing the NetflixContent object.
        """
        return jsonify(self.to_dict())

    def to_json_list(self):
        """
        Converts a list of NetflixContent objects to a JSON response.

        Returns:
            Response: A JSON response containing a list of NetflixContent objects.
        """
        return jsonify([i.to_dict() for i in self])


