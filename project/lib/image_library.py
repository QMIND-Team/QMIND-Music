"""
A library for all functions image-related
"""
import cv2
import numpy as np
from scipy.misc import imread
import glob

#list of images features for all images in data/small_album_images
def create_image_feature_array():
    images = glob.glob('data/small_album_images/*.jpg')
    feature_array = [get_image_features(img) for img in images]
    return feature_array

# Turn an image file into an array of features, returns 0s if fails
def get_image_features(image_path):
    features = extract_features(image_path)
    if(check_size(features)):
        return features
    else:
        features = resize_array(features)
        return features

#ensures array is size 200*64
def resize_array(array):
    num_vectors = len(array)
    for v in range(num_vectors):
    #ensure all vectors are length 64
        v_size = len(array[v])
        if(v_size < 64):
            array[v] = np.concatenate([array[v], np.zeros(64 - v_size)])
    #ensures 200 vectors
    if(num_vectors < 200):
        zero_vector = [np.zeros(64) for i in range(200-num_vectors)]
        array = np.concatenate([array, zero_vector])
    return array

#returns True if array is correct size, else False
def check_size(array):
    correct_size = True
    if(len(array) != 200):
        correct_size = False
    for v in range(len(array)):
        if(len(array[v]) != 64):
            correct_size = False
    return correct_size

#returns feature list of size 200*64
def extract_features(image_path, vector_size=200):
    image = imread(image_path, mode="RGB")
    try:
        alg = cv2.KAZE_create()
        # Finding image keypoints
        kps = alg.detect(image)
        # Getting first 200 of them. 
        # Number of keypoints is varies depend on image size and color pallet
        # Sorting them based on keypoint response value(bigger is better)
        kps = sorted(kps, key=lambda x: -x.response)[:vector_size]
        # computing descriptors vector
        if(len(kps) > 0):
            kps, dsc = alg.compute(image, kps)
        else:
            dsc = [[0]*64 for i in range(200)]
    except cv2.error as e:
        print ('Error: ', e)
        return [np.zeros(64) for i in range(200)]
    return dsc
