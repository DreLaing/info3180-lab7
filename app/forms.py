from flask_wtf import FlaskForm
from wtforms import TextAreaField
from flask_wtf.file import FileField, FileAllowed, FileRequired

class myForm(FlaskForm):
    description = TextAreaField('Description')
    photo = FileField('Photo', validators=[FileAllowed(['jpg', 'png']), FileRequired('Please provide a picture')])
