
from dataclasses import dataclass
from domain.repos import AbstractProductRepository
from domain.entities import Product


@dataclass
class CreateProductCommand:
    name: str
    price: float
    image: str
    stock: int


def create_product(command: CreateProductCommand, repo: AbstractProductRepository):
    product = Product(**command.dict())
    repo.insert(product)