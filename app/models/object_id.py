from bson import ObjectId as ObjectIdBson


class PydanticObjectId(ObjectIdBson):

    @classmethod
    def __get_validators__(cls):
        yield cls.validate

    @classmethod
    def validate(cls, v):
        if not PydanticObjectId.is_valid(v):
            raise ValueError('Invalid objectid')
        return PydanticObjectId(v)

    @classmethod
    def __modify_schema__(cls, field_schema):
        field_schema.update(type='string')
