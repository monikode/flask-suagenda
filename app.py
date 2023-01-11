from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def welcome():
   return render_template('welcome.html')

@app.route('/login')
def login():
   return render_template('login.html')

@app.route('/register')
def register():
   return render_template('register.html')

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