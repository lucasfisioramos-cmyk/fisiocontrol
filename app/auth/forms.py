from flask_wtf import FlaskForm

from wtforms import StringField
from wtforms import PasswordField
from wtforms import SubmitField

from wtforms.validators import DataRequired, Email, EqualTo, Length


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

class RegisterForm(FlaskForm):

    name = StringField(
        "Nome completo",
        validators=[DataRequired(), Length(min=3, max=80)]
    )

    email = StringField(
        "Email",
        validators=[DataRequired(), Email()]
    )

    password = PasswordField(
        "Senha",
        validators=[DataRequired(), Length(min=6)]
    )

    confirm_password = PasswordField(
        "Confirmar senha",
        validators=[
            DataRequired(),
            EqualTo("password", message="As senhas não coincidem.")
        ]
    )

    submit = SubmitField("Criar conta")