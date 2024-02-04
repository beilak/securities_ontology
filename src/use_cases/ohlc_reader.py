from datetime import date, datetime

from src.use_cases.models.enums import Candles
from src.use_cases.protocols.ohlc_provider import OhlcProviderProtocol
from src.use_cases.models.models import Ohlc


class OHLCReader:
    def __init__(
        self,
        data_provider: OhlcProviderProtocol,
    ) -> None:
        self._data_provider = data_provider

    async def execute(
        self,
        *,
        ticker: str,
        candles: Candles,
        from_: datetime | date,
        to_: datetime | date,
    ) -> list[Ohlc]:
        figi = await self._data_provider.fetch_figi_by_ticker(
            ticker=ticker,
        )
        ohlc_records: list = await self._data_provider.fetch_ohlc(
            figi=figi,
            candles=candles.value,
            from_=from_,
            to_=to_,
        )

        return [
            Ohlc(
                date=i.date_time,
                open=i.open,
                high=i.high,
                low=i.low,
                close=i.close,
                volume=i.volume,
            )
            for i in ohlc_records
        ]
