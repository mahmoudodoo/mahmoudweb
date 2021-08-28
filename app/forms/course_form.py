
from flask_wtf import FlaskForm
from wtforms import StringField,SubmitField,TextAreaField
from wtforms.validators import  DataRequired
from flask_wtf.file import FileField, FileRequired ,FileAllowed



# Create Login Form Using wtforms module
class AddCourseForm(FlaskForm):
    course_name = StringField('Course Name:', validators=[DataRequired()])
    description = TextAreaField(u'Description', validators=[DataRequired()])
    submit = SubmitField('ADD')


class DeleteCourseForm(FlaskForm):
    course_id = StringField('Course ID', validators=[DataRequired()])
    submit = SubmitField('DELETE')