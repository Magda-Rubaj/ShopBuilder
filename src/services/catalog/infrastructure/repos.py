from domain.repos import AbstractProductRepository, AbstractCategoryRepository
from sqlalchemy.orm import Session
from domain.entities import Category, Entity, Product


class ProductRepository(AbstractProductRepository):
    def __init__(self, session: Session):
        self._session = session

    def insert(self, entity: Product):
        self._session.add(entity)
        self._session.commit()


class CategoryRepository(AbstractCategoryRepository):
    def __init__(self, session: Session):
        self._session = session

    def insert(self, entity: Category):
        self._session.add(entity)
        self._session.commit()
