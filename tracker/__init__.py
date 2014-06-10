from flask.ext.sqlalchemy import SQLAlchemy
from flask.ext import restful
from flask import Flask


app = Flask(__name__)
db = SQLAlchemy(app)
api = restful.Api(app)
