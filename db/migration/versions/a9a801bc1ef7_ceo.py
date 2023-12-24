"""ceo

Revision ID: a9a801bc1ef7
Revises: 8123af3c9a68
Create Date: 2023-12-24 15:17:40.516318

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision: str = 'a9a801bc1ef7'
down_revision: Union[str, None] = '8123af3c9a68'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('ceo',
    sa.Column('issuer', postgresql.UUID(as_uuid=True), nullable=False),
    sa.Column('person', postgresql.UUID(as_uuid=True), nullable=False),
    sa.Column('date_start', sa.Date(), nullable=False),
    sa.Column('date_end', sa.Date(), nullable=True),
    sa.ForeignKeyConstraint(['issuer'], ['issuer.id'], ),
    sa.ForeignKeyConstraint(['person'], ['person.id'], ),
    sa.PrimaryKeyConstraint('issuer', 'person', 'date_start')
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('ceo')
    # ### end Alembic commands ###
