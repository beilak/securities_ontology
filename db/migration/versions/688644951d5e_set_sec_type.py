"""set_sec_type

Revision ID: 688644951d5e
Revises: 818aa682962f
Create Date: 2024-06-07 16:53:08.020814

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa
from tinkoff.invest import ShareType

# revision identifiers, used by Alembic.
revision: str = "688644951d5e"
down_revision: Union[str, None] = "818aa682962f"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    country_ins: str = ""
    for id_ in ShareType:
        country_ins += f"""
        INSERT INTO securities_type (id, name) 
        VALUES ('{id_.value}', '{id_.name}'); """
    op.execute(country_ins)


def downgrade() -> None:
    pass
