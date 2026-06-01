from app import db
from app.models.financial import Financial


def get_all_records():
    return Financial.query.order_by(
        Financial.due_date.desc()
    ).all()


def create_record(data):

    record = Financial(
        patient_id=data.get('patient_id') or None,
        description=data.get('description'),
        amount=data.get('amount'),
        transaction_type=data.get('transaction_type'),
        due_date=data.get('due_date')
    )

    db.session.add(record)
    db.session.commit()

    return record


def get_record_by_id(record_id):
    return Financial.query.get_or_404(record_id)