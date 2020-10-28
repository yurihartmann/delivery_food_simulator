from fastapi.responses import JSONResponse


def ErrorResponseModel(message: str):
    return JSONResponse(status_code=400, content={"message": message})
