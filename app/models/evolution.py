from datetime import datetime, UTC
from app.extensions import db


class Evolution(db.Model):

    __tablename__ = 'evolutions'
    id = db.Column(db.Integer, primary_key=True)
    patient_id = db.Column(
        db.Integer,
        db.ForeignKey('patients.id'),
        nullable=False
    )
    description = db.Column(
        db.Text,
        nullable=False
    )
    created_at = db.Column(
        db.DateTime,
        default=lambda: datetime.now(UTC)
    )
    def __repr__(self):
        return f'<Evolution {self.id}>'