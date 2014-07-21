from flask.ext import restful
from flask.ext.restful import reqparse


class BaseResource(restful.Resource):

    def __init__(self, *args, **kwargs):
        self._parser = None
        super(BaseResource, self).__init__(*args, **kwargs)

    @property
    def rp(self):
        if self._parser == None:
            self._parser = reqparse.RequestParser()

        return self._parser

