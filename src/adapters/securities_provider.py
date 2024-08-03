from datetime import date
from databases import Database
from databases.interfaces import Record


class SecuritiesDbAdapter:
    def __init__(self, db: Database):
        self._db = db

    async def fetch_securities(
        self,
        exchange: str,
        first_1d_candle: date,
        securities_type: int,
    ) -> list[Record]:
        print(first_1d_candle.strftime("%Y-%m-%d"))
        query: str = f"""
            SELECT * FROM securities 
            WHERE securities_type = {securities_type}
            and first_1day_candle_date <= '{first_1d_candle}'
            and exchange = '{exchange.upper()}'
        """

        return await self._db.fetch_all(
            query=query,
        )
