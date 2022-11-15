import uvicorn
from fastapi import FastAPI
from config.settings import get_settings
from config.container import Container


app = FastAPI()
settings = get_settings()
container = Container()
container.config.from_pydantic(settings)
container.wire(modules=[__name__])
