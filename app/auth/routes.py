from flask import render_template, redirect, url_for, flash
from flask_login import login_user, logout_user, login_required

from app.auth.forms import LoginForm, RegisterForm
from app.auth.services import authenticate_user, register_user
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

@auth_bp.route("/register", methods=["GET", "POST"])
def register():
    form = RegisterForm()

    if form.validate_on_submit():
        user, error = register_user(
            name=form.name.data,
            email=form.email.data,
            password=form.password.data,
        )

        if error:
            flash(error, "danger")
            return render_template("register.html", form=form)

        flash("Conta criada com sucesso! Faça login para continuar.", "success")
        return redirect(url_for("auth.login"))

    return render_template("register.html", form=form)