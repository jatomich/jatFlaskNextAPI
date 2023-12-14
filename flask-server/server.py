# Description: Flask server for the application
# Author: Andrew Tomich

from flask import Flask, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route('/api/test', methods=['GET'])
def test_api():
    """
    Returns a JSON response with a message.
    """
    return jsonify({
        'message': "Hello World!"
    })

if __name__ == '__main__':
    app.run(debug=True, port=8080)