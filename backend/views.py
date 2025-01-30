from flask import render_template, request, redirect, url_for
from flask_login import login_user, logout_user, current_user, login_required

from models import User, Response, Survey, Question, ResponderAnswer


def register_routes(app, db, bcrypt):
  pass