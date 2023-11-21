from typing import List

from sqlalchemy.orm import Session

from api.src.core.domain.creditcards.model import CreditCardModel


class CreditcardRepository:
    db: Session

    def __init__(self, db: Session) -> None:
        self.db = db

    def get_one_by_number(self, number: str):
        response = self.db.query(CreditCardModel).filter_by(number=number).first()
        return response

    def get_all(self) -> List[CreditCardModel] or List:
        try:
            response = self.db.query(CreditCardModel).all()
            return response
        except Exception as ex:
            raise ex

    def insert(self, creditcard_object: CreditCardModel):
        try:
            self.db.add(creditcard_object)
            self.db.commit()
            self.db.refresh(creditcard_object)
            return creditcard_object
        except Exception as ex:
            raise ex
