<<<<<<< HEAD
=======
import os
>>>>>>> 21ca090 (Move loading of database to app factory. Create DataManager class to provide flexible interface for database functions. Addresses issue #24.)
from datetime import datetime
from flask import current_app as app
from flask_sqlalchemy import SQLAlchemy
<<<<<<< HEAD
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
=======
import pandas as pd

db = SQLAlchemy()

        

# This class is used to define the NetflixContent table in the database.
class NetflixContent(db.Model):
>>>>>>> 21ca090 (Move loading of database to app factory. Create DataManager class to provide flexible interface for database functions. Addresses issue #24.)
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
<<<<<<< HEAD
        """
        Returns:
            str: A string representation of the NetflixContent object.
        """
        return f'<NetflixContent {self.title}>'
=======
        return '<NetflixContent {}>'.format(self.title)
    


        
# This class defines a wrapper for the ORM model classes which provides a set of methods to interact with the database.
class DataManager:

    def __init__(self,
        tables=[NetflixContent],
        filename: str="/home/at/Documents/CODE/jatFlaskNextAPI/flask-server/app/static/netflix_ss.csv"):
        """
        Initializes the DataManager class.
        """
        self.tables = tables
        self.filename = filename
        self.loader = self.select_loader(filename)

    def read_data_from_csv(self):
        file_path = os.path.join(app.root_path, 'static', self.filename)
        data = pd.read_csv(file_path)
        return data.to_dict('records')

    def select_loader(self, filename: str):
        """
        Selects the loader function based on the filename.
        Args:
            filename (str): The name of the file.
        Returns:
            function: The loader function.
        """
        if filename and filename is not None:
            if filename == "/home/at/Documents/CODE/jatFlaskNextAPI/flask-server/app/static/netflix_ss.csv":
                return self.load_netflix_data
            else:
                raise ValueError(f"Invalid filename: {filename}")

    # This function is used to read data from a CSV file.
    def clean_netflix_data(self, df: pd.DataFrame):
        """
        Cleans the Netflix dataframe.
        Args:
            df (pandas.DataFrame): The Netflix dataframe.
        Returns:
            pandas.DataFrame: The cleaned Netflix dataframe.
        """
        # Drop all 'NaN' values, sort the dataframe by title and reset the index
        df = df.dropna().sort_values(by='title').reset_index(drop=True)
        
        # Remove 's' character from start of 'show_id' column and convert to integer
        df['show_id'] = df['show_id'].str[1:].astype(int)

        # Convert 'date_added' column to datetime format
        df['date_added'] = pd.to_datetime(df['date_added'])

        # Create new columns for the year, the month and the day the content was added
        df['year_added'] = df['date_added'].dt.year.astype(int)
        df['month_added'] = df['date_added'].dt.month_name()
        df['day_added'] = df['date_added'].dt.day_name()

        # Drop the 'date_added' column
        df = df.drop(columns=['date_added'])

        # Create new integer column for the runtime of the content
        df['runtime'] = df['duration'].str.split(' ').str[0].astype(int)
        # Create new string column for the time denomination of the content
        df['time_denomination'] = df['duration'].str.split(' ').str[1]
        # Drop the 'duration' column
        df = df.drop(columns=['duration'])
        # Drop duplicate rows
        df = df.drop_duplicates()
        # Sort the dataframe by 'type' and 'title' and reset the index
        df = df.sort_values(by=['type', 'title']).reset_index(drop=True)

        # Return the dataframe
        return df

    # This function is used to load the Netflix content data from a CSV file into the database.
    def load_netflix_data(self):
        """
        Loads the Netflix content data from a CSV file into the database.
        Returns:
            dict: A dictionary containing the Netflix content data in JSON format.
        """
        try:
            # Read data from CSV file
            data = self.read_data_from_csv(self.filename)
            
            # Clean the Netflix data
            cleaned_data = self.clean_netflix_data(data)
            
            # Insert data into the database
            with db.session.begin():
                for row in cleaned_data.itertuples(index=False):
                    netflix_content = NetflixContent(*row)
                    db.session.add(netflix_content)
            
                    # Commit the changes
                    db.session.commit()
            
            return {"message": "Netflix content data loaded successfully."}
        except Exception as e:
            return {"error": f"Error loading Netflix content data: {e}"}
    
    
    def load_data(self):
        # Read in the CSV file
        df = pd.read_csv(self.filename)

        # Clean the Netflix data
        df = self.clean_netflix_data(df)

        # Load the dataframe into the database
        for _, row in df.iterrows():
            existing_content = self.tables[0].query.filter_by(show_id=row['show_id']).first()
            if existing_content is None:
                netflix_content = self.tables[0](
                    show_id=row['show_id'],
                    type=row['type'],
                    title=row['title'],
                    director=row['director'],
                    cast=row['cast'],
                    country=row['country'],
                    release_year=row['release_year'],
                    rating=row['rating'],
                    runtime=row['runtime'],
                    time_denomination=row['time_denomination'],
                    listed_in=row['listed_in'],
                    description=row['description']
                )
                db.session.add(netflix_content)
                db.session.commit()

    
    def query_all(self, index: int=None):
        """
        Retrieves all objects from the database.

        Returns:
            list: A list of objects.
        """
        target_table = self.tables[index] if index is not None else None
        return target_table.query.all()
    
    def query_by_id(self, id: int):
        """
        Retrieves an object from the database by its ID.

        Args:
            id (int): The ID of the object.

        Returns:
            object: The object with the specified ID.
        """
        return self.tables.query.get(id)
    
    def query_by_attribute(self, attribute: str, value: str):
        """
        Retrieves an object from the database by its attribute.

        Args:
            attribute (str): The attribute of the object.
            value (str): The value of the attribute.

        Returns:
            object: The object with the specified attribute.
        """
        return self.tables.query.filter(getattr(self.tables, attribute) == value).first()
    
    def query_by_attributes(self, attributes: dict):
        """
        Retrieves an object from the database by its attributes.

        Args:
            attributes (dict): The attributes of the object.

        Returns:
            object: The object with the specified attributes.
        """
        return self.tables.query.filter_by(**attributes).first()
    
    def query_by_attributes_all(self, attributes: dict):
        """
        Retrieves all objects from the database by their attributes.

        Args:
            attributes (dict): The attributes of the objects.

        Returns:
            list: A list of objects with the specified attributes.
        """
        return self.tables.query.filter_by(**attributes).all()
    
    def query_by_attributes_like(self, attributes: dict):
        """
        Retrieves all objects from the database by their attributes.

        Args:
            attributes (dict): The attributes of the objects.

        Returns:
            list: A list of objects with the specified attributes.
        """
        return self.tables.query.filter_by(**attributes).all()
    
>>>>>>> 21ca090 (Move loading of database to app factory. Create DataManager class to provide flexible interface for database functions. Addresses issue #24.)
