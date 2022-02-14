# Diabetes-Predictor-Application
Diabetes is a disease that occurs when your blood glucose, also called blood sugar, is too high. Victims of this disease are increasing day by day. 

In this respository, a diabetes prediction application is created having a web based frontend and a machine learning backend. Here different classification models are used to predict if a patient is diabetic or not by taking essential patient details as input such as number of pregnancies, Plasma glucose concentration, Diastolic blood pressure, Triceps skin fold thickness, 2-Hour serum insulin, Body mass index, Diabetes pedigree function, and Age to predict if the patient is diabetic or normal.   

The dataset is obtained from kaggle: https://www.kaggle.com/uciml/pima-indians-diabetes-database

Below are the screenshots:
<p align="center"><img src="https://github.com/RiturajSaha/Diabetes-Predictor-Application/blob/master/screenshots/1.png" height=300 width="600"></p>
<p align="center"><img src="https://github.com/RiturajSaha/Diabetes-Predictor-Application/blob/master/screenshots/2.png" height=300 width="600"></p>

Below are the various classification models applied to the dataset are compared using accuracy_score r2_score:
| Regression Models  | Accuracy | R2 Score |
| ------------- | ------------- | ------------- |
| K Nearest Neighbor  | 75.32  | -0.1636 |
| Naive Bayes  | 79.22  | 0.0200 |
| Random Forest Classification  |  75.32  | -0.1636 |
| Linear Support Vector Classification  | 70.12  | -0.3780 |
| Support Vector Classification  | 81.81  | 0.1425 |

accuracy_score is the percentage of the success of a model to predcit the independent attribute and r2_score is a statistical measure that represents the goodness of fit of a regression model. The ideal value for r2_score is 1, its range is from -1 to 1. Some other methods to determine the success of a classification model are mean_squared_error, mean_absolute_error, confusion_matrix, calssification_report. 

Out of all the  Classification models above Support Vector Classification has the highest accuracy of 81.81%, this model is deployed using flask inorder to provide a web based interactive interface for users.

