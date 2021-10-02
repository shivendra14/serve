#export FLASK_APP=application.py
#export FLASK_ENV=development
#flask run

from flask import Flask
app  = Flask(__name__)

@app.route('/')
def index():
    return 'Hello!'

@app.route('/drinks')
def get_drinks():
        return {"drink":"cola"}