from wtforms import Form, StringField, PasswordField
from wtforms.validators import DataRequired, Length, EqualTo, ValidationError
from database.models import User
from database.bcrypt import bcrypt

class LoginForm(Form):

    username = StringField('Username', validators=[DataRequired(), Length(min=2, max=20)])
    password = PasswordField('Password', validators=[DataRequired(), Length(max=40)])

    def validateUser(self, username): 

        if not User.query.filter_by(username=username.data).first():
            raise ValidationError("This username doesn't exist.")
        
    def validatePassword(self, username, password):

        user:User = User.query.filter_by(username=username.data).first()

        if not bcrypt.check_password_hash(user.password, password.data):
            return ValidationError("Incorrect password")

        



class RegisterForm(Form):

    username = StringField('Username', validators=[DataRequired(), Length(min=2, max=20)])
    password = PasswordField('Password', validators=[DataRequired(), Length(max=40)])
    confirm_password = PasswordField('Confirm Password', validators=[DataRequired(), Length(max=40), EqualTo('password', "The passwords don't match.")])

    def validateUsername(self, username):

        if User.query.filter_by(username=username.data).first():
            raise ValidationError("This username already exists.")
        
