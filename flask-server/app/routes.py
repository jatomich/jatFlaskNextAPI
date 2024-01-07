# Description: The view functions (along with any helper functions) for the Flask server.
# Author: Andrew Tomich

from datetime import datetime
from flask import jsonify, current_app as app
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
def load_database():
    """
    Loads the Netflix content data from a CSV file into the database.
    Returns:
        dict: A dictionary containing the Netflix content data in JSON format.
    """
    # Read in the CSV file
    # df = pd.read_csv(url_for('static', filename='netflix_ss.csv'))
    df = pd.read_csv('C:/Users/jandr/CODE/python/jatFlaskNextAPI/flask-server/app/static/netflix_ss.csv')


    # Clean the Netflix data
    df = clean_netflix_data(df)

    try:
        # If the database is empty, load the dataframe into the database
        if not NetflixContent.query[0]:
            raise IndexError
    except IndexError:
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

    # try:
        # Check if the database is empty
        # if not NetflixContent.query[0]:
            # Load the dataframe into the database
    #         for tup in df.itertuples():
    #             db.session.add(NetflixContent(
    #                 show_id=tup.show_id,
    #                 type=tup.type,
    #                 title=tup.title,
    #                 director=tup.director,
    #                 cast=tup.cast,
    #                 country=tup.country,
    #                 release_year=tup.release_year,
    #                 rating=tup.rating,
    #                 listed_in=tup.listed_in,
    #                 description=tup.description,
    #                 created_at=datetime.now(),
    #                 updated_at=datetime.now()
    #             ))
    #         db.session.commit()
    # except Exception as e:
    #     print(e)
    #     return jsonify({
    #         'data': 'Error'
    #     })

    return jsonify({
        'data': df.to_dict(orient='records')
    })

@app.route('/netflix_id/<int:show_id>', methods=['GET', 'POST'])
def get_netflix_content(show_id):
    """
    Returns the Netflix content data for the specified show ID.
    Args:
        show_id (int): The show ID.
    Returns:
        dict: A dictionary containing the Netflix content data in JSON format.
    """
    # Get the Netflix content data for the specified show ID
    content = NetflixContent.query.filter_by(show_id=show_id).first()
    if not content or content is None:
        return jsonify({
            'data': 'Error'
        })
    content_encoder = NetflixContent.NetflixContentEncoder()
    encoded_content = content_encoder.default(content)
    del encoded_content['_sa_instance_state']
    # Return the Netflix content data
    return jsonify({
        'data': encoded_content
    })