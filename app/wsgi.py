from starlette.applications import Starlette
from gino.ext.starlette import Gino

from app.errors import errors
from config.application import settings
from routes import applications

app = Starlette(debug=settings.DEBUG, routes=applications.routes)

app.add_exception_handler(404, errors.error_response)
app.add_exception_handler(500, errors.error_response)

database = Gino(app, dsn=settings.SQLALCHEMY_DATABASE_URI)
