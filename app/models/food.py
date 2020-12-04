from mongoengine import *

from app.api.v1.validations.food_validators import FoodFilterSchema
from app.core.logger import logger
from app.models.category import FoodCategory
from app.utils.uuid_utils import generate_uuid
from app.utils.serialize_document import SerializeDocument
from app.utils.settings import SETTINGS


class Food(Document, SerializeDocument):

    id = StringField(required=True, primary_key=True, default=generate_uuid)
    name = StringField(required=True, max_length=50)
    description = StringField(default='')
    food_categories = ListField(ReferenceField(FoodCategory))
    price = FloatField(min_value=0, required=True)
    url_photo = StringField(default=None)

    @classmethod
    def get_by_id(cls, id: str):
        return Food.objects(id=id).first()

    @classmethod
    def get_by_filters(cls, page: int, filters: FoodFilterSchema):
        logger.info(f"Food get_by_filters - {filters.serialize_query()}")
        food_query = Food.objects(**filters.serialize_query())
        return food_query.skip(SETTINGS.ITEM_PER_PAGE * (page - 1)).limit(SETTINGS.ITEM_PER_PAGE).all()
