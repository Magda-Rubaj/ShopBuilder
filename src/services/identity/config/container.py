from dependency_injector import containers, providers
from config.settings import Settings
from services.identity.application.services import GuestIdentityService


class Container(containers.DeclarativeContainer):
    config = providers.Configuration()
    wiring_config = containers.WiringConfiguration(modules=["api.routes", "main"])
    settings = providers.Singleton(Settings)
    guest_repository = providers.Factory(
        GuestIdentityService, redis=settings.redis_instance
    )
    guest_identity_service = providers.Factory(
        GuestIdentityService, repo=guest_repository
    )
