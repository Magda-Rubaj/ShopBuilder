from dependency_injector import containers, providers
from integration.eventbus import RabbitMQEventBus
from integration.event_handlers import ProductCreatedEventHandler


class Container(containers.DeclarativeContainer):
    config = providers.Configuration()
    wiring_config = containers.WiringConfiguration(modules=["api.routes", "main"])
    # product_repository = providers.Factory()
    event_bus = providers.Factory(RabbitMQEventBus)
    product_created_handler = providers.Factory(ProductCreatedEventHandler)
