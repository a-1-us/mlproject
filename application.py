from flask import Flask, request, render_template
import os
from src.pipeline.predict_pipeline import CustomData, PredictPipeline

application = Flask(__name__)

@application.route('/')
def index():
    return render_template('index.html')

@application.route('/predictdata', methods=['GET', 'POST'])
def predict_datapoint():
    if request.method == 'GET':
        return render_template('home.html')
    else:
       
        data = CustomData(
            gender=request.form.get('gender'),
            
        )
       
        return render_template('home.html', results=round(results[0], 2))

if __name__ == "__main__":
    application.run(host="0.0.0.0")
