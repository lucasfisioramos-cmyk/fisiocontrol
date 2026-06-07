from app.extensions import db
from app.models.patient import Patient
from datetime import date
from sqlalchemy.exc import IntegrityError


def get_all_patients():
    return Patient.query.filter_by(is_active=True).order_by(Patient.full_name).all()


def get_patient_by_id(patient_id):
    return db.get_or_404(Patient, patient_id)


def create_patient(data):
    """Retorna (Patient, None) em caso de sucesso ou (None, str_erro) em falha."""
    try:

        cpf = data.get('cpf')

        if cpf:

            existing = Patient.query.filter_by(
                cpf=cpf
            ).first()

            if existing:
                return None, (
                    'CPF já cadastrado.'
                )
    
        patient = Patient(
            full_name=data.get('full_name'),
            phone=data.get('phone'),
            cpf=data.get('cpf') or None,
            birth_date=(date.fromisoformat(data.get('birth_date'))
                if data.get('birth_date')
                else None
            ),
            gender=data.get('gender'),
            notes=data.get('notes'),
        )
        db.session.add(patient)
        db.session.commit()
        return patient, None
    except Exception as e:
        db.session.rollback()
        return None, str(e)


def update_patient(patient_id, data):
    """Retorna (Patient, None) em caso de sucesso ou (None, str_erro) em falha."""
    try:
        patient = db.get_or_404(Patient, patient_id)
        patient.full_name  = data.get('full_name', patient.full_name)
        patient.phone      = data.get('phone', patient.phone)
        patient.cpf        = data.get('cpf', patient.cpf) or None
        if data.get('birth_date'):

            patient.birth_date = (
                date.fromisoformat(
                    data.get('birth_date')
                )
            )
        patient.gender     = data.get('gender', patient.gender)
        patient.notes      = data.get('notes', patient.notes)
        db.session.commit()
        return patient, None
    except Exception as e:
        db.session.rollback()
        return None, str(e)


def deactivate_patient(patient_id):
    """Soft-delete: marca is_active=False."""
    try:
        patient = db.get_or_404(Patient, patient_id)
        patient.is_active = False
        db.session.commit()
        return True, None
    except Exception as e:
        db.session.rollback()
        return False, str(e)
