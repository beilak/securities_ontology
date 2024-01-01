from datetime import datetime
from decimal import Decimal

from pydantic import BaseModel


class OHLCRespModel(BaseModel):
    date: datetime
    open: Decimal
    high: Decimal
    low: Decimal
    close: Decimal
    volume: int
