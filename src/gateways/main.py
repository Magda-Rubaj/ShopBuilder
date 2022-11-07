from fastapi import FastAPI
from routers.catalog import catalog_router


app = FastAPI(docs_url="/api/docs", openapi_url="/api", redoc_url="/redoc")
app.include_router(catalog_router, prefix="/api")