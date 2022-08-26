
import tensorflow as tf
import keras
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv("D:/data/churn.csv")
df.shape
df.columns
x = df.iloc[:,2:12].values
y = df['Exited'].values


'''
# Encode categorical variables
from sklearn.preprocessing import LabelEncoder, OneHotEncoder
from sklearn.compose import ColumnTransformer

lb1 = LabelEncoder()
x[:,1] = lb1.fit_transform(x[:,1]) 

lb2 = LabelEncoder()
x[:,2] = lb2.fit_transform(x[:,2]) 

#oh1 = OneHotEncoder(categorical_features=[1])
ct = ColumnTransformer([("Country", OneHotEncoder(), [1])], remainder = 'passthrough')
x = ct.fit_transform(x)

help(OneHotEncoder)'''

x = df.iloc[:,2:12]
y = df['Exited']

x1 = pd.get_dummies(x,columns=['Geography','Gender'], drop_first=True)
x1 = x1.values

# Data Transformation

from sklearn.preprocessing import StandardScaler
sc = StandardScaler()
x1 = sc.fit_transform(x1)

from sklearn.model_selection import train_test_split
x_train,x_test,y_train,y_test = train_test_split(x1,y,test_size=0.2, random_state = 2)

# Build the layers

from keras.models import Sequential
from keras.layers import Dense

model = Sequential()

# Add the input layer and the hidden layers
model.add(Dense(units = 6, kernel_initializer= 'uniform', activation= 'relu', input_dim = 11))
model.add(Dense(units = 6, kernel_initializer= 'uniform', activation='relu'))
model.add(Dense(units=1, kernel_initializer= 'uniform', activation= 'sigmoid'))
model.compile(optimizer='adam', loss = 'binary_crossentropy', metrics=['accuracy'])
model.fit(x_train,y_train, batch_size= 25, epochs = 100)
pred = model.predict(x_test)

from sklearn.metrics import confusion_matrix
confusion_matrix(y_test,pred>0.5)
105/(105+41)

# Weights
# Bias
# Input layers
# Neurons
# Hidden layers
# Forward propagation
# Output layer
# Activation functions
# Loss fn/ Cost fn
# Optimizers
# Back-propagation
# Weight adjustments (Chain rule of differentiation)