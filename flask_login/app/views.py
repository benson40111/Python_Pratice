from app import app
from flask import render_template, session, request, redirect, url_for

app.secret_key = 'F12Zr47j\3yX R~X@H!jLwf/T'

@app.route('/')
def hello_world():
    return 'hello world'

@app.route('/login')
def login():
    return render_template("login.html")

@app.route('/do_login', methods=['POST'])
def do_login():
    name = request.form.get('user_name')
    if (name != ''):
        session['user_name'] = name
        return session['user_name']
    else:
        return redirect(url_for('login'))

@app.route('/show')
def show():
    return session['user_name']

@app.route('/logout')
def logout():
    session.pop('user_name', None)
    return redirect(url_for('login'))
