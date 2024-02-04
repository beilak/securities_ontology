from datetime import datetime, date
from decimal import Decimal

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
