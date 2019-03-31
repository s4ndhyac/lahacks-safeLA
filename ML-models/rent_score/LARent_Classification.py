import numpy as np
import pandas as pd
import seaborn as sns
from sklearn import preprocessing


dataset = pd.read_csv('LARent_Classification.csv')
# creating input features and target variables
X= dataset.drop(columns=['Amount'])
y= dataset[['Amount']]

min_max_scaler = preprocessing.MinMaxScaler()
X_scale = min_max_scaler.fit_transform(X)

from keras.utils import np_utils
from sklearn.preprocessing import LabelEncoder

# encode class values as integers
encoder = LabelEncoder()
encoder.fit(y)
encoded_Y = encoder.transform(y)
# convert integers to dummy variables (i.e. one hot encoded)
dummy_y = np_utils.to_categorical(encoded_Y)

from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X_scale, dummy_y, test_size=0.3)

from keras import Sequential
from keras.layers import Dense, Dropout
from keras.optimizers import SGD, Adam

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

#Compiling the neural network
model.compile(loss='binary_crossentropy',
                  optimizer=SGD(lr=1e-3),
                  metrics=['accuracy'])

#Fitting the data to the training dataset
model.fit(X_train,y_train, batch_size=32, epochs=10)

model.save_weights("/Users/sandhya/Documents/repos/lahacks-safeLA/ML-models/rent_score/LARent_weights_classification.npy")

predictions = model.predict(X_train[2:3])
print(predictions)


