from dependency_injector import containers, providers
from infrastructure.repos import BasketItemRepository
from application.basket_service import BasketService
from config.settings import Settings


class Container(containers.DeclarativeContainer):
    __self__ = providers.Self()
    config = providers.Configuration()
    wiring_config = containers.WiringConfiguration(modules=["api.routes", "main"])
    settings = providers.Singleton(Settings)
    basket_items_repository = providers.Factory(
        BasketItemRepository, redis=settings.provided.redis_instance
    )
    basket_service = providers.Factory(BasketService, repo=basket_items_repository)
