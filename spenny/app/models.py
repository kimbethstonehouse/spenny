from datetime import datetime
from app import db, login
from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash

class User(UserMixin, db.Model):
    __tablename__ = 'users'
    email = db.Column(db.String(120), unique=True, primary_key=True)
    name = db.Column(db.String(50), unique=False)
    birthdate = db.Column(db.String(120), unique=False)
    password = db.Column(db.String(50), unique=False)
    location = db.Column(db.String(50), unique=False)
    occupation = db.Column(db.String(50), unique=False)
    income = db.Column(db.String(10), unique=False)
    accomcost = db.Column(db.String(10), unique=False)
    adultdependents = db.Column(db.String(10), unique=False)
    childdependents = db.Column(db.String(10), unique=False)
    smoker = db.Column(db.String(50), unique=False)
    drinker = db.Column(db.String(50), unique=False)

    def check_password(self, password):
        return self.password == password


    def __init__(self, name=None, birthdate=None, email=None, password=None, location = None, occupation = None, income = None, accomcost = None, adultdependents = None, childdependents = None, smoker = None, drinker = None):
        self.name = name
        self.birthdate = birthdate
        self.email = email
        self.password = password
        self.location = location
        self.occupation = occupation
        self.income = income
        self.accomcost = accomcost
        self.adultdependents = adultdependents
        self.childdependents = childdependents
        self.smoker = smoker
        self.drinker = drinker

    def __repr__(self):
        return '<User %r>' % (self.email)
