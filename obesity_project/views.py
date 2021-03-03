"""
Routes and views for the flask application.
"""

from datetime import datetime
from flask import render_template
from . import app


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
