import aio_pika
from config.logger import logger
from integration.event_handlers import EventHandler



class RabbitMQEventBus:
    def __init__(self, channel):
        self.channel = channel

    async def subscribe(self, event_name: str, handler: EventHandler):
        queue = await self.channel.declare_queue(event_name, auto_delete=False)
        logger.info(f"Subscription started for {event_name}")
        async with queue.iterator() as queue_iter:
            async for message in queue_iter:
                async with message.process():
                    logger.info(f"Message recived for {event_name}")
                    handler.handle(message.body)

                    if queue.name in message.body.decode():
                        break
    

     
