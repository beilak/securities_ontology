"""ref

Revision ID: f7bf0ff01b47
Revises: 1a6eb18a2272
Create Date: 2023-12-24 14:49:00.193783

"""
from typing import Sequence, Union

import sqlalchemy as sa
from alembic import op
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision: str = "f7bf0ff01b47"
down_revision: Union[str, None] = "1a6eb18a2272"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column("issuer", sa.Column("country", sa.String(), nullable=False))
    op.drop_column("issuer", "currency")
    op.add_column("securities", sa.Column("country", sa.String(), nullable=False))
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column("securities", "country")
    op.add_column(
        "issuer",
        sa.Column("currency", postgresql.UUID(), autoincrement=False, nullable=False),
    )
    op.drop_column("issuer", "country")
    # ### end Alembic commands ###
