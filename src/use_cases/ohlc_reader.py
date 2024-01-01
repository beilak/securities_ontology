from datetime import datetime

from models.enums import Candles
from protocols.data_provider import DataProviderProtocol


class OHLCReader:
    def __init__(
        self,
        data_provider: DataProviderProtocol,
    ) -> None:
        self._data_provider = data_provider

    async def execute(
        self,
        *,
        candles: Candles,
        from_: datetime,
        to_: datetime,
    ) -> list[dict]:
        return await self._data_provider.fetch_ohlc(
            candles=candles.value,
            from_=from_,
            to_=to_,
        )
