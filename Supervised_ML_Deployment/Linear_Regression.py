#We will predict student percentage given the number of hours he/she studies using linear regression technique. 

#importing necessary libraries
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import pickle #to save serialised python object

#read data 
dataset=pd.read_csv("http://bit.ly/w-data")

#extracting features and labels
features=dataset['Hours']
labels=dataset['Scores']

#reshape features in 2D
features=np.asarray(features)
features=features.reshape((len(features),1))

#splitting our dataset
from sklearn.model_selection import train_test_split
features_train,features_test,labels_train,labels_test=train_test_split(features,labels,test_size=0.2)

#import Linear Regression 
from sklearn.linear_model import LinearRegression
model=LinearRegression()

#train using features_train and labels_train
model.fit(features_train,labels_train)

#saving model to disk
pickle.dump(model,open('Linear_Regression.pkl','wb'))