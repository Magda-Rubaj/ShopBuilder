from domain.repos import AbstractProductRepository
from dataclasses import asdict
from domain.entities import Product


class ProductRepository(AbstractProductRepository):
    def __init__(self, db):
        self.collection = db["products"]
    
    def insert(self, entity: Product):
        entity = asdict(entity)
        self.collection.insert_one(entity)
