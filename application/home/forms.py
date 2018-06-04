from flask_wtf import FlaskForm
from wtforms.fields import StringField, SubmitField, PasswordField, TextAreaField
from wtforms.validators import DataRequired, EqualTo, ValidationError
from application.models import User


class RegistForm(FlaskForm):
    name = StringField(
        label="Username",
        validators=[
            DataRequired("Username cannot be empty")
        ],
        description="Username",
        render_kw={
            "class": "form-control input lg",
            "placeholder": "please enter a username"
        }
    )
    pwd = PasswordField(
        label="Password",
        validators=[
            DataRequired("Password cannot be empty")
        ],
        description="Password",
        render_kw={
            "class": "form-control input lg",
            "placeholder": "please enter your password"
        }
    )
    repwd = PasswordField(
        label="Password confirmation",
        validators=[
            DataRequired("Password cannot be empty"),
            EqualTo('pwd', message="Passwords are not same")
        ],
        description="Password confirmation",
        render_kw={
            "class": "form-control input lg",
            "placeholder": "please enter your password again"
        }
    )
    submit = SubmitField(
        'Register',
        render_kw={
            "class": "btn btn-lg btn success btn-block"
        }
    )

    def validate_name(self, field):
        name = field.data
        user = User.query.filter_by(name=name).count()
        if user == 1:
            raise ValidationError("Username is already existed")


class LoginForm(FlaskForm):
    name = StringField(
        label="Username",
        validators=[
            DataRequired("Please enter your username")
        ],
        description="Username",
        render_kw={
            "class": "form-control input-lg",
            "placeholder": "Username",
        }
    )
    pwd = PasswordField(
        label="Password",
        validators=[
            DataRequired("Please enter your password")
        ],
        description="Password",
        render_kw={
            "class": "form-control input-lg",
            "placeholder": "Password",
        }
    )
    submit = SubmitField(
        'Login',
        render_kw={
            "class": "btn btn-lg btn-primary btn-block",
        }
    )