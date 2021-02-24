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
    return render_template(
        'index.html',
        title='Home Page',
        year=datetime.now().year,
    )


@app.route('/contact')
def contact():
    """Renders the contact page."""
    return render_template(
        'contact.html',
        title='Contact',
        year=datetime.now().year,
        message='Your contact page.'
    )


@app.route('/about')
def about():
    """Renders the about page."""
    return render_template(
        'about.html',
        title='About',
        year=datetime.now().year,
        message='Your application description page.'
    )


@app.route('/details')
def details():
    """Renders the about page."""
    return render_template(
        'details.html',
        title='Details',
        year=datetime.now().year,
        message='Your application description page.'
    )


@app.route('/plot')
def plot():
    """Renders the contact page."""
    return render_template(
        'plot.html',
        title='Financial Report',
        year=datetime.now().year,
        message='Your Financial report page.'
    )

@app.route('/test')
def test():
    """Renders the contact page."""
    return render_template(
        'test.html',
        title='How to add a page',
        year=datetime.now().year,
        message='Testing how to add a page'
    )
