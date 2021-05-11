from flask import Flask
from datetime import datetime

app = Flask(__name__)

counter = 0

@app.route('/')
def welcome():
  return 'Welcome to my page!'

@app.route('/date')
def date():
  return "this page was served at " + str(datetime.now())

@app.route('/num')
def num():
  global counter
  counter += 1
  return (f"this page was visited {counter} times")
