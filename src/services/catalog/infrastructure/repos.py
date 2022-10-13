from config.db import Base
from domain.repos import AbstractProductRepository
from sqlalchemy.orm import Session
from domain.entities import Entity
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import mapper


class ProductRepository(AbstractProductRepository):
    def __init__(self, session: Session):
        self._session = session

    def insert(self, entity: Entity):
        self.session.add(entity)
