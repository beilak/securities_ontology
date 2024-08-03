"""sec_link

Revision ID: 18aee59285f1
Revises: 21d061230634
Create Date: 2024-06-07 17:33:23.427156

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '18aee59285f1'
down_revision: Union[str, None] = '21d061230634'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass
