import typing as tp
from datetime import datetime
from decimal import Decimal


class ohlc(tp.TypedDict):
    date: datetime
    open: Decimal
    high: Decimal
    low: Decimal
    close: Decimal
    volume: int
