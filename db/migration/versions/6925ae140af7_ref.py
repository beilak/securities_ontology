"""ref

Revision ID: 6925ae140af7
Revises: 190fd039ab60
Create Date: 2023-12-24 18:51:42.458942

"""
from typing import Sequence, Union

import sqlalchemy as sa
from alembic import op

# revision identifiers, used by Alembic.
revision: str = "6925ae140af7"
down_revision: Union[str, None] = "190fd039ab60"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column("issuer", "sector", existing_type=sa.VARCHAR(), nullable=False)
    op.alter_column("issuer", "industry", existing_type=sa.VARCHAR(), nullable=False)
    op.alter_column("issuer", "country", existing_type=sa.VARCHAR(), nullable=False)
    op.create_foreign_key(None, "issuer", "industry", ["industry"], ["id"])
    op.create_foreign_key(None, "issuer", "sector", ["sector"], ["id"])
    op.create_foreign_key(None, "issuer", "country", ["country"], ["id"])
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, "issuer", type_="foreignkey")
    op.drop_constraint(None, "issuer", type_="foreignkey")
    op.drop_constraint(None, "issuer", type_="foreignkey")
    op.alter_column("issuer", "country", existing_type=sa.VARCHAR(), nullable=True)
    op.alter_column("issuer", "industry", existing_type=sa.VARCHAR(), nullable=True)
    op.alter_column("issuer", "sector", existing_type=sa.VARCHAR(), nullable=True)
    # ### end Alembic commands ###
