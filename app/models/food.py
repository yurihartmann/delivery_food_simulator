from pydantic import BaseModel, Field

from app.core.mongo_repository import food_collection
from app.utils.generate_id import generate_id


class Food(BaseModel):

    id: str = Field(default_factory=generate_id, alias='_id')
    name: str
    description: str
    price: float

