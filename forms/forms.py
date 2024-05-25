from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField
from wtforms.validators import DataRequired, Length, ValidationError, EqualTo
from database.models import User
from database.bcrypt import bcrypt

class NotEqualTo:
    def __init__(self, fieldname, message=None):
        self.fieldname = fieldname
        self.message = message

    def __call__(self, form, field):
        try:
            other = form[self.fieldname]
        except KeyError:
            raise ValidationError(field.gettext("Invalid field name '%s'.") % self.fieldname)

        if field.data == other.data:
            message = self.message
            if message is None:
                message = field.gettext('Field must be different from %s.' % self.fieldname)
            raise ValidationError(message)




class LoginForm(FlaskForm):

    username = StringField('Username', validators=[DataRequired(), Length(min=2, max=20)])
    password = PasswordField('Password', validators=[DataRequired(), Length(max=40)])


    def validate_username(self, username): 

        if not User.query.filter_by(username=username.data).first():
            raise ValidationError("This username doesn't exist.")
        

    def validate_password(self, password):

        user:User = User.query.filter_by(username=self.username.data).first()

        if not bcrypt.check_password_hash(user.password, password.data):
            return ValidationError("Incorrect password")



class RegisterForm(FlaskForm):

    username = StringField('Username', validators=[DataRequired(), Length(min=2, max=20)])
    password = PasswordField('Password', validators=[DataRequired(), Length(max=40)])
    confirm_password = PasswordField('Confirm Password', validators=[DataRequired(), Length(max=40), EqualTo('password', "The passwords don't match.")])


    def validate_username(self, username):

        if User.query.filter_by(username=username.data).first():
            raise ValidationError("This username already exists.")
        



class ChangePasswordForm(FlaskForm):

    previous_password = PasswordField('Password', validators=[DataRequired(), Length(max=40)])
    new_password = PasswordField('Confirm Password', validators=[DataRequired(), Length(max=40), NotEqualTo('previous_password', "The passwords can't be the same")])
