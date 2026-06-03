from flask import Flask

from config import Config

from app.extensions import (
    db,
    migrate,
    login_manager
)

from app.commands.command_user import create_admin


def create_app():

    app = Flask(__name__)
    app.config.from_object(Config)

    db.init_app(app)
    migrate.init_app(app, db)
    login_manager.init_app(app)

    login_manager.login_view = "auth.login"
    login_manager.login_message = (
        "Faça login para continuar."
    )

    from app.models.user import User

    @login_manager.user_loader
    def load_user(user_id):
        return db.session.get(
            User,
            int(user_id)
        )

    from app import models

    from app.auth import auth_bp

    from app.routes.dashboard_routes import dashboard_bp
    from app.routes.patient_routes import patient_bp
    from app.routes.appointment_routes import appointment_bp
    from app.routes.financial_routes import financial_bp

    app.register_blueprint(auth_bp)
    app.register_blueprint(dashboard_bp)
    app.register_blueprint(patient_bp)
    app.register_blueprint(appointment_bp)
    app.register_blueprint(financial_bp)

    app.cli.add_command(create_admin)

    return app