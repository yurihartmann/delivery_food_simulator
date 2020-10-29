from pydantic import BaseModel, validator


class Address(BaseModel):

    address: str
    city: str
    neighborhood: str
    uf: str
    number: int
    observation: str

    @validator('uf')
    def _validade_uf(cls, uf):
        if len(uf) != 2:
            raise ValueError('uf should be have 2 (two) char')
        return uf

    @validator('number')
    def _validade_uf(cls, number):
        if number < 0:
            raise ValueError('number do not be less than 0 (zero)')
        return number
