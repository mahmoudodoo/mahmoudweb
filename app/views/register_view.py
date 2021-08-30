

from flask.helpers import url_for
from app import app
from flask import render_template, flash, redirect
from app.models.user_model import User
from app.forms.register_form import RegistrationForm
import requests
host_name = 'https://mahmoudweb.azurewebsites.net/'
#host_name = 'http://127.0.0.1:5000/'
@app.route('/register',methods=['GET', 'POST'])
def register_view():
    form = RegistrationForm()
    if form.validate_on_submit():
        payload = {'name':form.username.data,'password':form.password.data,'is_admin':False}
        r = requests.post(f'{host_name}users',json=payload) 
        if r.ok:
            flash('Congratulations, you are now a registered user!')
            return redirect(url_for('login_view'))
        else:
            flash('Error: {}'.format(r.status_code))
    return render_template('register_template.html',title='Register', form=form)
