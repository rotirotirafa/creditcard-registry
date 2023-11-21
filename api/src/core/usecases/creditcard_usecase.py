from sqlalchemy.orm import Session

from creditcard import CreditCard

from api.src.core.domain.creditcards.model import CreditCardModel
from api.src.core.schemas.creditcard import CreditcardInputSchema
from api.src.infra.repositories.creditcard import CreditcardRepository

from api.src.utils import hash_credit_card_number, check_creditcard_hash


class CreditcardUseCase:

    def __init__(self, db_session: Session):
        self.db = db_session
        self.repository = CreditcardRepository(self.db)

    def create_creditcard(self, payload: CreditcardInputSchema):
        try:
            creditcard_object = CreditCardModel(
                expiration_date=payload.exp_date,
                holder=payload.holder,
                number=self.get_creditcard_number_encrypt(payload.number),
                cvv=payload.cvv,
                brand=self.get_brand_from_creditcard_number(payload.number)
            )
            ob = self.repository.insert(creditcard_object)
            return ob
        except Exception as ex:
            print(ex)
            raise ex

    def get_specific_creditcard_details(self, creditcard_number: str):
        encrypted = str(check_creditcard_hash(creditcard_number))
        card_details = self.repository.get_one_by_number(encrypted)
        return card_details

    def list_creditcards(self):
        return self.repository.get_all()

    @staticmethod
    def get_creditcard_number_encrypt(number) -> str or bool:
        cc = CreditCard(number)
        if cc.is_valid():
            return hash_credit_card_number(cc.number)
        raise ValueError('Número de cartão é inválido')

    @staticmethod
    def get_brand_from_creditcard_number(number) -> str:
        cc = CreditCard(number)
        brand = cc.get_brand()
        return brand
