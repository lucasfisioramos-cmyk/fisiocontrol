from app.models.patient import Patient


def get_all_patients():
    return Patient.query.all()