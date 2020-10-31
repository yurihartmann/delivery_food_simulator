from datetime import datetime
from enum import Enum
from typing import List

from pydantic import validator, BaseModel

from app.models.client import Client
from app.models.address import Address
from app.models.food import Food


class PaymentEnum(str, Enum):
    credit_card = 'credit_card'
    money = 'money'


class FoodOrder(BaseModel):
    food: Food
    quantity: int = 1
    observation: str

    @validator('quantity')
    def _validate_quantity(cls, quantity):
        if quantity < 1:
            raise ValueError('quantity do not be less than 1 (one)')
        return quantity


class Order(BaseModel):

    client: Client
    address: Address
    foods_order: List[FoodOrder]
    final_price: float = 0
    creation_date: datetime = datetime.utcnow()
    payment: PaymentEnum

    @validator('final_price')
    def passwords_match(cls, final_price, values, **kwargs):
        final_price = 0
        for food_order in values['foods_order']:
            final_price += food_order['food']['price'] * food_order['quantity']
        return final_price
