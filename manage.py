from flask.ext.script import Manager

from tracker import app
from config.base import BaseConfig


manager = Manager(app)

@manager.command
def runserver():
    app.config.from_object(BaseConfig)
    app.run(debug=True)


if __name__ == '__main__':
    manager.run()
