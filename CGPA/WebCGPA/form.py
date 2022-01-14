from flask_wtf import FlaskForm
from wtforms import IntegerField, SubmitField
from wtforms.validators import DataRequired, Length, ValidationError

#this to create the form so that we can enter the marks for the subjects
class subjects(FlaskForm):
    subjectOne = IntegerField("Enter", validators=[DataRequired()])
    subjectTwo = IntegerField("Enter", validators=[DataRequired()])
    subjectThree = IntegerField("Enter", validators=[DataRequired()])
    subjectFour = IntegerField("Enter", validators=[DataRequired()])

    submit = SubmitField("CGPA SCORE")

#this is to continue to the home page and delete the data in the database table
class score(FlaskForm):
    btn = SubmitField("Continue")