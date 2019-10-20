import uvicorn
from config.application import settings
from db.application import database
from routes import applications
from starlette.applications import Starlette

app = Starlette(debug=settings.DEBUG, routes=applications.routes)


@app.on_event("startup")
async def startup():
    await database.connect()


@app.on_event("shutdown")
async def shutdown():
    await database.disconnect()
