from datetime import datetime

from sqlalchemy import Column, Integer, DateTime, String, Numeric, Text

from api.src.infra.adapters.database.base import Base


class UsersModel(Base):

    __tablename__ = "users"

    user_id = Column(Integer, primary_key=True, index=True)

    password = Column(Text, nullable=False)
    email = Column(String(length=255), nullable=False, unique=True)

    created_date = Column(DateTime, default=datetime.now(), nullable=True)
