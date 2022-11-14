import os
import httpx
from fastapi import APIRouter, Request
from schemas import BasketItemPost


basket_router = router = APIRouter(tags=["basket"])
BASKET_URL = os.environ.get("BASKET_URL")


@router.post("/basket")
async def product_post(request: Request, data: BasketItemPost):
    response = httpx.post(f"{BASKET_URL}/add", json=data.dict())
    response.raise_for_status()
    return response.json()
