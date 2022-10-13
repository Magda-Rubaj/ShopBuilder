from abc import ABC, abstractmethod
from domain.entities import Entity

class AbstractProductRepository(ABC):
    @abstractmethod
    def insert(self, entity: Entity):
        ...