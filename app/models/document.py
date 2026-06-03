from datetime import datetime, UTC

from app.extensions import db


class Document(db.Model):

    __tablename__ = 'documents'

    id = db.Column(db.Integer, primary_key=True)

    patient_id = db.Column(
        db.Integer,
        db.ForeignKey('patients.id'),
        nullable=False
    )

    filename = db.Column(
        db.String(255),
        nullable=False
    )

    description = db.Column(
        db.String(255)
    )

    uploaded_at = db.Column(
        db.DateTime,
        default=lambda: datetime.now(UTC)
    )
    def __repr__(self):
        return f'<Document {self.filename}>'