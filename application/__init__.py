__author__ = 'fernando'
from flask import Flask, render_template, jsonify, json, Response
import flask.ext.restless
from models import *

app = Flask(__name__)
app.config['DEBUG'] = True
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///../flasktest.sqlite'

db.app = app
db.init_app(app)
db.create_all()

API_PREFIX = '/api/v1'
# Create the Flask-Restless API manager.
manager = flask.ext.restless.APIManager(app, flask_sqlalchemy_db=db)
manager.create_api(Provincia, methods=['GET'], url_prefix=API_PREFIX, collection_name='provincias')
manager.create_api(Coto, methods=['GET'], url_prefix=API_PREFIX, collection_name='cotos')
manager.create_api(Calibre, methods=['GET'], url_prefix=API_PREFIX, collection_name='calibres')
manager.create_api(Actividad, methods=['GET', 'POST'], url_prefix=API_PREFIX, collection_name='actividades')



import routes