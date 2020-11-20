import json


class SerializeDocument:

    def serialize(self, *args, **kwargs):
        return json.loads(self.to_json())
