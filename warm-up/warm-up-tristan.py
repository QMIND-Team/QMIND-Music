# -*- coding: utf-8 -*-
"""
Created on Tue Nov 20 21:48:53 2018

@author: trist
"""

import csv
from sklearn import tree
from spotify_api_client import search, search_all, get
import pandas as pd
import random


df = pd.read_csv('song_list.csv')

half = len(df)/2
end = len(df)

feature_fields = ['danceability', 'energy',
                  'key', 'loudness', 'mode', 'speechiness', 'acousticness', 'instrumentalness', 'liveness', 'tempo']
label_field = 'happy/sad'


# <<<open
# input a dataframe to be sorted, and the criteria and target value
# returns 2D list
def sortDataFrame(data, index):
    testList = data.loc[0:len(data), feature_fields].values
    compareList = data.loc[0:len(data), 'happy/sad'].values
    returnList = []
    for i in range(len(data)):
        if compareList[i] == index:
            returnList.append(testList[i])
    return returnList
# >>>close


# define happy and sad dataframes using func : sortDataFrame
# add labels to columns
dfHappy = pd.DataFrame(sortDataFrame(df, 1))
dfHappy.columns = feature_fields
dfSad = pd.DataFrame(sortDataFrame(df, 0))
dfSad.columns = feature_fields

# <<<open
# create training and testing dataframes

# length of smaller list, ensure length is even (for later calculations)
length = min([len(dfHappy), len(dfSad)])
if length % 2 == 1:
    length -= 1
halfLength = (int)(length/2)
random.seed()
# CTD does not work: instead generate separate happy and sad arrays
# then combine them with the CL function


def createTrainingData(listCTD, dataCTD, lengthCTD):
    startCTD = random.randint(0, len(dataCTD))
    for i in range(startCTD, startCTD+lengthCTD):
        listCTD.append(dataCTD.loc[i % len(dataCTD), feature_fields].values)
# generate random number between 0 and length of dataset
# take training data from happy and sad datasets
        '''
trainData = []
testData = []
createTrainingData(trainData,dfHappy,500)
createTrainingData(trainData,dfSad,500)
createTrainingData(testData,dfHappy,500)
createTrainingData(testData,dfSad,500)
'''


def combineLists(list1CL, list2CL):
    outListCL = []
    for row in list1CL:
        outListCL.append(row)
    for row in list2CL:
        outListCL.append(row)
    return outListCL


# create training data and labels
trainData1 = dfHappy.loc[0:halfLength, feature_fields].values
trainData2 = dfSad.loc[0:halfLength, feature_fields].values
trainData = combineLists(trainData1, trainData2)

numHappy = len(trainData1)
numSad = len(trainData2)
trainLabels = [0]*(numHappy + numSad)
for i in range(numHappy):
    trainLabels[i] += 1

# create testing data and labels
testData1 = dfHappy.loc[halfLength+1:length, feature_fields].values
testData2 = dfSad.loc[halfLength+1:length, feature_fields].values
testData = combineLists(testData1, testData2)

numHappy = len(testData1)
numSad = len(testData2)
testLabels = [0]*(numHappy + numSad)
for i in range(numHappy):
    testLabels[i] += 1
# >>>close


# <<<open
# returns percentage score of test data
def testTree(features, labels, testData, testLabels):
    clf = tree.DecisionTreeClassifier()
    clf.fit(features, labels)
    score = 0
    for i in range(len(testData)):
        if clf.predict([testData[i]]) == testLabels[i]:
            score += 1
    return score*100/len(testData)
# >>>close


score = testTree(trainData, trainLabels, testData, testLabels)
print(f'even score: {score}')


# <<<open
# Reading features and labels from the dataframe
trainFeatures = df.loc[0:half, feature_fields].values
trainLabels = df.loc[0:half, label_field].values
testFeatures = df.loc[half+1:end, feature_fields].values
testLabels = df.loc[half+1:end, label_field].values
# test with 1000
trainFeatures1000 = df.loc[0:1080, feature_fields].values
trainLabels1000 = df.loc[0:1080, label_field].values
testFeatures1000 = df.loc[1081:1081+1077, feature_fields].values
testLabels1000 = df.loc[1081:1081+1077, label_field].values
# removes a criteria from the dataframe, tests tree and prints score


def analysis(column):
        # remove column from temporary dataframe
    fields = feature_fields.copy()
    fields.remove(column)

    # create training and testing lists
    features_train = df.loc[0:half, fields].values
    labels_train = df.loc[0:half, label_field].values
    features_test = df.loc[half+1:end, fields].values
    labels_test = df.loc[half+1:end, label_field].values

    # create and test tree
    score = testTree(features_train, labels_train, features_test, labels_test)

    print(f'\t{score}')
# >>>close


# <<<open
# main operations:
    # print scores of
score = testTree(trainFeatures, trainLabels, testFeatures, testLabels)
print(f'uneven score: {score}')
score = testTree(trainFeatures1000, trainLabels1000,
                 testFeatures1000, testLabels1000)
print(f'uneven1000 score: {score}')

for feature in feature_fields:
    print(f'{feature}: ', end=' ')
    analysis(feature)

'''
score = [None]*100

for j in range(100):
    clf = tree.DecisionTreeClassifier()
    clf.fit(trainFeatures,trainLabels)
    score[j] = 0 #out of 100
    for i in range(len(testFeatures)):
        if clf.predict([testFeatures[i]]) == testLabels[i]:
            score[j] += 1
print(score)

avg = 0
for j in range(100):
    avg += score[j]/half

        
   
print(f'average score percent: {avg}')
'''
