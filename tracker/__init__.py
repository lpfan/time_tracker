from flask.ext.sqlalchemy import SQLAlchemy
from flask.ext import restful
from flask.ext.kvsession import KVSessionExtension
from simplekv.db.sql import SQLAlchemyStore as KVDBStore
from flask import Flask


app = Flask(__name__)
db = SQLAlchemy(app)
api = restful.Api(app)

store = KVDBStore(db.engine, db.metadata, 'sessions')
KVSessionExtension(store, app)

import routes
