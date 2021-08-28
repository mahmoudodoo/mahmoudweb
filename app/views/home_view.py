from app import app
from flask import render_template,flash, redirect,request
from flask_login import login_required
import requests


@app.route('/', methods=['GET', 'POST'])
def home_view():
    if request.method == 'GET':
        r = requests.get('http://127.0.0.1:5000/courses')
        try:
            courses = r.json()['courses']
        except KeyError:
            courses = {}    
    return render_template('home_template.html',courses=courses)