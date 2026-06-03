from app.models.user import User

def authenticate_user(email, password):

    user = User.query.filter_by(
        email=email
    ).first()

    if not user:
        return None

    if not user.check_password(password):
        return None

    return user