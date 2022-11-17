from dependency_injector import containers, providers
from integration.eventbus import RabbitMQEventBus
from infrastructure.repos import ProductRepository
from config.settings import Settings
from integration.event_handlers import ProductCreatedEventHandler


class Container(containers.DeclarativeContainer):
    config = providers.Configuration()
    wiring_config = containers.WiringConfiguration(modules=["api.routes", "main"])
    settings = providers.Singleton(Settings)
    product_repository = providers.Factory(
        ProductRepository, db=settings.provided.mongo_client
    )
    event_bus = providers.Factory(RabbitMQEventBus)
    product_created_handler = providers.Factory(
        ProductCreatedEventHandler, repo=product_repository
    )
