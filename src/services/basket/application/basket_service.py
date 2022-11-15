from domain.entities import BasketItem

class BasketService:
    def __init__(self, repo):
        self.repo = repo

    async def add_to_basket(self, data):
        item = BasketItem(**data)
        await self.repo.add("test", item)