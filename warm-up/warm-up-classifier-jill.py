import pandas as pd
from sklearn import tree
from spotify_api_client import search, search_all, get

# Read the CSV
df = pd.read_csv('song_list_2.csv')
# Relevant columns for features and labels
feature_fields = ['danceability', 'energy',
                  'key', 'loudness', 'mode', 'speechiness', 'acousticness', 'instrumentalness', 'liveness', 'tempo']
label_field = 'happy/sad'

# Reading features and labels from the dataframe
features = df.loc[:, feature_fields].values
labels = df.loc[:, label_field].values


def songAnalysis(song):

    fields = ['danceability', 'energy', 'key', 'mode', 'speechiness', 'instrumentalness', 'tempo']
    features_train = df.loc[0:2000, fields].values
    labels_train = df.loc[0:2000, label_field].values
    features_test = df.loc[2001:3987, fields].values
    labels_test = df.loc[2001:3987, label_field].values

    clf = tree.DecisionTreeClassifier() #importing the decision tree classifier
    #learning algorithm finds patterns in training data to create rules for classifier
    clf = clf.fit(features_train, labels_train) #create learning algorithm

    #loop over every song, predict, compare to real value, keep track of accuracy
    score = 0
    for i, feature in enumerate(features_test):
        result = clf.predict([feature])
        if (result == labels_test[i]):
            score += 1
        
    accuracy = (score/len(features_test))*100

    response = search(str(song), 'track')
    data = get(f'v1/audio-features/{response}')

    dataArray = list(data.values())
    #print(dataArray)

    features = []
    for index, item in enumerate(dataArray[0:11]):
        dataArray[index] = float(item)
    features.append(dataArray[0:3]) #only add the data from certain columns of the row !!!!!
    #want 0 1 2 4 5 7 9
    features[0].append(float(dataArray[4]))
    features[0].append(float(dataArray[5]))
    features[0].append(float(dataArray[7]))
    features[0].append(float(dataArray[9]))


    print (f'I predict this song is a {clf.predict(features)} with {accuracy} % accuracy.')

songAnalysis('that\'s life frank sinatra')

#note: ctrl+c stops the terminal while it is running
#note: must have cursor in code to use ctrl+r and run code
#note: 1 = happy, 0 = sad
#out of range for long searches ?