from flask import Blueprint, render_template, request, redirect, url_for
from flask_login import login_required
from app.services.patient_service import get_all_patients
from app.services.appointment_service import (
    get_all_appointments,
    get_appointment_by_id,
    create_appointment
)

appointment_bp = Blueprint(
    'appointments',
    __name__,
    url_prefix='/appointments'
)


@appointment_bp.route('/')
@login_required
def appointment_list():
    appointments = get_all_appointments()

    return render_template(
        'appointments/appointment_list.html',
        appointments=appointments
    )

@appointment_bp.route('/new', methods=['GET', 'POST'])
@login_required
def appointment_form():
    if request.method == 'POST':
        create_appointment(request.form)
        return redirect(url_for('appointments.appointment_list'))

    patients = get_all_patients()

    return render_template(
        'appointments/appointment_form.html',
        patients=patients
    )

@appointment_bp.route('/<int:id>/edit')
@login_required
def appointment_edit(id):
    appointment = get_appointment_by_id(id)

    return render_template(
        'appointments/appointment_detail.html',
        appointment=appointment
    )

