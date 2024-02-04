import typing as tp
from datetime import datetime, date
from decimal import Decimal


class Ohlc(tp.TypedDict):
    date: datetime
    open: Decimal
    high: Decimal
    low: Decimal
    close: Decimal
    volume: int


class Securities(tp.TypedDict):
    figi: str
    ticker: str
    name: str
    ipo_date: date
    first_1day_candle_date: date
    currency: str
    exchange: str
