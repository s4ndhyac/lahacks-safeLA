import numpy as np
import pandas as pd
import seaborn as sns

from keras import Sequential
from keras.layers import Dense
from numpy import array


def predictRentLA(x, y):
  NN_model = Sequential()
  NN_model.add(Dense(100, input_dim=2, kernel_initializer='normal', activation='relu'))
  NN_model.add(Dense(1, kernel_initializer='normal'))

  NN_model.load_weights("rentLA_weights.hdf5")

  data = array([[x,y]])
  predictions = NN_model.predict(data[0:1])
  return predictions


