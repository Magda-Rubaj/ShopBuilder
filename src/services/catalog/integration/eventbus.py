from abc import ABC
from dataclasses import asdict
from integration.events import IntegrationEvent
import json
from config.logger import logger


class EventBus(ABC):
    ...


class RabbitMQEventBus:
    def __init__(self, channel):
        self.channel = channel

    def publish(self, event: IntegrationEvent):
        name = event.get_event_name()
        event = asdict(event)
        self.channel.queue_declare(queue=name) 
        self.channel.basic_publish(
            exchange="",
            routing_key=name,
            body=json.dumps(event)
        )
        logger.info(f"Event {name} published to rabbitmq")



