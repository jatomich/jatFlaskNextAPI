# Description: The view functions (along with any helper functions) for the Flask server.
# Author: Andrew Tomich

from datetime import datetime
from flask import jsonify, url_for, current_app as app
import pandas as pd
from .models import db, NetflixContent

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
    df['date_added'] = df['date_added'].apply(lambda x: pd.to_datetime(x))

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


@app.route('/api/health', methods=['GET'])
def health_check():
    """
    Returns a JSON response with a message.
    """
    return jsonify({
        'data': "Success!"
    })


@app.route('/netflix', methods=['GET'])
def get_netflix_content():
    """
    Retrieves a list of Netflix content from the database and returns them as a JSON response.
    Args:
        type (str): The type of Netflix content to retrieve.
    Returns:
        dict: A dictionary containing the Netflix content data in JSON format.
    """
    try:
        # If the database is empty, load the dataframe into the database
        if not NetflixContent.query[0] or NetflixContent.query[0] is None:
            print("Not Loaded")
            raise IndexError
    except IndexError:
        # Read in the CSV file
        df = pd.read_csv(url_for('static', filename='netflix_ss.csv'))
        # df = pd.read_csv('C:/Users/jandr/CODE/python/jatFlaskNextAPI/flask-server/app/static/netflix_ss.csv')
        # Clean the Netflix data
        df = clean_netflix_data(df)
        for tup in df.itertuples():
            db.session.add(NetflixContent(
                show_id=tup.show_id,
                type=tup.type,
                title=tup.title,
                director=tup.director,
                cast=tup.cast,
                country=tup.country,
                release_year=tup.release_year,
                rating=tup.rating,
                listed_in=tup.listed_in,
                description=tup.description,
                created_at=datetime.now(),
                updated_at=datetime.now()
            ))
        db.session.commit()

    netflix_content = [nc.__dict__ for nc in NetflixContent.query.all()]
    for nc in netflix_content:
        del nc['_sa_instance_state']

    return jsonify({
        'data': netflix_content
    })

@app.route('/netflix/movies', methods=['GET'])
def get_netflix_movies():
    netflix_movies = [movie.__dict__ for movie in NetflixContent.query.filter_by(type='Movie').all()]
    for movie in netflix_movies:
        del movie['_sa_instance_state']
    return jsonify(
        {
            'data': netflix_movies
        }
    )

@app.route('/netflix/tv', methods=['GET'])
def get_netflix_tv():
    netflix_tv = [tv.__dict__ for tv in NetflixContent.query.filter_by(type='TV Show').all()]
    for tv in netflix_tv:
        del tv['_sa_instance_state']
    return jsonify(
        {
            'data': netflix_tv
        }
    )
# @app.route('/netflix_id/<int:show_id>', methods=['GET', 'POST'])
# def get_netflix_content(show_id):
#     """
#     Returns the Netflix content data for the specified show ID.
#     Args:
#         show_id (int): The show ID.
#     Returns:
#         dict: A dictionary containing the Netflix content data in JSON format.
#     """
    # Get the Netflix content data for the specified show ID
    # content = NetflixContent.query.filter_by(show_id=show_id).first()
    # if not content or content is None:
    #     return jsonify({
    #         'data': 'Error'
    #     })
    # content_encoder = NetflixContent.NetflixContentEncoder()
    # encoded_content = content_encoder.default(content)
    # del encoded_content['_sa_instance_state']
    # Return the Netflix content data
    # return jsonify({
    #     'data': encoded_content
    # })