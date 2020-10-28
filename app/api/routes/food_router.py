from fastapi import APIRouter

from app.core.mongo_repository import food_collection
from app.models.food import Food
from app.utils.error_response_model import ErrorResponseModel
from app.utils.settings import SETTINGS

food_router = APIRouter()
ITEM_PER_PAGE = SETTINGS().ITEM_PER_PAGE


@food_router.get('/', name="List foods")
def get_all_foods(page: int = 1):
    if page < 1:
        page = 1

    return [food for food in food_collection.find().skip(ITEM_PER_PAGE * (page - 1))]


@food_router.get('/{food_id}', name="Get food by id")
def get_food_by_id(food_id: str):
    for food in food_collection.find({"_id": food_id}):
        return food
    return ErrorResponseModel("Food do not exists")


@food_router.post('/', name="Add food")
def save_new_food(food: Food):
    food_collection.insert_one(food.dict(by_alias=True))
    return food


@food_router.put('/{food_id}', name="Edit food")
def update_food(food_id: str, food: Food):
    food.id = food_id
    food_dict = food.dict(by_alias=True)
    del food_dict['_id']
    query = food_collection.update_one({"_id": food_id}, {"$set": food_dict})

    if query.matched_count > 0:
        return food.dict(by_alias=True)
    elif query.raw_result.get('updatedExisting'):
        return ErrorResponseModel("Food do not exists")
    else:
        return ErrorResponseModel("Error in update food")


@food_router.delete('/{food_id}', name="Delete food")
def put_food(food_id: str):
    query = food_collection.delete_one({"_id": food_id})

    if query.matched_count > 0:
        return {"message": "Food deleted with success"}
    elif query.raw_result.get('updatedExisting'):
        return ErrorResponseModel("Food do not exists")
    else:
        return ErrorResponseModel("Error in delete food")
