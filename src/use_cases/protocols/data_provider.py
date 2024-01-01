import typing as tp
from datetime import datetime


class DataProviderProtocol(tp.Protocol):
    async def fetch_ohlc(
        self,
        *,
        candles: str,
        from_: datetime,
        to_: datetime,
    ) -> list[dict]:
        ...
