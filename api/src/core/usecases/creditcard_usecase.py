from sqlalchemy.orm import Session

from api.src.infra.repositories.creditcard import CreditcardRepository


class CreditcardUseCase:

    def __init__(self, db_session: Session):
        self.db = db_session
        self.repository = CreditcardRepository(self.db)

    def create_creditcard(self):
        pass

    def get_specific_creditcard_details(self):
        pass

    def list_creditcards(self):
        pass

