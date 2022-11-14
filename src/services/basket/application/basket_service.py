from domain.entities import BasketItem

class BasketService:
    def __init__(self, repo):
        self.repo = repo

    def add_to_basket(self, data):
        item = BasketItem(**data)
        self.repo.add(item)