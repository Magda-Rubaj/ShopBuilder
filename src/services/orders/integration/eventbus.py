from integration.events import IntegrationEvent
from integration.event_handlers import EventHandler
import aio_pika


class RabbitMQEventBus:
    def __init__(self, channel):
        self.channel = channel

    async def subscribe(self, event_name: str, handler: EventHandler):
        queue = await self.channel.declare_queue(event_name, auto_delete=False)
        print(f"Subscription started for {event_name}")
        async with queue.iterator() as queue_iter:
            async for message in queue_iter:
                async with message.process():
                    handler.handle(message.body)

                    if queue.name in message.body.decode():
                        break
    

     
