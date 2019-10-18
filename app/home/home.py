from starlette.endpoints import HTTPEndpoint
from starlette.responses import JSONResponse


class Home(HTTPEndpoint):
    async def get(self, request):
        response = {"status": "success", "message": "pong"}
        return JSONResponse(response)
