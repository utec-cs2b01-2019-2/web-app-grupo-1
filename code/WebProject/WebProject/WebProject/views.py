"""
Routes and views for the flask application.
"""

from flask import Flask, render_template, request, session, Response, redirect
from datetime import datetime
from WebProject import app


from WebProject.database import connector
from WebProject.model import entities

import json
import time

db = connector.Manager()
engine = db.createEngine()


#Pages

@app.route('/')
@app.route('/home')
def home():
    """Renders the home page."""
    return render_template(
        'index.html',
        title='Home Page',
        year=datetime.now().year,
    )
@app.route('/static/<content>')
def html(content):
    return render_template(content)


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


#Operations


@app.route('/users', methods = ['POST'])
def create_user():
    #c =  json.loads(request.form['values'])
    c =  json.loads(request.data)
    users = entities.User(fullname=c['fullname'], email=c['email'], password=c['password'])
    session = db.getSession(engine)
    session.add(users)
    session.commit()
    return 'Created User'

@app.route('/users', methods = ['GET'])
def get_users():
    session = db.getSession(engine)
    dbResponse = session.query(entities.User)
    data = dbResponse[:]
    return Response(json.dumps(data, cls=connector.AlchemyEncoder), mimetype='application/json')
