"""
Routes and views for the flask application.
"""

from datetime import datetime
from flask import render_template, request
from . import app
from obesity_project.ml_methods import RunPrediction

@app.route('/')
@app.route('/home')
def home():
    """Renders the home page."""
    return render_template('index.html',)


@app.route('/model')
def model():
    """Renders the machine learning model page."""
    return render_template('model.html')


@app.route('/predictor')
def predictor():
    """Renders the prediction page."""
    return render_template('predictor.html')

@app.route('/results',methods = ['POST'])
def results():
    """Renders the prediction page."""
    form_inputs = request.form.to_dict() 
    form_inputs = list(form_inputs.values()) 
    form_inputs = list(map(float, form_inputs)) 
    result = RunPrediction(form_inputs)         
    if int(result) == 0: 
        prediction ='By our predictions, maybe it\'s genetics, maybe it\'s malnourishment... You may be Under Weight'
    elif int(result) == 1:
        prediction ='By our predictions, you\'re probably maintaining a Healthy Weight'            
    elif int(result) == 2:
        prediction ='By our predictions, your habits are likely to make you Overweight, if you aren\'t already.'            
    elif int(result) == 3:
        prediction ='By our predictions, you could be getting Obese, if you aren\'t already.'            
    return render_template("results.html",
             prediction = prediction
             )