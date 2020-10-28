import os

from pydantic import BaseModel, validator


class SETTINGS(BaseModel):

    MONGO_URI: str = os.getenv('MONGO_URL', None)
    ITEM_PER_PAGE: int = 10

    @validator('MONGO_URI')
    def validate_mongo_uri(cls, mongo_url):
        if not mongo_url:
            raise ValueError('MONGO_URI should be not empty')
