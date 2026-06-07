from flask import Blueprint, render_template
from flask_login import login_required

from app.services.patient_service import get_all_patients
from app.services.appointment_service import get_all_appointments
from app.services.financial_service import get_summary


dashboard_bp = Blueprint(
    'dashboard',
    __name__
)


@dashboard_bp.route('/')
@login_required
def dashboard():
    patients     = get_all_patients()
    appointments = get_all_appointments()
    summary      = get_summary()

    return render_template(
        'dashboard/dashboard.html',
        total_patients=len(patients),
        total_appointments=len(appointments),
        financial_summary=summary,
    )
