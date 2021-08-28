from app import db
from app import app
from app.models.course_model import Course
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField,TextAreaField,IntegerField,SelectField
from wtforms.validators import ValidationError, DataRequired ,Regexp ,URL
from wtforms_sqlalchemy.fields  import QuerySelectField
from flask_wtf.file import FileField, FileRequired ,FileAllowed

def choices_query():
    return Course.query



class AddLessonForm(FlaskForm):
    lesson_name = StringField('lesson Name:', validators=[DataRequired()])
    course = QuerySelectField(query_factory=choices_query, allow_blank=True,get_label='name')
    video_link = StringField('Video Link:', validators=[DataRequired(),Regexp('https://www.youtube.com/.*', message="Just Youtube")])
    submit = SubmitField('ADD')


 

class DeleteLessonForm(FlaskForm):
    lesson_id = StringField('lesson ID', validators=[DataRequired()])
    submit = SubmitField('DELETE')