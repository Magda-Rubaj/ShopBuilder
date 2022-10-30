from typing import List
from fastapi import APIRouter
from dependency_injector.wiring import Provide, inject
from fastapi import Request

from config.container import Container



test_router = router = APIRouter(
    tags=["test"],
)


@router.get("/test")
@inject
async def test(request: Request, eventbus=Provide[Container.event_bus]):
    eventbus.subscribe()
    return "ok"