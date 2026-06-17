from flask_wtf import FlaskForm

from wtforms import StringField
from wtforms import PasswordField
from wtforms import SubmitField

from wtforms.validators import DataRequired, Email, EqualTo


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


class RegistrationForm(FlaskForm):

    name = StringField(
        "Nome",
        validators=[DataRequired()]
    )

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

    confirm_password = PasswordField(
        "Confirmar senha",
        validators=[
            DataRequired(),
            EqualTo("password", message="As senhas devem ser iguais")
        ]
    )

    submit = SubmitField("Criar conta")