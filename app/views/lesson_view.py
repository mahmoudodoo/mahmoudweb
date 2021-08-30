from app import app
from flask import render_template,flash, redirect,url_for,Flask
from app.forms.lesson_form import AddLessonForm,DeleteLessonForm
from flask_login import login_required
import requests
host_name = 'https://melearning.azurewebsites.net/'
#host_name = 'http://127.0.0.1:5000/'
@app.route('/lesson', methods=['GET', 'POST'])
def lesson_view():
    add_form = AddLessonForm()
    if add_form.validate_on_submit():
        lesson_name = add_form.lesson_name.data
        lesson_course = add_form.course.data
        video_link= add_form.video_link.data
        data = {
            'name':lesson_name,
            'video_link':video_link,
            'course_id':lesson_course.public_id
                }
        r= requests.post(f'{host_name}lessons',json=data)
        if r.ok:
            print('Lesson has been added!!')
            return redirect(url_for('home_view'))


    delete_form = DeleteLessonForm()
    if delete_form.validate_on_submit():
        lesson_id = delete_form.lesson_id.data
        r= requests.delete(f'{host_name}lessons/{lesson_id}')
        if r.ok:
            return redirect(url_for('home_view'))
        if r.status_code == 404:
            flash('Lesson ID not found!')
            return redirect(url_for('lesson_view'))

    return render_template('lesson_template.html',add_form =add_form,delete_form=delete_form)

