from tracker import db

from shared_lib import db_managers


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

    # Flask-Login integration
    def is_authenticated(self):
        return True

    def is_anonymous(self):
        return False

    def get_id(self):
        return self.id

    def save(self, *args, **kwargs):
        self.objects.save(*args, **kwargs)

    def __repr__(self):
        return "%s %s" % (self.id, self.username,)
