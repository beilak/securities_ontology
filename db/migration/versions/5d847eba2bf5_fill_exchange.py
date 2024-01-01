"""fill_exchange

Revision ID: 5d847eba2bf5
Revises: cf102c0b7f9d
Create Date: 2023-12-24 18:22:31.067847

"""
from typing import Sequence, Union

from alembic import op


# revision identifiers, used by Alembic.
revision: str = "5d847eba2bf5"
down_revision: Union[str, None] = "cf102c0b7f9d"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    country_ins: str = ""
    for exch in ["MOEX", "MOEX_EVENING_WEEKEND", "MOEX_WEEKEND", "MOEX_PLUS"]:
        country_ins += f"INSERT INTO exchange (id, name, country) VALUES ('{exch}', 'MOEX', 'RU'); "
    op.execute(country_ins)


def downgrade() -> None:
    op.execute("DELETE FROM exchange;")
