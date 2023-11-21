from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from infra.adapters.database.session import get_db
from core.schemas.users import UserInputSchema
from core.usecases.user_usecase import UsersUseCase


UsersRouter = APIRouter(
    prefix='/users'
)


@UsersRouter.post("/create-account")
def create_user_account(payload: UserInputSchema,  db: Session = Depends(get_db)) -> dict:
    try:
        users_use_case = UsersUseCase(db)
        email = users_use_case.create_user(payload)
        return {'email': email, 'msg': 'Criado com sucesso'}
    except Exception as ex:
        raise ex
