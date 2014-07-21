class BaseConfig(object):
    SECRET_KEY = '675d50af2aa51e006242f36804b35a1c'
    SQLALCHEMY_DATABASE_URI = "mysql://tracker:123456@127.0.0.1/time_tracker"
    AUTH_HEADER_NAME = 'Authentication'
