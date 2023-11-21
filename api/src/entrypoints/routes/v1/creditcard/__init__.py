from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from api.src.infra.adapters.database.session import get_db
from api.src.core.schemas.creditcard import CreditcardInputSchema
from api.src.core.usecases.creditcard_usecase import CreditcardUseCase


CreditCardRouter = APIRouter(
    prefix='/credit-card'
)


@CreditCardRouter.get('/')
def get(db: Session = Depends(get_db)):
    try:
        creditcard_use_case = CreditcardUseCase(db)
        return creditcard_use_case.list_creditcards()
    except Exception as ex:
        raise ex


@CreditCardRouter.get('/{creditcard_number}')
def get_one(creditcard_number: str, db: Session = Depends(get_db)):
    try:
        creditcard_use_case = CreditcardUseCase(db)
        return creditcard_use_case.get_specific_creditcard_details(creditcard_number)
    except Exception as ex:
        raise ex


@CreditCardRouter.post('/')
def create(payload: CreditcardInputSchema, db: Session = Depends(get_db)):
    try:
        creditcard_use_case = CreditcardUseCase(db)
        return creditcard_use_case.create_creditcard(payload)
    except Exception as ex:
        raise ex
