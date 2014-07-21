from flask.ext.restful import fields, marshal


resource_fields = {
    'status':fields.String(default='unsuccess'),
    'code': fields.String(default='200'),
    'reason': fields.String,
    'field':fields.String
}


class TtBaseApiException(Exception):

    msg = ''
    original_code = 500
    reason = ''
    field = ''

    def to_dict(self):
        '''Convert text error mesasge to dict'''
        error = {}
        error['reason'] = self.reason
        error['field'] = self.field
        return marshal(error, resource_fields)


class RecordExists(TtBaseApiException):

    def __init__(self, field, value, message='', *args, **kwargs):
        super(RecordExists, self).__init__(*args, **kwargs)
        self.reason = '%s with %s already exists in db' % (field, value,)
        self.field = field


class UserNotAuthorized(TtBaseApiException):

    def __init__(self, username, message, *args, **kwargs):
        super(UserNotAuthorized, self).__init__(*args, **kwargs)
        self.reason = 'Wrong password for user with username %s' % username
        self.field = username


class UserNotFound(TtBaseApiException):

    def __init__(self, username, message, *args, **kwargs):
        super(UserNotFound, self).__init__(*args, **kwargs)
        self.reason = 'User with username %s not found' % username
        self.field = username
