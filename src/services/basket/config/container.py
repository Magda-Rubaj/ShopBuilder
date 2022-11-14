from dependency_injector import containers, providers
from infrastructure.repos import BasketItemRepository
from application.basket_service import BasketService
from config.store import setup_store


class Container(containers.DeclarativeContainer):
    __self__ = providers.Self()
    config = providers.Configuration()
    wiring_config = containers.WiringConfiguration(modules=["api.routes", "main"])
    redis = providers.Singleton(setup_store)
    product_repository = providers.Factory(BasketItemRepository, redis=redis)
    basket_service =  providers.Factory(BasketService, repo=product_repository)

