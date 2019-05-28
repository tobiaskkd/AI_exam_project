
# Import libraries
import numpy as np
from sklearn.externals import joblib
from flask import Flask, request, jsonify, render_template
import pickle

# create an instance (our app)
app = Flask(__name__)

results = joblib.load('SARIMA_btc_pred.pkl')

@app.route('/', methods=['GET', 'POST'])
def predict():
    return render_template('prediction.html')

@app.route('/predicted', methods=['GET', 'POST'])
def predicted():
    if request.method == 'POST':
        months = int(request.form['months'])
        predicted = results.get_forecast(steps=months).predicted_mean
        
        predicted = predicted[len(predicted)-1]

        return render_template("predicted.html", months=months, prediction=predicted)

@app.route('/bye')
def bye():
    return render_template('bye.html')

if __name__ == '__main__':
    app.run(debug=True)
