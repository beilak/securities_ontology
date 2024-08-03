import typing as tp


class SecuritiesProviderProtocol(tp.Protocol):
    async def fetch_securities(
        self, exchange: str, first_1d_candle, securities_type: int | None = None
    ) -> list:
        ...
