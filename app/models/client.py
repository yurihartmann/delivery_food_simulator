from uuid import uuid4

from mongoengine import *

from app.models.address import Address


class Client(Document):

    nick_name = StringField(required=True)
    full_name = StringField(required=True)
    email = EmailField(required=True)
    password = StringField(required=True)
    photo = ImageField()
    address = ReferenceField(Address)

    meta = {
        'collection': 'clients',
        'indexes': ['email']
    }
