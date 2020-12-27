from app.utils.safe_mixin_document import SafeMixinDocument
from mongoengine import *

from app.utils.uuid_utils import generate_uuid


class Address(SafeMixinDocument, EmbeddedDocument):

    id = StringField(required=True, primary_key=True, default=generate_uuid)
    name = StringField()
    street = StringField(required=True)
    neighborhood = StringField(required=True)
    city = StringField(required=True)
    cep = IntField()
    number = IntField(required=True)
    observation = StringField(default="")

