
from flask.helpers import url_for
from app import app
from flask import render_template,flash, redirect
from app.forms.login_form import LoginForm
from app.models.user_model import User
import requests
from flask_login import logout_user,login_user,current_user




# Create login form view
@app.route('/login', methods=['GET', 'POST'])
def login_view():
    if current_user.is_authenticated:
        return redirect(url_for('home_view'))

    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(name=form.username.data).first()
        if user is None or not user.check_password(form.password.data):
            flash('Invalid username or password')
            return redirect(url_for('login'))
        login_user(user)
        return redirect(url_for('home_view'))
    return render_template('login_template.html', title='Sign In', form=form)



# Create Log out function
@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('login_view'))
