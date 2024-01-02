"""ref

Revision ID: 64b5597dc59a
Revises: 8ca70d322e44
Create Date: 2023-12-24 15:08:12.253216

"""
from typing import Sequence, Union

import sqlalchemy as sa
from alembic import op

# revision identifiers, used by Alembic.
revision: str = "64b5597dc59a"
down_revision: Union[str, None] = "8ca70d322e44"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_foreign_key(None, "country", "currency", ["currency"], ["id"])
    op.create_foreign_key(None, "issuer", "country", ["country"], ["id"])
    op.create_foreign_key(None, "securities", "country", ["country"], ["id"])
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, "securities", type_="foreignkey")
    op.drop_constraint(None, "issuer", type_="foreignkey")
    op.drop_constraint(None, "country", type_="foreignkey")
    # ### end Alembic commands ###
