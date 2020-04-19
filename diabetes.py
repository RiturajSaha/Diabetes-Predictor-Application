# -*- coding: utf-8 -*-
"""
Created on Sat Apr 18 15:03:10 2020

@author: R2J
"""

# libraries
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd



# Importing the Dataset
dataset=pd.read_csv("diabetes.csv")
newdataset=dataset
x=newdataset.iloc[:,0:8]
y=newdataset.iloc[:,-1]



# Splitting the dataset into the Training set and Test set
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(x, y, test_size = 0.2)



# Fitting K-NN to the Training set
from sklearn.neighbors import KNeighborsClassifier
classifier = KNeighborsClassifier(n_neighbors = 5, metric = 'minkowski', p = 2)
classifier.fit(X_train, y_train)


# Fitting Logistic Regression to the Training set
from sklearn.linear_model import LogisticRegression
classifier = LogisticRegression()
classifier.fit(X_train, y_train)


# Fitting Naive Bayes to the Training set
from sklearn.naive_bayes import GaussianNB
classifier = GaussianNB()
classifier.fit(X_train, y_train)


# Fitting Random Forest Classification to the Training set
from sklearn.ensemble import RandomForestClassifier
classifier = RandomForestClassifier(n_estimators = 500, criterion = 'entropy')
classifier.fit(X_train, y_train)


# Fitting Kernel LinearSVC to the Training set
from sklearn.svm import LinearSVC
classifier = LinearSVC()
classifier.fit(X_train, y_train)


# Fitting Kernel SVC to the Training set
from sklearn.svm import SVC
classifier = SVC(kernel = 'poly')
classifier.fit(X_train, y_train)



# Predicting the Test set results
y_pred = classifier.predict(X_test)



# Making the Confusion Matrix
from sklearn.metrics import confusion_matrix
cm = confusion_matrix(y_test, y_pred)


# Analyzing the output
from sklearn.metrics import r2_score,accuracy_score,classification_report 
print("R2 Score:",r2_score(y_test, y_pred)) 
print("Accuracy:",accuracy_score(y_test, y_pred)*100) 
print("Classification Report:\n",classification_report(y_test, y_pred)) 



# Saving the model
import pickle
pickle.dump(classifier, open('svcmodel.pkl','wb'))



# Sample test
model = pickle.load(open('svcmodel.pkl','rb'))
print(model.predict([[6,148,72,35,0,33.6,0.627,50]])[0])
