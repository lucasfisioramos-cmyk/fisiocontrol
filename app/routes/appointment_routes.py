from datetime import datetime

from flask import Blueprint, render_template, request, redirect, url_for, flash
from flask_login import login_required

from app.services.patient_service import get_all_patients
from app.services.appointment_service import (
    get_all_appointments,
    get_appointment_by_id,
    create_appointment,
    update_appointment,
)


appointment_bp = Blueprint(
    'appointments',
    __name__,
    url_prefix='/appointments'
)

# Status válidos para o model
VALID_STATUSES = ('scheduled', 'confirmed', 'completed', 'cancelled', 'no_show')


# ── Lista ────────────────────────────────────────────────────────────────────

@appointment_bp.route('/')
@login_required
def appointment_list():
    appointments = get_all_appointments()
    return render_template(
        'appointments/appointment_list.html',
        appointments=appointments
    )


# ── Novo agendamento ──────────────────────────────────────────────────────────

@appointment_bp.route('/new', methods=['GET', 'POST'])   # CORREÇÃO: methods=['GET','POST']
@login_required
def appointment_form():
    patients = get_all_patients()

    if request.method == 'POST':
        error = _validate_appointment_form(request.form)

        if error:
            flash(error, 'danger')
            return render_template(
                'appointments/appointment_form.html',
                patients=patients
            )

        appointment, err = create_appointment(request.form)

        if err:
            flash(f'Erro ao agendar consulta: {err}', 'danger')
            return render_template(
                'appointments/appointment_form.html',
                patients=patients
            )

        flash('Consulta agendada com sucesso!', 'success')
        return redirect(url_for('appointments.appointment_list'))

    return render_template(
        'appointments/appointment_form.html',
        patients=patients
    )


# ── Edição ────────────────────────────────────────────────────────────────────

@appointment_bp.route('/<int:id>/edit', methods=['GET', 'POST'])   # CORREÇÃO: methods=['GET','POST']
@login_required
def appointment_edit(id):
    appointment = get_appointment_by_id(id)
    patients = get_all_patients()

    if request.method == 'POST':
        error = _validate_appointment_form(request.form)

        if error:
            flash(error, 'danger')
            return render_template(
                'appointments/appointment_detail.html',
                appointment=appointment,
                patients=patients
            )

        appointment, err = update_appointment(id, request.form)

        if err:
            flash(f'Erro ao atualizar consulta: {err}', 'danger')
            return render_template(
                'appointments/appointment_detail.html',
                appointment=appointment,
                patients=patients
            )

        flash('Consulta atualizada com sucesso!', 'success')
        return redirect(url_for('appointments.appointment_list'))

    return render_template(
        'appointments/appointment_detail.html',
        appointment=appointment,
        patients=patients
    )


# ── Validação de formulário ───────────────────────────────────────────────────

def _validate_appointment_form(form):
    """Retorna mensagem de erro ou None se válido."""

    if not form.get('patient_id'):
        return 'Selecione um paciente.'

    date_str = form.get('appointment_date', '').strip()
    if not date_str:
        return 'Informe a data e hora da consulta.'

    try:
        datetime.fromisoformat(date_str)
    except ValueError:
        return 'Data/hora inválida. Use o formato correto.'

    status = form.get('status', 'scheduled')
    if status not in VALID_STATUSES:
        return f'Status inválido: {status}.'

    return None
