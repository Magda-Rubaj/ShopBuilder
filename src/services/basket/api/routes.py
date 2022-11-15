from fastapi import APIRouter, Depends, Request
from dependency_injector.wiring import Provide, inject
from typing import Dict
from pydantic import BaseModel
from config.container import Container



basket_router = router = APIRouter(
    tags=["basket"],
)

class Model(BaseModel):
    name: str

@router.post("/add", status_code=201)
@inject
async def add_item(
    request: Request,
    body: Dict,
    service = Depends(Provide[Container.basket_service])
):
    await service.add_to_basket(body)


