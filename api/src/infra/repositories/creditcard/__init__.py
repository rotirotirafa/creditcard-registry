from sqlalchemy.orm import Session


class CreditcardRepository:
    db: Session

    def __init__(self, db: Session) -> None:
        self.db = db

