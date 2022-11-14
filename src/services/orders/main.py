import asyncio

import aio_pika
import uvicorn
from fastapi import FastAPI
from starlette.middleware.sessions import SessionMiddleware

from api.routes import test_router
from config.app import AppConfig
from config.container import Container
from integration.events import ProductCreated


config = AppConfig()
app = FastAPI()
app.add_middleware(SessionMiddleware, secret_key=config.secret_key)

@app.on_event('startup')    
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

if __name__ == "__main__":
    uvicorn.run(
        "main:app",
        host="0.0.0.0",
        log_level="debug",
        reload=True,
        port=8888,
    )


