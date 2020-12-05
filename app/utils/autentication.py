from datetime import timedelta, datetime

import jwt
from fastapi import Depends, Security, HTTPException
from fastapi.security import OAuth2PasswordBearer
from starlette import status

from app.models.admin_user import AdminUser
from app.utils.settings import SETTINGS

oauth2_scheme = OAuth2PasswordBearer(
    tokenUrl="v1/admin/login",
)


def get_admin_current_user(token: str = Depends(oauth2_scheme)):
    try:
        payload = jwt.decode(token, SETTINGS.SECRET_KEY, algorithms=[SETTINGS.ALGORITHM])
        user = AdminUser.get_by_email(payload.get('email'))
        if not user:
            raise Exception
        return user

    except (Exception):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Could not validate credentials",
        )


def authenticate_admin_user(current_user: AdminUser = Security(get_admin_current_user)):
    return current_user


def create_access_token(data: dict):
    data.update({"exp": datetime.utcnow() + timedelta(minutes=SETTINGS.ACCESS_TOKEN_EXPIRE_MINUTES)})
    return jwt.encode(data, SETTINGS.SECRET_KEY, algorithm=SETTINGS.ALGORITHM)
