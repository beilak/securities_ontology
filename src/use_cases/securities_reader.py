from src.use_cases.models.models import Securities
from src.use_cases.protocols.securities_provider import SecuritiesProviderProtocol


class SecuritiesReader:
    def __init__(
        self,
        data_provider: SecuritiesProviderProtocol,
    ) -> None:
        self._data_provider = data_provider

    async def execute(self) -> list[Securities]:
        securities: list = await self._data_provider.fetch_securities()

        return [
            Securities(
                figi=i.figi,
                ticker=i.ticker,
                name=i.name,
                ipo_date=i.ipo_date,
                first_1day_candle_date=i.first_1day_candle_date,
                currency=i.currency,
                exchange=i.exchange,
            )
            for i in securities
        ]
