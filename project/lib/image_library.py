"""
A library for all functions image-related
"""
import cv2
import numpy as np
import math
import imageio
import glob
from PIL import Image

#list of images features for all images in data/small_album_images
def create_image_feature_array():
    images = glob.glob('data/small_album_images/*.jpg')
    feature_array = [get_image_features(img) for img in images]
    return feature_array

# Turn an image file into an array of features, returns 0s if fails
def get_image_features(image_path):
    features = extract_features(image_path)
    features = resize_array(features)
    features = normalize(features)

#ensures array is size 200*64
def resize_array(array):
    if(check_size(array)):
        return array
    else:
        num_vectors = len(array)
        #ensure all vectors are length 64
        for v in range(num_vectors):
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
    image = imageio.imread(image_path)
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

#returns integer in range [1,11]
def create_pixel_array(image_path):
    img = Image.open(image_path)  #loading pixel array
    pixels = img.load()
    width, height = img.size
    px = []
    for x in range(width):
        for y in range(height):
            cpixel = pixels[x, y]
            px.append(cpixel)   #px is pixel array
    return px

#converts 2D list of tuples to 2D list of lists(size 3)
def convert_to_array(tuple_array):
    for i in range(len(tuple_array)):
        for j in range(len(tuple_array[0])):
            array_rep = [0,0,0]
            for k in range(3):
                array_rep[k] = tuple_array[i][j][k]
            tuple_array[i][j] = array_rep
    return tuple_array

#sigmoid function has output range [0,1], 0 is mapped to 0.5
def sigmoid(x):
     return 1 / (1 + math.e ** -x)

#apply sigmoid function to every element in an array
def normalize(array):
    for i in array:
        i = sigmoid(i)

#returns most common colour range in an image
def find_key(image_path):
    px = create_pixel_array(image_path)
    px = convert_to_array(px)
    categories = [0 for i in range(12)]
    for pixel_row in px:
        for pixel in pixel_row:
            cat = find_pixel_cat(pixel)
            categories[cat] += 1
    return max_element(categories)

#returns colour range for a single pixel
def find_pixel_cat(pixel):
    if(pixel[0] > 170):
        category = 8
    elif(pixel[0] > 85):
        category = 4
    else:
        category = 0
    if(pixel[1] > 127):
        category += 2
    if(pixel[2] > 127):
        category += 1
    return category

#returns index of largest element in a list
def max_element(array):
    if (len(array) == None):
        print("array is empty")
        return None
    maxi = 0
    for i in range(len(array)):
        if(array[i] > maxi):
            maxi = i
    return maxi