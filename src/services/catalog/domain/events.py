
from dataclasses import dataclass

from domain.value_objects import Price


@dataclass
class Event:
    ...


@dataclass
class ProductCreated(Event):
    name: str
    price: Price