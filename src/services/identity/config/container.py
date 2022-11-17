from dependency_injector import containers, providers
from config.settings import Settings
from application.services import GuestIdentityService
from infrastructure.repos import GuestRepository


class Container(containers.DeclarativeContainer):
    config = providers.Configuration()
    wiring_config = containers.WiringConfiguration(modules=["api.routes", "main"])
    settings = providers.Singleton(Settings)
    guest_repository = providers.Factory(
        GuestRepository, redis=settings.provided.redis_instance
    )
    guest_identity_service = providers.Factory(
        GuestIdentityService, repo=guest_repository
    )
