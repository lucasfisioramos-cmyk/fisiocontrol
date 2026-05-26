from flask import Blueprint, render_template


financial_bp = Blueprint(
    'financial',
    __name__,
    url_prefix='/financial'
)


@financial_bp.route('/')
def financial_dashboard():
    return render_template('financial/financial_dashboard.html')