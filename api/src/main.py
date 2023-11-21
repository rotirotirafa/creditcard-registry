from fastapi import FastAPI

from api.src.entrypoints.routes.v1 import v1_router

app = FastAPI()

app.include_router(v1_router)

@app.get('/')
def health_check():
    return 'ok'
