"""
A library for all functions data related
"""
import pandas as pd
import requests
import os

# Downloads mp3s and jpgs from the dataset


def create_songs_and_images():
    # create the folder to hold the data
    path1 = 'data/song_preview_clips'
    path2 = 'data/small_album_images'
    path3 = 'data/large_album_images'

    if not os.path.isdir(path1):
        os.mkdir(path1)
    if not os.path.isdir(path2):
        os.mkdir(path2)
    if not os.path.isdir(path3):
        os.mkdir(path3)

    # read the csv from the data folder into a pandas dataframe
    df = pd.read_csv('data/trackData.csv')

    path1_is_empty = len(os.listdir(path1)) == 0
    path2_is_empty = len(os.listdir(path2)) == 0
    path3_is_empty = len(os.listdir(path3)) == 0

    for num in range(df.shape[0]):  # iterate over every row
        row = df.loc[num, :]  # take one row with every corresponding column

        preview_url = row[4]  # get the urls and track id from each row
        track_id = row[1]
        pic_url = row[5]
        large_pic_url = row[2]

        # get the files and put them in the folders
        if path1_is_empty:
            r = requests.get(str(preview_url), allow_redirects=True)
            open(f'{path1}/{track_id}_preview.mp3', 'wb').write(r.content)
        if path2_is_empty:
            s = requests.get(str(pic_url), allow_redirects=True)
            open(f'{path2}/{track_id}_art.jpg', 'wb').write(s.content)
        if path3_is_empty:
            t = requests.get(str(large_pic_url), allow_redirects=True)
            open(f'{path3}/{track_id}_big_art.jpg', 'wb').write(t.content)
