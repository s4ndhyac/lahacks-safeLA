import numpy as np
import pandas as pd
import seaborn as sns


dataset = pd.read_csv('LArent.csv')


from keras.utils import np_utils
from sklearn.preprocessing import LabelEncoder

# # encode class values as integers
# encoder = LabelEncoder()
# encoder.fit(y)
# encoded_Y = encoder.transform(y)
# # convert integers to dummy variables (i.e. one hot encoded)
# dummy_y = np_utils.to_categorical(encoded_Y)

from sklearn.preprocessing import MinMaxScaler

scaler = MinMaxScaler(feature_range=(0, 1))
scaled_dataset = scaler.fit_transform(dataset)

# from sklearn.model_selection import train_test_split
# X_train, X_test, y_train, y_test = train_test_split(X, dummy_y, test_size=0.3)

from keras import Sequential
from keras.layers import Dense
from keras.optimizers import Adadelta

#create model
model = Sequential()

#First Hidden Layer
model.add(Dense(100, activation='relu', kernel_initializer='random_normal', input_shape=(2,)))
#Second  Hidden Layer
model.add(Dense(50, activation='relu'))
#Output Layer
model.add(Dense(100, activation='relu'))
model.add(Dense(1))

#Compiling the neural network
model.compile(loss='mean_squared_error',
                  optimizer=Adadelta(),
                  metrics=['accuracy'])


# creating input features and target variables
X= scaled_dataset.drop(columns=['Amount'])
y= scaled_dataset[['Amount']]

#Fitting the data to the training dataset
model.fit(X[:] ,y[:], batch_size=1, epochs=2)

model.save_weights("/Users/sandhya/Documents/repos/lahacks-safeLA/ML-models/safety_score/safeLA_weights.npy")

#inference
prediction = model.predict(X[:1])
y_0 = prediction[0][0]
print('Prediction with scaling - {}',format(y_0))
print("Housing Price Prediction  - ${}".format(y_0))

