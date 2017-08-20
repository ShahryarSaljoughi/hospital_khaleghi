from flask_wtf import Form
from wtforms import StringField, BooleanField, PasswordField
from wtforms.validators import DataRequired


class LoginForm(Form):

    username = StringField('user name', validators=[DataRequired()])
    password = PasswordField(
        'password',
        validators=[DataRequired(message="password must be enterd")]
    )
    remember_me = BooleanField('remember', default=False)


class SignupForm(Form):
    pass