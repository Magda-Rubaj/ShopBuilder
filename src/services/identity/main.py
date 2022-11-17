from fastapi import FastAPI
from config.container import Container
from api.routes import iam_router


app = FastAPI()
app.include_router(iam_router, prefix="/api")
container = Container()
container.wire(modules=[__name__])
