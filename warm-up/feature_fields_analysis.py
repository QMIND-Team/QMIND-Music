import pandas as pd
from sklearn import tree
import itertools as it

# Read the CSV
df = pd.read_csv('song_list_2.csv')
# Relevant columns for features and labels
feature_fields = ['danceability', 'energy',
                  'key', 'loudness', 'mode', 'speechiness', 'acousticness', 'instrumentalness', 'liveness', 'tempo']
label_field = 'happy/sad'

# Reading features and labels from the dataframe
features = df.loc[:, feature_fields].values
labels = df.loc[:, label_field].values


def newAnalysis(colSet):
    fields = feature_fields.copy()
    noGoList = []
    for col in fields:
        if col not in colSet:
            noGoList.append(col)
    for item in noGoList:
        fields.remove(item)
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
    print(accuracy)
    return accuracy


results2 = {}
for comb in range(1, len(feature_fields)+1):
    for subset in it.combinations(feature_fields, comb):
        results2[subset] = newAnalysis(subset)

print(results2)

maxValKey = max(results2, key=results2.get)

print (f'maximum accuracy: {results2[maxValKey]}')
print (f'best keys to use: {maxValKey}')
#note: ctrl+c stops the terminal while it is running
#note: must have cursor in code to use ctrl+r and run code



