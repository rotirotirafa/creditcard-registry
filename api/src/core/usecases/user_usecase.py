from sqlalchemy.orm import Session

from core.domain.users.model import UsersModel
from core.schemas.users import UserInputSchema
from infra.repositories.users import UsersRepository
from utils import hash_pw


class UsersUseCase:

    def __init__(self, db_session: Session):
        self.db = db_session
        self.repository = UsersRepository(self.db)

    def create_user(self, payload: UserInputSchema) -> str:
        try:
            user_object = UsersModel(
                email=payload.email,
                password=hash_pw(payload.password)
            )
            user = self.repository.insert(user_object)
            return user.email
        except Exception as ex:
            raise ex
