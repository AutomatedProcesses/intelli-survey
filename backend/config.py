from decouple import config
import os

BASE_DIR = os.path.dirname(os.path.realpath(__file__))

class Config:
  SECRET_KEY=config('SECRET_KEY')
  SQLALCHEMY_TRACK_MODIFICATIONS=config('SQLALCHEMY_TRACK_MODIFICATIONS', default=False, cast=bool)


class DevConfig(Config):
  SQLALCHEMY_DATABASET_URI='sqlite:///'+os.path.join(BASE_DIR, 'dev.db')
  DEBUG=True
  SQLALCHEMY_ECHO=True


class ProdConfig(Config):
  SQLALCHEMY_DATABASE_URI=config('DATABASE_URL', default='sqlite:///' + os.path.join(BASE_DIR, 'prod.db'))
  DEBUG=False


class TestConfig(Config):
  SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(BASE_DIR, 'test.db')
  DEBUG = True
  TESTING = True