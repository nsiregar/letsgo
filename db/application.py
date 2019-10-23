from importlib import import_module
from pkgutil import iter_modules
from app.wsgi import database
from app import models

for (module_loader, name, ispkg) in iter_modules(models.__path__):
    import_module(f"app.models.{name}", __package__)
