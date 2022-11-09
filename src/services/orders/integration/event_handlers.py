import json
from abc import ABC, abstractmethod
from config.logger import logger
from domain.repos import AbstractProductRepository
from domain.entities import Product
from integration.events import ProductCreated


class EventHandler(ABC):
    @abstractmethod
    def handle(self):
        raise NotImplementedError


class ProductCreatedEventHandler(EventHandler):
    def __init__(self, repo: AbstractProductRepository):
        self.repo = repo

    def handle(self, message):
        event = ProductCreated(**json.loads(message))
        product = Product(name=event.name, price=event.price)
        self.repo.insert(product)