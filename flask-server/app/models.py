import os
from sqlalchemy.ext.declarative import declarative_base
from datetime import datetime
from flask_sqlalchemy import SQLAlchemy
import pandas as pd
from flask import current_app as app
import sqlite3
from sqlalchemy import MetaData

db = SQLAlchemy()

Base = declarative_base()


# This class is used to define the NetflixContent table in the database.
class NetflixContent(Base, db.Model):
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
    date_added = db.Column(db.DateTime(100))
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

    def __init__(self,
                 tablename=__tablename__,
                 id=id,
                 show_id=show_id,
                 type=type,
                 title=title,
                 director=director,
                 cast=cast,
                 country=country,
                 date_added=date_added, 
                 release_year=release_year,
                 rating=rating,
                 runtime=runtime,
                 time_denomination=time_denomination,
                 listed_in=listed_in,
                 description=description,
                 year_added=year_added,
                 month_added=month_added,
                 day_added=day_added):
        self.id = id
        self.show_id = show_id
        self.type = type
        self.title = title
        self.director = director
        self.cast = cast
        self.country = country
        self.date_added = date_added
        self.release_year = release_year
        self.rating = rating
        self.runtime = runtime
        self.time_denomination = time_denomination
        self.listed_in = listed_in
        self.description = description
        self.year_added = year_added
        self.month_added = month_added
        self.day_added = day_added
        self.tablename = tablename

    def __repr__(self):
        return '<NetflixContent {}>'.format(self.title)
    
    def query_all(self):
        """
        Retrieves all NetflixContent objects from the database.

        Returns:
            list: A list of NetflixContent objects.
        """
        return self.query
    
    # def to_dict(self):
    #     """
    #     Converts the NetflixContent object to a dictionary.

    #     Returns:
    #         dict: A dictionary representation of the NetflixContent object.
    #     """
    #     return {
    #         'id': self.id,
    #         'show_id': self.show_id,
    #         'type': self.type,
    #         'title': self.title,
    #         'director': self.director,
    #         'cast': self.cast,
    #         'country': self.country,
    #         'date_added': self.date_added,
    #         'release_year': self.release_year,
    #         'rating': self.rating,
    #         'duration': self.duration,
    #         'listed_in': self.listed_in,
    #         'description': self.description,
    #         'created_at': self.created_at,
    #         'updated_at': self.updated_at
    #     }
    
    # def to_json(self):
    #     """
    #     Converts the NetflixContent object to a JSON response.

    #     Returns:
    #         Response: A JSON response containing the NetflixContent object.
    #     """
    #     return jsonify(self.to_dict())

    # def to_json_list(self):
    #     """
    #     Converts a list of NetflixContent objects to a JSON response.

    #     Returns:
    #         Response: A JSON response containing a list of NetflixContent objects.
    #     """
    #     return jsonify([i.to_dict() for i in self])

def read_data_from_csv(filename):
    file_path = os.path.join(app.root_path, 'static', filename)
    data = pd.read_csv(file_path)
    return data.to_dict('records')

def load_dataframe_to_sqlite(dataframe, database_name, table_name):
    """
    Loads a pandas DataFrame into a SQLite database.

    Args:
        dataframe (pandas.DataFrame or list): The DataFrame or list to be loaded.
        database_name (str): The name of the SQLite database.
        table_name (str): The name of the table to be created.

    Returns:
        bool: True if the DataFrame is successfully loaded, False otherwise.
    """
    try:
        # Connect to the SQLite database
        conn = sqlite3.connect(database_name)

        # Convert list to DataFrame if necessary
        if isinstance(dataframe, list):
            dataframe = pd.DataFrame(dataframe)

        # Load the DataFrame into the database
        dataframe.to_sql(table_name, conn, if_exists='replace', index=False)

        # Commit the changes and close the connection
        conn.commit()
        conn.close()

        return True
    except Exception as e:
        print(f"Error loading DataFrame to SQLite database: {e}")
        return False

def are_tables_formatted():
    """
    Checks if the tables are properly formatted.

    Returns:
        bool: True if the tables are properly formatted, False otherwise.
    """
    try:
        # Get the table names from the database
        meta = MetaData()
        meta.reflect(bind=db.engine)
        table_names = [table.name for table in meta.tables.values()]

        # Check if the table names match the class names
        if set(table_names) == set([NetflixContent.__tablename__]):
            return True
        else:
            return False
    except Exception as e:
        print(f"Error checking table formatting: {e}")
        return False
    
def drop_tables():
    """
    Drops all tables from the database.

    Returns:
        bool: True if the tables are dropped, False otherwise.
    """
    try:
        # Drop all tables from the database
        with app.app_context():
            db.drop_all()
        return True
    except Exception as e:
        print(f"Error dropping tables: {e}")
        return False

def check_or_load_data():
    # Check if the database file exists
    if not os.path.exists('app.db'):
        # Load data from 'netflix_ss.csv' file
        data = read_data_from_csv('netflix_ss.csv')
        
        # Create the database and tables
        with app.app_context():
            db.create_all()
        
        # Insert data into the database
        load_dataframe_to_sqlite(data, 'app.db', 'netflix_content')
    else:
        # Check if the tables are properly formatted
        if not are_tables_formatted():
            # Drop existing tables
            drop_tables()
            
            # Create new tables
            with app.app_context():
                db.create_all()
            
            # Load data from 'netflix_ss.csv' file
            data = read_data_from_csv('netflix_ss.csv')
            
            # Insert data into the database
            load_dataframe_to_sqlite(data, 'app.db', 'netflix_content')
        


