from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from core.schemas.auth import AuthInputSchema, AuthBearerResponse
from core.usecases.auth_usecase import AuthUseCase
from infra.adapters.database.session import get_db

AuthRoute = APIRouter(
    prefix='/authentication'
)


@AuthRoute.post("/")
def authenticate_user(payload: AuthInputSchema, db: Session = Depends(get_db)) -> AuthBearerResponse:
    try:
        auth_use_case = AuthUseCase(db)
        return auth_use_case.authenticate_user(payload)
    except Exception as ex:
        raise ex
