import os
import cv2
import numpy as np

from time import time
from flask import Flask, request, send_from_directory
from flask_cors import CORS
from google.cloud import storage

from lib import *

app = Flask(__name__, static_folder="client/build/static")
CORS(app)

model = create_network()
model.load_weights("weights.hdf5")
model._make_predict_function()

os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = 'google-config.json'
client = storage.Client()
bucket = client.get_bucket('qmusicbucket')


@app.route('/song', methods=['POST'])
def song():
    # Get image from request
    timestamp = time()
    image_file = request.files['image'].read()
    image_blob = bucket.blob(f'img-{timestamp}')
    image_blob.upload_from_string(image_file)
    nparr = np.fromstring(image_file, np.uint8)
    image = cv2.imdecode(nparr, cv2.IMREAD_COLOR)

    # Feed image to neural net
    image_features = get_image_features(None, 200, image)
    output = model.predict(np.array([image_features]))
    output_to_wav(output[0])

    song_blob = bucket.blob(f'song-{timestamp}.wav')
    song_blob.upload_from_filename('output.wav')
    return song_blob.public_url


# Serve React App
@app.route('/', defaults={'path': ''})
@app.route('/<path:path>')
def serve(path):
    if path != "" and os.path.exists("client/build/" + path):
        return send_from_directory('client/build', path)
    else:
        return send_from_directory('client/build', 'index.html')


app.run(debug=True, host='0.0.0.0', port=4000)
