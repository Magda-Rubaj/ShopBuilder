from dataclasses import dataclass
from __future__ import annotations


@dataclass
class Entity:
    pass


@dataclass
class Category(Entity):
    name: str
    parent: Category
    level: int = 1

    def set_level(self):
        self.level = self.parent.level + 1


@dataclass
class Product(Entity):
    name: str
    price: float
    image: str
    stock: int
    description: str
    category: Category
