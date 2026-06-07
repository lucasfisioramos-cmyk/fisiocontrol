from flask import Blueprint, render_template, request, redirect, url_for, flash
from flask_login import login_required

from app.services.financial_service import (
    get_all_records,
    get_record_by_id,
    create_record,
    get_summary,
)
from app.services.patient_service import get_all_patients


financial_bp = Blueprint(
    'financial',
    __name__,
    url_prefix='/financial'
)

VALID_TYPES   = ('income', 'expense')
VALID_METHODS = ('pix', 'credit_card', 'debit_card', 'cash', 'bank_transfer')
VALID_STATUS  = ('pending', 'paid', 'cancelled')


# ── Dashboard financeiro ──────────────────────────────────────────────────────

@financial_bp.route('/dashboard')          # CORREÇÃO: era "/" duplicado, agora "/dashboard"
@login_required
def financial_dashboard():
    summary = get_summary()
    return render_template(
        'financial/financial_dashboard.html',
        summary=summary
    )


# ── Lista de lançamentos ──────────────────────────────────────────────────────

@financial_bp.route('/')
@login_required
def financial_list():
    records = get_all_records()
    return render_template(
        'financial/financial_list.html',
        records=records
    )


# ── Novo lançamento ───────────────────────────────────────────────────────────

@financial_bp.route('/new', methods=['GET', 'POST'])
@login_required
def financial_form():
    patients = get_all_patients()

    if request.method == 'POST':
        error = _validate_financial_form(request.form)

        if error:
            flash(error, 'danger')
            return render_template(
                'financial/financial_form.html',
                patients=patients
            )

        record, err = create_record(request.form)

        if err:
            flash(f'Erro ao salvar lançamento: {err}', 'danger')
            return render_template(
                'financial/financial_form.html',
                patients=patients
            )

        flash('Lançamento registrado com sucesso!', 'success')
        return redirect(url_for('financial.financial_list'))

    return render_template(
        'financial/financial_form.html',
        patients=patients
    )


# ── Edição de lançamento ──────────────────────────────────────────────────────

@financial_bp.route('/<int:id>/edit', methods=['GET', 'POST'])
@login_required
def financial_edit(id):
    record = get_record_by_id(id)
    patients = get_all_patients()

    if request.method == 'POST':
        error = _validate_financial_form(request.form)

        if error:
            flash(error, 'danger')
            return render_template(
                'financial/financial_form.html',
                record=record,
                patients=patients
            )

        from app.services.financial_service import update_record
        record, err = update_record(id, request.form)

        if err:
            flash(f'Erro ao atualizar lançamento: {err}', 'danger')
            return render_template(
                'financial/financial_form.html',
                record=record,
                patients=patients
            )

        flash('Lançamento atualizado com sucesso!', 'success')
        return redirect(url_for('financial.financial_list'))

    return render_template(
        'financial/financial_form.html',
        record=record,
        patients=patients
    )


# ── Validação de formulário ───────────────────────────────────────────────────

def _validate_financial_form(form):
    """Retorna mensagem de erro ou None se válido."""

    if not form.get('description', '').strip():
        return 'Informe uma descrição para o lançamento.'

    amount_str = form.get('amount', '').strip()
    if not amount_str:
        return 'Informe o valor do lançamento.'
    try:
        amount = float(amount_str)
        if amount <= 0:
            return 'O valor deve ser maior que zero.'
    except ValueError:
        return 'Valor inválido. Use apenas números.'

    if form.get('transaction_type') not in VALID_TYPES:
        return 'Tipo de transação inválido (income ou expense).'

    payment_method = form.get('payment_method')
    if payment_method and payment_method not in VALID_METHODS:
        return 'Método de pagamento inválido.'

    status = form.get('status', 'pending')
    if status not in VALID_STATUS:
        return 'Status inválido.'

    return None
