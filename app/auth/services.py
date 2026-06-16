from app.models.user import User
from app.extensions import db

def authenticate_user(email, password):

    user = User.query.filter_by(
        email=email
    ).first()

    if not user:
        return None

    if not user.check_password(password):
        return None

    return user

def register_user(name, email, password):
    """
    Cria um novo usuário.
    Retorna (User, None) em sucesso ou (None, str_erro) em falha.
    """
    existing = User.query.filter_by(email=email).first()
    if existing:
        return None, "Este e-mail já está cadastrado."

    try:
        user = User(name=name, email=email)
        user.set_password(password)
        db.session.add(user)
        db.session.commit()
        return user, None
    except Exception as e:
        db.session.rollback()
        return None, str(e)
