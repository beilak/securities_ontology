from uuid import uuid4

import sqlalchemy as sa
from sqlalchemy.dialects.postgresql import UUID

metadata = sa.MetaData()

## Dict tables

securities_type = sa.Table(
    "securities_type",
    metadata,
    sa.Column("id", UUID(as_uuid=True), primary_key=True, default=uuid4()),
    sa.Column("name", sa.String),
)

sector = sa.Table(
    "sector",
    metadata,
    sa.Column("id", UUID(as_uuid=True), primary_key=True, default=uuid4()),
    sa.Column("name", sa.String),
)

industry = sa.Table(
    "industry",
    metadata,
    sa.Column("id", UUID(as_uuid=True), primary_key=True, default=uuid4()),
    sa.Column("name", sa.String),
)

currency = sa.Table(
    "currency",
    metadata,
    sa.Column("id", UUID(as_uuid=True), primary_key=True, default=uuid4()),
    sa.Column("name", sa.String),
)

currency = sa.Table(
    "country",
    metadata,
    sa.Column("id", UUID(as_uuid=True), primary_key=True, default=uuid4()),
    sa.Column("name", sa.String),
    sa.Column(
        "currency", UUID(as_uuid=True), sa.ForeignKey("currency.id"), nullable=False
    ),
)
