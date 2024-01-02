import typing as tp
from datetime import date, datetime

from databases.interfaces import Record


class DataProviderProtocol(tp.Protocol):
    async def fetch_figi_by_ticker(self, ticker: str) -> str:
        ...

    async def fetch_ohlc(
        self,
        *,
        figi: str,
        candles: str,
        from_: datetime | date,
        to_: datetime | date,
    ) -> list[Record]:
        ...
