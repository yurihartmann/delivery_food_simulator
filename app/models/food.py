from mongoengine import *

from app.api.v1.validations.food import FoodFilterSchema
from app.models.category import FoodCategory
from app.utils.generate_id import generate_id
from app.utils.serialize_document import SerializeDocument
from app.utils.settings import SETTINGS


class Food(Document, SerializeDocument):

    id = StringField(required=True, primary_key=True, default=generate_id)
    name = StringField(required=True, max_length=50)
    description = StringField(default='')
    food_categories = ListField(ReferenceField(FoodCategory))
    price = FloatField(min_value=0, required=True)
    photo = ImageField()

    @classmethod
    def get_by_filters(cls, page: int, filters: FoodFilterSchema = None):
        if filters:
            food_query = Food.objects(**filters.serialize())
        else:
            food_query = Food.objects()
        return food_query.skip(SETTINGS.ITEM_PER_PAGE * (page - 1)).limit(SETTINGS.ITEM_PER_PAGE).all()
