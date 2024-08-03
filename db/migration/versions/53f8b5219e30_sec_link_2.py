"""sec_link_2

Revision ID: 53f8b5219e30
Revises: 38a2adf43194
Create Date: 2024-06-07 17:35:39.002600

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '53f8b5219e30'
down_revision: Union[str, None] = '38a2adf43194'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass
