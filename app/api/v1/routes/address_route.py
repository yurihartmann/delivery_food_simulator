from fastapi import APIRouter, Security
from starlette.responses import JSONResponse

from app.api.v1.validations.address_validators import AddressSchema
from app.core.logger import logger
from app.models.address import Address
from app.models.user import User
from app.utils.autentication import authenticate_user

address_route = APIRouter()


@address_route.get('/')
async def get_addresses_by_user(current_user: User = Security(authenticate_user)):
    """Get address by user"""
    try:
        return [address.serialize() for address in current_user.addresses]

    except (Exception) as err:
        logger.error(f"Error in get addresses by user - Error: {err}")
        return JSONResponse(status_code=400, content={"message": "Error in get address by user"})


@address_route.post('/')
async def save_address_by_user(address_schema: AddressSchema, current_user: User = Security(authenticate_user)):
    """Save address by user"""
    try:
        if not address_schema.name:
            address_schema.name = f"{address_schema.street}, {address_schema.number}"

        address = Address(**address_schema.dict())
        current_user.addresses.append(address)
        current_user.save()

        return address.serialize()

    except (Exception) as err:
        logger.error(f"Error in get addresses by user - Error: {err}")
        return JSONResponse(status_code=400, content={"message": "Error in get address by user"})
