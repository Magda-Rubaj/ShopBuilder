import asyncio
from fastapi import FastAPI
import aio_pika
from config.container import Container
from config.settings import Settings
from infrastructure.mappers import begin_mapping
from config.container import Container
from api.routes import catalog_router
from config.logger import logger

config = Settings()
app = FastAPI(debug=True)
app.include_router(catalog_router, prefix="/api")


@app.on_event("startup")
async def start():
    container = Container()
    container.config.from_pydantic(config)
    container.wire(modules=[__name__])
    begin_mapping()
