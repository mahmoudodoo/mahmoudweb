from app import app
from flask import render_template,request
import requests
import os

@app.route('/video_lesson', methods=['GET', 'POST'])
def video_lesson_view():
    queries = request.args
    data ={}
    for k, v in request.args.items():
        data[k] = v
    print(data)
    return render_template('video_template.html',video_link=data['video_link'])