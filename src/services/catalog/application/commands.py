
from dataclasses import dataclass
from domain.repos import ProductRepository


@dataclass
class CreateProductCommand:
    name: str
    price: float
    image: str
    stock: int


def create_product(command: CreateProductCommand, repo: ProductRepository):
    pass