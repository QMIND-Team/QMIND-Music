import os
import cv2
import numpy as np

from flask import Flask, request
from flask_cors import CORS

from lib import *

app = Flask(__name__)
CORS(app)

model = create_network()
model.load_weights("weights.hdf5")
model._make_predict_function()


@app.route('/song', methods=['POST'])
def song():
    # Get image from request
    image_file = request.files['image'].read()
    nparr = np.fromstring(image_file, np.uint8)
    image = cv2.imdecode(nparr, cv2.IMREAD_COLOR)

    # Feed image to neural net
    image_features = get_image_features(None, 200, image)
    output = model.predict(np.array([image_features]))
    return 'Hello World from Python Flask!'


app.run(host='0.0.0.0', port=os.getenv('PORT') or 4000)
