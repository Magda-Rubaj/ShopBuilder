from fastapi import APIRouter, Depends, Request
from dependency_injector.wiring import Provide, inject
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
):  
    key = await service.assign_key()
    response = JSONResponse("ok", status_code=200)
    response.set_cookie(
        key="g_key",
        value=key,
        httponly=True,
    )
    return response
