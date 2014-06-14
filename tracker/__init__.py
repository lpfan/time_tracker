from flask.ext.sqlalchemy import SQLAlchemy
from flask.ext import restful
from flask.ext.kvsession import KVSessionExtension
from flask.ext import login
from simplekv.db.sql import SQLAlchemyStore as KVDBStore
from flask import Flask

from config.base import BaseConfig


app = Flask(__name__)
app.config.from_object(BaseConfig)
db = SQLAlchemy(app)
api = restful.Api(app)

store = KVDBStore(db.engine, db.metadata, 'sessions')
KVSessionExtension(store, app)

login_manager = login.LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'login_view'

import routes
