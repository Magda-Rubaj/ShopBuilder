from __future__ import annotations
from dataclasses import asdict, dataclass, fields
from domain.value_objects import Price, ValueObject



@dataclass
class Entity:
    pass


@dataclass
class Category(Entity):
    name: str
    parent: Category = None
    level: int = 1

    def set_level(self):
        """sets nesting level if category isn't root"""
        if self.parent:
            self.level = self.parent.level + 1 


@dataclass
class Product(Entity):
    name: str
    price: Price
    image: str
    stock: int
    description: str
    category: Category


