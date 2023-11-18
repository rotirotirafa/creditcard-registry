from fastapi import FastAPI


from src.entrypoints.routes.v1 import api_router


app = FastAPI()

app.include_router(api_router)


@app.get("/")
async def hello() -> dict:
    return {"app": "Creditcard Registry API"}
