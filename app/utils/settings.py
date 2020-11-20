import os

from app.core.singleton_model import SingletonModel


class SETTINGS(metaclass=SingletonModel):

    MONGO_URI: str = os.getenv('MONGO_URL', None)
    ITEM_PER_PAGE: int = 2

    def __init__(self):
        self.validate_mongo_uri()

    def validate_mongo_uri(self):
        if not self.MONGO_URI:
            raise ValueError('MONGO_URI should be not empty')
