from fastapi import FastAPI
from mongoengine import connect

from app.api.v1.routes.food_category_route import food_category_route
from app.utils.settings import SETTINGS

app = FastAPI()


@app.on_event("startup")
def on_startup():
    connect(host=SETTINGS.MONGO_URI)


app.include_router(
    food_category_route,
    prefix="/food_category",
    tags=['food_category']
)


@app.get("/")
def hello():
    return {"Hello": "World"}
