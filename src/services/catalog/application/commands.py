from dataclasses import dataclass, asdict
from domain.repos import (
    AbstractProductRepository,
    AbstractCategoryRepository,
    Repository,
)
from domain.entities import Category, Product


@dataclass
class Command:
    pass


@dataclass
class CreateCategoryCommand(Command):
    name: str
    parent: int


def create_category(command: CreateCategoryCommand, repo: AbstractCategoryRepository):
    category = Category(**asdict(command))
    category.set_level()
    repo.insert(category)


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
    handlers = {
        CreateProductCommand: create_product,
        CreateCategoryCommand: create_category
    }

    def execute_command(self, command: Command, repository: Repository):
        handler = self.handlers.get(type(command))
        return handler(command, repository)
