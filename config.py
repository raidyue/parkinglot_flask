import os


class Config(object):
    SQLALCHEMY_DATABASE_URI = "mysql://root:123456@127.0.0.1/demo"
    SQLALCHEMY_TRACK_MODIFICATIONS = True
    DEBUG = True
    SECRET_KEY = 'guess'

class ProductConfig(Config):
    DEBUG = False
