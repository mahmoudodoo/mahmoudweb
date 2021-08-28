from flask import jsonify, request, abort,make_response
from app import db
from app import app
from app.models.course_model import Course
from app.models.lesson_model import Lesson
import uuid





@app.route('/courses', methods=['GET'])
def get_all_courses():
    courses= Course.query.all()
    output = []
    if not courses:
        return jsonify({'message':'No courses!'}),404

    for course in courses:
        course_data = {}
        course_data['public_id'] =course.public_id
        course_data['name']= course.name
        course_data['description'] = course.description
        output.append(course_data)

    return jsonify({'courses':output})

@app.route('/courses/<public_id>',methods=['GET'])
def get_one_course(public_id):
    course = Course.query.filter_by(public_id=public_id).first()
    if not course:
        return jsonify({'message':'Course not Found!!!!'}),404
    course_data = {}
    course_data['public_id'] =course.public_id
    course_data['name']= course.name
    course_data['description'] = course.description
   
    return jsonify({'Course':course_data})

@app.route('/courses',methods=['POST'])
def create_course():
    data = request.get_json()
    new_course = Course(public_id=str(uuid.uuid4()), name=data['name'],description= data['description'])
    db.session.add(new_course)
    db.session.commit()
    return jsonify({'message' :'New Course has been created!'})


@app.route('/courses/<public_id>',methods=['DELETE'])
def delete_course(public_id):
    
    course = Course.query.filter_by(public_id=public_id).first()
    if not course:
        return jsonify({'message':'Course not Found!!!!'}),404
    db.session.delete(course)
    db.session.commit()
    return jsonify({'message': 'Course has been deleted!'}),200