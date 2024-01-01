"""fill_dict

Revision ID: 38bd4d28fe60
Revises: ba8158747de6
Create Date: 2023-12-24 16:37:05.891584

"""
from typing import Sequence, Union

from alembic import op

# revision identifiers, used by Alembic.
revision: str = "38bd4d28fe60"
down_revision: Union[str, None] = "ba8158747de6"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    curr_ins: str = ""
    for curr in {"RUB", "USD"}:
        curr_ins += f"INSERT INTO currency (id, name) VALUES ('{curr}', '{curr}');"
    op.execute(curr_ins)


def downgrade() -> None:
    curr_del: str = ""
    for curr in {"RUB", "USD"}:
        curr_del += f"DELETE FROM currency WHERE ID = '{curr}'; "
    op.execute(curr_del)
