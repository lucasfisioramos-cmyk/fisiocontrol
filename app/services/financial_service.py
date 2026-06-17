def get_all_records():
    return Financial.query.order_by(
        Financial.due_date.desc()
    ).all()


def create_record(data):

    from decimal import Decimal
    from datetime import datetime
    from app.extensions import db
    from app.models.financial import Financial

    # Parse amount
    amount_raw = data.get('amount')
    amount = None
    if amount_raw:
        try:
            amount = Decimal(amount_raw)
        except Exception:
            amount = None

    # Parse due_date (YYYY-MM-DD)
    due_date = None
    if data.get('due_date'):
        try:
            due_date = datetime.strptime(data.get('due_date'), '%Y-%m-%d').date()
        except Exception:
            due_date = None

    record = Financial(
        patient_id=int(data.get('patient_id')) if data.get('patient_id') else None,
        description=data.get('description'),
        amount=amount,
        transaction_type=data.get('transaction_type'),
        due_date=due_date
    )

    db.session.add(record)
    db.session.commit()

    return record


def get_record_by_id(record_id):
    return Financial.query.get_or_404(record_id)