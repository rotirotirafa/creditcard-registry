from pydantic import BaseModel


class CreditcardInputSchema(BaseModel):
    exp_date: str
    holder: str
    number: str
    cvv: int

