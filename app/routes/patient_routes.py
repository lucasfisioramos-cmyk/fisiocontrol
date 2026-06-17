from flask import Blueprint, render_template, request, redirect, url_for, flash
from flask_login import login_required
from app.services.patient_service import (
    create_patient,
    get_all_patients,
    get_patient_by_id
)
from app.extensions import db
from app.models.anamnesis import Anamnesis
from app.models.evolution import Evolution

patient_bp = Blueprint(
    'patients',
    __name__,
    url_prefix='/patients'
)

@patient_bp.route('/')
@login_required
def patient_list():
    patients = get_all_patients()
    return render_template('patients/patient_list.html', patients=patients)

@patient_bp.route('/new', methods=['GET', 'POST'])
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
    patient = get_patient_by_id(id)
    return render_template('patients/patient_profile.html', patient=patient, patient_id=id)

@patient_bp.route('/<int:id>/anamnesis', methods=['GET', 'POST'])
@login_required
def anamnesis_form(id):
    if request.method == 'POST':
        # Map form fields to model
        data = request.form
        anam = Anamnesis(
            patient_id=id,
            chief_complaint=data.get('chief_complaint'),
            current_history=data.get('current_history'),
            pain_intensity=data.get('pain_intensity') or None,
            aggravating_factors=data.get('aggravating_factors'),
            relieving_factors=data.get('relieving_factors'),
            comorbidities=data.get('comorbidities'),
            medications=data.get('medications'),
            surgeries=data.get('surgeries'),
            physical_activity=data.get('physical_activity'),
            occupation=data.get('occupation'),
            sleep_hours=data.get('sleep_hours') or None,
            patient_goals=data.get('patient_goals')
        )

        db.session.add(anam)
        db.session.commit()

        flash('Anamnese salva com sucesso.')
        return redirect(url_for('patients.patient_profile', id=id))

    return render_template('patients/anamnesis_form.html', patient_id=id)

@patient_bp.route('/<int:id>/evolutions')
@login_required
def evolution_list(id):
    return render_template('patients/evolution_list.html',
        patient_id=id)

@patient_bp.route('/<int:id>/evolutions/new', methods=['GET', 'POST'])
@login_required
def evolution_form(id):
    if request.method == 'POST':
        description = request.form.get('description')
        if description:
            evo = Evolution(patient_id=id, description=description)
            db.session.add(evo)
            db.session.commit()
            flash('Evolução salva com sucesso.')
            return redirect(url_for('patients.evolution_list', id=id))

    return render_template('patients/evolution_form.html', patient_id=id)

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