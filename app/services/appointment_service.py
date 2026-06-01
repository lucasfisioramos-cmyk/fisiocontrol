from app.models.appointment import Appointment
from app import db

def get_all_appointments():
    return Appointment.query.all()

def get_appointment_by_id(id):
    return Appointment.query.get_or_404(id)

def create_appointment(data):

    appointment = Appointment(
        patient_id=data.get('patient_id'),
        appointment_date=data.get('appointment_date'),
        status=data.get('status'),
        notes=data.get('notes')
    )

    db.session.add(appointment)
    db.session.commit()

    return appointment