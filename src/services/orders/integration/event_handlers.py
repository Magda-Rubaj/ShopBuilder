from abc import ABC, abstractmethod
from domain.repos import AbstractProductRepository
from domain.entities import Product


class EventHandler(ABC):
    @abstractmethod
    def handle(self):
        raise NotImplementedError


class ProductCreatedEventHandler(EventHandler):
    def __init__(self):
        #self.repo = repo
        pass

    def handle(self, event):
        print(event)
        #product = Product(name=event.name, price=event.price)
        #self.repo.inser(product)