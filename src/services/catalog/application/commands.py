
from dataclasses import dataclass, asdict
from domain.repos import AbstractProductRepository
from domain.entities import Product


@dataclass
class CreateProductCommand:
    name: str
    price: float
    image: str
    stock: int
    description: str


def create_product(command: CreateProductCommand, repo: AbstractProductRepository):
    product = Product(**asdict(command))
    repo.insert(product)