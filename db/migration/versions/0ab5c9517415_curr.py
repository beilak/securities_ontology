"""curr

Revision ID: 0ab5c9517415
Revises: 88b3d0eaf2fd
Create Date: 2023-12-30 15:16:10.231920

"""
from typing import Sequence, Union

from alembic import op


# revision identifiers, used by Alembic.
revision: str = "0ab5c9517415"
down_revision: Union[str, None] = "88b3d0eaf2fd"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None
currs: set = {
    "HKD",
    "KZT",
}


def upgrade() -> None:
    curr_ins: str = ""
    for curr in currs:
        curr_ins += f"INSERT INTO currency (id, name) VALUES ('{curr}', '{curr}'); "
    op.execute(curr_ins)


def downgrade() -> None:
    for curr in currs:
        op.execute(f"DELETE FROM currency WHERE id = '{curr}';")
