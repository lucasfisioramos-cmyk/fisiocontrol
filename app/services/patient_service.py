from app.models.patient import Patient
from app.extensions import db

def get_all_patients():
    return Patient.query.all()

def get_patient_by_id(patient_id):
    return Patient.query.get_or_404(patient_id)

def create_patient(data):

    patient = Patient(
        full_name=data.get("full_name"),
        phone=data.get("phone"),
        cpf=data.get("cpf"),
        birth=data.get("birth_date"),
        gender=data.get("gender"),
        notes=data.get("notes")
    )

    db.session.add(patient)
    db.session.commit()

    return patient