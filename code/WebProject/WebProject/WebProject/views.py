"""
Routes and views for the flask application.
"""

from datetime import datetime
from flask import render_template
from WebProject import app

@app.route('/')
@app.route('/home')
def home():
    """Renders the home page."""
    return render_template(
        'index.html',
        title='Home Page',
        year=datetime.now().year,
    )

@app.route('/login')
def login():
    """Renders login """
    return render_template(
        'login.html',
        title='Login',
        year=datetime.now().year,
        message='Your contact page.'
    )

@app.route('/signup')
def about():
    """Renders signup"""
    return render_template(
        'signup.html',
        title='Sign Up',
        year=datetime.now().year,
        message='Your application description page.'
    )
