import hashlib
import time
import datetime

from flask.ext.restful import fields, marshal
from flask.ext.login import login_required, current_user

from base import BaseResource
from tracker.shared_lib.decorators import validate_input
from tracker.models import Task


class DashboardView(BaseResource):

    @login_required
    def get(self):
        return 'success'


class SyncNewTask(BaseResource):

    fields = {
        'uuid': fields.String
    }

    def post_validator(self):
        self.rp.add_argument('title', type=str, required=True)
        self.rp.add_argument('description', type=str, required=True)
        self.rp.add_argument('start_time', type=str, required=True)
        return self.rp

    @login_required
    @validate_input
    def post(self, valid_data):
        uuid = hashlib.md5('%s'%time.time()).hexdigest()
        new_task = Task().objects.create(
            uuid = uuid,
            title = valid_data['title'],
            description = valid_data['description'],
            start_time = valid_data['start_time'],
            date = datetime.date.today(),
            user_id = current_user.id
        )
        return marshal({'uuid':uuid}, self.fields)


class FinishNewTask(BaseResource):

    fields = {'status':fields.String}

    def post_validator(self):
        self.rp.add_argument('uuid', type=str, required=True)
        self.rp.add_argument('end_time', type=str, required=True)
        return self.rp

    @login_required
    @validate_input
    def post(self, valid_data):
        uuid = valid_data['uuid']
        current_task = Task().objects.get_by_uuid(uuid)
        current_task.end_time = valid_data['end_time']
        current_task.save()
        return marshal({'status':'success'}, self.fields)
