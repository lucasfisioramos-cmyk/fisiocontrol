from app import db


class Patient(db.Model):
    __tablename__ = 'patients'

    id = db.Column(db.Integer, primary_key=True)
    full_name = db.Column(db.String(120), nullable=False)
    phone = db.Column(db.String(20))
    email = db.Column(db.String(120))
    birth_date = db.Column(db.String(20))
    health_insurance = db.Column(db.String(120))
    status = db.Column(db.String(50), default='Ativo')

    def __repr__(self):
        return f'<Patient {self.full_name}>'