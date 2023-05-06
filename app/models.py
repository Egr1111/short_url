
from flask import Flask

from flask_sqlalchemy import SQLAlchemy
import datetime
from . import db


class User(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    username = db.Column(db.String(255), unique = True)
    password = db.Column(db.String())
    email = db.Column(db.String(100), unique = True)

class Urls(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    url = db.Column(db.String(255), nullable = False)
    username = db.Column(db.Integer, db.ForeignKey("user.id"), unique = True)
    data_created = db.Column(db.DateTime, default=datetime.datetime.utcnow)
