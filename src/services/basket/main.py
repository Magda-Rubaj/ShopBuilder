import uvicorn
from fastapi import FastAPI
from api.routes import basket_router
from config.container import Container


app = FastAPI(docs_url="/api/docs", openapi_url="/api", redoc_url="/redoc")
app.include_router(basket_router, prefix="/api")

@app.on_event('startup')    
async def main():
    container = Container()
    container.wire(modules=[__name__])

if __name__ == "__main__":
    uvicorn.run(
        "main:app",
        host="0.0.0.0",
        log_level="debug",
        reload=True,
        port=5555,
    )
