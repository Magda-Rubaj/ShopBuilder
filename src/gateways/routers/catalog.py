import os
import httpx
from fastapi import APIRouter, Request
from fastapi.encoders import jsonable_encoder
from schemas import ProductPost, CategoryPost


catalog_router = router = APIRouter(tags=["catalog"])
CATALOG_URL = os.environ.get("CATALOG_URL")


@router.post("/products")
async def product_post(request: Request, data: ProductPost):
    response = httpx.post(f"{CATALOG_URL}/api/products/create", json=jsonable_encoder(data))
    response.raise_for_status()
    return response.json()


@router.post("/categories")
async def product_post(request: Request, data: CategoryPost):
    response = httpx.post(f"{CATALOG_URL}/api/categories/create", json=jsonable_encoder(data))
    response.raise_for_status()
    return response.json()