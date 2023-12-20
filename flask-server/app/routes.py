# Description: The routes for the Flask server.
# Author: Andrew Tomich

from flask import jsonify, url_for, current_app as app
import pandas as pd
from .models import db

def clean_netflix_data(df: pd.DataFrame):
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

    # Return the dataframe
    return df


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
#     movie = 'movie'
#     tv = 'tv'

# @app.route('/api/netflix/<string:type>', methods=['GET'])
# def get_netflix_movies(type):
#     """
#     Retrieves a list of Netflix movies from a CSV file and returns them as a JSON response.
#         Step 0: Read in the CSV file
#         Step 1: Filter the dataframe to only include movies
#         Step 2: Drop all 'NaN' values, sort the dataframe by title and reset the index
#         Step 3: Remove 's' character from start of 'show_id' column and convert to integer
#         Step 4: Return the JSON response
#     Returns:
#         dict: A dictionary containing the movie data in JSON format.
#     """
    # Check if the specified type is valid
        # if type and type is not None:
        #     if type not in [nt.value for nt in NetflixType.__iter__()]:
        #         print([nt.value for nt in NetflixType.__iter__()])
        #         raise ValueError(f'Invalid Netflix type: {type}')


#     # Filter the dataframe to only include the specified type
#     filtered_df = app.df[app.df['type'] == type.capitalize()]

#     # Return the JSON response
#     return jsonify({
#         'data': app.df.to_dict(orient='records')
#     })


# @app.route('/api/netflix', methods=['GET'])
# def get_netflix_content():
#     """
#     Retrieves a list of Netflix content from the database and returns them as a JSON response.
#     Args:
#         type (str): The type of Netflix content to retrieve.
#     Returns:
#         dict: A dictionary containing the Netflix content data in JSON format.
#     """
#     print(NetflixContent.query)
#     # Retrieve the Netflix content from the database by querying the db object
#     return
#     # Return the JSON response
#     return jsonify({
#         'data': [i.to_dict() for i in netflix_content]
#     })

@app.route('/api', methods=['GET'])
def load_database():
    """
    Loads the Netflix content data from a CSV file into the database.
    Returns:
        dict: A dictionary containing the Netflix content data in JSON format.
    """
    # Read in the CSV file
    df = pd.read_csv(url_for('static', filename='netflix_ss.csv'))

    # Clean the Netflix data
    df = clean_netflix_data(df)

    # Load the dataframe into the database
    df.to_sql('netflix_content', db.engine, if_exists='replace', index=False)

    # Return the JSON response
    return jsonify({
        'data': df.to_dict(orient='records')
    })



    