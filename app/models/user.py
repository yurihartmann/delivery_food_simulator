from app.models.address import Address
from app.utils.safe_mixin_document import SafeMixinDocument
from mongoengine import *

from app.utils.uuid_utils import generate_uuid

PERMISSIONS = ['client', 'admin']


class User(SafeMixinDocument, Document):

    id = StringField(required=True, primary_key=True, default=generate_uuid)
    first_name = StringField(required=True, max_length=50)
    last_name = StringField(required=True, max_length=50)
    email = EmailField(required=True, unique=True)
    hashed_password = StringField(required=True)
    url_photo = URLField(default=None)
    addresses = EmbeddedDocumentListField(Address)
    permissions = ListField(StringField(choices=PERMISSIONS, default=PERMISSIONS[0]), required=True)

    meta = {
        'collection': 'users',
        'indexes': [
            'first_name',
            'last_name',
            'email',
            'permissions'
        ]
    }

    @classmethod
    def get_by_email(cls, email):
        return User.objects(email=email).first()

    @classmethod
    def authenticate(cls, email, password):
        return User.objects(email=email, hashed_password=password).first()

    @classmethod
    def get_by_id(cls, id):
        return User.objects(id=id).first()

    @classmethod
    def get_address_by_user(cls, user):
        user = User.objects(id=user.id).first()
        return user.addresses
