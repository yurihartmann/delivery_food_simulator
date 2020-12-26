from fastapi import APIRouter, Depends, HTTPException, Security
from fastapi.security import OAuth2PasswordRequestForm

from app.models.user import User
from app.utils.autentication import authenticate_admin_user, create_access_token, authenticate_user

user_route = APIRouter()


@user_route.get('/current_user')
async def current_user(current_user: User = Security(authenticate_user)):
    return current_user.serialize()


@user_route.post("/login")
async def login_for_access_token(form_data: OAuth2PasswordRequestForm = Depends()):
    user = User.authenticate(email=form_data.username, password=form_data.password)
    if not user:
        raise HTTPException(status_code=400, detail="Incorrect username or password")

    access_token = create_access_token(data={"email": user.email})
    return {"access_token": access_token, "token_type": "bearer"}
