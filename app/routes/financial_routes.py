from flask import Blueprint, render_template, request, redirect, url_for
from flask_login import login_required
from app.services.financial_service import(
    get_all_records,
    create_record
)
from app.services.patient_service import (
    get_all_patients
)

financial_bp = Blueprint(
    'financial',
    __name__,
    url_prefix='/financial'
)

@financial_bp.route('/')
@login_required
def financial_list():

    records = get_all_records()

    return render_template(
        'financial/financial_list.html',
        records=records
    )

@financial_bp.route('/new', methods=['GET', 'POST'])
@login_required
def financial_form():

    if request.method == 'POST':

        create_record(request.form)

        return redirect(
            url_for('financial.financial_list')
        )

    patients = get_all_patients()

    return render_template(
        'financial/financial_form.html',
        patients=patients
    )


@financial_bp.route('/')
@login_required
def financial_dashboard():
    return render_template('financial/financial_dashboard.html')