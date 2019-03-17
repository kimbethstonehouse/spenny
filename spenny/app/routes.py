from flask import render_template, flash, redirect, url_for, request
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
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.username.data).first()
        if user is None or not user.check_password(form.password.data):
            flash('Invalid username or password')
            return redirect(url_for('login'))
        login_user(user, remember=form.remember_me.data)
        next_page = request.args.get('next')
        if not next_page or url_parse(next_page).netloc != '':
            next_page = url_for('index')
        return redirect(next_page)
    return render_template('login.html', title='Sign In', form=form)


@app.route('/logout')
def logout():
    logout_user()
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
        flash('Congratulations, you are now a registered user!')
        return redirect(url_for('login'))

    return render_template('register.html', title='Register', form=form)
    

@app.route('/dashboard')
@login_required
def dashboard():
    return render_template('index.html', title='Welcome')


