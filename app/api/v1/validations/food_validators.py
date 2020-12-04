import uuid
from typing import List

from pydantic import validator, BaseModel

from app.utils.uuid_utils import is_valid_uuid


class FoodSchema(BaseModel):
    name: str
    description: str = ""
    food_categories_id: List[str]
    price: float

    @validator('price')
    def validate_price(cls, price):
        if price < 0:
            raise ValueError('price can not be less than zero!')
        return price

    @validator('food_categories_id')
    def validate_price(cls, food_categories_id):
        for food_category_id in food_categories_id:
            if not is_valid_uuid(food_category_id):
                raise ValueError(f"Is not a valid food_category_id {food_category_id}")
        return food_categories_id


class FoodFilterSchema(BaseModel):
    food_category_id: str = None
    name: str = None
    min_price: float = None
    max_price: float = None

    @validator('min_price')
    def validate_min_price(cls, min_price):
        if min_price and min_price < 0:
            raise ValueError('min_price can not be less than zero!')
        return min_price

    @validator('max_price')
    def validate_max_price(cls, max_price, values):
        if max_price and max_price < 0:
            raise ValueError('max_price can not be less than zero!')
        if values.get('min_price') and max_price <= values['min_price']:
            raise ValueError('max_price can not be less than min_price!')
        return max_price

    def serialize_query(self):
        result = {}
        if self.food_category_id:
            result['food_categories'] = self.food_category_id
        if self.name:
            result['name__contains'] = self.name
        if self.min_price:
            result['price__gte'] = self.min_price
        if self.max_price:
            result['price__lte'] = self.max_price
        return result
