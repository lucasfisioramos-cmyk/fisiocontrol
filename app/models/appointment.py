from datetime import datetime, UTC

from app.extensions import db


class Appointment(db.Model):

    __tablename__ = 'appointments'

    id = db.Column(db.Integer, primary_key=True)

    patient_id = db.Column(
        db.Integer,
        db.ForeignKey('patients.id'),
        nullable=False
    )

    appointment_date = db.Column(
        db.DateTime,
        nullable=False
    )

    status = db.Column(
        db.String(30),
        nullable=False,
        default='scheduled'
    )

    notes = db.Column(
        db.Text
    )

    created_at = db.Column(
        db.DateTime,
        default=lambda: datetime.now(UTC)
    )
    def __repr__(self):
        return (
            f'<Appointment '
            f'{self.patient_id} '
            f'{self.appointment_date}>'
        )