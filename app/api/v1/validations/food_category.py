from pydantic import BaseModel


class FoodCategorySchema(BaseModel):
    name: str
    description: str = ""
