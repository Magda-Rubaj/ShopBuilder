
from dataclasses import dataclass, asdict
from domain.repos import AbstractProductRepository, Repository
from domain.entities import Product

@dataclass
class Command:
    pass


@dataclass
class CreateProductCommand(Command):
    name: str
    price: float
    image: str
    stock: int
    description: str


def create_product(command: CreateProductCommand, repo: AbstractProductRepository):
    product = Product(**asdict(command))
    repo.insert(product)


class CommandMapper:
    handlers = {CreateProductCommand: create_product}

    def execute_command(self, command: Command, repository: Repository):
        handler = self.handlers.get(type(command))
        return handler(repository)
