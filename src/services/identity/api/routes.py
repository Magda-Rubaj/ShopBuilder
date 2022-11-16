from fastapi import APIRouter, Depends, Request
from dependency_injector.wiring import Provide, inject
from typing import Dict
from config.settings import get_settings
from pydantic import BaseModel
from starlette.responses import JSONResponse
from config.container import Container



iam_router = router = APIRouter(
    tags=["iam"],
)


@router.get("/guest-key")
@inject
async def generate_guest_key(
    request: Request, 
    service = Depends(Provide[Container.guest_identity_service]), 
    settings = Depends(Provide[Container.settings])
):  
    key = await service.assign_key()
    response = JSONResponse()
    response.set_cookie(
        key="g_key",
        value=key,
        httponly=True,
        domain=settings.cookies_domain,
    )
    return response
