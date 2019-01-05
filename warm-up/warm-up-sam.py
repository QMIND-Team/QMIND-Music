import pandas as pd
from sklearn import tree
# Read the CSV
df = pd.read_csv('song_list.csv')
# Relevant columns for features and labels
feature_fields = ['danceability', 'energy',
                  'key', 'loudness', 'mode', 'speechiness', 'acousticness', 'instrumentalness', 'liveness', 'tempo']
label_field = 'happy/sad'

# Reading features and labels from the dataframe
features = df.loc[:, feature_fields].values
labels = df.loc[:, label_field].values


def analysis(column):
    fields = feature_fields.copy()
    fields.remove(column)
    features_train = df.loc[0:2000, fields].values
    labels_train = df.loc[0:2000, label_field].values
    features_test = df.loc[2001:3500, fields].values
    labels_test = df.loc[2001:3500, label_field].values
    clf = tree.DecisionTreeClassifier()
    clf.fit(features_train, labels_train)
    count = 0
    for i, feature in enumerate(features_test):
        output = clf.predict([feature])
        # print(output)
        if(output == labels_test[i]):
            count += 1

    print(count/len(features_test)*100, "%")


for feature in feature_fields:
    print(f'feature:{feature}')
    analysis(feature)
