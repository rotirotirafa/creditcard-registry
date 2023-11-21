from fastapi import APIRouter

from .authentication import AuthRoute
from .creditcard import CreditCardRouter
from .users import UsersRouter

v1_router = APIRouter(
    prefix='/api/v1'
)

v1_router.include_router(CreditCardRouter, tags=['CreditCard'])
v1_router.include_router(UsersRouter, tags=['User'])
v1_router.include_router(AuthRoute, tags=['Authentication'])


