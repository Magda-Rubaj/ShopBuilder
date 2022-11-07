import os
import httpx
from fastapi import APIRouter, Request
from schemas import ProductPost, CategoryPost


catalog_router = router = APIRouter(tags=["catalog"])
CATALOG_URL = os.environ("CATALOG_URL")


@router.post("/products", response_model=ProductPost)
async def product_post(request: Request, data: dict):
    response = httpx.post(f"{CATALOG_URL}/products/create", json=data)


@router.post("/categories", response_model=CategoryPost)
async def product_post(request: Request, data: dict):
    response = httpx.post(f"{CATALOG_URL}/categories/create", json=data)