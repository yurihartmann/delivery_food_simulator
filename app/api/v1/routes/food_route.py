from fastapi import APIRouter
from starlette.responses import JSONResponse

from app.api.v1.validations.food import FoodFilterSchema
from app.models.food import Food
from app.utils.settings import SETTINGS

food_route = APIRouter()


@food_route.get("/")
def get_all_foods(page: int = 1, filters: FoodFilterSchema = None):
    """List food for filter"""
    try:
        food_query = Food.get_by_filters(page=page, filters=filters)
        return {
            "info": {
                "page": page,
                "next_page": page + 1 if SETTINGS.ITEM_PER_PAGE * page < food_query.count() else None,
                "total": food_query.count()
            },
            "data": [food_categories.serialize() for food_categories in food_query]
        }
    except Exception as err:
        return JSONResponse(status_code=400, content={"message": "Error in get food categories"})
