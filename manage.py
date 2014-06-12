from flask.ext.script import Manager

from tracker import app
from tracker import db
from config.base import BaseConfig


manager = Manager(app)

@manager.command
def runserver():
    app.config.from_object(BaseConfig)
    app.run(debug=True)

@manager.command
def db_create():
    app.config.from_object(BaseConfig)
    db.create_all()

if __name__ == '__main__':
    manager.run()
