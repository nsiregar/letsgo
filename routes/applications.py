from app.home.home import Home
from starlette.routing import Route

routes = [Route("/", endpoint=Home, methods=["GET"])]
