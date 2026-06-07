from decimal import Decimal
from datetime import date
from sqlalchemy import func

from app.extensions import db
from app.models.financial import Financial


def get_all_records():
    return Financial.query.order_by(Financial.due_date.desc()).all()


def get_record_by_id(record_id):
    return db.get_or_404(Financial, record_id)


def get_records_by_patient(patient_id):
    return (
        Financial.query
        .filter_by(patient_id=patient_id)
        .order_by(Financial.due_date.desc())
        .all()
    )


def create_record(data):
    """Retorna (Financial, None) ou (None, str_erro)."""
    try:

        record = Financial(

            patient_id=(
                data.get('patient_id')
                or None
            ),

            description=data.get(
                'description'
            ),

            amount=data.get(
                'amount'
            ),

            transaction_type=data.get(
                'transaction_type'
            ),

            status=data.get(
                'status'
            ),

            due_date=(
                date.fromisoformat(
                    data.get('due_date')
                )
                if data.get('due_date')
                else None
            ),

            payment_date=(
                date.fromisoformat(
                    data.get(
                        'payment_date'
                    )
                )
                if data.get(
                    'payment_date'
                )
                else None
            ),

            payment_method=data.get(
                'payment_method'
            )
        )

        db.session.add(record)

        db.session.commit()

        return record, None

    except Exception as e:

        db.session.rollback()

        return None, str(e)

def update_record(record_id, data):
    """Retorna (Financial, None) ou (None, str_erro)."""
    try:
        record = db.get_or_404(Financial, record_id)
        record.patient_id       = int(data['patient_id']) if data.get('patient_id') else None
        record.description      = data.get('description', record.description)
        record.amount           = Decimal(data.get('amount', record.amount))
        record.transaction_type = data.get('transaction_type', record.transaction_type)
        record.status           = data.get('status', record.status)
        record.due_date         = data.get('due_date') or record.due_date
        record.payment_method   = data.get('payment_method') or record.payment_method
        db.session.commit()
        return record, None
    except Exception as e:
        db.session.rollback()
        return None, str(e)


def get_summary():
    """Retorna totais de receitas, despesas e saldo para o dashboard."""
    income = db.session.scalar(
        func.coalesce(
            func.sum(Financial.amount).filter(Financial.transaction_type == 'income'),
            0
        )
    )
    expense = db.session.scalar(
        func.coalesce(
            func.sum(Financial.amount).filter(Financial.transaction_type == 'expense'),
            0
        )
    )
    return {
        'income':  income,
        'expense': expense,
        'balance': income - expense,
    }
