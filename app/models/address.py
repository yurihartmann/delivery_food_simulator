from mongoengine import *


class Address(Document):

    address = StringField(required=True)
    city = StringField(required=True)
    neighborhood = StringField(required=True)
    uf = StringField(required=True)
    number = IntField(required=True)
    observation = StringField()

    meta = {
        'collection': 'address'
    }
