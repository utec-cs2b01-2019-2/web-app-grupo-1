"""
Routes and views for the flask application.
"""

from flask import Flask, render_template, request, session, Response, redirect
from datetime import datetime
from os import environ


from database import connector
from model import entities


import json
import time


db = connector.Manager()
engine = db.createEngine()

app = Flask(__name__)
app.secret_key = "lmao"



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
        'about_final.html',
        title= 'About',
        year=datetime.now().year,
        message='About App'
        )

@app.route('/linkchip')
def linkchip():
    return render_template(
        'chiplink.html',
        year=datetime.now().year
        )

@app.route('/balance')
def balance():
    return render_template(
        'balance.html',
        year=datetime.now().year,
        message='Check your current balance'
        )


@app.route('/login')
def login():
    """Renders login """
    return render_template(
        'login_final.html',
        title='Login',
        year=datetime.now().year,
        message='Login to your existing account'
    )

@app.route('/signup')
def signup():
    """Renders signup"""
    return render_template(
        'register.html',
        title='Sign Up',
        year=datetime.now().year,
        message='Create a new account'
    )


#Operations



#Users

@app.route('/users', methods = ['POST'])
def create_user():
    #c =  json.loads(request.form['values'])
    c =  json.loads(request.data)
    user = entities.User(fullname=c['fullname'], email=c['email'], password=c['password'], balance='0')
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

@app.route('/auth', methods = ['POST'])
def auth():

    message = json.loads(request.data)
    email = message['email']
    password = message['password']
    #remembercheck = message['remembercheck']

    db_session = db.getSession(engine)
    user = db_session.query(entities.User).filter_by(email=email).one()

    if user and (user.password==password):

        #if (remembercheck == 1):
        #    session.permanent = True;
        #else:
        #    session.permanent = False;

        session['logged_user'] = user.id
        session['logged_name'] = user.fullname
        message = {'message':'Authorized'}
        message = {'message':'Authorized', 'id': user.id, 'email': user.email, 'fullname': user.fullname}
        return Response(json.dumps(message,cls=connector.AlchemyEncoder), status=200,mimetype='application/json')
    else:
        message = {'message':'Unauthorized'}
        return Response(json.dumps(message,cls=connector.AlchemyEncoder), status=401,mimetype='application/json')

@app.route('/current', methods = ['GET'])
def current_user():
    db_session = db.getSession(engine)
    user = db_session.query(entities.User).filter(entities.User.id == session['logged_user']).first()
    return Response(json.dumps(user,cls=connector.AlchemyEncoder),mimetype='application/json')



@app.route('/logout', methods = ['GET'])
def logout():
    session.clear()
    return render_template('index.html')

#Balance

@app.route('/balance/current', methods = ['GET'])
def get_balance():
    db_session = db.getSession(engine)
    id = session['logged_user']
    user = db_session.query(entities.User).filter_by(id=id).one()
    balance = { "balance": user.balance }
    js = json.dumps(balance, cls=connector.AlchemyEncoder)
    return  Response(js, status=200, mimetype='application/json')




#API Chips

@app.route('/chips', methods = ['POST'])
def create_chip():
    db_session = db.getSession(engine)
    c= json.loads(request.data)
    chip = entities.Chips(code_from_user=c['code_from_user'], code=c['code'])
    db_session.add(chip)
    db_session.commit()

    return 'Linked Chip'

@app.route('/addchips', methods = ['POST'])
def add_chip():
    db_session = db.getSession(engine)
    c= json.loads(request.data)
    chip = entities.Chips(code=c['code'], code_from_user=session['logged_user'])
    db_session.add(chip)
    db_session.commit()
    js = json.dumps(chip, cls=connector.AlchemyEncoder)
    return Response(js,status=200,mimetype='application/json')   

@app.route('/chips/<id>', methods = ['GET'])
def get_chip(id):
    db_session = db.getSession(engine)
    chips = db_session(entities.Chips).filter(entities.Chips.id == id)
    for chip in chips:
        js = json.dumps(chip, cls=connector.AlchemyEncoder)
        return Response(js,status=200,mimetype='application/json')
    chip = {'status':404, 'chip': 'not found'}
    return Response(chip, status = 404, mimetype='application/json')


@app.route('/chips', methods = ['GET'])
def get_chips():
    sessionc = db.getSession(engine)
    dbResponse = sessionc.query(entities.Chips)
    data = dbResponse[:]
    return Response(json.dumps(data, cls=connector.AlchemyEncoder), mimetype='application/json')

@app.route('/chips/<code_from_user>', methods = ['GET'])
def get_chip_user(code_from_user):
    db_session = db.getSession(engine)
    chip_from = db_session.query(entities.Message).filter(
        entities.Message.user_from_id == code_from_user)

    data = []
    for chip in chip_from:
        data.append(chip)

    return Response(json.dumps(data, cls=connector.AlchemyEncoder), mimetype='application/json')

@app.route('/chips', methods = ['PUT'])
def update_chip():
    session = db.getSession(engine)
    id = request.form['key']
    chip = session.query(entities.Chips).filter(entities.Chips.id == id).first()
    c = json.loads(request.form['values'])
    for key in c.keys():
        setattr(chip, key, c[key])
    session.add(chip)
    session.commit()
    return 'Updated Chip'

@app.route('/chips', methods = ['DELETE'])
def delete_chip():
    id = request.form['key']
    session = db.getSession(engine)
    chip = session.query(entities.Chips).filter(entities.Chips.id == id).one()
    session.delete(chip)
    session.commit()
    return "Deleted Chip"


if __name__ == '__main__':
    app.run(port=8000, threaded=True, use_reloader=False)