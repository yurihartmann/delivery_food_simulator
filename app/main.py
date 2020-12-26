import mongoengine
from fastapi import FastAPI
from mongoengine import connect

from app.api.v1.v1_route import v1_route
from app.models.user import User, PERMISSIONS
from app.utils.settings import SETTINGS

app = FastAPI()


@app.on_event("startup")
def on_startup():
    connect(host=SETTINGS.MONGO_URI)
    mongoengine.get_db()


app.include_router(
    v1_route,
    prefix="/v1"
)


@app.get("/")
def hello():
    u = User()
    u.first_name = 'Yuri'
    u.last_name = "Hartmann"
    u.email = "yuri@gmail.com"
    u.hashed_password = "123"
    u.permissions = PERMISSIONS
    u.save()
    return {"Hello": "World"}
