import os
from datetime import datetime
from flask_sqlalchemy import SQLAlchemy

connection_string = f"Driver={'ODBC Driver 18 for SQL Server'}; \
    Server=tcp:jatdev.database.windows.net,1433; \
        Database=flaskapi; \
            Uid=jandr; \
                Pwd=f'{os.environ.get('DB_PASSWORD', '')}'; \
                    Encrypt=yes; \
                        TrustServerCertificate=no; \
                            Connection Timeout=30;"

db = SQLAlchemy()


# This class is used to define the NetflixContent table in the database.
class NetflixContent(db.Model):
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
    created_at = db.Column(db.DateTime())
    updated_at = db.Column(db.DateTime())

    
    def __init__(
            self,
            show_id,
            type,
            title,
            director,
            cast,
            country,
            release_year,
            rating,
            runtime,
            time_denomination,
            listed_in,
            description,
            year_added,
            month_added,
            day_added,
            created_at=datetime.now(),
            updated_at=datetime.now()
            ):
        """
        Args:
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
            year_added (int): The year the content was added to Netflix.
            month_added (str): The month the content was added to Netflix.
            day_added (str): The day the content was added to Netflix.
        """
        self.show_id = show_id
        self.type = type
        self.title = title
        self.director = director
        self.cast = cast
        self.country = country
        self.release_year = release_year
        self.rating = rating
        self.runtime = runtime
        self.time_denomination = time_denomination
        self.listed_in = listed_in
        self.description = description
        self.year_added = year_added
        self.month_added = month_added
        self.day_added = day_added
        self.created_at = created_at
        self.updated_at = updated_at

    def __repr__(self):
        """
        Returns:
            str: A string representation of the NetflixContent object.
        """
        return f'<NetflixContent {self.title}>'
