from fastapi import APIRouter
from starlette.responses import JSONResponse

from app.api.v1.validations.food_validators import FoodFilterSchema, FoodSchema
from app.core.logger import logger
from app.models.food import Food
from app.utils.settings import SETTINGS

food_route = APIRouter()


@food_route.get("/")
def get_all_foods(page: int = 1,
                  food_category_id: str = None,
                  name: str = None,
                  min_price: float = None,
                  max_price: float = None):
    """List food for filter"""
    try:
        filters = FoodFilterSchema(food_category_id=food_category_id,
                                   name=name,
                                   min_price=min_price,
                                   max_price=max_price)

        food_query = Food.get_by_filters(page=page, filters=filters)
        return {
            "info": {
                "page": page,
                "next_page": page + 1 if SETTINGS.ITEM_PER_PAGE * page < food_query.count() else None,
                "total": food_query.count()
            },
            "data": [food_categories.serialize() for food_categories in food_query]
        }
    except (Exception) as err:
        logger.error(f"Error in get food categories - Error: {err}")
        return JSONResponse(status_code=400, content={"message": "Error in get food categories"})


@food_route.get("/{id}")
def get_food_by_id(id: str):
    """Get food for id"""
    try:
        food = Food.get_by_id(id)

        if not food:
            return JSONResponse(status_code=404, content={"message": "Food do not exist!"})

        return food.serialize()

    except (Exception) as err:
        logger.error(f"Error in get food - Error: {err}")
        return JSONResponse(status_code=400, content={"message": "Error in get food"})


@food_route.post("/")
def get_food_by_id(food: FoodSchema):
    """Save new food"""
    try:
        return Food(**food.dict()).save()

    except (Exception) as err:
        logger.error(f"Error in save food - Error: {err}")
        return JSONResponse(status_code=400, content={"message": "Error in save food"})