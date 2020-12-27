from pydantic import BaseModel, validator


class AddressSchema(BaseModel):
    name: str = None
    street: str
    neighborhood: str
    city: str
    cep: int
    number: int
    observation: str = ""

    @validator('cep')
    def validate_cep(cls, cep):
        if len(str(cep)) != 8:
            raise ValueError('cep should be have 8 digits')
        return cep

    @validator('number')
    def validate_number(cls, number):
        if number < 0:
            raise ValueError('number should be more than 0')
        return number
