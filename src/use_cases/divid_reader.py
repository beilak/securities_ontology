from datetime import date
from src.adapters.divid_provider import DividDbAdapter
from src.use_cases.models.models import Dividens, Securities, Div
from src.use_cases.protocols.securities_provider import SecuritiesProviderProtocol
from tinkoff.invest import ShareType


class DividReader:
    def __init__(
        self,
        data_provider: DividDbAdapter,
    ) -> None:
        self._data_provider = data_provider

    async def execute(
        self,
        ticker: str,
    ) -> Dividens:
        divs: list = await self._data_provider.fetch_dividend(
            ticker=ticker,
        )
        if not len(divs):
            return []

        figi = divs[0]["figi"]

        return Dividens(
            figi=figi,
            ticker=ticker,
            div=[
                Div(
                    declared_date=i.declared_date,
                    last_buy_date=i.last_buy_date,
                    payment_date=i.payment_date,
                    dividend_net=i.dividend_net,
                )
                for i in divs
            ],
        )
