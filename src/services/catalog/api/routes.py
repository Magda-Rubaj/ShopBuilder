from application.commands import CreateCategoryCommand, CreateProductCommand, CommandMapper
from config.container import Container
from dependency_injector.wiring import Provide, inject, Closing
from fastapi import APIRouter, status, Depends
from infrastructure.repos import CategoryRepository, ProductRepository
from integration.eventbus import EventBus


catalog_router = router = APIRouter(tags=["catalog"])


@catalog_router.post("/products/create", status_code=status.HTTP_201_CREATED)
@inject
def add_product(
    product: dict,
    command_mapper: CommandMapper = Depends(Provide[Container.command_mapper]),
    repo: ProductRepository = Depends(Provide[Container.product_repository]),
    publisher: EventBus = Depends(Closing[Provide[Container.rabbit_publisher]]),
):
    command = CreateProductCommand(**product)
    command_mapper.execute_command(command, repo, publisher)
    return {"status": "OK"}


@catalog_router.post("/categories/create", status_code=status.HTTP_201_CREATED)
@inject
def add_category(
    category: dict,
    command_mapper: CommandMapper = Depends(Provide[Container.command_mapper]),
    repo: CategoryRepository = Depends(Provide[Container.category_repository]),
):
    command = CreateCategoryCommand(**category)
    command_mapper.execute_command(command, repo)
    return {"status": "OK"}

