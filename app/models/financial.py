from app import db


class Financial(db.Model):
    __tablename__ = 'financial'

    id = db.Column(db.Integer, primary_key=True)
    patient_name = db.Column(db.String(120), nullable=False)
    amount = db.Column(db.Float, nullable=False)
    payment_status = db.Column(db.String(50), default='Pendente')
    payment_date = db.Column(db.String(20))

    def __repr__(self):
        return f'<Financial {self.patient_name}>'