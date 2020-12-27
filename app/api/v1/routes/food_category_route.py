from fastapi import APIRouter, Security
from starlette.responses import JSONResponse

from app.api.v1.validations.food_category_validators import FoodCategorySchema
from app.core.logger import logger
from app.models.category import FoodCategory
from app.models.user import User
from app.utils.autentication import authenticate_admin_user
from app.utils.settings import SETTINGS

food_category_route = APIRouter()


@food_category_route.get('/')
async def get_all_food_categories(page: int = 1, name: str = None):
    """Get All food categories"""
    try:
        food_categories_query = FoodCategory.get_all(page=page, name=name)
        return {
            "info": {
                "page": page,
                "next_page": page + 1 if SETTINGS.ITEMS_PER_PAGE * page < food_categories_query.count() else None,
                "total": food_categories_query.count(),
                "items_per_page": SETTINGS.ITEMS_PER_PAGE
            },
            "data": [food_categories.serialize() for food_categories in food_categories_query]
        }
    except (Exception) as err:
        logger.error(f"Error in get food categories - Error: {err}")
        return JSONResponse(status_code=400, content={"message": "Error in get food categories"})


@food_category_route.get('/{food_category_id}')
async def get_food_categories_by_id(food_category_id: str):
    """Get food category by id"""
    try:
        food_category = FoodCategory.get_by_id(id=food_category_id)
        if not food_category:
            return JSONResponse(status_code=400, content={"message": "Food category do not exists"})

        return food_category.serialize()

    except (Exception) as err:
        logger.error(f"Error in get food category - Error: {err}")
        return JSONResponse(status_code=400, content={"message": "Error in get food category"})


@food_category_route.post('/')
async def save_food_categories(fody_category_schema: FoodCategorySchema, current_user: User = Security(authenticate_admin_user)):
    """Save a new food category"""
    try:
        food_category = FoodCategory(**fody_category_schema.dict()).save()
        return JSONResponse(status_code=200, content=food_category.serialize())

    except (Exception) as err:
        logger.error(f"Error in save food category - Error: {err}")
        return JSONResponse(status_code=400, content={"message": "Error in save food category"})


@food_category_route.delete('/{food_category_id}')
async def delete_food_categories(food_category_id: str, current_user: User = Security(authenticate_admin_user)):
    """Delete food category"""
    try:
        food_category = FoodCategory.get_by_id(id=food_category_id)
        if not food_category:
            return JSONResponse(status_code=400, content={"message": "Food category do not exists"})

        food_category.delete()
        return {"message": "Food category deleted!"}

    except (Exception) as err:
        logger.error(f"Error in delete food category - Error: {err}")
        return JSONResponse(status_code=400, content={"message": "Error in delete food category"})
