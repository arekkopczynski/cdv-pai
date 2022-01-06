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

    def __init__(self, id, name, value):
        self.id = id
        self.name = name
        self.value = value

db.create_all()
