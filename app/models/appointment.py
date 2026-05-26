from app import db


class Appointment(db.Model):
    __tablename__ = 'appointments'

    id = db.Column(db.Integer, primary_key=True)
    patient_id = db.Column(db.Integer, nullable=False)
    appointment_date = db.Column(db.String(20), nullable=False)
    appointment_time = db.Column(db.String(10), nullable=False)
    appointment_type = db.Column(db.String(100))
    notes = db.Column(db.Text)

    def __repr__(self):
        return f'<Appointment {self.id}>'