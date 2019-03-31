import numpy as np
import pandas as pd
import seaborn as sns


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

from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, dummy_y, test_size=0.3)

from keras import Sequential
from keras.layers import Dense
from keras.optimizers import Adadelta

#create model
model = Sequential()

#First Hidden Layer
model.add(Dense(20, activation='relu', kernel_initializer='random_normal', input_shape=(2,)))
#Second  Hidden Layer
model.add(Dense(20, activation='relu'))
#Output Layer
model.add(Dense(10, activation='softmax'))

#Compiling the neural network
model.compile(loss='categorical_crossentropy',
                  optimizer=Adadelta(),
                  metrics=['accuracy'])

#Fitting the data to the training dataset
model.fit(X_train,y_train, batch_size=1, epochs=30)

model.save_weights("/Users/sandhya/Documents/repos/lahacks-safeLA/ML-models/safety_score/safeLA_weights.npy")

predictions = model.predict(X_train[30:31])
print(predictions)


