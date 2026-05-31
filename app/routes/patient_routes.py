from flask import Blueprint, render_template

patient_bp = Blueprint(
    'patients',
    __name__,
    url_prefix='/patients'
)

@patient_bp.route('/')
def patient_list():
    return render_template('patients/patient_list.html')

@patient_bp.route('/new')
def patient_form():
    return render_template('patients/patient_form.html')

@patient_bp.route('/<int:id>')
def patient_profile(id):

    # futuramente:
    # patient = Patient.query.get_or_404(id)

    return render_template('patients/patient_profile.html',
        patient_id=id)

@patient_bp.route('/<int:id>/anamnesis')
def anamnesis_form(id):
    return render_template('patients/anamnesis_form.html',
        patient_id=id)

@patient_bp.route('/<int:id>/evolutions')
def evolution_list(id):
    return render_template('patients/evolution_list.html',
        patient_id=id)

@patient_bp.route('/<int:id>/evolutions/new')
def evolution_form(id):
    return render_template('patients/evolution_form.html',
        patient_id=id)

@patient_bp.route('/<int:id>/treatment-plan')
def treatment_plan(id):
    return render_template('patients/treatment_plan.html',
        patient_id=id)

@patient_bp.route('/<int:id>/documents')
def documents(id):
    return render_template('patients/documents.html',
        patient_id=id)

@patient_bp.route('/<int:id>/appointments')
def appointments(id):
    return render_template('patients/appointments.html',
        patient_id=id)