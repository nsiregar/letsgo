import uvicorn
from starlette.applications import Starlette

from app.errors import errors
from app.middlewares.database import DatabaseMiddleware
from config.application import settings
from db.application import database
from routes import applications

app = Starlette(debug=settings.DEBUG, routes=applications.routes)

app.add_middleware(DatabaseMiddleware)

app.add_exception_handler(404, errors.error_response)
app.add_exception_handler(500, errors.error_response)
