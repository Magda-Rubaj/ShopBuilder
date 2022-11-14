from domain.repos import AbstractBasketItemRepository
from domain.entities import BasketItem


class BasketItemRepository(AbstractBasketItemRepository):

    def __init__(self, redis):
        self.redis = redis


    def add(self, key, entity: BasketItem):
        entity_dict = entity.__dict__
        self.redis.set(key, value=entity_dict.encode("utf-8"))