from flask_wtf import FlaskForm
from flask_wtf.file import FileRequired
from wtforms import StringField, SubmitField, FileField
from wtforms.validators import DataRequired


class AddNewSupermarket(FlaskForm):
    new_supermarket_name = StringField('Enter the supermarket name:', validators=[DataRequired()])
    new_supermarket_location = StringField('Where is new supermarket situated(city)?', validators=[DataRequired()])
    new_supermarket_image = FileField('Choose the logo', validators=[FileRequired()])
    submit = SubmitField('Click here to add')
