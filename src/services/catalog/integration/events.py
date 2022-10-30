
from dataclasses import dataclass
from datetime import datetime

from domain.value_objects import Price


@dataclass
class IntegrationEvent:
    #created: datetime

    def get_event_name(self) -> str:
        return self.__class__.__name__


@dataclass
class ProductCreated(IntegrationEvent):
    name: str
    price: Price


