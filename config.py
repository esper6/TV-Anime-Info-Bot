import os

class Config(object):
    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(os.path.dirname(__file__), 'anime.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False