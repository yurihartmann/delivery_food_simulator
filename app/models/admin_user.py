from app.utils.safe_mixin_document import SafeMixinDocument
from mongoengine import *

from app.utils.uuid_utils import generate_uuid


class AdminUser(SafeMixinDocument, Document):

    id = StringField(required=True, primary_key=True, default=generate_uuid)
    first_name = StringField(required=True, max_length=50)
    last_name = StringField(required=True, max_length=50)
    email = EmailField(required=True, unique=True)
    hashed_password = StringField(required=True)
    url_photo = URLField(default=None)

    meta = {
        'collection': 'admin_users',
        'indexes': [
            'first_name',
            'last_name',
            'email',
        ]
    }

    @classmethod
    def get_by_email(cls, email):
        return AdminUser.objects(email=email).first()

    @classmethod
    def authenticate(cls, email, password):
        return AdminUser.objects(email=email, hashed_password=password).first()
