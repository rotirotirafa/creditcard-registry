from fastapi import APIRouter, Depends

AuthRoute = APIRouter(
    prefix='/authentication'
)


@AuthRoute.post("/")
def authenticate_user():
    pass


@AuthRoute.post("/refresh-token")
def refresh_token():
    pass
