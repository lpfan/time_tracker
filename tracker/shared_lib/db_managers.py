from sqlalchemy import exc

from tracker import db
from tracker.shared_lib import patterns
from tracker.shared_lib import errors


class BaseManager(object):

    def __init__(self):
        self.session = db.session
        self.model = None

    def store(self):
        self.session.commit()

    def revert(self):
        self.session.rollback()

    def safe_execute(self, method=None, *args, **kwargs):
        on_success = self.store
        on_failure = self.revert

        try:
            if method:
                res = method(*args, **kwargs)
                on_success()
                return res
            on_success()
        except exc.IntegrityError as err:
            on_failure()
            match = patterns.SA_UNIQ_PATTERN.search(err.orig.args[1])

            if match is not None:
                raise errors.RecordExists(
                    match.group('field_name'),
                    match.group('value'),
                    err.message
                )

        except exc.SQLAlchemyError as err:
            on_failure()
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


class TaskManager(BaseManager):

    def __init__(self, model, *args, **kwargs):
        super(TaskManager, self).__init__(*args, **kwargs)
        self.model = model

    def _create(self, **kwargs):
        """Create new Task and fill it with passed values of it's properties.
        """
        for key, value in kwargs.iteritems():
            if hasattr(self.model, key):
                setattr(self.model, key, value)

        self.session.add(self.model)
        self.session.commit()
        return self.model

    def create(self, **kwargs):
        """Trigger creater of new tags.
        """
        return self.safe_execute(self._create, **kwargs)

    def get_by_uuid(self, uuid):
        q = self.session.query(self.model.__class__).\
            filter(self.model.__class__.uuid == uuid)
        return q.one()

    def get_tasks_by_date(self, date_str):
        q = self.session.query(self.model.__class__).filter(
            self.model.__class__.date == date_str
        )
        return q.all()

    def save(self):
        self.safe_execute()
