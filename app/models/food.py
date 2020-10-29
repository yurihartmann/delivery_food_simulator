from pydantic import BaseModel, Field, validator

from app.core.mongo_repository import food_collection
from app.utils.generate_id import generate_id


class Food(BaseModel):

    id: str = Field(default_factory=generate_id, alias='_id')
    name: str
    description: str
    price: float

    @validator('price')
    def _price_not_lenn_than_zero(cls, price):
        if price < 0:
            raise ValueError('price do not less than 0 (zero)')
        return price
