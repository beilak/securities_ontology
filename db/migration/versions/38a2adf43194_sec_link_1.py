"""sec_link_1

Revision ID: 38a2adf43194
Revises: 18aee59285f1
Create Date: 2024-06-07 17:33:59.877194

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = "38a2adf43194"
down_revision: Union[str, None] = "18aee59285f1"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.add_column("securities", sa.Column("securities_type", sa.Integer, nullable=True))


def downgrade() -> None:
    pass
