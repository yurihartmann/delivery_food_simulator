from app.utils.safe_mixin_document import SafeMixinDocument
from mongoengine import *

from app.utils.uuid_utils import generate_uuid


class Address(SafeMixinDocument, Document):

    id = StringField(required=True, primary_key=True, default=generate_uuid)
    name = StringField()
    street = StringField(required=True)
    neighborhood = StringField(required=True)
    city = StringField(required=True)
    cep = StringField(min_length=8, max_length=8)
    number = IntField(required=True)
    observation = StringField(default="")

    meta = {
        'collection': 'addresses',
        'indexes': [
            'street',
            'cep',
        ]
    }

