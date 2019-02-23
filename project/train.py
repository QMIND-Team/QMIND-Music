from lib import *
from os import mkdir, path
from keras.callbacks import ModelCheckpoint

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
model = create_network()

checkpoint = ModelCheckpoint("weights.hdf5",
                             monitor='loss',
                             verbose=0,
                             save_best_only=True,
                             mode='min')

model.fit(image_features, song_features, batch_size=100,
          epochs=4000, callbacks=[checkpoint])
