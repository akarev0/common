from flask_wtf import FlaskForm
from flask_wtf.file import FileRequired
from wtforms import StringField, SubmitField, FileField
from wtforms.validators import DataRequired


class AddNewProduct(FlaskForm):
    new_product_name = StringField(validators=[DataRequired()])
    new_product_description = StringField(validators=[DataRequired()])
    new_product_image = FileField(validators=[FileRequired()])
    new_product_price = StringField(validators=[DataRequired()])
    submit = SubmitField('Send')
