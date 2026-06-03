from datetime import datetime, UTC

from app.extensions import db


class Financial(db.Model):

    __tablename__ = 'financial_records'

    id = db.Column(
        db.Integer,
        primary_key=True
    )

    patient_id = db.Column(
        db.Integer,
        db.ForeignKey('patients.id'),
        nullable=True
    )

    description = db.Column(
        db.String(255),
        nullable=False
    )

    amount = db.Column(
        db.Numeric(10, 2),
        nullable=False
    )

    transaction_type = db.Column(
        db.String(20),
        nullable=False
    )
    # income | expense

    status = db.Column(
        db.String(20),
        default='pending'
    )
    # pending | paid | cancelled

    due_date = db.Column(
        db.Date
    )

    payment_date = db.Column(
        db.Date
    )

    payment_method = db.Column(
    db.String(30)
    ) 
    # pix
    #credit_card
    #debit_card
    #cash
    #bank_transfer

    created_at = db.Column(
        db.DateTime,
        default=lambda: datetime.now(UTC)
    )

    def __repr__(self):
        return (
            f'<Financial '
            f'{self.description} '
            f'{self.amount}>'
        )