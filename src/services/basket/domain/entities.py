from dataclasses import dataclass
from domain.value_objects import Price
from typing import List


@dataclass
class Entity:
    pass


@dataclass
class Aggregate:
    pass


@dataclass
class BasketItem(Entity):
    name: str
    price: Price
    quantity: int
    attributes: dict


@dataclass
class Basket(Aggregate):
    hash_id: str
    items: List[BasketItem]