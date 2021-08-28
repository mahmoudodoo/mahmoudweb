from app import app
from flask import render_template,flash, redirect,request

@app.route('/about_me', methods=['GET', 'POST'])
def about_me_view():
    return render_template('about_me_template.html')