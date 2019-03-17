from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField, SelectField
from wtforms.fields.html5 import DateField
from wtforms.validators import ValidationError, DataRequired, Email, EqualTo
from app.models import User

class LoginForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    submit = SubmitField('Sign In')

class RegisterForm(FlaskForm):
    name = StringField('Name', validators=[DataRequired()])
    birthdate = DateField('Date Of Birth', format="%Y-%m-%d")
    email = StringField('Email', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    location = SelectField('Location', choices=[('England', 'England'), ('North East', 'North East'), ('North West', 'North West'), 
                                                ('Yorkshire and The Humber', 'Yorkshire and The Humber'), ('East Midlands', 'East Midlands'), ('West Midlands', 'West Midlands'),
                                                ('East', 'East'), ('London', 'London'), ('South East', 'South East'),
                                                ('South West', 'South West'), ('Wales', 'Wales'), ('Scotland', 'Scotland'),
                                                ('North Ireland', 'North Ireland')])
    occupation = SelectField('Occupation', choices=[('full', 'Full Time Employed'), ('part', 'Part Time Employed'), ('stud', 'Student'), 
                                                ('ret', 'Retired'), ('unemp', 'Unemployed')])    
    income = StringField('Annual Disposable Income (After Taxes, including benefits)', validators=[DataRequired()])
    accomcost = StringField('Rent/Mortgage Costs', validators=[DataRequired()])
    adultdependents = StringField('Household Adults', validators=[DataRequired()])
    childdependents = StringField('Household Children', validators=[DataRequired()])
    smoker = SelectField('Are you a Smoker?', choices=[('NULL', 'Do you smoke?'), ('True', 'Yes, I smoke.'), ('False', 'Non-Smoker')]) 
    drinker = SelectField('Do you drink Alcohol?', choices=[('NULL', 'Do you drink alcohol?'), ('True', 'Yes'), ('False', 'Don\'t Drink')]) 
    submit = SubmitField('Register')    