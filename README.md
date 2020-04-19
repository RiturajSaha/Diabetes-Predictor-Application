# Diabetes-Prediction
Diabetes is a disease that occurs when your blood glucose, also called blood sugar, is too high.

In this respository a differnt classification models are used to predict if a patient is diabetic or not from the various attributes in the dataset(https://www.kaggle.com/uciml/pima-indians-diabetes-database).

The various regression models appied to the dataset are compared using accuracy_score:
| Regression Models  | Accuracy |
| ------------- | ------------- |
| K Nearest Neighbor  | 71.42%  |
| Logistic Regression  | 78.57%  |
| Naive Bayes  | 77.27%  |
| Random Forest Classification  | 78.57%  |
| Linear Support Vector Classification  | 55.84%  |
| Support Vector Classification  | 80.51%  |

Out of all the  regression models Support Vector Classification has the highest accuracy of 80.51%, this model was then deployed using flask.
