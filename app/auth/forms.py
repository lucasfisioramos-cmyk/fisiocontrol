from flask_wtf import FlaskForm

from wtforms import StringField
from wtforms import PasswordField
from wtforms import SubmitField

from wtforms.validators import DataRequired, Email


class LoginForm(FlaskForm):

    email = StringField(
        "Email",
        validators=[
            DataRequired(),
            Email()
        ]
    )

    password = PasswordField(
        "Senha",
        validators=[DataRequired()]
    )

    submit = SubmitField("Entrar")