import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from config import DevConfig, ProdConfig, TestConfig
from extensions import db, ma


def create_app():
  app = Flask(__name__)

  config_name = os.getenv('FLASK_ENV', 'development')

  if config_name == 'production':
    app.config.from_object(ProdConfig)
  elif config_name == 'testing':
    app.config.from_object(TestConfig)
  else:
    app.config.from_object(DevConfig)
  
  db.init_app(app)
  ma.init_app(app)
  
  from views import register_routes
  register_routes(app, db)
  
  Migrate(app, db)
  
  return app
  
