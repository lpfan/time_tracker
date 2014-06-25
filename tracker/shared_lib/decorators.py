import flask

from functools import wraps


def validate_input(method):
    """Decorator allows to validate input data for HTTP handler"""

    def wrapper(self, *args, **kwargs):
        validator_name = '%s_validator' % (flask.request.method.lower(),)
        validator = getattr(self, validator_name, None)

        if validator is None or not callable(validator):
            raise TypeError(
                'You have to define "%s" method in the "%s" class in order to get input validation works'
                % (validator_name, self.__class__.__name__)
            )

        parser = validator()
        valid_data = parser.parse_args()
        return method(self, valid_data=valid_data, *args, **kwargs)
    return wrapper
