"""fill_sectors

Revision ID: f141977db4ef
Revises: 6925ae140af7
Create Date: 2023-12-24 18:52:06.039712

"""
from typing import Sequence, Union

from alembic import op

# revision identifiers, used by Alembic.
revision: str = "f141977db4ef"
down_revision: Union[str, None] = "6925ae140af7"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    sector_ins: str = ""
    for sector in [
        "energy",
        "financial",
        "health_care",
        "it",
        "consumer",
        "materials",
        "industrials",
        "telecom",
        "ecomaterials",
        "other",
        "real_estate",
        "electrocars",
        "utilities",
        "green_energy",
        "green_buildings",
    ]:
        sector_ins += f"INSERT INTO sector (id, name) VALUES ('{sector}', '{sector}');"
    op.execute(sector_ins)


def downgrade() -> None:
    op.execute("DELETE FROM sector;")
