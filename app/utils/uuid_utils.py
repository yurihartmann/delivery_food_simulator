import uuid


def generate_uuid() -> str:
    return str(uuid.uuid4())


def is_valid_uuid(uuid_to_test):
    try:
        uuid_obj = uuid.UUID(uuid_to_test, version=4)
    except ValueError:
        return False

    return str(uuid_obj) == uuid_to_test
