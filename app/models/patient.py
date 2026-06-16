from app.extensions import db

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

    anamneses = db.relationship(
        'Anamnesis',
        backref='patient',
        lazy=True,
        order_by='desc(Anamnesis.created_at)'
    )

    evolutions = db.relationship(
        'Evolution',
        backref='patient',
        lazy=True,
        cascade='all, delete-orphan'
    )

    documents = db.relationship(
        'Document',
        backref='patient',
        lazy=True,
        cascade='all, delete-orphan'
    )

    appointments = db.relationship(
        'Appointment',
        backref='patient',
        lazy=True,
        cascade='all, delete-orphan'
    )

    treatment_plan = db.relationship(
        'TreatmentPlan',
        uselist=False,
        backref='patient',
        cascade='all, delete-orphan'
    )

    financial_records = db.relationship(
    'Financial',
    backref='patient',
    lazy=True,
    cascade='all, delete-orphan'
    )
    
    def __repr__(self):
        return f'<Patient {self.full_name}>'