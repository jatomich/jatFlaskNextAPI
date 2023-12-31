# Description: The view functions (along with any helper functions) for the Flask server.
# Author: Andrew Tomich

from flask import jsonify, current_app as app
from .models import DataManager, db
from enum import Enum


@app.route('/api/health', methods=['GET'])
def health_check():
    """
    Returns a JSON response with a message.
    """
    return jsonify({
        'data': "Success!"
    })


# class NetflixType(Enum):
#     """
#     An enumeration of the different types of Netflix media.
#     """
#     movies = 1
#     tv = 2

# @app.route('/netflix/tv', methods=['GET'])
# @app.route('/netflix/<string:type>', methods=['GET'])
@app.route('/netflix/movies', methods=['GET'])
def get_netflix_movies():
    """
    Retrieves a list of Netflix movies from a CSV file and returns them as a JSON response.

    Parameters:
        type (str): The type of Netflix content to retrieve.

    Returns:
        dict: A dictionary containing the movie data in JSON format.

    Raises:
        ValueError: If the specified Netflix type is invalid.
    """
    data_manager = DataManager()
    netflix_table = data_manager.tables[0]
    # netflix_manager = DataManager()
    # netflix_table = netflix_manager.tables[0]
    # Check if the specified type is valid
    # type_checker = netflix_manager.tables[0][type.lower()].value
    # if type_checker and type_checker is not None:
        # if type_checker == 1 or type_checker == 2:
        # Retrieve the Netflix content of the specified type from the database by querying the db object
    netflix_content = [media for media in netflix_table.query_by_attributes({'type': 'Movie'})]

    # Return the JSON response
    return jsonify({
        'data': [entry.to_dict() for entry in netflix_content]
    })
        # else:
            # Return an error message
            # return jsonify({
            #     'data': "Invalid Netflix type!"
            # })

    # return jsonify({
    #     'data': "Navigation error encountered!"
    # })


@app.route('/netflix', methods=['GET'])
def get_netflix_content():
    """
    Retrieves a list of Netflix content from the database and returns them as a JSON response.
    Args:
        type (str): The type of Netflix content to retrieve.
    Returns:
        dict: A dictionary containing the Netflix content data in JSON format.
    """
    # Instantiate a data manager object
    netflix_manager = DataManager()
    # Return the JSON response
    return jsonify({
        'data': [i.to_dict() for i in netflix_manager.tables[0].query.all()]
    })

# @app.route('/netflix', methods=['GET'])
# def load_database():
#     """
#     Loads the Netflix content data from a CSV file into the database.
#     Returns:
#         dict: A dictionary containing the Netflix content data in JSON format.
#     """
#     def clean_netflix_data(df: pd.DataFrame):
#         """
#         Cleans the Netflix dataframe.
#         Args:
#             df (pandas.DataFrame): The Netflix dataframe.
#         Returns:
#             pandas.DataFrame: The cleaned Netflix dataframe.
#         """
#         # Drop all 'NaN' values, sort the dataframe by title and reset the index
#         df = df.dropna().sort_values(by='title').reset_index(drop=True)
        
#         # Remove 's' character from start of 'show_id' column and convert to integer
#         df['show_id'] = df['show_id'].str[1:].astype(int)

#         # Convert 'date_added' column to datetime format
#         df['date_added'] = pd.to_datetime(df['date_added'])

#         # Create new columns for the year, the month and the day the content was added
#         df['year_added'] = df['date_added'].dt.year.astype(int)
#         df['month_added'] = df['date_added'].dt.month_name()
#         df['day_added'] = df['date_added'].dt.day_name()

#         # Drop the 'date_added' column
#         df = df.drop(columns=['date_added'])

#         # Create new integer column for the runtime of the content
#         df['runtime'] = df['duration'].str.split(' ').str[0].astype(int)
#         # Create new string column for the time denomination of the content
#         df['time_denomination'] = df['duration'].str.split(' ').str[1]
#         # Drop the 'duration' column
#         df = df.drop(columns=['duration'])
#         # Drop duplicate rows
#         df = df.drop_duplicates()
#         # Sort the dataframe by 'type' and 'title' and reset the index
#         df = df.sort_values(by=['type', 'title']).reset_index(drop=True)

#         # Return the dataframe
#         return df

#     # Read in the CSV file
#     df = pd.read_csv(url_for('static', filename='netflix_ss.csv'))

#     # Clean the Netflix data
#     df = clean_netflix_data(df)

#      # Load the dataframe into the database
#     for index, row in df.iterrows():
#         netflix_content = NetflixContent(
#             show_id=row['show_id'],
#             type=row['type'],
#             title=row['title'],
#             director=row['director'],
#             cast=row['cast'],
#             country=row['country'],
#             release_year=row['release_year'],
#             rating=row['rating'],
#             duration=row['duration'],
#             listed_in=row['listed_in'],
#             description=row['description']
#         )
#         db.session.add(netflix_content)
#     db.session.commit()

#     # Return the JSON response
#     return jsonify({
#         'data': [i.to_dict() for i in NetflixContent.query.all()]
#     })


    
