from dependency_injector import containers, providers
from integration.eventbus import RabbitMQEventBus
from infrastructure.repos import ProductRepository
from config.db import setup_db
from integration.event_handlers import ProductCreatedEventHandler


class Container(containers.DeclarativeContainer):
    config = providers.Configuration()
    wiring_config = containers.WiringConfiguration(modules=["api.routes", "main"])
    mongo_client = providers.Singleton(setup_db)
    product_repository = providers.Factory(ProductRepository, db=mongo_client)
    event_bus = providers.Factory(RabbitMQEventBus)
    product_created_handler = providers.Factory(ProductCreatedEventHandler, repo=product_repository)
