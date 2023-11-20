from fastapi import APIRouter

CreditCardRouter = APIRouter(
    prefix='/credit-card'
)


@CreditCardRouter.get('/')
def list_credit_cards() -> dict:
    return {"v1": "Creditcard Registry API"}


@CreditCardRouter.get('/{creditcard_number}')
def get_credit_card_by_number(creditcard_number: int) -> dict:
    return {"number": creditcard_number}


@CreditCardRouter.post('/')
def create_credit_card():
    pass
