from pydantic import BaseModel


class UserInputSchema(BaseModel):
    email: str
    password: str

