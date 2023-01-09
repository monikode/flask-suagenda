from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def welcome():
   return render_template('welcome.html')

@app.route('/login')
def login():
   return render_template('login.html')

@app.route('/register')
def login():
   return render_template('register.html')