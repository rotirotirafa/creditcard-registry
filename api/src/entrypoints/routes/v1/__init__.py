from fastapi import APIRouter

from .creditcard import CreditCardRouter

v1_router = APIRouter(
    prefix='/api/v1'
)

v1_router.include_router(CreditCardRouter, tags=['CreditCard'])
