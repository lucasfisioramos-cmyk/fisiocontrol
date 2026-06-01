from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

from config import Config


db = SQLAlchemy()
migrate = Migrate()


def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    db.init_app(app)
    migrate.init_app(app, db)


    from app.routes.dashboard_routes import dashboard_bp
    from app.routes.patient_routes import patient_bp
    from app.routes.appointment_routes import appointment_bp
    from app.routes.financial_routes import financial_bp

    app.register_blueprint(dashboard_bp)
    app.register_blueprint(patient_bp)
    app.register_blueprint(appointment_bp)
    app.register_blueprint(financial_bp)

    from app import models

    return app