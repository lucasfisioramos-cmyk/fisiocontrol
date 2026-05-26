from app.models.appointment import Appointment


def get_all_appointments():
    return Appointment.query.all()