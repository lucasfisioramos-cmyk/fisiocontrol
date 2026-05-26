from flask import Blueprint, render_template


appointment_bp = Blueprint(
    'appointments',
    __name__,
    url_prefix='/appointments'
)


@appointment_bp.route('/')
def appointment_list():
    return render_template('appointments/appointment_list.html')