from app.extensions import db
from datetime import datetime


class Anamnesis(db.Model):

    __tablename__ = 'anamneses'

    id = db.Column(
        db.Integer,
        primary_key=True
    )

    patient_id = db.Column(
        db.Integer,
        db.ForeignKey('patients.id'),
        nullable=False,
        index=True
    )

    # Identificação do episódio de tratamento
    title = db.Column(
        db.String(150),
        nullable=False
    )

    status = db.Column(
        db.String(20),
        default='Ativo'
    )

    # Dados clínicos
    chief_complaint = db.Column(db.Text)

    current_history = db.Column(db.Text)

    pain_intensity = db.Column(db.Integer)

    aggravating_factors = db.Column(db.Text)

    relieving_factors = db.Column(db.Text)

    comorbidities = db.Column(db.Text)

    medications = db.Column(db.Text)

    surgeries = db.Column(db.Text)

    physical_activity = db.Column(db.Text)

    occupation = db.Column(db.String(150))

    sleep_hours = db.Column(db.Integer)

    patient_goals = db.Column(db.Text)

    # Auditoria
    created_at = db.Column(
        db.DateTime,
        default=datetime.utcnow
    )

    updated_at = db.Column(
        db.DateTime,
        default=datetime.utcnow,
        onupdate=datetime.utcnow
    )

    def __repr__(self):
        return (
            f'<Anamnesis '
            f'{self.id} - '
            f'{self.title}>'
        )