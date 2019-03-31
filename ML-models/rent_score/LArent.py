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

def plot_history(history):
  hist = pd.DataFrame(history.history)
  hist['epoch'] = history.epoch
  
  plt.figure()
  plt.xlabel('Epoch')
  plt.ylabel('Mean Abs Error')
  plt.plot(hist['epoch'], hist['mean_absolute_error'],
           label='Train Error')
  plt.plot(hist['epoch'], hist['val_mean_absolute_error'],
           label = 'Val Error')
  plt.ylim([0,5])
  plt.legend()
  
  plt.figure()
  plt.xlabel('Epoch')
  plt.ylabel('Mean Square Error')
  plt.plot(hist['epoch'], hist['mean_squared_error'],
           label='Train Error')
  plt.plot(hist['epoch'], hist['val_mean_squared_error'],
           label = 'Val Error')
  plt.ylim([0,20])
  plt.legend()
  plt.show()



dataset = pd.read_csv("test_rent.csv")
# target = dataset.Amount
# dataset.drop(['Amount'],axis = 1 , inplace = True)


train_dataset = dataset.sample(frac=0.8,random_state=0)
test_dataset = dataset.drop(train_dataset.index)
print(train_dataset)
print(test_dataset)

train_labels = train_dataset.pop('Amount')
test_labels = test_dataset.pop('Amount')


NN_model = Sequential()
NN_model.add(Dense(10, input_dim=2, kernel_initializer='random_normal', activation='relu'))
NN_model.add(Dense(1))
# Compile model
NN_model.compile(loss='mean_squared_error', optimizer='adam', metrics=['mean_absolute_error', 'mean_squared_error'])

checkpoint_name = 'rentLA_weights.hdf5' 
checkpoint = ModelCheckpoint(checkpoint_name, monitor='val_loss', verbose = 1, save_best_only = True, mode ='auto')
callbacks_list = [checkpoint]

history = NN_model.fit(train_dataset, train_labels, epochs=30, batch_size=32, validation_split = 0.2, callbacks=callbacks_list)

loss, mae, mse = NN_model.evaluate(test_dataset, test_labels, verbose=0)
print("Testing set Mean Abs Error: {:5.2f}".format(mae))

test_predictions = NN_model.predict(test_dataset).flatten()

print(test_predictions)