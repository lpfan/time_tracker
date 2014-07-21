from base import BaseResource

from tracker.shared_lib.decorators import validate_input
from tracker.models import User
from tracker import bcrypt


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
