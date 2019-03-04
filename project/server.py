import os

from flask import Flask, request
from flask_cors import CORS

app = Flask(__name__)
CORS(app)


@app.route('/song', methods=['POST'])
def song():
    image_file = request.files['image'].stream
    return 'Hello World from Python Flask!'


app.run(host='0.0.0.0', port=os.getenv('PORT') or 4000)
