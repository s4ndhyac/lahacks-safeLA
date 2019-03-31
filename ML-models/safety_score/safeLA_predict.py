import numpy as np
import pandas as pd
import seaborn as sns

from keras import Sequential
from keras.layers import Dense
from numpy import array


def predictSafeLA(x, y):
  #create model
  model = Sequential()

  #First Hidden Layer
  model.add(Dense(20, activation='relu', kernel_initializer='random_normal', input_shape=(2,)))
  #Second  Hidden Layer
  model.add(Dense(20, activation='relu'))
  #Output Layer
  model.add(Dense(10, activation='softmax'))

  model.load_weights("safeLA_weights.npy")

  data = array([[x,y]])
  predictions = model.predict(data[0:1])
  return predictions


