from flask import Blueprint, render_template

patient_bp = Blueprint(
    'patients',
    __name__,
    url_prefix='/patients'
)


@patient_bp.route('/')
def patient_list():
    return render_template('patients/patient_list.html')