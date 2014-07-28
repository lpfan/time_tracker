from sqlalchemy.orm import exc
from itsdangerous import TimedJSONWebSignatureSerializer as Serializer

from tracker import db
from tracker import bcrypt
from tracker import app

from shared_lib import db_managers
from shared_lib import errors


def generate_token(user_id, expiration = 600):
    s = Serializer(app.config['SECRET_KEY'], expires_in = expiration)
    return s.dumps({'id':user_id})


class User(db.Model):

    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), unique=True)
    first_name = db.Column(db.String(200), nullable=True)
    last_name = db.Column(db.String(200), nullable=True)
    is_active = db.Column(db.Boolean, default=False)
    avatar = db.Column(db.String(200))
    email = db.Column(db.String(200))
    password = db.Column(db.String(200))

    @property
    def objects(self):
        return db_managers.UserManager(self)


    @staticmethod
    def verify_auth_token(token):
        s = Serializer(app.config['SECRET_KEY'])
        try:
            data = s.loads(token)
        except SignatureExpired:
            return None # valid token, but expired
        except BadSignature:
            return None # invalid token
        user = self.objects.get(data['id'])
        return user

    @classmethod
    def authorize(cls, username, password):
        q = db.session.query(cls).filter(cls.username == username)
        try:
            user = q.one()
            if bcrypt.check_password_hash(user.password, password):
                token = generate_token(user.id)
                return user, token
            else:
                raise errors.UserNotAuthorized(
                    username,
                    'Wrong password'
                )
        except exc.NoResultFound as error:
            raise errors.UserNotFound(
                username,
                error.message
            )

    # Flask-Login interation
    def is_authenticated(self):
        return True

    def is_active(self):
        return self.is_active

    def is_anonymous(self):
        return False

    def get_id(self):
        return self.id

    def save(self, *args, **kwargs):
        self.objects.save(*args, **kwargs)

    def __repr__(self):
        return "%s %s" % (self.id, self.username,)


class Task(db.Model):

    __tablename__ = 'tasks'

    id = db.Column(db.Integer, primary_key=True)
    date = db.Column(db.Date)
    start_time = db.Column(db.TIMESTAMP)
    end_time = db.Column(db.TIMESTAMP)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id', ondelete="CASCADE"))

    user = db.relationship('User', backref = db.backref('tasks', lazy='dynamic'))
