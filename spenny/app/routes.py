from flask import render_template, flash, redirect, url_for, request, session
from flask_login import login_user, logout_user, current_user, login_required
from werkzeug.urls import url_parse
from app import app, db
from app.forms import LoginForm, RegisterForm
from app.models import User



@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html', title='Welcome')

from flask import render_template, flash, redirect

@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.username.data).first()
        if user is None or not user.check_password(form.password.data):
            flash('Invalid username or password')
            return redirect(url_for('login'))
        else:
            session['username'] = form.username.data
            return redirect(url_for('dashboard'))
    return render_template('login.html', title='Sign In', form=form)


@app.route('/logout')
def logout():
    logout_user()
    del session['username']

    return redirect(url_for('index'))



@app.route('/register', methods=['GET', 'POST'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    form = RegisterForm()
#    if form.validate_on_submit():
    if request.method == 'POST':
        newUser = User(name=form.name.data, birthdate=form.birthdate.data,
                       email=form.email.data, password=form.password.data,
                       location=form.location.data, occupation=form.occupation.data,
                       income=form.income.data, accomcost=form.accomcost.data,
                       adultdependents=form.adultdependents.data, childdependents=form.childdependents.data,
                       smoker=form.smoker.data, drinker=form.drinker.data)
        db.session.add(newUser)
        db.session.commit()
        return redirect(url_for('login'))

    return render_template('register.html', title='Register', form=form)
    

@app.route('/dashboard/')
def dashboard():
    
    userTemp = User.query.filter_by(email=session['username']).first()
    region = userTemp.location
    salary = userTemp.income
    spendingPattern = "Moderate"
    drinks = bool(userTemp.drinker)
    smokes = bool(userTemp.smoker)
    rent = userTemp.accomcost
    numAdults = userTemp.adultdependents
    numChildren = userTemp.childdependents
    yearsToSave = 0
    initalAssets = 0
    amountToSave = 0
    return render_template('dashboard.html', title='Welcome', user=userTemp)



