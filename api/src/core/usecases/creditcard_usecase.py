from sqlalchemy.orm import Session

from api.src.core.schemas.creditcard import CreditcardInputSchema
from api.src.infra.repositories.creditcard import CreditcardRepository


class CreditcardUseCase:

    def __init__(self, db_session: Session):
        self.db = db_session
        self.repository = CreditcardRepository(self.db)

    def create_creditcard(self, payload: CreditcardInputSchema):
        pass

    def get_specific_creditcard_details(self, creditcard_number: str):
        pass

    def list_creditcards(self):
        pass

