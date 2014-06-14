from sqlalchemy import exc

from tracker import db


class BaseManager(object):

    def __init__(self):
        self.session = db.session
        self.model = None

    def store(self):
        self.session.commit()

    def revert(self):
        self.session.rallback()

    def safe_execute(self, method=None, *args, **kwargs):
        on_success = self.store
        on_failure = self.revert

        try:
            if method:
                res = method(*args, **kwargs)
                on_success()
                return res
            on_success()
        except exc.SQLAlchemyError as err:
            print err

    def get(self, id):
        self.session.query(self.model).get(id)


class UserManager(BaseManager):

    def __init__(self, model):
        super(UserManager, self).__init__()
        self.model = model

    def save(self, *args, **kwargs):
        self.session.add(self.model)
        self.safe_execute()
