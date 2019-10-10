from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField, TextAreaField
from wtforms.validators import DataRequired, Length, Email, EqualTo #this checks that the username is not left blank, between 2-10 characters, and is valid
class RegistrationForm(FlaskForm):
    #validators: arguments/parameters (no blank usernames and 2-10 characters)
    username = StringField('Username',
                            validators=[DataRequired(),
                            Length(min=2, max=15)])
    email = StringField('Email',
                        validators=[DataRequired(),
                        Email()
                        ])

    password = PasswordField('Password',
                validators=[DataRequired()])
    confirm_password = PasswordField('Confirm Password',
                            validators=[DataRequired(),
                            EqualTo('password')]) #This checks that passwords match
    submit = SubmitField('Submit')

class LoginForm(FlaskForm):
    #validators: arguments/parameters (no blank usernames and 2-10 characters)
    username = StringField('Username',
                            validators=[DataRequired(),
                            Length(min=2, max=15)])
    password = PasswordField('Password',
                validators=[DataRequired()])
    #boolean field(true or false)
    remember = BooleanField('Remember Me')
    submit = SubmitField('Login')

class PostForm(FlaskForm):
    title = StringField('Title', validators=[DataRequired()])
    content = TextAreaField('Content', validators=[DataRequired()])
    submit = SubmitField('Post')
