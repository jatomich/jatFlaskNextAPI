# Description: Local executable script to define a shell context and run the Flask server.
# Author: Andrew Tomich

from flask_cors import CORS
from app import create_app
from app.models import db, NetflixContent

app = create_app()
CORS(app)

@app.shell_context_processor
def make_shell_context():
    """
    Defines the shell context for the Flask application.
    Returns:
        dict: A dictionary of the shell context.
    """
    return {'app': app, 'db': db, 'NetflixContent': NetflixContent}
