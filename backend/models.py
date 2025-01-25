import os
from re import S
from flask import Flask, request, jsonify, make_response
from sqlalchemy.orm import CascadeOptions
from flask_marshmallow import Marshmallow
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
import uuid
from datetime import datetime, timezone
from config import DevConfig, ProdConfig, TestConfig

app = Flask(__name__)

CORS(app)

config_name = os.getenv('FLASK_ENV', 'development')

if config_name == 'production':
  app.config.from_object(ProdConfig)
elif config_name == 'testing':
  app.config.from_object(TestConfig)
else:
  app.config.from_object(DevConfig)

basedir = os.path.abspath(os.path.dirname(__file__))

db = SQLAlchemy(app)
ma = Marshmallow(app)


class User(db.Model):
  '''
  Model for admin user
  '''
  __tablename__ = 'user'
  obj_id = db.Column(db.Integer, primary_key=True)
  username = db.Column(db.String(50), unique=True, nullable=False)
  password = db.Column(db.String(50), nullable=False)        # consider bcrypt for encryption
  email = db.Column(db.String(50), unique=True, nullable=False)
  date_created = db.Column(db.DateTime, default=lambda: datetime.now(timezone.utc))
  #is_admin = db.Column(db.Boolean, default=False)


class Response(db.Model):
  '''
  model of response - used for storing responses
  '''
  __tablename__ = 'response'
  obj_id = db.Column(db.Integer, primary_key=True)
  date_responded = db.Column(db.DateTime, default=lambda: datetime.now(timezone.utc))
  
  responder_answers = db.relationship('ResponderAnswer', cascade='all,delete', back_populates='response')
  

class Survey(db.Model):
  '''
  Model of the survey with general info, hash_key and array of corresponding question
  '''
  __tablename__ = 'survey'
  obj_id = db.Column(db.Integer, primary_key=True)
  hash_key = db.Column(db.String(36), unique=True, nullable=False, default=lambda: str(uuid.uuid4()))
  name = db.Column(db.String(100), unique=True, nullable=False)
  description = db.Column(db.Text, nullable=True)
  date_created = db.Column(db.DateTime, default=lambda: datetime.now(timezone.utc))
  
  questions = db.relationship('Question', cascade='all,delete', back_populates='survey')


class Question(db.Model):
  __tablename__ = 'question'
  obj_id = db.Column(db.Integer, primary_key=True)
  survey_id = db.Column(db.Integer, db.ForeignKey(Survey.obj_id))
  text = db.Column(db.Text, nullable=False)
  
  survey = db.relationship('Survey', back_polulates='questions')
  responder_answers = db.relationship('ResponderAnswer', cascade='all,delete', back_populates='question')


class ResponderAnswer(db.Model):
  '''
  Model of answers of each question of given suervey
  Each answer has relationship with question and questin has relationship with survey
  '''
  __tablename__ = 'responder_answer'
  response_id = db.Column(db.Integer, db.ForeignKey(Response.obj_id), primary_key=True, autoincrement=False)
  question_id = db.Column(db.Integer, db.ForeignKey(Question.obj_id), primary_key=True, autoincrement=False)
  answer = db.Column(db.Text)
  
  response = db.relationship('Response', back_populates='responder_answers')
  question = db.relationship('Question', back_populates='responder_answers')


class UserSchema(ma.Schema):
  class Meta:
    fields = ('obj_id', 'username', 'email', 'is_admin', 'date_created')


class QuestionSchema(ma.Schema):
  class Meta:
    fields = ('obj_id', 'survey_id', 'text')


class SurveySchema(ma.Schema):
  class Meta:
    fields = ('obj_id', 'hash_key', 'name', 'description', 'date_created')


class ResponderAnswerSchema(ma.Schema):
  class Meta:
    fields = ('response_id', 'survey_id', 'question_id', 'answer')          #survey_id