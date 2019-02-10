"""
A library for all functions data related
"""


# Downloads mp3s and jpgs from the dataset
def create_songs_and_images():
    import pandas as pd
    import requests
    import os
    
    #create the folder to hold the data
    path1 = 'data/song_preview_clips'
    path2 = 'data/small_album_images'
    
    os.mkdir(path1)
    os.mkdir(path2)
    
    df = pd.read_csv('data/trackData.csv') #read the csv from the data folder into a pandas dataframe
    
    for num in range(df.shape[0]): #iterate over every row
        row = df.loc[num, :] #take one row with every corresponding column
        
        preview_url = row[4] #get the urls and track id from each row
        track_id = row[1]
        pic_url = row[5]
        
        #get the files and put them in the folders
        r = requests.get(str(preview_url), allow_redirects=True)
        open(f'{path1}/{track_id}_preview.mp3', 'wb').write(r.content)
        s = requests.get(str(pic_url), allow_redirects=True)
        open(f'{path2}/{track_id}_art.jpg', 'wb').write(s.content)
