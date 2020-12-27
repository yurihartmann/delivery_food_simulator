from datetime import datetime

from bson import DBRef
from mongoengine import *


class SafeMixinDocument:

    created_at = DateTimeField(required=True)
    updated_at = DateTimeField(required=True)

    def save(self, *args, **kwargs):
        if not self.created_at:
            self.created_at = datetime.utcnow()

        self.updated_at = datetime.utcnow()

        return super(SafeMixinDocument, self).save(*args, **kwargs)

    def serialize(self, *args, **kwargs) -> dict:
        dict_json = {}
        for field_name in self:
            data_field_name = self._data.get(field_name, None)

            if isinstance(data_field_name, datetime):
                dict_json[field_name] = data_field_name.isoformat()
            elif isinstance(data_field_name, list) and len(data_field_name) > 0:
                if isinstance(data_field_name[0], DBRef):
                    list_of_ids = []
                    for dbrefs in data_field_name:
                        list_of_ids.append(str(dbrefs.id))
                    dict_json[field_name] = list_of_ids
                else:
                    dict_json[field_name] = data_field_name
            else:
                dict_json[field_name] = data_field_name
        return dict_json
