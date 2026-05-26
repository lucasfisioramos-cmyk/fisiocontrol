from app.models.financial import Financial


def get_all_financial_records():
    return Financial.query.all()