"""exchange

Revision ID: 88b3d0eaf2fd
Revises: e10d7dc2e05a
Create Date: 2023-12-30 01:37:37.268411

"""
from typing import Sequence, Union

from alembic import op


# revision identifiers, used by Alembic.
revision: str = "88b3d0eaf2fd"
down_revision: Union[str, None] = "e10d7dc2e05a"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None

exchs = [
    "SPB_RU_MORNING",
    "SPB_CLOSE",
    "OTC_NCC",
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
