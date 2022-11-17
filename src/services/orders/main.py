import asyncio

import aio_pika
from fastapi import FastAPI
from starlette.middleware.sessions import SessionMiddleware

from config.container import Container
from config.settings import Settings
from integration.events import ProductCreated


config = Settings()
app = FastAPI()
app.add_middleware(SessionMiddleware, secret_key=config.secret_key)


@app.on_event("startup")
async def main():
    container = Container()
    container.config.from_pydantic(config)
    container.wire(modules=[__name__])
    loop = asyncio.get_event_loop()
    connection = await aio_pika.connect_robust(config.amqp_url, loop=loop)
    channel = await connection.channel()
    event_bus = container.event_bus(channel)
    asyncio.ensure_future(
        event_bus.subscribe(
            ProductCreated.__name__, container.product_created_handler()
        )
    )
