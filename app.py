from flask import Flask, render_template, request, url_for, flash, redirect
from flask_login import login_manager, LoginManager, login_user

import sqlite3

app = Flask(__name__)
app.secret_key = "mySuperSecretKey"

login_manager.login_view = "/login"


def get_db_connection():
    conn = sqlite3.connect('database.db')
    conn.row_factory = sqlite3.Row
    return conn


@app.route('/')
def welcome():
   return render_template('welcome.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
   if request.method == 'POST':
      email = request.form['email']
      password = request.form['password']

      conn = get_db_connection()
      user = conn.execute('SELECT * FROM user where email = "?" and password = "?"', (email, password)).fetchall()
      print(user)
      conn.close()
   else:
      return render_template('login.html')

@app.route('/register')
def register():
   return render_template('register.html')

def signup_post():
    return redirect(url_for('auth.login'))

class events:
    def __init__(self, date, title, desc):
        self.date = date
        self.title = title
        self.desc = desc
 
# creating list
list = []
 
# appending instances to list
list.append(events('15h30', 'Levar meu hamster para o jiu jitsu', 'Lorem ipsum dolor si amet'))
list.append(events('15h30', 'Levar meu hamster para o jiu jitsu', 'Lorem ipsum dolor si amet'))
list.append(events('15h30', 'Levar meu hamster para o jiu jitsu', 'Lorem ipsum dolor si amet'))
list.append(events('15h30', 'Levar meu hamster para o jiu jitsu', 'Lorem ipsum dolor si amet'))
list.append(events('15h30', 'Levar meu hamster para o jiu jitsu', 'Lorem ipsum dolor si amet'))
list.append(events('15h30', 'Levar meu hamster para o jiu jitsu', 'Lorem ipsum dolor si amet'))


@app.route('/daily-view')
def daily_view():
    return render_template('daily-view.html', view="D", title="Atividades do dia", events=list)

@app.route('/month-view')
def month_view():
   return render_template('month-view.html', view="M", title="Visão mensal")