from sqlalchemy.orm import Session

from core.domain.users.model import UsersModel


class UsersRepository:
    db: Session

    def __init__(self, db: Session) -> None:
        self.db = db

    def insert(self, user_object: UsersModel):
        try:
            self.db.add(user_object)
            self.db.commit()
            self.db.refresh(user_object)
            return user_object
        except Exception as ex:
            raise ex
