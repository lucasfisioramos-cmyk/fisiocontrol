from app.models.appointment import Appointment
from app.extensions import db
from datetime import datetime

def get_all_appointments():
    return Appointment.query.all()

def get_appointment_by_id(id):
    return Appointment.query.get_or_404(id)

def create_appointment(data):

    # Parse datetime-local input (YYYY-MM-DDTHH:MM)
    raw_dt = data.get('appointment_date')
    appointment_dt = None
    if raw_dt:
        try:
            # handle possible seconds
            appointment_dt = datetime.fromisoformat(raw_dt)
        except Exception:
            try:
                appointment_dt = datetime.strptime(raw_dt, '%Y-%m-%dT%H:%M')
            except Exception:
                appointment_dt = None

    appointment = Appointment(
        patient_id=int(data.get('patient_id')) if data.get('patient_id') else None,
        appointment_date=appointment_dt,
        status=data.get('status') or 'scheduled',
        notes=data.get('notes')
    )

    db.session.add(appointment)
    db.session.commit()

    return appointment