from fastapi import APIRouter

from app.api.v1.routes.food_category_route import food_category_route
from app.api.v1.routes.food_route import food_route

v1_route = APIRouter()

v1_route.include_router(
    food_category_route,
    prefix="/food_category",
    tags=['Food Category']
)

v1_route.include_router(
    food_route,
    prefix="/food",
    tags=['Food']
)
