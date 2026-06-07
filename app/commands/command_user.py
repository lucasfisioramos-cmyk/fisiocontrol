from flask.cli import with_appcontext
import click

from app.extensions import db
from app.models.user import User


@click.command("create-admin")
@click.option("--name", prompt=True)
@click.option("--email", prompt=True)
@click.option(
    "--password",
    prompt=True,
    hide_input=True,
    confirmation_prompt=True
)
@with_appcontext
def create_admin(name, email, password):

    existing = User.query.filter_by(
        email=email
    ).first()

    if existing:
        click.echo("Usuário já existe.")
        return

    user = User(
        name=name,
        email=email
    )

    user.set_password(password)

    db.session.add(user)
    db.session.commit()

    click.echo("Administrador criado com sucesso.")