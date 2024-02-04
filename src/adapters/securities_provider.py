from databases import Database
from databases.interfaces import Record


class SecuritiesDbAdapter:
    def __init__(self, db: Database):
        self._db = db

    async def fetch_securities(
        self,
    ) -> list[Record]:
        query: str = """
            SELECT * FROM securities
        """

        return await self._db.fetch_all(
            query=query,
        )
