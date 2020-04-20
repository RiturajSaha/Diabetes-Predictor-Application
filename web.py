import numpy as np
from flask import Flask, request, jsonify, render_template
import pickle

app = Flask(__name__)
model =pickle.load(open('SVC_model.pkl', 'rb'))

@app.route('/')
def homepage():
    return render_template('diabetes.html')

@app.route('/predict',methods=['POST'])
def predict():
    try:
      features = [np.array([x for x in request.form.values()])]
      print(features)
      prediction = model.predict(features)
      print(prediction)
      output ="Diabetic !" if prediction[0]==1 else "Normal !"
      return render_template('diabetes.html', prediction_text='The Patient is {}'.format(output))
    except:
        return render_template('diabetes.html', prediction_text="Invalid Input!")

if __name__ == "__main__":
    app.run(debug=True)