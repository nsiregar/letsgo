import uvicorn
from config.application import settings
from routes import applications
from starlette.applications import Starlette
from starlette.responses import PlainTextResponse

app = Starlette(debug=settings.DEBUG, routes=applications.routes)
