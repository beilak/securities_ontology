"""sec_link

Revision ID: 21d061230634
Revises: 688644951d5e
Create Date: 2024-06-07 17:07:14.479393

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '21d061230634'
down_revision: Union[str, None] = '688644951d5e'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass
