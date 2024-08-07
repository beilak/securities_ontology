from uuid import uuid4

import sqlalchemy as sa
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.types import DECIMAL

metadata = sa.MetaData()

# ToDo Ref. spliat this file

## Dict tables

securities_type = sa.Table(
    "securities_type",
    metadata,
    # sa.Column("id", UUID(as_uuid=True), primary_key=True, default=uuid4()),
    sa.Column("id", sa.Integer, primary_key=True),
    sa.Column("name", sa.String),
)

sector = sa.Table(
    "sector",
    metadata,
    sa.Column("id", sa.String, primary_key=True),
    sa.Column("name", sa.String),
)

industry = sa.Table(
    "industry",
    metadata,
    sa.Column("id", sa.String, primary_key=True),
    sa.Column("name", sa.String),
)

currency = sa.Table(
    "currency",
    metadata,
    sa.Column("id", sa.String, primary_key=True),
    sa.Column("name", sa.String),
)

country = sa.Table(
    "country",
    metadata,
    sa.Column("id", sa.String, primary_key=True),
    sa.Column("name", sa.String),
    sa.Column("currency", sa.String, sa.ForeignKey("currency.id"), nullable=False),
)

exchange = sa.Table(
    "exchange",
    metadata,
    sa.Column("id", sa.String, primary_key=True),
    sa.Column(
        "name",
        sa.String,
    ),
    sa.Column("country", sa.String, sa.ForeignKey("country.id"), nullable=False),
)


# main tables
issuer = sa.Table(
    "issuer",
    metadata,
    sa.Column("id", UUID(as_uuid=True), primary_key=True, default=uuid4()),
    sa.Column("name", sa.String),
    sa.Column("sector", sa.String, sa.ForeignKey("sector.id"), nullable=False),
    sa.Column("industry", sa.String, sa.ForeignKey("industry.id"), nullable=True),
    sa.Column("country", sa.String, sa.ForeignKey("country.id"), nullable=False),
)

securities = sa.Table(
    "securities",
    metadata,
    sa.Column("figi", sa.String, primary_key=True),
    sa.Column("ticker", sa.String, nullable=False),
    sa.Column("name", sa.String, nullable=False),
    sa.Column("ipo_date", sa.Date),
    sa.Column("first_1day_candle_date", sa.Date),
    sa.Column("currency", sa.String, sa.ForeignKey("currency.id")),
    sa.Column("exchange", sa.String, sa.ForeignKey("exchange.id"), nullable=False),
    sa.Column("securities_type", sa.ForeignKey("securities_type.id"), nullable=True),
)

divid = sa.Table(
    "divid",
    metadata,
    sa.Column("figi", sa.String, primary_key=True),
    sa.Column("declared_date", sa.DateTime, primary_key=True),
    sa.Column("last_buy_date", sa.DateTime, primary_key=True),
    sa.Column("payment_date", sa.DateTime, primary_key=True),
    sa.Column("dividend_net", DECIMAL(18, 9), nullable=False),
)

ohlc = sa.Table(
    "ohlc_1d",
    metadata,
    sa.Column("figi", sa.String, sa.ForeignKey("securities.figi"), primary_key=True),
    sa.Column("date_time", sa.DateTime, primary_key=True),
    sa.Column("open", DECIMAL(18, 9), nullable=False),
    sa.Column("high", DECIMAL(18, 9), nullable=False),
    sa.Column("low", DECIMAL(18, 9), nullable=False),
    sa.Column("close", DECIMAL(18, 9), nullable=False),
    sa.Column("volume", sa.BigInteger, nullable=False),
)

central_bank_rate = sa.Table(
    "central_bank_rate",
    metadata,
    sa.Column("date", sa.Date, primary_key=True),
    sa.Column("country", sa.String, sa.ForeignKey("country.id"), nullable=False),
    sa.Column("rate", sa.Float, nullable=False),
)

gdp = sa.Table(
    "gdp",
    metadata,
    sa.Column("date", sa.Date, primary_key=True),
    sa.Column("country", sa.String, sa.ForeignKey("country.id"), nullable=False),
    sa.Column("gdp", DECIMAL(10, 9), nullable=False),
)

person = sa.Table(
    "person",
    metadata,
    sa.Column("id", UUID(as_uuid=True), primary_key=True, default=uuid4()),
    sa.Column("name", sa.String, nullable=False),
)

ceo = sa.Table(
    "ceo",
    metadata,
    sa.Column(
        "issuer",
        UUID(as_uuid=True),
        sa.ForeignKey("issuer.id"),
        nullable=False,
        primary_key=True,
    ),
    sa.Column(
        "person",
        UUID(as_uuid=True),
        sa.ForeignKey("person.id"),
        nullable=False,
        primary_key=True,
    ),
    sa.Column("date_start", sa.Date, primary_key=True),
    sa.Column("date_end", sa.Date),
)


person = sa.Table(
    "twitter",
    metadata,
    sa.Column("id", UUID(as_uuid=True), primary_key=True, default=uuid4()),
    sa.Column("date_time", sa.DateTime, nullable=False),
    sa.Column("text", sa.String, nullable=False),
    sa.Column("related_issuer", UUID(as_uuid=True), sa.ForeignKey("issuer.id")),
)
