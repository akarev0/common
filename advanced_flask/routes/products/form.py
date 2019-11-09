from flask_wtf import FlaskForm
from flask_wtf.file import FileRequired
from wtforms import StringField, SubmitField, FileField
from wtforms.validators import DataRequired


class AddNewProduct(FlaskForm):
    new_product_name = StringField('Enter the name of the product:', validators=[DataRequired()])
    new_product_description = StringField('And two words about is', validators=[DataRequired()])
    new_product_image = FileField('Choose the image', validators=[FileRequired()])
    new_product_price = StringField('At least, price ', validators=[DataRequired()])
    submit = SubmitField('Send')
