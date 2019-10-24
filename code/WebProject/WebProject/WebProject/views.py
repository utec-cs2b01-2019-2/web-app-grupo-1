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
app.secret_key = ".."


#Pages

@app.route('/')
@app.route('/home')
def home():
    """Renders the home page."""
    if 'logged_name' in session:

        return render_template(
            'home.html',
            name=session['logged_name'],
            title='Home Page',
            year=datetime.now().year,
        )
    else:
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
    user = entities.User(fullname=c['fullname'], email=c['email'], password=c['password'])
    db_session = db.getSession(engine)
    db_session.add(user)
    db_session.commit()
    return 'Created User'

@app.route('/users', methods = ['GET'])
def get_users():
    db_session = db.getSession(engine)
    dbResponse = db_session.query(entities.User)
    data = dbResponse[:]
    return Response(json.dumps(data, cls=connector.AlchemyEncoder), mimetype='application/json')

@app.route('/users/<id>', methods = ['GET'])
def get_user(id):
    db_session = db.getSession(engine)
    users = db_session.query(entities.User).filter(entities.User.id == id)
    for user in users:
        js = json.dumps(user, cls=connector.AlchemyEncoder)
        return  Response(js, status=200, mimetype='application/json')

    message = { 'status': 404, 'message': 'Not Found'}
    return Response(message, status=404, mimetype='application/json')



@app.route('/authenticate', methods = ['POST'])
def authenticate():
    message = json.loads(request.data)
    email = message['email']
    password = message['password']

    db_session = db.getSession(engine)
    user = db_session.query(entities.User).filter_by(email=email
            #).filter(entities.User.password==password
            ).one()
    if user and (user.password==password):        
        session['logged_user'] = user.id
        session['logged_name'] = user.fullname
        message = {'message':'Authorized'}
        return Response(json.dumps(message,cls=connector.AlchemyEncoder), status=200,mimetype='application/json')
    else:
        message = {'message':'Unauthorized'}
        return Response(json.dumps(message,cls=connector.AlchemyEncoder), status=401,mimetype='application/json')

@app.route('/current', methods = ['GET'])
def current_user():
    db_session = db.getSession(engine)
    user = db_session.query(entities.User).filter(entities.User.id == session['logged_user']).first()
    return Response(json.dumps(user,cls=connector.AlchemyEncoder),mimetype='application/json')