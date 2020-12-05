from mongoengine import *

from app.api.v1.validations.food_validators import FoodFilterSchema
from app.core.logger import logger
from app.models.category import FoodCategory
from app.utils.uuid_utils import generate_uuid
from app.utils.safe_mixin_document import SafeMixinDocument
from app.utils.settings import SETTINGS


class Food(SafeMixinDocument, Document):

    id = StringField(required=True, primary_key=True, default=generate_uuid)
    name = StringField(required=True, max_length=50)
    description = StringField(default='')
    food_categories = ListField(ReferenceField(FoodCategory))
    price = FloatField(min_value=0, required=True)
    url_photo = StringField(default=None)

    meta = {
        'collection': 'foods',
        'indexes': ['name', 'price']
    }

    @classmethod
    def get_by_id(cls, id: str):
        return Food.objects(id=id).first()

    @classmethod
    def get_by_filters(cls, page: int, filters: FoodFilterSchema):
        logger.info(f"Food get_by_filters - {filters.serialize_query()}")
        food_query = Food.objects(**filters.serialize_query())
        return food_query.skip(SETTINGS.ITEMS_PER_PAGE * (page - 1)).limit(SETTINGS.ITEMS_PER_PAGE).all()
