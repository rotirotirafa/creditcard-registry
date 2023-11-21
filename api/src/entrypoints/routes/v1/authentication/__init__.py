from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from infra.adapters.database.session import get_db

AuthRoute = APIRouter(
    prefix='/authentication'
)


@AuthRoute.post("/")
def authenticate_user(db: Session = Depends(get_db)):
    pass


@AuthRoute.post("/refresh-token")
def refresh_token(db: Session = Depends(get_db)):
    pass
