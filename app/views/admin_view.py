from app import db
from app import app
from flask import render_template,flash, redirect,request
import requests
import os
from app import Config

@app.route('/admin', methods=['GET', 'POST'])
def admin_view():
    return render_template('admin_page_template.html')