from datetime import datetime

from mongoengine import *

from app.models.client import Client
from app.models.address import Address
from app.models.food import Food


class FoodOrder(EmbeddedDocument):
    food = EmbeddedDocumentField(Food, required=True)
    quantity = IntField(required=True, default=1)
    observation = StringField()


class Order(Document):

    client = ReferenceField(Client, required=True)
    address = EmbeddedDocumentField(Address, required=True)
    foods_order = EmbeddedDocumentListField(FoodOrder)
    final_price = FloatField()
    creation_date = DateTimeField(required=True, default=datetime.utcnow())

    meta = {
        'collection': 'orders',
        'indexes': ['client.id']
    }
