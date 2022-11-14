import uvicorn
from fastapi import FastAPI
from routers.catalog import catalog_router
from routers.basket import basket_router


app = FastAPI(docs_url="/api/docs", openapi_url="/api", redoc_url="/redoc")
app.include_router(catalog_router, prefix="/api")
app.include_router(basket_router, prefix="/api")


if __name__ == "__main__":
    uvicorn.run(
        "main:app",
        host="0.0.0.0",
        log_level="debug",
        reload=True,
        port=8000,
    )