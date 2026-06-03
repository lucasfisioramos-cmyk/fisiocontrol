from app.extensions import db


class Anamnesis(db.Model):

    __tablename__ = 'anamneses'

    id = db.Column(db.Integer, primary_key=True)

    patient_id = db.Column(
        db.Integer,
        db.ForeignKey('patients.id'),
        nullable=False
    )

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

    def __repr__(self):
        return f'<Anamnesis {self.patient_id}>'