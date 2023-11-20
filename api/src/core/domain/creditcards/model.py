from datetime import datetime

from sqlalchemy import Column, Integer, DateTime, String, Numeric

from api.src.infra.adapters.database.base import Base


class CreditCardModel(Base):
    __tablename__ = "creditcards"

    creditcard_id = Column(Integer, primary_key=True, index=True)

    expiration_date = Column(DateTime, nullable=False)
    holder = Column(String(255), nullable=False)
    number = Column(String(255), nullable=False)
    cvv = Column(Numeric(4, asdecimal=False), nullable=True)
    brand = Column(String(40), nullable=True)

    created_date = Column(DateTime, default=datetime.now(), nullable=True)
