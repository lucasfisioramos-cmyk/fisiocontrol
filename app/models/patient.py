from app import db

from datetime import datetime, UTC

class Patient(db.Model):

    __tablename__ = 'patients'

    id = db.Column(db.Integer, primary_key=True)

    full_name = db.Column(
        db.String(150),
        nullable=False
    )
    phone = db.Column(
        db.String(20)
    )
    cpf = db.Column(
        db.String(14),
        unique=True
    )
    birth_date = db.Column(
        db.Date
    )
    gender = db.Column(
        db.String(20)
    )
    notes = db.Column(
        db.Text
    )
    is_active = db.Column(
        db.Boolean,
        default=True
    )
    created_at = db.Column(
        db.DateTime,
        default=lambda: datetime.now(UTC)
    )
    # RELACIONAMENTOS

    anamnesis = db.relationship(
        'Anamnesis',
        uselist=False,
        backref='patient'
    )

    evolutions = db.relationship(
        'Evolution',
        backref='patient',
        lazy=True
    )

    documents = db.relationship(
        'Document',
        backref='patient',
        lazy=True
    )

    appointments = db.relationship(
        'Appointment',
        backref='patient',
        lazy=True
    )

    treatment_plan = db.relationship(
        'TreatmentPlan',
        uselist=False,
        backref='patient'
    )
    def __repr__(self):
        return f'<Patient {self.full_name}>'