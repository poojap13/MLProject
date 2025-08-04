from flask import Flask, request, render_template
import numpy as np
import pandas as pd
import sklearn
print("scikit-learn version on Render:", sklearn.__version__)

from sklearn.preprocessing import StandardScaler
from src.pipeline.predict_pipeline import CustomData, PredictPipeline

application = Flask(__name__)  # Use "application" for Render

@application.route('/')
def index():
    # Directly show the main form page
    return render_template('home.html')

@application.route('/predictdata', methods=['GET', 'POST'])
def predict_datapoint():
    if request.method == 'GET':
        return render_template('home.html')
    else:
        try:
            # Get form data
            data = CustomData(
                gender=request.form.get('gender'),
                race_ethnicity=request.form.get('race_ethnicity'),
                parental_level_of_education=request.form.get('parental_level_of_education'),
                lunch=request.form.get('lunch'),
                test_preparation_course=request.form.get('test_preparation_course'),
                reading_score=float(request.form.get('reading_score')),
                writing_score=float(request.form.get('writing_score'))
            )

            # Convert to DataFrame
            pred_df = data.get_data_as_data_frame()
            print(pred_df)

            # Make prediction
            predict_pipeline = PredictPipeline()
            results = predict_pipeline.predict(pred_df)

            # Clamp and round result
            score = round(max(0, min(100, results[0])), 2)

            return render_template(
                'home.html',
                results=score,
                gender=request.form.get('gender'),
                race_ethnicity=request.form.get('race_ethnicity'),
                parental_level_of_education=request.form.get('parental_level_of_education'),
                lunch=request.form.get('lunch'),
                test_preparation_course=request.form.get('test_preparation_course'),
                reading_score=request.form.get('reading_score'),
                writing_score=request.form.get('writing_score')
            )

        except Exception as e:
            return f"Something went wrong: {e}", 500

if __name__ == "__main__":
    application.run(debug=True)
