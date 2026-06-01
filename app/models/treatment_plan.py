from app import db

class TreatmentPlan(db.Model):

    __tablename__ = 'treatment_plans'

    id = db.Column(db.Integer, primary_key=True)

    patient_id = db.Column(
        db.Integer,
        db.ForeignKey('patients.id'),
        nullable=False
    )

    goals = db.Column(db.Text)

    strategies = db.Column(db.Text)

    guidance = db.Column(db.Text)

    frequency = db.Column(db.String(50))

    def __repr__(self):
        return f'<TreatmentPlan {self.patient_id}>'