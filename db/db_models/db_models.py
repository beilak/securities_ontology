from uuid import uuid4

import sqlalchemy as sa
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.types import DECIMAL


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


# main tables
issuer = sa.Table(
    "issuer",
    metadata,
    sa.Column("id", UUID(as_uuid=True), primary_key=True, default=uuid4()),
    sa.Column("name", sa.String),
    sa.Column("ipo_date", sa.Date),
    sa.Column("sector", UUID(as_uuid=True), sa.ForeignKey("sector.id"), nullable=False),
    sa.Column(
        "industry", UUID(as_uuid=True), sa.ForeignKey("industry.id"), nullable=False
    ),
    sa.Column(
        "currency", UUID(as_uuid=True), sa.ForeignKey("currency.id"), nullable=False
    ),
)

securities = sa.Table(
    "securities",
    metadata,
    sa.Column("figi", sa.String, primary_key=True),
    sa.Column("ticker", sa.String, nullable=False),
    sa.Column("name", sa.String, nullable=False),
    sa.Column("issuer", UUID(as_uuid=True), sa.ForeignKey("issuer.id"), nullable=False),
    sa.Column(
        "type", UUID(as_uuid=True), sa.ForeignKey("securities_type.id"), nullable=False
    ),
)

ohlc = sa.Table(
    "ohlc_1d",
    metadata,
    sa.Column("figi", sa.String, sa.ForeignKey("securities.figi"), primary_key=True),
    sa.Column("date_time", sa.DateTime, primary_key=True),
    sa.Column("open", DECIMAL(10, 9), nullable=False),
    sa.Column("high", sa.String, nullable=False),
    sa.Column("low", sa.String, nullable=False),
    sa.Column("close", sa.String, nullable=False),
    sa.Column("volume", sa.Integer, nullable=False),
)
