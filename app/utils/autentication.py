from datetime import timedelta, datetime

import jwt
from fastapi import Depends, Security, HTTPException
from fastapi.security import OAuth2PasswordBearer
from starlette import status

from app.models.user import User
from app.utils.settings import SETTINGS

oauth2_scheme = OAuth2PasswordBearer(
    tokenUrl="v1/user/login",
)


def get_current_user(token: str = Depends(oauth2_scheme)):
    try:
        payload = jwt.decode(token, SETTINGS.SECRET_KEY, algorithms=[SETTINGS.ALGORITHM])
        user = User.get_by_email(payload.get('email'))
        if not user:
            raise Exception
        return user

    except (Exception):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Could not validate credentials",
        )


def authenticate_user(current_user: User = Security(get_current_user)):
    return current_user


def authenticate_admin_user(current_user: User = Security(get_current_user)):
    if "admin" in current_user.permissions:
        return current_user

    raise HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Do not permission for this action",
    )


def authenticate_client_user(current_user: User = Security(get_current_user)):
    if "client" in current_user.permissions:
        return current_user

    raise HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Do not permission for this action",
    )


def create_access_token(data: dict):
    data.update({"exp": datetime.utcnow() + timedelta(minutes=SETTINGS.ACCESS_TOKEN_EXPIRE_MINUTES)})
    return jwt.encode(data, SETTINGS.SECRET_KEY, algorithm=SETTINGS.ALGORITHM)
