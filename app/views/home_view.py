from app import app
from flask import render_template,flash, redirect,request
from flask_login import login_required
import requests

host_name = 'https://melearning.azurewebsites.net/'
#host_name = 'http://127.0.0.1:5000/'
@app.route('/', methods=['GET', 'POST'])
def home_view():
    if request.method == 'GET':
        r = requests.get(f'{host_name}courses')
        try:
            courses = r.json()['courses']
        except:
            courses = {}    
    return render_template('home_template.html',courses=courses)
