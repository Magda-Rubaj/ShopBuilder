from domain.exceptions import GuestKeyExistsException
from domain.repos import AbstractGuestRepository


class GuestRepository(AbstractGuestRepository):
    def __init__(self, redis):
        self.redis = redis
        
    async def add(self, key):    
        guest = await self.redis.get(key)
        if guest:
            raise GuestKeyExistsException   
        await self.redis.set(key, value=0)