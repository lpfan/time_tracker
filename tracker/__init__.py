from flask.ext.sqlalchemy import SQLAlchemy
from flask.ext.kvsession import KVSessionExtension
from flask.ext import login
from flask.ext.bcrypt import Bcrypt
from simplekv.db.sql import SQLAlchemyStore as KVDBStore
from flask import Flask

from config.base import BaseConfig
from tracker.api import Api


app = Flask(__name__)
app.config.from_object(BaseConfig)
db = SQLAlchemy(app)
tt_api = Api(app)
bcrypt = Bcrypt(app)

store = KVDBStore(db.engine, db.metadata, 'sessions')
KVSessionExtension(store, app)

login_manager = login.LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'login_view'
login_manager.session_protection = "strong"

import routes
import api.routes
