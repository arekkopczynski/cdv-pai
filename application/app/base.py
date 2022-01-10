from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from app import app

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db/application.db'
db = SQLAlchemy(app)

class Expenses(db.Model):

    __tablename__ = 'expenses'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    value = db.Column(db.Integer)

    def __init__(self, name, value):
        self.name = name
        self.value = value

class Incomes(db.Model):

    __tablename__ = 'incomes'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    value = db.Column(db.Integer)

    def __init__(self, name, value):
        self.name = name
        self.value = value

db.create_all()

def total_funds():
    incomes = Incomes.query.all()
    expenses = Expenses.query.all();

    total_incomes = (sum([fund.value for fund in incomes]))
    total_expenses = (sum([fund.value for fund in expenses]))

    total_funds = total_incomes-total_expenses
    return total_funds
