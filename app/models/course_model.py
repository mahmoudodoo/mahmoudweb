from app import db



class Course(db.Model):
    id = db.Column(db.Integer, primary_key=True,autoincrement=True)
    public_id= db.Column(db.String(50), unique=True)
    name = db.Column(db.String(64), index=True, unique=True)
    description = db.Column(db.String(64), index=True, unique=True)
    lessons = db.relationship("Lesson", backref='lesson', lazy='dynamic')

    def __repr__(self):
        return '<Lessons {}>'.format(self.name)