from typing import List
from domain.events import Event
from domain.broker import EventPublisher


class RabbitMQEventPublisher(EventPublisher):
    def __init__(self, channel):
        self.channel = channel

    def publish(self, exchange, events: List[Event]):
        for event in events:
            self.channel.basic_publish(
                exchange=exchange,
                routing_key="shopbuilder",
                body=event
            )