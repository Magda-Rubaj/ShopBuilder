from abc import ABC, abstractmethod
from domain.entities import Entity


class Repository(ABC):
    ...


class AbstractProductRepository(Repository):
    @abstractmethod
    def insert(self, entity: Entity):
        ...


class AbstractCategoryRepository(Repository):
    @abstractmethod
    def insert(self, entity: Entity):
        ...