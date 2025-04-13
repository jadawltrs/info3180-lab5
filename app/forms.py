'''
Create a form class called MovieForm that has three (3) fields 
and appropriate validation rules. A String field called 'title' for the Movie Title, 
TextArea field called 'description' that requires a user to fill in a brief description 
or summary of the movie and a FileField called 'poster' that only allows images of 
a movie poster to be uploaded.
'''

# Add any form classes for Flask-WTF here

from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileRequired, FileAllowed  # Correct import for FileAllowed
from wtforms import StringField, TextAreaField, SubmitField
from wtforms.validators import DataRequired, Length

# Add any form classes for Flask-WTF here
class MovieForm(FlaskForm):
    title = StringField('Movie Title', validators=[DataRequired(), Length(max=100)])
    description = TextAreaField('Description', validators=[DataRequired()])
    poster = FileField('Poster Image', validators=[FileRequired(), FileAllowed(['jpg', 'png', 'jpeg'], 'Images only!')])
    submit = SubmitField('Submit')