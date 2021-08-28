from flask import jsonify, request, abort,make_response
from app import db
from app import app
from app.models.lesson_model import Lesson
import uuid





@app.route('/lessons', methods=['GET'])
def get_all_lessons():
    lessons= Lesson.query.all()
    output = []
    if not lessons:
        return jsonify({'message':'No lessons!'})

    for lesson in lessons:
        lesson_data = {}
        lesson_data['public_id'] =lesson.public_id
        lesson_data['name']= lesson.name
        lesson_data['video_link'] = lesson.video_link
        lesson_data['course_id'] = lesson.course_id
        output.append(lesson_data)

    return jsonify({'lessons':output})

@app.route('/lessons/<public_id>',methods=['GET'])
def get_one_lesson(public_id):
    lesson = Lesson.query.filter_by(public_id=public_id).first()
    if not lesson:
        return jsonify({'message':'lesson not Found!!!!'})
    lesson_data = {}
    lesson_data['public_id'] =lesson.public_id
    lesson_data['name']= lesson.name
    lesson_data['video_link'] = lesson.video_link
    lesson_data['course_id'] = lesson.course_id
    return jsonify({'lesson':lesson_data})

@app.route('/lessons',methods=['POST'])
def create_lesson():
    data = request.get_json()
    new_lesson = Lesson(public_id=str(uuid.uuid4()), name=data['name'],video_link=data['video_link'],course_id=data['course_id'])
    db.session.add(new_lesson)
    db.session.commit()
    return jsonify({'message' :'New lesson has been created!'})


@app.route('/lessons/<public_id>',methods=['DELETE'])
def delete_lesson(public_id):
    lesson = Lesson.query.filter_by(public_id=public_id).first()
    if not lesson:
        return jsonify({'message':'lesson not Found!!!!'}),404
    db.session.delete(lesson)
    db.session.commit()
    return jsonify({'message': 'lesson has been deleted!'}),200