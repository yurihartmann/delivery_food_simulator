from pydantic import BaseModel, Field, validator

from app.models.address import Address
from app.utils.generate_id import generate_id


class Client(BaseModel):

    id: str = Field(default_factory=generate_id, alias='_id')
    full_name: str
    email: str
    password: str
    photo: str = None
    address: Address = None
