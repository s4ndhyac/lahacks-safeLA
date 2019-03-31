import numpy as np
import pandas as pd
import seaborn as sns
from sklearn import preprocessing


dataset = pd.read_csv('safeLA.csv')
# creating input features and target variables
X= dataset.drop(columns=['Score'])
y= dataset[['Score']]

from keras.utils import np_utils
from sklearn.preprocessing import LabelEncoder

# encode class values as integers
encoder = LabelEncoder()
encoder.fit(y)
encoded_Y = encoder.transform(y)
# convert integers to dummy variables (i.e. one hot encoded)
dummy_y = np_utils.to_categorical(encoded_Y)

min_max_scaler = preprocessing.MinMaxScaler()
X_scale = min_max_scaler.fit_transform(X)

from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X_scale, dummy_y, test_size=0.3)

from keras import Sequential
from keras.layers import Dense
from keras.optimizers import Adadelta
from keras.optimizers import SGD, Adam

#create model
model = Sequential()

#First Hidden Layer
model.add(Dense(40, activation='relu', kernel_initializer='random_normal', input_shape=(2,)))
#Second  Hidden Layer
model.add(Dense(30, activation='relu'))
model.add(Dense(20, activation='relu'))
#Output Layer
model.add(Dense(10, activation='softmax'))

#Compiling the neural network
model.compile(loss='binary_crossentropy',
                  optimizer=SGD(lr=1e-2),
                  metrics=['accuracy'])

#Fitting the data to the training dataset
model.fit(X_train,y_train, batch_size=32, epochs=1)

model.save_weights("/Users/sandhya/Documents/repos/lahacks-safeLA/ML-models/safety_score/safeLA_weights.npy")

predictions = model.predict(X_train[2:3])
print(predictions)


