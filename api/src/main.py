from fastapi import FastAPI

from .entrypoints.routes.v1 import v1_router

app = FastAPI()

app.include_router(v1_router)

