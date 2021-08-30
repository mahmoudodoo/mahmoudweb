
from app import app
from flask import render_template,flash, redirect,request,send_from_directory,url_for,Flask
from app.forms.course_form import AddCourseForm,DeleteCourseForm
import requests


host_name = 'https://melearning.azurewebsites.net/'
#host_name = 'http://127.0.0.1:5000/'


@app.route('/course', methods=['GET', 'POST'])
def course_view():
    add_form = AddCourseForm()
    if add_form.validate_on_submit():
        course_name = add_form.course_name.data
        description = add_form.description.data
        data = {'name':course_name,'description':description}
        r= requests.post(f'{host_name}courses',json=data)
        if r.ok:
            print('course has been added!!')
            return redirect(url_for('home_view'))

    delete_form = DeleteCourseForm()
    if delete_form.validate_on_submit():
        course_id = delete_form.course_id.data
        r= requests.delete(f'{host_name}courses/{course_id}')
        if r.ok:
            print('This course {} has been deleted!!'.format(course_id))
            return redirect(url_for('home_view'))
        if r.status_code == 404:
            flash('course ID not found!')
            return redirect(url_for('home_view'))
    return render_template('course_template.html',add_form =add_form,delete_form=delete_form)


@app.route('/course/lessons/<public_id>', methods=['GET', 'POST'])
def course_lessons(public_id):
    if request.method == 'GET':
        r = requests.get(f'{host_name}lessons')
        try:
            lessons = r.json()['lessons']
            output_dict = [x for x in lessons if x['course_id'] == public_id]
            queries = request.args
            data ={}
            for k, v in request.args.items():
                data[k] = v
        except:
            output_dict = {}

    return render_template('course_lessons_template.html',lessons=output_dict, course_description=data['description'])
