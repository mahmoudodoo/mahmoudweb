from app import db



class Lesson(db.Model):
    id = db.Column(db.Integer, primary_key=True,autoincrement=True)
    public_id= db.Column(db.String(50), unique=True)
    name = db.Column(db.String(64), index=True, unique=True)
    course_id = db.Column(db.String(50), db.ForeignKey('course.public_id'))
    video_link = db.Column(db.String(300))


    def __repr__(self):
        return '<Courses {}>'.format(self.name)