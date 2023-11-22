from fastapi import HTTPException, status, Depends
from jose import jwt, JWTError
from sqlalchemy.orm import Session

from config import SECRET_KEY
from core.schemas.auth import AuthInputSchema, AuthBearerResponse
from core.usecases.user_usecase import UsersUseCase
from utils import pwd_context, oauth2_scheme, verify_password_hash


class AuthUseCase:

    def __init__(self, db_session: Session):
        self.db = db_session
        self.user_use_case = UsersUseCase(self.db)

    def authenticate_user(self, payload: AuthInputSchema) -> AuthBearerResponse:
        user = self.user_use_case.get_user_info_for_auth(payload)

        if payload.email and verify_password_hash(user.password):
            token = self.create_jwt_token(payload.email)
            return AuthBearerResponse(
                access_token=token,
                token_type='bearer'
            )

        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid credentials",
            headers={"WWW-Authenticate": "Bearer"},
        )

    @staticmethod
    def create_jwt_token(email: str) -> str:
        return jwt.encode({"sub": email}, SECRET_KEY, algorithm="HS256")

    @staticmethod
    def get_user(token: str = Depends(oauth2_scheme)):
        credentials_exception = HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid credentials",
            headers={"WWW-Authenticate": "Bearer"},
        )
        try:
            payload = jwt.decode(token, SECRET_KEY, algorithms=["HS256"])
            email: str = payload.get("sub")
            return email
        except JWTError:
            raise credentials_exception
