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


@app.route('/about')
def about():
    return render_template(
        'about.html',
        title= 'About',
        year=datetime.now().year,
        message='About App'
        )




@app.route('/login')
def login():                     
    """Renders login """
    return render_template(
        'login.html',
        title='Login',
        year=datetime.now().year,
        message='Login to your existing account'
    )

@app.route('/signup')
def signup():
    """Renders signup"""
    return render_template(
        'signup.html',
        title='Sign Up',
        year=datetime.now().year,
        message='Create a new account'
    )
