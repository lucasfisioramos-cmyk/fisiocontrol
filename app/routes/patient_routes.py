from flask import Blueprint, render_template, request, redirect, url_for, flash
from flask_login import login_required

from app.services.patient_service import (
    create_patient,
    get_all_patients,
    get_patient_by_id,
    update_patient
)
from app.services.appointment_service import get_appointments_by_patient
from app.services.financial_service import get_records_by_patient


patient_bp = Blueprint(
    'patients',
    __name__,
    url_prefix='/patients'
)


# ── Lista ────────────────────────────────────────────────────────────────────

@patient_bp.route('/')
@login_required
def patient_list():
    patients = get_all_patients()
    
    return render_template('patients/patient_list.html', patients=patients)


# ── Cadastro ─────────────────────────────────────────────────────────────────

@patient_bp.route('/new', methods=['GET', 'POST'])   
@login_required
def patient_form():
    if request.method == 'POST':
        patient, error = create_patient(request.form)

        if error:
            flash(f'Erro ao cadastrar paciente: {error}', 'danger')
            return render_template('patients/patient_form.html')

        flash('Paciente cadastrado com sucesso!', 'success')
        return redirect(url_for('patients.patient_list'))

    return render_template('patients/patient_form.html')


# ── Perfil ────────────────────────────────────────────────────────────────────

@patient_bp.route('/<int:id>', methods=['GET'])
@login_required
def patient_profile(id):
    patient = get_patient_by_id(id)   
    return render_template('patients/patient_profile.html', patient=patient)


# ── Edição ────────────────────────────────────────────────────────────────────

@patient_bp.route('/<int:id>/edit', methods=['GET', 'POST'])
@login_required
def patient_edit(id):
    patient = get_patient_by_id(id)

    if request.method == 'POST':
        patient, error = update_patient(id, request.form)

        if error:
            flash(f'Erro ao atualizar paciente: {error}', 'danger')
            return render_template('patients/patient_form.html', patient=patient)

        flash('Paciente atualizado com sucesso!', 'success')
        return redirect(url_for('patients.patient_profile', id=id))

    return render_template('patients/patient_form.html', patient=patient)


# ── Anamnese ──────────────────────────────────────────────────────────────────

@patient_bp.route('/<int:id>/anamnesis', methods=['GET', 'POST'])
@login_required
def anamnesis_form(id):
    patient = get_patient_by_id(id)

    if request.method == 'POST':
        flash('Anamnese salva com sucesso!', 'success')
        return redirect(url_for('patients.patient_profile', id=id))

    return render_template(
        'patients/anamnesis_form.html',
        patient=patient,
        patient_id=id
    )


# ── Evoluções ─────────────────────────────────────────────────────────────────

@patient_bp.route('/<int:id>/evolutions')
@login_required
def evolution_list(id):
    patient = get_patient_by_id(id)
    return render_template(
        'patients/evolution_list.html',
        patient=patient,
        patient_id=id
    )


@patient_bp.route('/<int:id>/evolutions/new', methods=['GET', 'POST'])
@login_required
def evolution_form(id):
    patient = get_patient_by_id(id)

    if request.method == 'POST':
        flash('Evolução registrada com sucesso!', 'success')
        return redirect(url_for('patients.evolution_list', id=id))

    return render_template(
        'patients/evolution_form.html',
        patient=patient,
        patient_id=id
    )


# ── Plano de tratamento ───────────────────────────────────────────────────────

@patient_bp.route('/<int:id>/treatment-plan', methods=['GET', 'POST'])
@login_required
def treatment_plan(id):
    patient = get_patient_by_id(id)

    if request.method == 'POST':
        flash('Plano de tratamento salvo com sucesso!', 'success')
        return redirect(url_for('patients.patient_profile', id=id))

    return render_template(
        'patients/treatment_plan.html',
        patient=patient,
        patient_id=id
    )


# ── Documentos ────────────────────────────────────────────────────────────────

@patient_bp.route('/<int:id>/documents')
@login_required
def documents(id):
    patient = get_patient_by_id(id)
    return render_template(
        'patients/documents.html',
        patient=patient,
        patient_id=id
    )


# ── Consultas do paciente ─────────────────────────────────────────────────────

@patient_bp.route('/<int:id>/appointments')
@login_required
def appointments(id):
    patient = get_patient_by_id(id)
    appointments = get_appointments_by_patient(id)
    return render_template(
        'patients/appointments.html',
        patient=patient,
        appointments=appointments,
        patient_id=id
    )
