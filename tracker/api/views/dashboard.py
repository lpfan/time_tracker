from flask.ext.restful import fields, marshal
from flask.ext.login import login_required

from base import BaseResource
from tracker.shared_lib.decorators import validate_input


class DashboardView(BaseResource):

    @login_required
    def get(self):
        return 'success'


class SyncNewTask(BaseResource):

    def post_validator(self):
        self.rp.add_argument('title', type=str, required=True)
        self.rp.add_argument('description', type=str, required=True)
        self.rp.add_argument('start_time', type=str, required=True)
        return self.rp

    @login_required
    @validate_input
    def post(self, valid_data):
        return valid_data
