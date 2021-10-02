'''
python3 -m venv .venv
source .venv/bin/activate
pip3 install flask
pip3 install flask-sqlalchemy
pip3 install requests
touch requirements.txt
pip3 freeze > requirements.txt
'''

'''
#export FLASK_APP=application.py
#export FLASK_ENV=development
#flask run
'''

'''
from application import db
from application import Drink
db.create_all()
db.session.add(Drink(name="Cherry", description="awesome"))
db.session.commit()
Drink.query.all()
'''

from flask import Flask, request
from flask_sqlalchemy import SQLAlchemy
app  = Flask(__name__)
db  = SQLAlchemy(app)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.db'
class Drink(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), unique=True, nullable=False)
    description = db.Column(db.String(120))

    def __repr__(self) -> str:
        return f"{self.name} - {self.description}"

@app.route('/')
def index():
    return 'Hello!'

@app.route('/drinks')
def get_drinks():
    drinks = Drink.query.all()
    output = []
    for drink in drinks:
        data = {'name': drink.name, 'description':drink.description}
        output.append(data)

    return {"drinks":output}

@app.route('/drinks/<id>')
def get_drink(id):
    drink = Drink.query.get_or_404(id)
    return {'name': drink.name, 'description':drink.description}

@app.route('/drinks', methods=['POST'])
def add_drink():
    drink = Drink(name=request.json['name'], description=request.json['description'])
    db.session.add(drink)
    db.session.commit()
    return {'id': drink.id}

@app.route('/drinks/<id>', methods=['DELETE'])
def delete_drink(id):
    drink = Drink.query.get(id)
    if drink is None:
        return {"error":"not found"}
    else:
        db.session.delete(drink)
        db.session.commit()
        return {"message":"done deleted"}