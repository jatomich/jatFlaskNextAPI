from flask import current_app as app, jsonify, url_for
import pandas as pd
from enum import Enum


@app.route('/api/health', methods=['GET'])
def health_check():
    """
    Returns a JSON response with a message.
    """
    return jsonify({
        'data': "Success!"
    })

@app.route('/api/netflix/<string:type>', methods=['GET'])
def get_netflix_movies(type):
    """
    Retrieves a list of Netflix movies from a CSV file and returns them as a JSON response.
        Step 0: Read in the CSV file
        Step 1: Filter the dataframe to only include movies
        Step 2: Drop all 'NaN' values, sort the dataframe by title and reset the index
        Step 3: Remove 's' character from start of 'show_id' column and convert to integer
        Step 4: Return the JSON response
    Returns:
        dict: A dictionary containing the movie data in JSON format.
    """
    # Check if the specified type is valid
    if type not in NetflixType.__members__:
        raise ValueError(f'Invalid Netflix type: {type.capitalize()}')

    # Filter the dataframe to only include the specified type
    app.df = app.df[app.df['type'] == type.capitalize()]

    # Return the JSON response
    return jsonify({
        'data': app.df.to_dict(orient='records')
    })

@app.before_request
def load_data():
    """
    Load the Netflix data into memory before the first request.
    """
    app.df = pd.read_csv(url_for('static', filename='netflix_titles.csv'))
    app.df = clean_netflix_data(app.df)

@app.after_request
def cors_after_request(response):
    # Add CORS headers to the response
    response.headers.add('Access-Control-Allow-Origin', '*')
    response.headers.add('Access-Control-Allow-Headers', 'Content-Type,Authorization')
    response.headers.add('Access-Control-Allow-Methods', 'GET,PUT,POST,DELETE')
    return response


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

    # Return the dataframe
    return df

class NetflixType(Enum):
    """
    An enumeration of the different types of Netflix media.
    """
    movie = 'movie'
    tv = 'tv'


    