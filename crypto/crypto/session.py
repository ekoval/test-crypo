import jwt
from fastapi.exceptions import HTTPException

SECRET = 'secret'


def authenticate(username):
    return jwt.encode({'username': username}, SECRET, algorithm='HS256')


def get_session(token):
    try:
        return jwt.decode(token, SECRET, algorithms='HS256')
    except jwt.InvalidTokenError:
        raise HTTPException(403)


def has_admin_permission(username):
    return username == 'admin'
