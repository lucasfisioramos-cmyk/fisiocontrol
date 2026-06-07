from datetime import datetime

from app.extensions import db
from app.models.appointment import Appointment


def get_all_appointments():
    return Appointment.query.order_by(Appointment.appointment_date.desc()).all()


def get_appointment_by_id(appointment_id):
    return db.get_or_404(Appointment, appointment_id)


def get_appointments_by_patient(patient_id):
    return (
        Appointment.query
        .filter_by(patient_id=patient_id)
        .order_by(Appointment.appointment_date.desc())
        .all()
    )


def create_appointment(data):
    """Retorna (Appointment, None) ou (None, str_erro)."""
    try:

        appointment = Appointment(

            patient_id=data.get(
                'patient_id'
            ),

            appointment_date=(
                datetime.fromisoformat(
                    data.get(
                        'appointment_date'
                    )
                )
            ),

            status=data.get(
                'status'
            ),

            notes=data.get(
                'notes'
            )
        )

        db.session.add(
            appointment
        )

        db.session.commit()

        return appointment, None

    except Exception as e:

        db.session.rollback()

        return None, str(e)


def update_appointment(appointment_id, data):
    """Retorna (Appointment, None) ou (None, str_erro)."""
    try:
        appointment = db.get_or_404(Appointment, appointment_id)
        appointment.patient_id       = int(data.get('patient_id', appointment.patient_id))
        appointment.appointment_date = datetime.fromisoformat(data.get('appointment_date'))
        appointment.status           = data.get('status', appointment.status)
        appointment.notes            = data.get('notes', appointment.notes) or None
        db.session.commit()
        return appointment, None
    except Exception as e:
        db.session.rollback()
        return None, str(e)
