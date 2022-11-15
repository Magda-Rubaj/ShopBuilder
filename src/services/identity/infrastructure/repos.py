
from domain.repos import AbstractGuestRepository


class GuestRepository(AbstractGuestRepository):
    def __init__(self, redis):
        self.redis = redis
        
    def add(self, key):
        pass