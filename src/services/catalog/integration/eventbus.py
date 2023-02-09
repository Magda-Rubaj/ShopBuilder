import json
from abc import ABC
from dataclasses import asdict
from aio_pika import DeliveryMode, ExchangeType, Message, connect
from config.logger import logger
from integration.events import IntegrationEvent


class EventBus(ABC):
    ...


class RabbitMQEventBus:
    def __init__(self, channel):
        self.channel = channel

    async def publish(self, event: IntegrationEvent):
        name = event.get_event_name()
        event = asdict(event)
        message = Message(
            json.dumps(event),
            delivery_mode=DeliveryMode.PERSISTENT,
        )
        await self.channel.default_exchange.publish(
            message, routing_key=name,
        )
        logger.info(f"Event {name} published to rabbitmq")



