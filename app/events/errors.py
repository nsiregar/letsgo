from starlette.responses import JSONResponse


async def error_response(request, exc):
    response = {"status": exc.status_code, "detail": exc.detail}
    return JSONResponse(response)
