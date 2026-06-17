from flask import render_template
from flask import redirect
from flask import url_for
from flask import flash

from flask_login import login_user
from flask_login import logout_user

from app.auth.forms import LoginForm, RegistrationForm
from app.auth.services import authenticate_user
from app.auth import auth_bp
from app.extensions import db
from app.models.user import User


@auth_bp.route("/login", methods=["GET", "POST"])
def login():

    form = LoginForm()

    if form.validate_on_submit():

        user = authenticate_user(
            form.email.data,
            form.password.data
        )

        if user:

            login_user(user)

            return redirect(
                url_for("dashboard.dashboard")
            )

        flash("Credenciais inválidas")

    return render_template(
        "login.html",
        form=form
    )


@auth_bp.route("/register", methods=["GET", "POST"])
def register():

    form = RegistrationForm()

    if form.validate_on_submit():

        if User.query.filter_by(email=form.email.data).first():
            flash("Este email já está cadastrado.")
        else:
            user = User(
                name=form.name.data,
                email=form.email.data
            )
            user.set_password(form.password.data)
            db.session.add(user)
            db.session.commit()

            flash("Cadastro realizado com sucesso. Faça login para continuar.")
            return redirect(url_for("auth.login"))

    return render_template(
        "register.html",
        form=form
    )


@auth_bp.route("/logout")
def logout():

    logout_user()

    return redirect(
        url_for("auth.login")
    )