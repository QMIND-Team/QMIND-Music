"""
A library for all functions image-related
"""
import cv2
import numpy as np
from scipy.misc import imread



# Turn an image file into an array of features, returns 0s if fails
def get_image_features(image_path):
    
    features = extract_features(image_path)
    resize_array(features)
    if(check_size(features) == 1):
        return features
    else:
        return [np.zeros(64) for i in range(200)]
    #pass

#ensures array is size 200*64
def resize_array(array):
    num_vectors = len(array)
    for i in range(num_vectors):
        #ensure all vectors are length 64
        v_size = array[i].size
        if(v_size < 64):
            array[i] = np.concatenate([array[i], np.zeros(64 - v_size)])
    if(num_vectors < 200):
        zero_vector = [np.zeros(64) for i in range(200-num_vectors)]
        array = np.concatenate([array, zero_vector])
    return array

#returns 1 if array is correct size, else 0
def check_size(array):
    correct_size = 0
    if(len(array) == 200):
        correct_size = 1
    for i in range(200):
        if(array[i].size != 64):
            correct_size = 0
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
        kps, dsc = alg.compute(image, kps)
    except cv2.error as e:
        print ('Error: ', e)
        return [np.zeros(64) for i in range(200)]
    return dsc