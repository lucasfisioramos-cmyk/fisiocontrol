from app.extensions import db

class Tenant(db.Model):

    __tablename__ = "tenants"

    id = db.Column(
        db.Integer,
        primary_key=True
    )

    name = db.Column(
        db.String(150),
        nullable=False
    )

    database_name = db.Column(
        db.String(255),
        unique=True
    )