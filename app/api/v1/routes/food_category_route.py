from fastapi import APIRouter
from starlette.responses import JSONResponse

from app.api.v1.validations.food_category import FoodCategorySchema
from app.models.category import FoodCategory
from app.utils.settings import SETTINGS

food_category_route = APIRouter()


@food_category_route.get('/')
def get_all_food_categories(page: int = 1, name: str = None):
    """Get All food categories"""
    try:
        food_categories_query = FoodCategory.get_all(page=page, name=name)
        return {
            "info": {
                "page": page,
                "next_page": page + 1 if SETTINGS.ITEM_PER_PAGE * page < food_categories_query.count() else None,
                "total": food_categories_query.count()
            },
            "data": [food_categories.serialize() for food_categories in food_categories_query]
        }
    except (Exception) as err:
        return JSONResponse(status_code=400, content={"message": "Error in get food categories"})


@food_category_route.get('/{food_category_id}')
def get_food_categories_by_id(food_category_id: str):
    """Get food categories by id"""
    try:
        food_category = FoodCategory.get_by_id(id=food_category_id)
        if not food_category:
            return JSONResponse(status_code=400, content={"message": "Food category do not exists"})

        return food_category.serialize()

    except (Exception) as err:
        return JSONResponse(status_code=400, content={"message": "Error in get food category"})


@food_category_route.post('/')
def save_food_categories(fody_category_schema: FoodCategorySchema):
    """Save a new food categories"""
    try:
        food_category = FoodCategory(**fody_category_schema.dict())
        food_category.save()
        return JSONResponse(status_code=200, content=food_category.serialize())

    except (Exception) as err:
        print(err)
        return JSONResponse(status_code=400, content={"message": "Error in save food category"})
