"""exchange_add

Revision ID: aabb5d68ec2e
Revises: e38df90cae16
Create Date: 2024-04-11 23:21:39.560943

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = "aabb5d68ec2e"
down_revision: Union[str, None] = "e38df90cae16"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


exchs = [
    "FX",
    "FX_MTL",
]


def upgrade() -> None:
    exch_ins: str = ""
    for exch in exchs:
        exch_ins += (
            f"INSERT INTO exchange (id, name, country) VALUES ('{exch}', 'SPB', 'RU'); "
        )
    op.execute(exch_ins)


def downgrade() -> None:
    for exch in exchs:
        op.execute(f"DELETE FROM exchange WHERE id = '{exch}';")
