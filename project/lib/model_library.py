"""
A library for all functions related to the neural network
"""
import numpy as np

from keras.models import Sequential
from keras.layers import Dense, Dropout, Activation, LSTM


def create_network():
    model = Sequential()
    model.add(LSTM(
        512,
        input_shape=(200, 64),
        return_sequences=True
    ))
    model.add(Dropout(0.3))
    model.add(LSTM(512, return_sequences=True))
    model.add(Dropout(0.3))
    model.add(LSTM(512))
    model.add(Dense(256))
    model.add(Dropout(0.3))
    model.add(Dense(60))
    model.add(Activation('softmax'))
    model.compile(loss='categorical_crossentropy', optimizer='rmsprop')
    return model
