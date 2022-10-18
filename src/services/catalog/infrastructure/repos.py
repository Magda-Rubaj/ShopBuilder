from domain.repos import AbstractProductRepository
from sqlalchemy.orm import Session
from domain.entities import Entity


class ProductRepository(AbstractProductRepository):
    def __init__(self, session: Session):
        self._session = session

    def insert(self, entity: Entity):
        self._session.add(entity)
