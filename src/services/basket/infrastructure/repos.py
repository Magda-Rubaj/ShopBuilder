from domain.repos import AbstractBasketItemRepository
from domain.entities import BasketItem


class BasketItemRepository(AbstractBasketItemRepository):

    def __init__(self, redis):
        self.redis = redis

    async def add(self, key, entity: BasketItem):
        entity_dict = entity.__dict__
        await self.redis.set(key, value=str(entity_dict))
