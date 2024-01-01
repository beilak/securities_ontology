"""add curr

Revision ID: 0b8b95f0c047
Revises: f141977db4ef
Create Date: 2023-12-24 19:16:52.939233

"""
from typing import Sequence, Union

import sqlalchemy as sa
from alembic import op
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision: str = "0b8b95f0c047"
down_revision: Union[str, None] = "f141977db4ef"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column("issuer", "industry", existing_type=sa.VARCHAR(), nullable=True)
    op.add_column("securities", sa.Column("currency", sa.String(), nullable=True))
    op.drop_constraint("securities_type_fkey", "securities", type_="foreignkey")
    op.create_foreign_key(None, "securities", "currency", ["currency"], ["id"])
    op.drop_column("securities", "type")
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column(
        "securities",
        sa.Column("type", postgresql.UUID(), autoincrement=False, nullable=False),
    )
    op.drop_constraint(None, "securities", type_="foreignkey")
    op.create_foreign_key(
        "securities_type_fkey", "securities", "securities_type", ["type"], ["id"]
    )
    op.drop_column("securities", "currency")
    op.alter_column("issuer", "industry", existing_type=sa.VARCHAR(), nullable=False)
    # ### end Alembic commands ###
