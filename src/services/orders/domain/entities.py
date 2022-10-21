from dataclasses import dataclass
from datetime import datetime
from typing import List
from domain.value_objects import Address, Price


@dataclass
class Entity:
    pass


@dataclass
class Product(Entity):
    name: str
    price: Price


@dataclass
class OrderItem(Entity):
    product: Product


@dataclass
class Order(Entity):
    reference: str
    status: str
    address: Address
    date: datetime
    total: float
    customer: str
    items: List[OrderItem]

