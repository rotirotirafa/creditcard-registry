from pydantic import BaseModel


class AuthInputSchema(BaseModel):
    email: str
    password: str


class AuthBearerResponse(BaseModel):
    access_token: str
    token_type: str
