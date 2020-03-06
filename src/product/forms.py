# src/product/forms.py

# imports
from flask_wtf import FlaskForm
from wtforms import StringField,PasswordField,SubmitField,TextAreaField
from wtforms.fields.html5 import EmailField,IntegerField
from flask_wtf.file import FileField,FileAllowed
from wtforms.validators import DataRequired,Email,EqualTo,ValidationError


# ***********************************************************ADD PRODCUT FORM***********************************************************
class AddProductForm(FlaskForm):
    '''add product form'''

    name=StringField('product name',validators=[DataRequired()])
    price=IntegerField('price',validators=[DataRequired()])
    description=TextAreaField('description',validators=[DataRequired()])
    submit=SubmitField('add product')
    
# ***********************************************************ADD PRODUCT IMAGE FORM***********************************************************
class AddProductImageForm(FlaskForm):
    '''add product image form'''

    image=FileField('product image',validators=[DataRequired(),FileAllowed(['jpg'])])
    submit=SubmitField('add image')

# ***********************************************************UPDATE PRODUCT FORM***********************************************************
class UpdateProductForm(FlaskForm):
    '''Update product form'''

    name=StringField('product name',validators=[DataRequired()])
    price=IntegerField('price',validators=[DataRequired()])
    description=TextAreaField('description',validators=[DataRequired()])
    submit=SubmitField('update product')
