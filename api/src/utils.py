import bcrypt

import hashlib

from fastapi.security import OAuth2PasswordBearer
from passlib.context import CryptContext


def hash_credit_card_number(card_number):
    salt = "123"
    hashed_number = hashlib.sha256((card_number + salt).encode('utf-8')).hexdigest()
    return hashed_number


def check_creditcard_hash(card_number) -> str:
    hash_input = hash_credit_card_number(card_number)
    return hash_input


def hash_pw(password: str) -> bytes:
    pw = password.encode('utf-8')
    salt = bcrypt.gensalt(10)
    pw_hashed = bcrypt.hashpw(pw, salt)
    return pw_hashed


def verify_password_hash(password: str) -> bool:
    pw = password.encode('utf-8')
    verified = bcrypt.checkpw(pw, hash_pw(password))
    if verified:
        return True
    return False


oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")
# Configuração do Contexto de Senha para hashing e verificação
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

