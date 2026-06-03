from flask import Blueprint, render_template, request, redirect, url_for
from flask_login import login_required
from app.services.patient_service import (
    create_patient,
    get_all_patients
                                          )

patient_bp = Blueprint(
    'patients',
    __name__,
    url_prefix='/patients'
)

@patient_bp.route('/')
@login_required
def patient_list():
    patients = get_all_patients()
    return render_template('patients/patient_list.html')

@patient_bp.route('/new')
@login_required
def patient_form():
    if request.method == 'POST':    

        create_patient(request.form)

        return redirect(
            url_for('patients.patient_list')
        )

    return render_template(
        'patients/patient_form.html'
    )

@patient_bp.route('/<int:id>')
@login_required
def patient_profile(id):

    # futuramente:
    # patient = Patient.query.get_or_404(id)

    return render_template('patients/patient_profile.html',
        patient_id=id)

@patient_bp.route('/<int:id>/anamnesis')
@login_required
def anamnesis_form(id):
    return render_template('patients/anamnesis_form.html',
        patient_id=id)

@patient_bp.route('/<int:id>/evolutions')
@login_required
def evolution_list(id):
    return render_template('patients/evolution_list.html',
        patient_id=id)

@patient_bp.route('/<int:id>/evolutions/new')
@login_required
def evolution_form(id):
    return render_template('patients/evolution_form.html',
        patient_id=id)

@patient_bp.route('/<int:id>/treatment-plan')
@login_required
def treatment_plan(id):
    return render_template('patients/treatment_plan.html',
        patient_id=id)

@patient_bp.route('/<int:id>/documents')
@login_required
def documents(id):
    return render_template('patients/documents.html',
        patient_id=id)

@patient_bp.route('/<int:id>/appointments')
@login_required
def appointments(id):
    return render_template('patients/appointments.html',
        patient_id=id)