from keras.callbacks import ModelCheckpoint
from keras.models import Sequential
from keras.layers import Dense, Activation, Flatten
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_absolute_error 
import seaborn as sb
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
from numpy import array
from sklearn import preprocessing



dataset = pd.read_csv("LArent.csv")
target = dataset.Amount
dataset.drop(['Amount'],axis = 1 , inplace = True)

min_max_scaler = preprocessing.MinMaxScaler()
X_scale = min_max_scaler.fit_transform(dataset)

NN_model = Sequential()
NN_model.add(Dense(100, input_dim=2, kernel_initializer='normal', activation='relu'))
NN_model.add(Dense(1, kernel_initializer='normal'))
# Compile model
NN_model.compile(loss='mean_squared_error', optimizer='adam')

checkpoint_name = 'rentLA_weights.hdf5' 
checkpoint = ModelCheckpoint(checkpoint_name, monitor='val_loss', verbose = 1, save_best_only = True, mode ='auto')
callbacks_list = [checkpoint]

NN_model.fit(X_scale, target, epochs=30, batch_size=32, validation_split = 0.2, callbacks=callbacks_list)

test = array([[34.274431,-118.30714]])
predictions = NN_model.predict(test[0:1])
print(predictions)