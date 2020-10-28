from fastapi import FastAPI

from app.api.routes.food_router import food_router

app = FastAPI()

app.include_router(food_router, tags=["Food"], prefix="/food")


@app.get("/")
def hello():
    return {"Hello": "World"}
