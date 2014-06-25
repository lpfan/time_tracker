from flask.ext import restful

from tracker.shared_lib.errors import TtBaseApiException


class Api(restful.Api):

    def handle_error(self, error):
        '''custom error handler for our projects'''
        if not issubclass(error.__class__, TtBaseApiException):
            #@TODO: add logging
            return restful.Api.handle_error(self, error)

        return self.make_response(error.to_dict(), 200)
