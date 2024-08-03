from datetime import date
from src.use_cases.models.models import Securities
from src.use_cases.protocols.securities_provider import SecuritiesProviderProtocol
from tinkoff.invest import ShareType


class SecuritiesReader:
    def __init__(
        self,
        data_provider: SecuritiesProviderProtocol,
    ) -> None:
        self._data_provider = data_provider

    async def execute(
        self, securities_type: ShareType, exchange: str, first_1d_candle: date
    ) -> list[Securities]:
        securities: list = await self._data_provider.fetch_securities(
            exchange=exchange,
            securities_type=securities_type.value,
            first_1d_candle=first_1d_candle,
        )

        return [
            Securities(
                figi=i.figi,
                ticker=i.ticker,
                name=i.name,
                ipo_date=i.ipo_date,
                first_1day_candle_date=i.first_1day_candle_date,
                currency=i.currency,
                exchange=i.exchange,
                securities_type=i.securities_type,
            )
            for i in securities
        ]
