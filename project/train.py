from lib import *

# Make the songs and images
print("Creating data set.")
create_songs_and_images()

# Get features from songs
print("Creating song features.")
song_features = create_song_features_array()

# Get features from images
print("Creating image features.")
image_features = create_image_feature_array()

# Train the network
print("Training the network")
