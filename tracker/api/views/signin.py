from flask.ext.restful import fields, marshal

from base import BaseResource
from tracker.shared_lib.decorators import validate_input
from tracker.models import User


resource_fields = {
    'status':fields.String(default='unsuccess'),
    'code': fields.String(default='200'),
    'token': fields.String,
}


class SignInView(BaseResource):

    def post_validator(self):
        self.rp.add_argument('username', type=str, required=True)
        self.rp.add_argument('password', type=str, required=True)
        return self.rp

    @validate_input
    def post(self, valid_data):
        username = valid_data['username']
        password = valid_data['password']
        token = User().authorize(username, password)
        return marshal({'token':token, 'status':'success'},resource_fields)
