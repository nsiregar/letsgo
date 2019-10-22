from starlette.middleware.base import BaseHTTPMiddleware
from db.application import session


class DatabaseMiddleware(BaseHTTPMiddleware):
    async def dispatch(self, request, call_next):
        request.state.db = session
        response = await call_next(request)
        request.state.db.close()
        return response
