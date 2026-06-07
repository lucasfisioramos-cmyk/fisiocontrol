from flask import render_template
from flask import redirect
from flask import url_for
from flask import flash

from flask_login import login_user
from flask_login import logout_user

from app.auth.forms import LoginForm
from app.auth.services import authenticate_user
from app.auth import auth_bp


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

@auth_bp.route("/logout")
def logout():

    logout_user()

    return redirect(
        url_for("auth.login")
    )