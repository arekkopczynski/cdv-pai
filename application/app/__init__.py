# __init__.py

from flask import Flask

app = Flask(__name__)
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

from app import base, routes

# Uncomment below line to import exmaple data and run project, after that comment it and re-run project
# from app import insert
