import os
from re import S
from flask import Flask, request, jsonify, make_response
from flask_marshmellow import Marshmellow
from flask_alchemy import SQLAlchemy
from flask_cors import CORS
import uuid
import datetime

app = Flask(__name__)

db = SQLAlchemy(app)
ma = Marshmellow(app)

class User(db.Model):
  '''
  Model for admin user
  '''
  __tablename__ = 'user'
  obj_id = db.Column(db.Integer, primary_key=True)
