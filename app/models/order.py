from datetime import datetime

from app.models.address import Address
from app.models.user import ClientUser
from app.models.food import Food
from app.utils.safe_mixin_document import SafeMixinDocument, Document
from mongoengine import *

from app.utils.uuid_utils import generate_uuid


def datetime_now():
    return datetime.utcnow()


class Order(SafeMixinDocument, Document):

    id = StringField(required=True, primary_key=True, default=generate_uuid)
    client = ReferenceField(ClientUser, required=True)
    address = EmbeddedDocumentField(Address, required=True)
    foods = EmbeddedDocumentListField(Food)
    order_datetime = DateTimeField(required=True, default=datetime_now)
    observation = StringField(default="")

    meta = {
        'collection': 'orders',
        'indexes': [
            'order_datetime',
        ]
    }
