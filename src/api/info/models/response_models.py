from datetime import datetime, date
from decimal import Decimal
from enum import StrEnum, auto

from pydantic import BaseModel


class OHLCRespModel(BaseModel):
    date: datetime
    open: Decimal
    high: Decimal
    low: Decimal
    close: Decimal
    volume: int


class SecuritiesRespModel(BaseModel):
    figi: str
    ticker: str
    name: str
    ipo_date: date
    first_1day_candle_date: date
    currency: str
    exchange: str
    securities_type: int | None


class DviRespModel(BaseModel):
    declared_date: date
    last_buy_date: date
    payment_date: date
    dividend_net: Decimal


class DividensRespModel(BaseModel):
    figi: str
    ticker: str
    div: list[DviRespModel]


class Exchanges(StrEnum):
    MOEX = auto()
    MOEX_EVENING_WEEKEND = auto()
