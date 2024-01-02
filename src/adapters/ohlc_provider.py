from datetime import date, datetime

from databases import Database
from databases.interfaces import Record


class OhlcDbAdapter:
    CANDLESS_TABLE_NAME: dict = {
        "1d": "ohlc_1d",
    }

    def __init__(self, db: Database):
        self._db = db

    async def fetch_figi_by_ticker(self, ticker: str) -> str:
        query: str = """
            SELECT figi from securities WHERE ticker = :TICKER
        """

        return await self._db.fetch_val(query=query, values={"TICKER": ticker.upper()})

    def _choose_table(self, candles: str) -> str:
        return self.CANDLESS_TABLE_NAME[candles]

    async def fetch_ohlc(
        self,
        *,
        figi: str,
        candles: str,
        from_: datetime | date,
        to_: datetime | date,
    ) -> list[Record]:
        table_name = self._choose_table(candles)

        query: str = f"""
            SELECT * FROM {table_name}
            WHERE figi = :figi
              and date_time >= :from_
              and date_time <= :to_
        """

        values: dict = {
            "figi": figi,
            "from_": from_,
            "to_": to_,
        }

        return await self._db.fetch_all(
            query=query,
            values=values,
        )
