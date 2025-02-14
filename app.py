from flask import Flask, render_template, request
import numpy as np
import pandas as pd
import os
from mlproject.pipeline.prediction import PredictionPipeline

app = Flask(__name__)  # Initializing the Flask app

# Route for the home page
@app.route('/', methods=['GET'])
def homePage():
    return render_template("index.html")

# Route to predict wine quality
@app.route('/predict', methods=['POST'])
def predict():
    try:
        # Collect input values from the form
        features = [
            float(request.form['fixed_acidity']),
            float(request.form['volatile_acidity']),
            float(request.form['citric_acid']),
            float(request.form['residual_sugar']),
            float(request.form['chlorides']),
            float(request.form['free_sulfur_dioxide']),
            float(request.form['total_sulfur_dioxide']),
            float(request.form['density']),
            float(request.form['pH']),
            float(request.form['sulphates']),
            float(request.form['alcohol'])
        ]

        # Convert input into a NumPy array
        data = np.array(features).reshape(1, -1)

        # Load the trained model and predict
        model = PredictionPipeline()
        prediction = model.predict(data)

        return render_template("results.html", prediction=int(prediction[0]))

    except Exception as e:
        return f"Error: {str(e)}"

# Route to train the model
@app.route('/train', methods=['GET'])
def training():
    os.system("python main.py")  # Runs main.py for training
    return "Training Successful!"

if __name__ == "__main__":
    app.run(debug=True)
