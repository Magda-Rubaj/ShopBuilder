import uvicorn
from fastapi import FastAPI
from api.routes import basket_router
from config.container import Container


app = FastAPI()
app.include_router(basket_router, prefix="/api")

@app.on_event('startup')    
async def main():
    container = Container()
    container.wire(modules=[__name__])

