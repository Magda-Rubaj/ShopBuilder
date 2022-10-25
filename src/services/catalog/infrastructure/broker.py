from typing import List
from dataclasses import asdict
import json
from domain.events import Event
from domain.broker import EventPublisher


class RabbitMQEventPublisher(EventPublisher):
    def __init__(self, channel):
        self.channel = channel

    def publish(self, exchange, events: List[Event]):
        for event in events:
            event = asdict(event)
            self.channel.basic_publish(
                exchange=exchange,
                routing_key="shopbuilder",
                body=json.dumps(event)
            )