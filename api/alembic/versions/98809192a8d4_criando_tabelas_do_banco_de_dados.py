"""Criando tabelas do Banco de Dados

Revision ID: 98809192a8d4
Revises: 
Create Date: 2023-11-20 20:05:32.964936

"""
from datetime import datetime
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa

# revision identifiers, used by Alembic.
revision: str = '98809192a8d4'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table(
        "creditcards",
        sa.Column("creditcard_id", sa.Integer, primary_key=True, index=True),
        sa.Column("expiration_date", sa.String(45), nullable=False),
        sa.Column("holder", sa.String(255), nullable=False),
        sa.Column("number", sa.String(255), nullable=False),
        sa.Column("cvv", sa.Numeric(4, asdecimal=False), nullable=True),
        sa.Column("brand", sa.String(40), nullable=True),
        sa.Column("created_date", sa.DateTime, default=datetime.now(), nullable=True),
    )

    op.create_table(
        "users",
        sa.Column("user_id", sa.Integer, primary_key=True, index=True),
        sa.Column("password", sa.Text, nullable=False),
        sa.Column("email", sa.String(255), nullable=False, unique=True),
        sa.Column("created_date", sa.DateTime, default=datetime.now(), nullable=True)
    )


def downgrade() -> None:
    op.drop_table("users")
    op.drop_table("creditcards")
