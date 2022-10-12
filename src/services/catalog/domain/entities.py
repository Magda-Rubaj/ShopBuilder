from dataclasses import dataclass


@dataclass
class Entity:
    pass


@dataclass
class Product(Entity):
    name: str
    price: float
    image: str
    stock: int
    description: str
