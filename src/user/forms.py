# src/user/forms.py

# imports
from flask_wtf import FlaskForm
from wtforms import StringField,PasswordField,SubmitField,TextAreaField
from wtforms.fields.html5 import EmailField,IntegerField
from wtforms.validators import DataRequired,Email,EqualTo,ValidationError
from src.user.models import UserModel

# ***********************************************************USER LOGIN FORM***********************************************************
class LoginForm(FlaskForm):
    '''login form for user'''

    email=EmailField('email',validators=[DataRequired()])
    password=PasswordField('password',validators=[DataRequired()])
    submit=SubmitField('login')

# ***********************************************************USER SIGNUP FORM***********************************************************
class SignupForm(FlaskForm):
    '''signup form for user'''

    email=EmailField('email',validators=[DataRequired()])
    password=PasswordField('password',validators=[DataRequired()])
    cpassword=PasswordField('confirm password',validators=[DataRequired(),EqualTo('password')])
    mobile=IntegerField('mobile no',validators=[DataRequired()])
    submit=SubmitField('signup')


# ***********************************************************UPDATE USER FORM***********************************************************
class UpdateUserForm(FlaskForm):
    '''user update form'''

    email=EmailField('email',validators=[DataRequired()])
    mobile=IntegerField('mobile no',validators=[DataRequired()])
    baddress=TextAreaField('billing address')
    daddress=TextAreaField('delivery address')
    submit=SubmitField('update')

# ***********************************************************UPDATE PASSWORD FORM***********************************************************
class UpdatePasswordForm(FlaskForm):
    '''password update form'''
    
    opassword=PasswordField('old password',validators=[DataRequired()])
    password=PasswordField('new password',validators=[DataRequired()])
    cpassword=PasswordField('confirm new password',validators=[DataRequired(),EqualTo('password')])
    submit=SubmitField('update password')
