import os
from flask import Flask
from flask_login.utils import _secret_key
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from config import DevConfig, ProdConfig, TestConfig
from extensions import db, ma
from flask_login import LoginManager, login_manager
from flask_bcrypt import Bcrypt


def create_app():
  app = Flask(__name__)

  config_name = os.getenv('FLASK_ENV', 'development')

  if config_name == 'production':
    app.config.from_object(ProdConfig)
  elif config_name == 'testing':
    app.config.from_object(TestConfig)
  else:
    app.config.from_object(DevConfig)

  app.secret_key = os.getenv('SECRET_KEY')
  
  db.init_app(app)
  ma.init_app(app)

  login_manager = LoginManager()
  login_manager.init_app(app)

  from models import User

  @login_manager.user_loader
  def load_user(user_id):
    return User.query.get(user_id)

  bcrypt = Bcrypt(app)
  
  from views import register_routes
  register_routes(app, db, bcrypt)
  
  Migrate(app, db)
  
  return app
  
