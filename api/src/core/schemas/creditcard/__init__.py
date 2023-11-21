from datetime import datetime

from pydantic import BaseModel, field_validator


class CreditcardListAllOutput(BaseModel):
    exp_date: str
    holder: str
    brand: str
    created_date: datetime


class CreditcardInputSchema(BaseModel):
    exp_date: str
    holder: str
    number: str
    cvv: int

    @field_validator('exp_date')
    @classmethod
    def date_is_valid(cls, value: str):
        try:
            # Converte a string para um objeto datetime
            data_str = datetime.strptime(value, '%m/%Y')

            # Obtém a data atual
            actual_date = datetime.now().date()

            # Verifica se a data é válida e não é menor que a data atual
            if data_str.date() >= actual_date:
                return data_str.strftime("%m/%Y")

            raise ValueError('Data não é válida')

        except ValueError as ex:
            # Se a conversão para datetime falhar, a data não é válida
            raise ex

    @field_validator('holder')
    @classmethod
    def verify_holder(cls, value: str):
        if len(value) <= 2:
            raise ValueError("O campo deve ter mais de 2 caracteres")
        return value
