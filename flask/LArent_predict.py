import numpy as np
import pandas as pd
import seaborn as sns

from keras import Sequential
from keras.layers import Dense, Dropout
from numpy import array


def predictRentLA(x, y):
  #create model
  model = Sequential()

  #First Hidden Layer
  model.add(Dense(100, activation='relu', kernel_initializer='random_normal', input_shape=(2,)))
  #Output Layer
  model.add(Dense(90, activation='relu'))
  model.add(Dense(80, activation='relu'))
  model.add(Dense(70, activation='relu'))
  model.add(Dense(60, activation='relu'))
  model.add(Dense(50, activation='relu'))
  model.add(Dense(40, activation='relu'))
  model.add(Dropout(0.25))
  model.add(Dense(31, activation='softmax'))

  model.load_weights("LARent_weights_classification.npy")

  from sklearn import preprocessing
  min_max_scaler = preprocessing.MinMaxScaler()
  data = array([[x,y]])
  data_scale = min_max_scaler.fit_transform(data)

  predictions = model.predict(data_scale[0:1])
  return predictions


