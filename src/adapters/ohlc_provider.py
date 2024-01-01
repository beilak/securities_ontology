from datetime import datetime

from databases import Database
from databases.interfaces import Record


class OHLC_Db_adapter:
    CANDLESS_TABLE_NAME: dict = {
        "1d": "ohlc_1d",
    }

    def __init__(self, db: Database):
        self._db = db

    def _choose_table(self, candles: str) -> str:
        return self.CANDLESS_TABLE_NAME[candles]

    async def fetch_ohlc(
        self,
        *,
        figi: str,
        candles: str,
        from_: datetime,
        to_: datetime,
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
            from_: from_,
            to_: to_,
        }

        return await self._db.fetch_all(
            query=query,
            values=values,
        )
