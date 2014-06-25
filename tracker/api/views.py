from flask.ext import restful
from flask.ext.restful import reqparse

from tracker.shared_lib.decorators import validate_input
from tracker.models import User
from tracker import bcrypt


class BaseResource(restful.Resource):

    def __init__(self, *args, **kwargs):
        self._parser = None
        super(BaseResource, self).__init__(*args, **kwargs)

    @property
    def rp(self):
        if self._parser == None:
            self._parser = reqparse.RequestParser()

        return self._parser


class RegisterView(BaseResource):

    def post_validator(self):
        self.rp.add_argument('username', type=str, required=True)
        self.rp.add_argument('email', type=str, required=True)
        return self.rp

    @validate_input
    def post(self, valid_data):
        user = User()
        user.username = valid_data['username']
        user.email = valid_data['email']
        user.password = bcrypt.generate_password_hash('12345')
        user.save()
