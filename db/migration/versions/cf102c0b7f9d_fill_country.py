"""fill_country

Revision ID: cf102c0b7f9d
Revises: 38bd4d28fe60
Create Date: 2023-12-24 18:05:01.852751

"""
from typing import Sequence, Union

from alembic import op


# revision identifiers, used by Alembic.
revision: str = "cf102c0b7f9d"
down_revision: Union[str, None] = "38bd4d28fe60"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    country_ins: str = ""
    for country, curr in [["RU", "RUB"], ["USA", "USD"]]:
        country_ins += f"INSERT INTO country (id, name, currency) VALUES ('{country}', '{country}', '{curr}'); "
    op.execute(country_ins)


def downgrade() -> None:
    op.execute("DELETE FROM country;")
