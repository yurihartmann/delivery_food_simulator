from mongoengine import *

from app.utils.serialize_document import SerializeDocument
from app.utils.generate_id import generate_id
from app.utils.settings import SETTINGS


class FoodCategory(Document, SerializeDocument):

    id = StringField(required=True, primary_key=True, default=generate_id)
    name = StringField(required=True, max_length=50)
    description = StringField(default='')

    meta = {
        'collection': 'food_category',
        'indexes': ['name']
    }

    @classmethod
    def get_all(cls, page: int = 1, name: str = None) -> list:
        if name:
            food_category_query = FoodCategory.objects(name__contains=name)
        else:
            food_category_query = FoodCategory.objects()
        return food_category_query.skip(SETTINGS.ITEM_PER_PAGE * (page - 1)).limit(SETTINGS.ITEM_PER_PAGE).all()

    @classmethod
    def get_by_id(cls, id: str):
        return FoodCategory.objects(id=id).first()
