from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField, SelectField
from wtforms.fields.html5 import DateField
from wtforms.validators import DataRequired, EqualTo


class LoginForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    remember_me = BooleanField('Remember Me')
    submit = SubmitField('Sign In')

class RegisterForm(FlaskForm):
    name = StringField('Name', validators=[DataRequired()])
    birthdate = DateField('Date Of Birth', format="%Y-%m-%d")
    email = StringField('Email', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    location = SelectField('Location', choices=[('1', 'England'), ('2', 'North East'), ('3', 'North West'), 
                                                ('4', 'Yorkshire and The Humber'), ('5', 'East Midlands'), ('6', 'West Midlands'),
                                                ('7', 'East'), ('8', 'London'), ('9', 'South East'),
                                                ('10', 'South West'), ('11', 'Wales'), ('12', 'Scotland'),
                                                ('13', 'North Ireland')])
    occupation = SelectField('Occupation', choices=[('full', 'Full Time Employed'), ('part', 'Part Time Employed'), ('stud', 'Student'), 
                                                ('ret', 'Retired'), ('unemp', 'Unemployed')])    
    income = StringField('Annual Disposable Income (After Taxes, including benefits)', validators=[DataRequired()])
    accomcost = StringField('Rent/Mortgage Costs', validators=[DataRequired()])
    adultdependents = StringField('Household Adults', validators=[DataRequired()])
    childdependents = StringField('Household Children', validators=[DataRequired()])
    smoker = SelectField('Are you a Smoker?', choices=[('YES', 'Smoker'), ('NO', 'Non-Smoker')]) 
    drinker = SelectField('Do you drink Alcohol?', choices=[('YES', 'Drink Alcohol'), ('NO', 'Don\'t Drink')]) 
    submit = SubmitField('Register')    