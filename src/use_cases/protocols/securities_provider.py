import typing as tp


class SecuritiesProviderProtocol(tp.Protocol):
    async def fetch_securities(self) -> list:
        ...
