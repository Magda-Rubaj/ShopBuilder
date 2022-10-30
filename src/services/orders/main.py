import uvicorn
import pika
import aio_pika
import asyncio
from fastapi import FastAPI, Request
from config.app import AppConfig
from config.container import Container
from dependency_injector.wiring import Provide, inject
from integration.events import ProductCreated
from integration.event_handlers import ProductCreatedEventHandler
from api.routes import test_router
from starlette.middleware.sessions import SessionMiddleware

from integration.eventbus import RabbitMQEventBus


config = AppConfig()
app = FastAPI(docs_url="/api/docs", openapi_url="/api", redoc_url="/redoc")
app.add_middleware(SessionMiddleware, secret_key=config.secret_key)
app.include_router(test_router, prefix="/api", tags=["test"])

# def callback(ch, method, properties, body):
#     print(body)

# def main():
#     connection = pika.BlockingConnection(pika.ConnectionParameters("localhost"))
#     channel = connection.channel()
#     channel.queue_declare(queue='ProductCreated')

#     def callback(ch, method, properties, body):
#         print(" [x] Received %r" % body)

#     channel.basic_consume(queue='ProductCreated', on_message_callback=callback, auto_ack=True)

#     print(' [*] Waiting for messages. To exit press CTRL+C')
#     channel.start_consuming()
# #     # container = Container()
# #     # container.config.from_pydantic(config)
# #     # container.wire(modules=[__name__])
# #     # event_bus = container.event_bus(container.config.rabbit_channel)
# #     # event_bus.subscribe(
# #     #     ProductCreated.__name__, container.product_created_handler()
# #     # )
# #     #self.channel.exchange_declare(exchange=event_name, exchange_type='fanout'
# #     try:
# #         channel = config.rabbit_channel
# #         channel.queue_declare(queue="SHOPBUILDER")
# #         #channel.queue_bind(exchange="ProductCreated", queue="SHOPBUILDER")
# #         channel.basic_consume(
# #             queue="SHOPBUILDER", 
# #             on_message_callback=callback, 
# #             auto_ack=True
# #         )
# #         print("RABBIT WORKS -----------------")
# #         channel.start_consuming()
# #     except Exception as e:
# #         print("retrying")
# #         print(e)

# # # @inject
# # # def start_eventbus(event_bus = container.event_bus()):
# # #     event_bus.subscribe(
# # #         ProductCreated.__name__, Provide[Container.product_created_handler]
# # #     )

MAPPER = {
    ProductCreated: ProductCreatedEventHandler
}


@app.on_event('startup')    
async def main():
    container = Container()
    container.config.from_pydantic(config)
    container.wire(modules=[__name__])
    loop = asyncio.get_event_loop()
    connection = await aio_pika.connect_robust("amqp://guest:guest@127.0.0.1/", loop=loop)
    channel = await connection.channel()
    event_bus = container.event_bus(channel)
    asyncio.ensure_future(event_bus.subscribe(ProductCreated.__name__, container.product_created_handler()))

if __name__ == "__main__":
    uvicorn.run(
        "main:app",
        host="0.0.0.0",
        log_level="debug",
        reload=True,
        port=8888,
    )


