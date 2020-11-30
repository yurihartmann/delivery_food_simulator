from pydantic import validator, BaseModel


class FoodFilterSchema(BaseModel):
    food_category_id: str = None
    name: str = None

    @validator('price')
    def validate_price(cls, price):
        if price < 0:
            raise ValueError('price can not be less than zero!')
        return price

    def serialize(self):
        result = {}
        if self.food_category_id:
            result['food_categories'] = self.food_category_id
        if self.name:
            result['name__contains'] = self.name
        return result
