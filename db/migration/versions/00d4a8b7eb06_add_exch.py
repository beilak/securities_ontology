"""add_exch

Revision ID: 00d4a8b7eb06
Revises: 53f8b5219e30
Create Date: 2024-06-07 17:41:51.678841

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = "00d4a8b7eb06"
down_revision: Union[str, None] = "53f8b5219e30"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None

exchs = [
    "LSE_MORNING",
]


def upgrade() -> None:
    exch_ins: str = f"INSERT INTO exchange (id, name, country) VALUES ('LSE_MORNING', 'LSE_MORNING', 'RU');"
    op.execute(exch_ins)


def downgrade() -> None:
    pass
