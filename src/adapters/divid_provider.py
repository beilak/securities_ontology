from datetime import date
from databases import Database
from databases.interfaces import Record


class DividDbAdapter:
    def __init__(self, db: Database):
        self._db = db

    async def fetch_dividend(
        self,
        ticker: str,
    ) -> list[Record]:
        query: str = f"""
            SELECT securities.ticker, divid.* 
            FROM divid 
            JOIN securities ON securities.figi = divid.figi           
            WHERE securities.ticker = '{ticker}'
        """

        return await self._db.fetch_all(
            query=query,
        )
