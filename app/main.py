import uvicorn
from app.errors import errors
from config.application import settings
from db.application import database
from routes import applications
from starlette.applications import Starlette

app = Starlette(debug=settings.DEBUG, routes=applications.routes)

app.add_event_handler("startup", database.connect)
app.add_event_handler("shutdown", database.disconnect)

app.add_exception_handler(404, errors.error_response)
app.add_exception_handler(500, errors.error_response)
