from mongoengine import *

from app.utils.safe_mixin_document import SafeMixinDocument
from app.utils.uuid_utils import generate_uuid
from app.utils.settings import SETTINGS


class FoodCategory(SafeMixinDocument, Document):

    id = StringField(required=True, primary_key=True, default=generate_uuid)
    name = StringField(required=True, max_length=50)
    description = StringField(default='')

    meta = {
        'collection': 'food_categories',
        'indexes': ['name']
    }

    @classmethod
    def get_all(cls, page: int = 1, name: str = None) -> list:
        if name:
            food_category_query = FoodCategory.objects(name__contains=name)
        else:
            food_category_query = FoodCategory.objects()
        return food_category_query.skip(SETTINGS.ITEMS_PER_PAGE * (page - 1)).limit(SETTINGS.ITEMS_PER_PAGE).all()

    @classmethod
    def get_by_id(cls, id: str):
        return FoodCategory.objects(id=id).first()

    @classmethod
    def get_by_name(cls, name: str):
        return FoodCategory.objects(name=name).first()
